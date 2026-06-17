-- ============================================================================
-- RetroVerse — Modelo de datos relacional en ESQUEMA SNOWFLAKE
-- Actividad Formativa N.º 2 — Algoritmos y Estructuras de Datos (UTN-FRRe)
-- Motor: PostgreSQL
--
-- El esquema demuestra explícitamente los TIPOS DE CLAVE de la Unidad 2:
--   (PK)  Clave Primaria   -> PRIMARY KEY  (surrogate simple en cada dimensión)
--   (FK)  Clave Foránea    -> FOREIGN KEY  (puente entre tablas/archivos)
--   (SEC) Clave Secundaria -> INDEX no único (agrupar / ordenar / buscar)
--   (SIM) Clave Simple     -> 1 solo campo contenido (dni, sku, codigo_iso)
--   (CPX) Clave Compleja   -> campo continente / varias columnas (UNIQUE compuesta)
--
-- REGISTRO MAESTRO: dim_comprador (orientado a cliente-comprador).
-- Cardinalidad pedida: N:1  ->  muchos compradores compran a UN vendedor
--                      (dim_comprador.id_vendedor -> dim_vendedor)
-- ============================================================================

DROP SCHEMA IF EXISTS retroverse CASCADE;
CREATE SCHEMA retroverse;
SET search_path TO retroverse;

-- ----------------------------------------------------------------------------
-- DIMENSIÓN GEOGRÁFICA (jerarquía normalizada = "copo de nieve")
--   dim_pais  <--  dim_provincia  <--  dim_ciudad
-- ----------------------------------------------------------------------------
CREATE TABLE dim_pais (
    id_pais     SERIAL       PRIMARY KEY,            -- (PK)(SIM) clave primaria simple
    nombre      VARCHAR(60)  NOT NULL,
    codigo_iso  CHAR(2)      NOT NULL UNIQUE          -- (SIM) clave candidata natural simple (AR, UY, CL)
);

CREATE TABLE dim_provincia (
    id_provincia SERIAL      PRIMARY KEY,             -- (PK)(SIM)
    nombre       VARCHAR(80) NOT NULL,
    id_pais      INT         NOT NULL
        REFERENCES dim_pais(id_pais)                  -- (FK) puente hacia dim_pais
);

CREATE TABLE dim_ciudad (
    id_ciudad    SERIAL      PRIMARY KEY,             -- (PK)(SIM)
    nombre       VARCHAR(80) NOT NULL,
    cod_postal   VARCHAR(10),
    id_provincia INT         NOT NULL
        REFERENCES dim_provincia(id_provincia)        -- (FK) puente hacia dim_provincia
);

-- ----------------------------------------------------------------------------
-- DIMENSIÓN VENDEDOR (tienda). "UNO" de la relación N:1 con compradores.
-- ----------------------------------------------------------------------------
CREATE TABLE dim_vendedor (
    id_vendedor   SERIAL      PRIMARY KEY,            -- (PK)(SIM)
    cuit          VARCHAR(13) NOT NULL UNIQUE,        -- (SIM) clave natural del vendedor
    nombre_tienda VARCHAR(120) NOT NULL,
    descripcion   TEXT,
    reputacion    NUMERIC(2,1) DEFAULT 5.0,           -- 0.0 a 5.0
    id_ciudad     INT         NOT NULL
        REFERENCES dim_ciudad(id_ciudad)              -- (FK)
);

