-- ============================================================================
--  HEXTECH BAZAAR  ·  Esquema Snowflake (copo de nieve)
--  Actividad Formativa N.º 2 — Algoritmos y Estructuras de Datos (UTN-FRRe, ISI 2026)
--  Aplicación de la Unidad 2: estructuras tipo REGISTRO y diseño de CLAVES.
--
--  Dialecto: SQLite (la app corre sin servidor de BD). El DDL muestra de forma
--  explícita los 5 tipos de clave de la teoría: PRIMARIA, FORÁNEA, SECUNDARIA,
--  SIMPLE y COMPLEJA/COMPUESTA.
--
--  Forma de copo de nieve = dimensiones NORMALIZADAS en sub-dimensiones encadenadas:
--    · Rama COMPRADOR:  dim_comprador → dim_servidor → dim_region   (FK en cadena)
--    · Rama PRODUCTO:   dim_producto  → dim_categoria → dim_familia  (FK en cadena)
--  La tabla de HECHOS (hecho_compra) queda en el centro referenciando dimensiones.
-- ============================================================================

PRAGMA foreign_keys = ON;

-- ----------------------------------------------------------------------------
-- RAMA GEOGRÁFICA DEL COMPRADOR (sub-dimensiones encadenadas)
-- ----------------------------------------------------------------------------

-- dim_region: agrupación continental de servidores (AMÉRICA, EUROPA, ASIA).
CREATE TABLE IF NOT EXISTS dim_region (
  id_region   INTEGER PRIMARY KEY AUTOINCREMENT,   -- PK SIMPLE (surrogate)
  codigo      TEXT NOT NULL UNIQUE,                 -- clave candidata natural (UNIQUE)
  nombre      TEXT NOT NULL
);

-- dim_servidor: servidor de juego (LAN, LAS, NA, EUW...). Encadena a dim_region.
CREATE TABLE IF NOT EXISTS dim_servidor (
  id_servidor INTEGER PRIMARY KEY AUTOINCREMENT,    -- PK SIMPLE (surrogate)
  codigo      TEXT NOT NULL UNIQUE,                 -- 'LAN', 'NA'... (UNIQUE natural)
  nombre      TEXT NOT NULL,
  id_region   INTEGER NOT NULL,
  -- FK encadenada: servidor → region (lo que hace "snowflake" y no "star")
  FOREIGN KEY (id_region) REFERENCES dim_region (id_region)
);

-- ----------------------------------------------------------------------------
-- REGISTRO MAESTRO: dim_comprador  (CLIENTE-COMPRADOR / "Invocador")
--   Es el registro principal pedido por la consigna. Reúne campos heterogéneos
--   (texto, fecha, enteros). Cardinalidad N:1 → muchos compradores por servidor.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS dim_comprador (
  id_comprador     INTEGER PRIMARY KEY AUTOINCREMENT, -- PK SIMPLE: clave PRIMARIA del registro maestro
  email            TEXT NOT NULL UNIQUE,              -- clave candidata SIMPLE (UNIQUE)
  nick_invocador   TEXT NOT NULL,                     -- parte "GameName" del Riot ID
  riot_tag         TEXT NOT NULL,                     -- parte "#TAG" del Riot ID
  nombre           TEXT NOT NULL,
  apellido         TEXT NOT NULL,                     -- usado por clave SECUNDARIA (índice)
  fecha_nacimiento TEXT,                              -- DATE 'YYYY-MM-DD' → campo CONTINENTE (D/M/A)
  fecha_alta       TEXT NOT NULL,                     -- DATE 'YYYY-MM-DD'
  nivel_invocador  INTEGER NOT NULL DEFAULT 1,           -- ENTERO
  horas_jugadas    REAL    NOT NULL DEFAULT 0,            -- REAL (horas de juego acumuladas)
  cuenta_premium   INTEGER NOT NULL DEFAULT 0,            -- BOOLEANO (0/1: pase premium)
  id_servidor      INTEGER NOT NULL,
  -- FK: comprador → servidor (relación N:1, eje del registro maestro)
  FOREIGN KEY (id_servidor) REFERENCES dim_servidor (id_servidor),
  -- CLAVE COMPLEJA / COMPUESTA (natural): el Riot ID es GameName#TAG.
  UNIQUE (nick_invocador, riot_tag)
);

-- ----------------------------------------------------------------------------
-- RAMA DE PRODUCTO (sub-dimensiones encadenadas) + dimensiones descriptivas
-- ----------------------------------------------------------------------------

-- dim_familia: nivel más alto del catálogo (COLECCIONABLE vs EQUIPO).
CREATE TABLE IF NOT EXISTS dim_familia (
  id_familia INTEGER PRIMARY KEY AUTOINCREMENT,       -- PK SIMPLE
  codigo     TEXT NOT NULL UNIQUE,                    -- UNIQUE natural
  nombre     TEXT NOT NULL,
  descripcion TEXT
);

-- dim_categoria: encadena a familia (Campeón/Skin bajo Coleccionable; Ataque/Magia/Defensa/Bota bajo Equipo).
CREATE TABLE IF NOT EXISTS dim_categoria (
  id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,     -- PK SIMPLE
  codigo       TEXT NOT NULL UNIQUE,                  -- UNIQUE natural
  nombre       TEXT NOT NULL,
  id_familia   INTEGER NOT NULL,
  -- FK encadenada: categoria → familia (rama del copo de nieve)
  FOREIGN KEY (id_familia) REFERENCES dim_familia (id_familia)
);

