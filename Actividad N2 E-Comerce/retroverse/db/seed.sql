-- ============================================================================
-- RetroVerse — Datos de ejemplo (seed) para navegar la app
-- ============================================================================
SET search_path TO retroverse;

-- Geografía (jerarquía snowflake)
INSERT INTO dim_pais (nombre, codigo_iso) VALUES
  ('Argentina','AR'), ('Uruguay','UY'), ('Chile','CL');

INSERT INTO dim_provincia (nombre, id_pais) VALUES
  ('Chaco', 1), ('Buenos Aires', 1), ('Córdoba', 1),
  ('Montevideo', 2), ('Región Metropolitana', 3);

INSERT INTO dim_ciudad (nombre, cod_postal, id_provincia) VALUES
  ('Resistencia','3500',1), ('CABA','1000',2), ('La Plata','1900',2),
  ('Córdoba Capital','5000',3), ('Montevideo','11000',4), ('Santiago','8320000',5);

-- Vendedores (cada uno es el "UNO" de la relación N:1)
INSERT INTO dim_vendedor (cuit, nombre_tienda, descripcion, reputacion, id_ciudad) VALUES
  ('30-71122334-5','NeonByte Retro','Computadoras y consolas restauradas de los 80/90.', 4.8, 1),
  ('30-99887766-1','Vinilo & Voltaje','Vinilos, walkmans y audio analógico.', 4.6, 2),
  ('33-55667788-9','PixelPalace','Cartuchos, joysticks y memorabilia gamer.', 4.9, 4);

-- Compradores (REGISTRO MAESTRO) — N:1 hacia un vendedor
INSERT INTO dim_comprador (dni, email, nombre, apellido, fecha_nacimiento, id_ciudad, id_vendedor) VALUES
  ('38111222','lucia.gomez@mail.com','Lucía','Gómez','1995-04-12', 1, 1),
  ('40222333','marco.diaz@mail.com','Marco','Díaz','1990-11-03', 1, 1),
  ('29333444','sofia.ruiz@mail.com','Sofía','Ruiz','1988-07-21', 2, 1),
  ('41444555','juan.perez@mail.com','Juan','Pérez','2000-01-30', 2, 2),
  ('37555666','ana.torres@mail.com','Ana','Torres','1993-09-15', 4, 3),
  ('35666777','diego.lopez@mail.com','Diego','López','1985-02-28', 4, 3);

-- Jerarquía de producto (snowflake): familia -> categoria
INSERT INTO dim_familia (nombre) VALUES
  ('Tecnología Retro'), ('Audio Analógico'), ('Gaming Clásico');

INSERT INTO dim_categoria (nombre, id_familia) VALUES
  ('Computadoras', 1), ('Consolas', 1),
  ('Reproductores', 2), ('Vinilos', 2),
  ('Cartuchos', 3), ('Accesorios Gamer', 3);

INSERT INTO dim_marca (nombre) VALUES
  ('Commodore'), ('Nintendo'), ('Sega'), ('Sony'), ('Atari'), ('Panasonic'), ('Genérico');

INSERT INTO dim_condicion (nombre) VALUES
  ('Nuevo'), ('Restaurado'), ('Usado - Bueno'), ('Vintage'), ('Para repuestos');

INSERT INTO dim_decada (etiqueta, anio_ini, anio_fin) VALUES
  ('70s',1970,1979), ('80s',1980,1989), ('90s',1990,1999), ('2000s',2000,2009);