-- ----------------------------------------------------------------------------
-- *** REGISTRO MAESTRO ***  dim_comprador (cliente-comprador)
--   Clave primaria elegida: id_comprador (surrogate, simple, estable).
--   N:1 -> cada comprador está asociado a UN vendedor (id_vendedor).
-- ----------------------------------------------------------------------------
CREATE TABLE dim_comprador (
    id_comprador     SERIAL       PRIMARY KEY,        -- (PK)(SIM) <-- CLAVE DEL REGISTRO MAESTRO
    dni              VARCHAR(11)  NOT NULL UNIQUE,     -- (SIM) clave candidata natural (simple, contenido)
    email            VARCHAR(120) NOT NULL UNIQUE,     -- (SIM) otra clave candidata natural
    nombre           VARCHAR(60)  NOT NULL,
    apellido         VARCHAR(60)  NOT NULL,
    -- "Fecha de nacimiento" es un campo CONTINENTE (Día/Mes/Año). En SQL se
    -- almacena como DATE; la app puede descomponerlo en sus subcampos.
    fecha_nacimiento DATE,
    fecha_alta       DATE         NOT NULL DEFAULT CURRENT_DATE,
    id_ciudad        INT          NOT NULL
        REFERENCES dim_ciudad(id_ciudad),             -- (FK) snowflake: comprador->ciudad->provincia->pais
    id_vendedor      INT          NOT NULL
        REFERENCES dim_vendedor(id_vendedor)          -- (FK) *** N:1 muchos compradores -> un vendedor ***
);
-- (SEC) clave secundaria: NO identifica único, sirve para AGRUPAR/ORDENAR
--       (p.ej. corte de control por vendedor, o listados por apellido).
CREATE INDEX idx_comprador_vendedor ON dim_comprador(id_vendedor);
CREATE INDEX idx_comprador_apellido ON dim_comprador(apellido);

