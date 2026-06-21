-- ============================================================================
--  HEXTECH BAZAAR · Seed de DIMENSIONES estáticas (no provienen de Data Dragon)
--  Se carga ANTES de seed-productos.sql. Las claves de negocio (codigo, email,
--  fecha) permiten que los productos y hechos referencien por subconsulta.
-- ============================================================================

-- dim_region (continental)
INSERT OR IGNORE INTO dim_region (codigo, nombre) VALUES
  ('AMERICAS', 'América'),
  ('EUROPE',   'Europa'),
  ('ASIA',     'Asia');

-- dim_servidor (FK → dim_region por codigo)
INSERT OR IGNORE INTO dim_servidor (codigo, nombre, id_region) VALUES
  ('LAN',  'Latinoamérica Norte', (SELECT id_region FROM dim_region WHERE codigo='AMERICAS')),
  ('LAS',  'Latinoamérica Sur',   (SELECT id_region FROM dim_region WHERE codigo='AMERICAS')),
  ('NA',   'Norteamérica',        (SELECT id_region FROM dim_region WHERE codigo='AMERICAS')),
  ('BR',   'Brasil',              (SELECT id_region FROM dim_region WHERE codigo='AMERICAS')),
  ('EUW',  'Europa Oeste',        (SELECT id_region FROM dim_region WHERE codigo='EUROPE')),
  ('EUNE', 'Europa Nórdica/Este', (SELECT id_region FROM dim_region WHERE codigo='EUROPE')),
  ('KR',   'Corea',               (SELECT id_region FROM dim_region WHERE codigo='ASIA'));

-- dim_familia
INSERT OR IGNORE INTO dim_familia (codigo, nombre, descripcion) VALUES
  ('COLECCIONABLE', 'Coleccionable', 'Campeones y aspectos (skins) del universo de Runeterra.'),
  ('EQUIPO',        'Equipo de invocador', 'Ítems de juego comprables con oro en la Grieta.');

-- dim_categoria (FK → dim_familia por codigo)
INSERT OR IGNORE INTO dim_categoria (codigo, nombre, id_familia) VALUES
  ('CAMPEON', 'Campeón', (SELECT id_familia FROM dim_familia WHERE codigo='COLECCIONABLE')),
  ('SKIN',    'Aspecto', (SELECT id_familia FROM dim_familia WHERE codigo='COLECCIONABLE')),
  ('ATAQUE',  'Ítem de Ataque',  (SELECT id_familia FROM dim_familia WHERE codigo='EQUIPO')),
  ('MAGIA',   'Ítem de Magia',   (SELECT id_familia FROM dim_familia WHERE codigo='EQUIPO')),
  ('DEFENSA', 'Ítem de Defensa', (SELECT id_familia FROM dim_familia WHERE codigo='EQUIPO')),
  ('BOTA',    'Botas',           (SELECT id_familia FROM dim_familia WHERE codigo='EQUIPO'));

-- dim_rareza
INSERT OR IGNORE INTO dim_rareza (codigo, nombre, color_hex) VALUES
  ('COMUN',      'Común',      '#9aa4af'),
  ('EPICO',      'Épico',      '#3b82f6'),
  ('LEGENDARIO', 'Legendario', '#a855f7'),
  ('MITICO',     'Mítico',     '#f59e0b'),
  ('ULTIMATE',   'Ultimate',   '#ef4444');

-- dim_region_lore (regiones del universo Runeterra)
INSERT OR IGNORE INTO dim_region_lore (codigo, nombre) VALUES
  ('IONIA',        'Jonia'),
  ('NOXUS',        'Noxus'),
  ('DEMACIA',      'Demacia'),
  ('PILTOVER',     'Piltóver'),
  ('ZAUN',         'Zaun'),
  ('FRELJORD',     'Freljord'),
  ('SHURIMA',      'Shurima'),
  ('SHADOW_ISLES', 'Islas de las Sombras'),
  ('BILGEWATER',   'Aguasturbias'),
  ('TARGON',       'Monte Targon'),
  ('VOID',         'El Vacío'),
  ('RUNETERRA',    'Runeterra');

-- dim_medio_pago
INSERT OR IGNORE INTO dim_medio_pago (codigo, nombre) VALUES
  ('TARJETA',         'Tarjeta de crédito'),
  ('RP_COMPRADO',     'RP comprados'),
  ('ESENCIA_AZUL',    'Esencia Azul'),
  ('ESENCIA_NARANJA', 'Esencia Naranja');

-- dim_tiempo (campo continente fecha → dia/mes/anio). Fechas usadas por los hechos.
INSERT OR IGNORE INTO dim_tiempo (fecha, dia, mes, anio, nombre_mes) VALUES
  ('2026-06-05', 5,  6, 2026, 'Junio'),
  ('2026-06-08', 8,  6, 2026, 'Junio'),
  ('2026-06-12', 12, 6, 2026, 'Junio'),
  ('2026-06-15', 15, 6, 2026, 'Junio'),
  ('2026-06-18', 18, 6, 2026, 'Junio'),
  ('2026-06-20', 20, 6, 2026, 'Junio');

-- dim_comprador (REGISTRO MAESTRO). FK → dim_servidor por codigo.
INSERT OR IGNORE INTO dim_comprador
  (email, nick_invocador, riot_tag, nombre, apellido, fecha_nacimiento, fecha_alta, nivel_invocador, horas_jugadas, cuenta_premium, id_servidor) VALUES
  ('faker.demo@hextech.gg',   'HideOnBush', 'KR1',  'Sang-hyeok', 'Lee',     '1996-05-07', '2021-03-10', 712, 4820.5, 1, (SELECT id_servidor FROM dim_servidor WHERE codigo='KR')),
  ('luna.rojas@hextech.gg',   'LunaIonia',  'LAN',  'Luna',      'Rojas',    '2002-11-21', '2022-07-01', 154, 612.0,  0, (SELECT id_servidor FROM dim_servidor WHERE codigo='LAN')),
  ('marco.vega@hextech.gg',   'NoxusKnight','LAS',  'Marco',     'Vega',     '1999-02-14', '2020-12-15', 233, 1340.75,1, (SELECT id_servidor FROM dim_servidor WHERE codigo='LAS')),
  ('sofia.luz@hextech.gg',    'DemaciaLux', 'EUW1', 'Sofía',     'Luz',      '2004-08-30', '2023-01-20', 88,  210.25, 0, (SELECT id_servidor FROM dim_servidor WHERE codigo='EUW')),
  ('diego.pena@hextech.gg',   'ZaunRunner', 'NA1',  'Diego',     'Peña',     '2000-04-03', '2021-09-09', 167, 980.5,  1, (SELECT id_servidor FROM dim_servidor WHERE codigo='NA'));