-- dim_rareza: tier del coleccionable / ítem (Común, Épico, Legendario, Mítico, Ultimate).
CREATE TABLE IF NOT EXISTS dim_rareza (
  id_rareza INTEGER PRIMARY KEY AUTOINCREMENT,        -- PK SIMPLE
  codigo    TEXT NOT NULL UNIQUE,
  nombre    TEXT NOT NULL,
  color_hex TEXT
);

-- dim_region_lore: región del universo Runeterra de origen (Noxus, Demacia, Jonia...).
CREATE TABLE IF NOT EXISTS dim_region_lore (
  id_region_lore INTEGER PRIMARY KEY AUTOINCREMENT,   -- PK SIMPLE
  codigo         TEXT NOT NULL UNIQUE,
  nombre         TEXT NOT NULL
);

-- dim_producto: el ítem vendible (un campeón, una skin o un ítem de juego).
CREATE TABLE IF NOT EXISTS dim_producto (
  id_producto    INTEGER PRIMARY KEY AUTOINCREMENT,   -- PK SIMPLE
  sku            TEXT NOT NULL UNIQUE,                 -- clave de NEGOCIO candidata (UNIQUE), p.ej. 'SKIN-266-1'
  nombre         TEXT NOT NULL,
  subtitulo      TEXT,                                 -- título del campeón / resumen del ítem
  descripcion    TEXT,
  imagen         TEXT,                                 -- ruta servida desde /img/...
  precio         INTEGER NOT NULL,                     -- valor numérico
  moneda         TEXT NOT NULL DEFAULT 'RP',           -- 'RP' (skins/campeones) | 'Oro' (ítems)
  stock          INTEGER NOT NULL DEFAULT 0,
  destacado      INTEGER NOT NULL DEFAULT 0,           -- 0/1: aparece en la portada
  ddragon_ref    TEXT,                                 -- id/clave original de Data Dragon (trazabilidad)
  id_categoria   INTEGER NOT NULL,
  id_rareza      INTEGER NOT NULL,
  id_region_lore INTEGER NOT NULL,
  -- FKs del producto hacia sus dimensiones:
  FOREIGN KEY (id_categoria)   REFERENCES dim_categoria   (id_categoria),
  FOREIGN KEY (id_rareza)      REFERENCES dim_rareza      (id_rareza),
  FOREIGN KEY (id_region_lore) REFERENCES dim_region_lore (id_region_lore)
);

-- ----------------------------------------------------------------------------
-- DIMENSIONES DE LA TABLA DE HECHOS
-- ----------------------------------------------------------------------------

-- dim_tiempo: ilustra el CAMPO CONTINENTE → 'fecha' agrupa día/mes/año.
CREATE TABLE IF NOT EXISTS dim_tiempo (
  id_tiempo  INTEGER PRIMARY KEY AUTOINCREMENT,        -- PK SIMPLE
  fecha      TEXT NOT NULL UNIQUE,                     -- DATE (campo continente)
  dia        INTEGER NOT NULL,                         -- subcampo
  mes        INTEGER NOT NULL,                         -- subcampo
  anio       INTEGER NOT NULL,                         -- subcampo
  nombre_mes TEXT NOT NULL
);

-- dim_medio_pago: forma de pago (Tarjeta, RP, Esencia Azul...).
CREATE TABLE IF NOT EXISTS dim_medio_pago (
  id_medio_pago INTEGER PRIMARY KEY AUTOINCREMENT,     -- PK SIMPLE
  codigo        TEXT NOT NULL UNIQUE,
  nombre        TEXT NOT NULL
);

-- ----------------------------------------------------------------------------
-- TABLA DE HECHOS (centro del copo de nieve)
--   GRANO declarado: 1 fila = 1 ítem (línea) de una orden de compra.
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS hecho_compra (
  id_hecho        INTEGER PRIMARY KEY AUTOINCREMENT,   -- PK SIMPLE (surrogate)
  nro_orden       INTEGER NOT NULL,
  nro_linea       INTEGER NOT NULL,
  id_comprador    INTEGER NOT NULL,
  id_producto     INTEGER NOT NULL,
  id_tiempo       INTEGER NOT NULL,
  id_medio_pago   INTEGER NOT NULL,
  cantidad        INTEGER NOT NULL DEFAULT 1,
  precio_unitario INTEGER NOT NULL,
  subtotal        INTEGER NOT NULL,
  -- FKs hacia cada dimensión (todas las "puentes" del hecho):
  FOREIGN KEY (id_comprador)  REFERENCES dim_comprador  (id_comprador),
  FOREIGN KEY (id_producto)   REFERENCES dim_producto   (id_producto),
  FOREIGN KEY (id_tiempo)     REFERENCES dim_tiempo     (id_tiempo),
  FOREIGN KEY (id_medio_pago) REFERENCES dim_medio_pago (id_medio_pago),
  -- CLAVE COMPLEJA / COMPUESTA de negocio: identifica la línea dentro de la orden.
  UNIQUE (nro_orden, nro_linea)
);

-- ----------------------------------------------------------------------------
-- CLAVES SECUNDARIAS (índices sobre columnas NO únicas: agrupar/ordenar/buscar)
-- ----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_comprador_apellido ON dim_comprador (apellido);
CREATE INDEX IF NOT EXISTS idx_producto_categoria ON dim_producto  (id_categoria);
CREATE INDEX IF NOT EXISTS idx_producto_nombre    ON dim_producto  (nombre);
CREATE INDEX IF NOT EXISTS idx_hecho_tiempo       ON hecho_compra  (id_tiempo);
CREATE INDEX IF NOT EXISTS idx_hecho_comprador    ON hecho_compra  (id_comprador);