-- Productos
INSERT INTO dim_producto (sku, nombre, descripcion, precio, stock, imagen_url, id_categoria, id_marca, id_condicion, id_decada, id_vendedor) VALUES
  ('RV-CBM64','Commodore 64','La computadora hogareña más vendida de la historia. Restaurada y funcionando.', 185000, 3, '/img/RV-CBM64.jpg', 1, 1, 2, 2, 1),
  ('RV-NESC','Nintendo NES','Consola de 8 bits con dos joysticks. Clásico atemporal.', 145000, 5, '/img/RV-NESC.png', 2, 2, 3, 2, 1),
  ('RV-SNES','Super Nintendo','16 bits de gloria. Incluye Super Mario World.', 165000, 4, '/img/RV-SNES.png', 2, 2, 2, 3, 1),
  ('RV-MEGADRV','Sega Mega Drive','La guerra de los bits en su máxima expresión.', 138000, 2, '/img/RV-MEGADRV.jpg', 2, 3, 3, 3, 1),
  ('RV-WALKMAN','Sony Walkman WM-10','El reproductor portátil que cambió todo. Sonido analógico puro.', 92000, 6, '/img/RV-WALKMAN.png', 3, 4, 4, 2, 2),
  ('RV-DISCMAN','Sony Discman D-50','Primer reproductor de CD portátil. Pieza de colección.', 110000, 3, '/img/RV-DISCMAN.jpg', 3, 4, 4, 2, 2),
  ('RV-VINILO1','Vinilo - Synthwave Dreams','Compilado de synth ochentoso. Edición limitada.', 28000, 12, '/img/RV-VINILO1.jpg', 4, 7, 1, 2, 2),
  ('RV-VINILO2','Vinilo - Retro Arcade OST','Bandas sonoras de arcades clásicos en vinilo.', 31000, 9, '/img/RV-VINILO2.jpg', 4, 7, 1, 3, 2),
  ('RV-ATARI','Atari 2600','La que empezó todo en el living. Funcionando.', 120000, 2, '/img/RV-ATARI.png', 2, 5, 4, 1, 3),
  ('RV-CARTZELDA','Cartucho - The Legend of Zelda','Cartucho dorado original NES. Para coleccionistas.', 75000, 4, '/img/RV-CARTZELDA.png', 5, 2, 3, 2, 3),
  ('RV-CARTSONIC','Cartucho - Sonic the Hedgehog','Mega Drive. La mascota azul más veloz.', 45000, 7, '/img/RV-CARTSONIC.jpg', 5, 3, 3, 3, 3),
  ('RV-JOYARCADE','Joystick Arcade','Joystick con microswitches estilo fichín. Plug & play.', 38000, 15, '/img/RV-JOYARCADE.png', 6, 7, 1, 4, 3),
  ('RV-GAMEBOY','Game Boy Classic','Portátil de 8 bits. Incluye Tetris.', 98000, 6, '/img/RV-GAMEBOY.png', 2, 2, 2, 3, 3),
  ('RV-AMIGA','Commodore Amiga 500','Multimedia adelantada a su época. Restaurada.', 210000, 1, '/img/RV-AMIGA.jpg', 1, 1, 2, 2, 1);

-- Medios de pago (solo visual)
INSERT INTO dim_medio_pago (nombre) VALUES
  ('Tarjeta de Crédito'), ('Transferencia'), ('Efectivo'), ('RetroCoins (demo)');

-- Tiempo (algunas fechas)
INSERT INTO dim_tiempo (fecha, dia, mes, anio, trimestre, nombre_mes) VALUES
  ('2026-06-01', 1, 6, 2026, 2, 'Junio'),
  ('2026-06-05', 5, 6, 2026, 2, 'Junio'),
  ('2026-06-10',10, 6, 2026, 2, 'Junio'),
  ('2026-06-15',15, 6, 2026, 2, 'Junio');

-- Hechos de venta (demostrativos; grano = ítem de pedido)
INSERT INTO hecho_venta (nro_pedido, nro_linea, id_comprador, id_producto, id_tiempo, id_medio_pago, cantidad, precio_unitario) VALUES
  (1001, 1, 1, 1, 1, 1, 1, 185000),
  (1001, 2, 1, 7, 1, 1, 2,  28000),
  (1002, 1, 2, 2, 2, 2, 1, 145000),
  (1003, 1, 4, 5, 3, 3, 1,  92000),
  (1004, 1, 5,10, 4, 1, 1,  75000),
  (1004, 2, 5,12, 4, 1, 1,  38000);
