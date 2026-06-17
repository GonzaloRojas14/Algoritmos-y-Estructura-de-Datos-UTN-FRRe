import { query } from './db';

export type Producto = {
  id_producto: number;
  sku: string;
  nombre: string;
  descripcion: string | null;
  precio: string; // numeric llega como string desde pg
  stock: number;
  imagen_url: string | null;
  categoria: string;
  familia: string;
  marca: string;
  condicion: string;
  decada: string;
  id_vendedor: number;
  nombre_tienda: string;
};

export type Vendedor = {
  id_vendedor: number;
  cuit: string;
  nombre_tienda: string;
  descripcion: string | null;
  reputacion: string;
  ciudad: string;
  provincia: string;
  pais: string;
};

export type Filtro = { familia?: string; decada?: string; q?: string };

export async function getCatalogo(f: Filtro = {}): Promise<Producto[]> {
  const where: string[] = [];
  const params: any[] = [];
  if (f.familia) { params.push(f.familia); where.push(`familia = $${params.length}`); }
  if (f.decada)  { params.push(f.decada);  where.push(`decada = $${params.length}`); }
  if (f.q)       { params.push(`%${f.q}%`); where.push(`(nombre ILIKE $${params.length} OR marca ILIKE $${params.length})`); }
  const sql = `SELECT * FROM v_catalogo ${where.length ? 'WHERE ' + where.join(' AND ') : ''} ORDER BY nombre`;
  return query<Producto>(sql, params);
}

export async function getProducto(id: number): Promise<Producto | null> {
  const rows = await query<Producto>('SELECT * FROM v_catalogo WHERE id_producto = $1', [id]);
  return rows[0] ?? null;
}

export async function getFamilias(): Promise<string[]> {
  const rows = await query<{ nombre: string }>('SELECT nombre FROM dim_familia ORDER BY nombre');
  return rows.map((r) => r.nombre);
}

export async function getDecadas(): Promise<string[]> {
  const rows = await query<{ etiqueta: string }>('SELECT etiqueta FROM dim_decada ORDER BY anio_ini');
  return rows.map((r) => r.etiqueta);
}

export async function getVendedor(id: number): Promise<Vendedor | null> {
  const rows = await query<Vendedor>(
    `SELECT v.id_vendedor, v.cuit, v.nombre_tienda, v.descripcion, v.reputacion,
            c.nombre AS ciudad, pr.nombre AS provincia, pa.nombre AS pais
     FROM dim_vendedor v
     JOIN dim_ciudad c    ON c.id_ciudad = v.id_ciudad
     JOIN dim_provincia pr ON pr.id_provincia = c.id_provincia
     JOIN dim_pais pa     ON pa.id_pais = pr.id_pais
     WHERE v.id_vendedor = $1`,
    [id],
  );
  return rows[0] ?? null;
}

export async function getProductosDeVendedor(id: number): Promise<Producto[]> {
  return query<Producto>('SELECT * FROM v_catalogo WHERE id_vendedor = $1 ORDER BY nombre', [id]);
}

// Métrica para mostrar la cardinalidad N:1 (compradores por vendedor)
export async function getCompradoresPorVendedor(id: number): Promise<number> {
  const rows = await query<{ n: string }>(
    'SELECT COUNT(*)::int AS n FROM dim_comprador WHERE id_vendedor = $1',
    [id],
  );
  return Number(rows[0]?.n ?? 0);
}
