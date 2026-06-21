import { getDb } from './db';

export type Producto = {
  id_producto: number;
  sku: string;
  nombre: string;
  subtitulo: string | null;
  descripcion: string | null;
  imagen: string | null;
  precio: number;
  moneda: string;
  stock: number;
  destacado: number;
  ddragon_ref: string | null;
  categoria: string;
  categoria_codigo: string;
  familia: string;
  familia_codigo: string;
  rareza: string;
  rareza_codigo: string;
  rareza_color: string | null;
  region_lore: string;
  region_codigo: string;
};

export type Filtro = {
  q?: string;
  familia?: string;
  categoria?: string;
  rareza?: string;
  region?: string;
  orden?: 'precio_asc' | 'precio_desc' | 'nombre';
};

const SELECT_PRODUCTO = `
  SELECT p.id_producto, p.sku, p.nombre, p.subtitulo, p.descripcion, p.imagen,
         p.precio, p.moneda, p.stock, p.destacado, p.ddragon_ref,
         cat.nombre  AS categoria,  cat.codigo AS categoria_codigo,
         fam.nombre  AS familia,    fam.codigo AS familia_codigo,
         rar.nombre  AS rareza,     rar.codigo AS rareza_codigo, rar.color_hex AS rareza_color,
         reg.nombre  AS region_lore, reg.codigo AS region_codigo
  FROM dim_producto p
  JOIN dim_categoria   cat ON cat.id_categoria   = p.id_categoria
  JOIN dim_familia     fam ON fam.id_familia     = cat.id_familia
  JOIN dim_rareza      rar ON rar.id_rareza      = p.id_rareza
  JOIN dim_region_lore reg ON reg.id_region_lore = p.id_region_lore
`;

export function getProductos(f: Filtro = {}): Producto[] {
  const db = getDb();
  const where: string[] = [];
  const params: Record<string, unknown> = {};
  if (f.q) { where.push('(p.nombre LIKE @q OR p.subtitulo LIKE @q)'); params.q = `%${f.q}%`; }
  if (f.familia) { where.push('fam.codigo = @familia'); params.familia = f.familia; }
  if (f.categoria) { where.push('cat.codigo = @categoria'); params.categoria = f.categoria; }
  if (f.rareza) { where.push('rar.codigo = @rareza'); params.rareza = f.rareza; }
  if (f.region) { where.push('reg.codigo = @region'); params.region = f.region; }

  let sql = SELECT_PRODUCTO;
  if (where.length) sql += ' WHERE ' + where.join(' AND ');
  sql += f.orden === 'precio_asc' ? ' ORDER BY p.precio ASC'
    : f.orden === 'precio_desc' ? ' ORDER BY p.precio DESC'
    : ' ORDER BY p.destacado DESC, p.nombre ASC';
  return db.prepare(sql).all(params) as Producto[];
}

export function getProducto(id: number): Producto | undefined {
  return getDb().prepare(SELECT_PRODUCTO + ' WHERE p.id_producto = @id').get({ id }) as Producto | undefined;
}

export function getDestacados(limit = 8): Producto[] {
  return getDb().prepare(SELECT_PRODUCTO + ' WHERE p.destacado = 1 ORDER BY p.nombre LIMIT @limit').all({ limit }) as Producto[];
}

export function getRelacionados(p: Producto, limit = 4): Producto[] {
  return getDb().prepare(
    SELECT_PRODUCTO + ' WHERE reg.codigo = @region AND p.id_producto <> @id ORDER BY RANDOM() LIMIT @limit'
  ).all({ region: p.region_codigo, id: p.id_producto, limit }) as Producto[];
}

// ---- Facetas para los filtros del catálogo ----
export type Faceta = { codigo: string; nombre: string; total: number; color?: string | null };

export function getFamilias(): Faceta[] {
  return getDb().prepare(`
    SELECT fam.codigo, fam.nombre, COUNT(p.id_producto) AS total
    FROM dim_familia fam
    LEFT JOIN dim_categoria cat ON cat.id_familia = fam.id_familia
    LEFT JOIN dim_producto p ON p.id_categoria = cat.id_categoria
    GROUP BY fam.id_familia ORDER BY fam.nombre`).all() as Faceta[];
}

export function getCategorias(): (Faceta & { familia: string })[] {
  return getDb().prepare(`
    SELECT cat.codigo, cat.nombre, fam.codigo AS familia, COUNT(p.id_producto) AS total
    FROM dim_categoria cat
    JOIN dim_familia fam ON fam.id_familia = cat.id_familia
    LEFT JOIN dim_producto p ON p.id_categoria = cat.id_categoria
    GROUP BY cat.id_categoria ORDER BY fam.nombre, cat.nombre`).all() as (Faceta & { familia: string })[];
}

export function getRarezas(): Faceta[] {
  return getDb().prepare(`
    SELECT rar.codigo, rar.nombre, rar.color_hex AS color, COUNT(p.id_producto) AS total
    FROM dim_rareza rar
    LEFT JOIN dim_producto p ON p.id_rareza = rar.id_rareza
    GROUP BY rar.id_rareza ORDER BY rar.id_rareza`).all() as Faceta[];
}

export function getRegiones(): Faceta[] {
  return getDb().prepare(`
    SELECT reg.codigo, reg.nombre, COUNT(p.id_producto) AS total
    FROM dim_region_lore reg
    LEFT JOIN dim_producto p ON p.id_region_lore = reg.id_region_lore
    GROUP BY reg.id_region_lore HAVING total > 0 ORDER BY reg.nombre`).all() as Faceta[];
}

// Conteo de filas por tabla (usado para totales en la portada).
export function getConteoTablas(): { tabla: string; filas: number }[] {
  const db = getDb();
  const tablas = ['dim_region', 'dim_servidor', 'dim_comprador', 'dim_familia', 'dim_categoria',
    'dim_rareza', 'dim_region_lore', 'dim_producto', 'dim_tiempo', 'dim_medio_pago', 'hecho_compra'];
  return tablas.map((t) => ({ tabla: t, filas: (db.prepare(`SELECT COUNT(*) AS n FROM ${t}`).get() as { n: number }).n }));
}