-- ----------------------------------------------------------------------------
-- DIMENSIÓN PRODUCTO (jerarquía normalizada: producto -> categoria -> familia)
-- + sub-dimensiones marca, condición y década (snowflake)
-- ----------------------------------------------------------------------------
CREATE TABLE dim_familia (
    id_familia SERIAL      PRIMARY KEY,               -- (PK)(SIM)
    nombre     VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE dim_categoria (
    id_categoria SERIAL      PRIMARY KEY,             -- (PK)(SIM)
    nombre       VARCHAR(60) NOT NULL,
    id_familia   INT         NOT NULL
        REFERENCES dim_familia(id_familia)            -- (FK) categoria -> familia
);

CREATE TABLE dim_marca (
    id_marca SERIAL      PRIMARY KEY,                 -- (PK)(SIM)
    nombre   VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE dim_condicion (
    id_condicion SERIAL      PRIMARY KEY,             -- (PK)(SIM)
    nombre       VARCHAR(30) NOT NULL UNIQUE          -- Nuevo, Restaurado, Usado, Vintage, Para repuestos
);

CREATE TABLE dim_decada (
    id_decada SERIAL      PRIMARY KEY,                -- (PK)(SIM)
    etiqueta  VARCHAR(10) NOT NULL UNIQUE,            -- "70s","80s","90s","2000s"
    anio_ini  SMALLINT    NOT NULL,
    anio_fin  SMALLINT    NOT NULL
);

CREATE TABLE dim_producto (
    id_producto  SERIAL       PRIMARY KEY,            -- (PK)(SIM)
    sku          VARCHAR(20)  NOT NULL UNIQUE,        -- (SIM) clave natural del producto
    nombre       VARCHAR(140) NOT NULL,
    descripcion  TEXT,
    precio       NUMERIC(12,2) NOT NULL CHECK (precio >= 0),
    stock        INT          NOT NULL DEFAULT 0 CHECK (stock >= 0),
    imagen_url   VARCHAR(255),
    id_categoria INT NOT NULL REFERENCES dim_categoria(id_categoria),  -- (FK)
    id_marca     INT NOT NULL REFERENCES dim_marca(id_marca),          -- (FK)
    id_condicion INT NOT NULL REFERENCES dim_condicion(id_condicion),  -- (FK)
    id_decada    INT NOT NULL REFERENCES dim_decada(id_decada),        -- (FK)
    id_vendedor  INT NOT NULL REFERENCES dim_vendedor(id_vendedor)     -- (FK) producto pertenece a un vendedor
);
-- (SEC) claves secundarias para filtrado/agrupamiento del catálogo
CREATE INDEX idx_producto_categoria ON dim_producto(id_categoria);
CREATE INDEX idx_producto_decada    ON dim_producto(id_decada);
CREATE INDEX idx_producto_vendedor  ON dim_producto(id_vendedor);

-- ----------------------------------------------------------------------------
-- DIMENSIÓN TIEMPO (clásica). La fecha se descompone en subcampos
-- (Día/Mes/Año) -> ejemplo de campo CONTINENTE materializado.
-- ----------------------------------------------------------------------------
CREATE TABLE dim_tiempo (
    id_tiempo  SERIAL      PRIMARY KEY,               -- (PK)(SIM)
    fecha      DATE        NOT NULL UNIQUE,           -- (SIM) clave natural
    dia        SMALLINT    NOT NULL,
    mes        SMALLINT    NOT NULL,
    anio       SMALLINT    NOT NULL,
    trimestre  SMALLINT    NOT NULL,
    nombre_mes VARCHAR(12) NOT NULL
);

-- ----------------------------------------------------------------------------
-- DIMENSIÓN MEDIO DE PAGO (solo visual; la app NO procesa pagos reales)
-- ----------------------------------------------------------------------------
CREATE TABLE dim_medio_pago (
    id_medio_pago SERIAL      PRIMARY KEY,            -- (PK)(SIM)
    nombre        VARCHAR(40) NOT NULL UNIQUE
);

-- ----------------------------------------------------------------------------
-- TABLA DE HECHOS (FACT)  hecho_venta
--   Grano declarado: 1 fila = 1 ÍTEM (línea) de un pedido.
--   Clave primaria: surrogate id_hecho.
--   Clave COMPLEJA (continente) natural: (nro_pedido, nro_linea) UNIQUE.
--   Está rodeada por las dimensiones vía claves foráneas (estrella normalizada).
-- ----------------------------------------------------------------------------
CREATE TABLE hecho_venta (
    id_hecho        BIGSERIAL    PRIMARY KEY,         -- (PK)(SIM) surrogate de la fact
    nro_pedido      INT          NOT NULL,
    nro_linea       SMALLINT     NOT NULL,
    id_comprador    INT NOT NULL REFERENCES dim_comprador(id_comprador),   -- (FK)
    id_producto     INT NOT NULL REFERENCES dim_producto(id_producto),     -- (FK)
    id_tiempo       INT NOT NULL REFERENCES dim_tiempo(id_tiempo),         -- (FK)
    id_medio_pago   INT NOT NULL REFERENCES dim_medio_pago(id_medio_pago), -- (FK)
    cantidad        INT          NOT NULL CHECK (cantidad > 0),
    precio_unitario NUMERIC(12,2) NOT NULL,
    subtotal        NUMERIC(14,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    -- (CPX) CLAVE COMPLEJA/COMPUESTA: varias columnas forman la clave natural
    CONSTRAINT uq_pedido_linea UNIQUE (nro_pedido, nro_linea)
);
-- (SEC) claves secundarias para corte de control / agregaciones por dimensión
CREATE INDEX idx_hecho_tiempo    ON hecho_venta(id_tiempo);
CREATE INDEX idx_hecho_comprador ON hecho_venta(id_comprador);
CREATE INDEX idx_hecho_producto  ON hecho_venta(id_producto);

-- ============================================================================
-- VISTA de apoyo (catálogo "aplanado" para la app: junta producto con sus
-- dimensiones normalizadas del copo de nieve).
-- ============================================================================
CREATE VIEW v_catalogo AS
SELECT p.id_producto, p.sku, p.nombre, p.descripcion, p.precio, p.stock, p.imagen_url,
       c.nombre  AS categoria, f.nombre AS familia,
       m.nombre  AS marca,     cond.nombre AS condicion,
       d.etiqueta AS decada,
       v.id_vendedor, v.nombre_tienda
FROM dim_producto p
JOIN dim_categoria c   ON c.id_categoria = p.id_categoria
JOIN dim_familia   f   ON f.id_familia   = c.id_familia
JOIN dim_marca     m   ON m.id_marca     = p.id_marca
JOIN dim_condicion cond ON cond.id_condicion = p.id_condicion
JOIN dim_decada    d   ON d.id_decada    = p.id_decada
JOIN dim_vendedor  v   ON v.id_vendedor  = p.id_vendedor;
