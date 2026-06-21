import Link from 'next/link';
import {
  getProductos, getFamilias, getCategorias, getRarezas, getRegiones, type Filtro,
} from '@/lib/queries';
import ProductCard from '../components/product-card';

type SP = { [k: string]: string | undefined };

function href(sp: SP, patch: SP): string {
  const merged: SP = { ...sp, ...patch };
  const qs = Object.entries(merged)
    .filter(([, v]) => v)
    .map(([k, v]) => `${k}=${encodeURIComponent(v as string)}`)
    .join('&');
  return `/catalogo${qs ? `?${qs}` : ''}`;
}

export default function Catalogo({ searchParams }: { searchParams: SP }) {
  const f: Filtro = {
    q: searchParams.q, familia: searchParams.familia, categoria: searchParams.categoria,
    rareza: searchParams.rareza, region: searchParams.region,
    orden: searchParams.orden as Filtro['orden'],
  };
  const productos = getProductos(f);
  const familias = getFamilias();
  const categorias = getCategorias();
  const rarezas = getRarezas().filter((r) => r.total > 0);
  const regiones = getRegiones();

  const activos = Object.entries(searchParams).filter(([k, v]) => v && k !== 'orden');

  const Facet = ({ param, codigo, nombre, total, color }:
    { param: keyof SP; codigo: string; nombre: string; total: number; color?: string | null }) => {
    const active = searchParams[param] === codigo;
    return (
      <Link className={`facet${active ? ' active' : ''}`} href={href(searchParams, { [param]: active ? undefined : codigo })}>
        <span style={color ? { color } : undefined}>{nombre}</span>
        <span className="n">{total}</span>
      </Link>
    );
  };

  return (
    <div className="container catalog">
      <aside className="filters">
        <form className="search" action="/catalogo" method="get">
          {f.familia && <input type="hidden" name="familia" value={f.familia} />}
          {f.categoria && <input type="hidden" name="categoria" value={f.categoria} />}
          <input type="text" name="q" placeholder="Buscar…" defaultValue={f.q ?? ''} />
          <button className="btn btn-teal" style={{ padding: '0 14px' }}>Ir</button>
        </form>

        <h4>Familia</h4>
        <div className="facets">
          {familias.map((x) => <Facet key={x.codigo} param="familia" {...x} />)}
        </div>

        <h4>Categoría</h4>
        <div className="facets">
          {categorias.map((x) => <Facet key={x.codigo} param="categoria" {...x} />)}
        </div>

        <h4>Rareza</h4>
        <div className="facets">
          {rarezas.map((x) => <Facet key={x.codigo} param="rareza" {...x} />)}
        </div>

        <h4>Región (lore)</h4>
        <div className="facets">
          {regiones.map((x) => <Facet key={x.codigo} param="region" {...x} />)}
        </div>
      </aside>

      <div className="catalog-main">
        <div className="toolbar">
          <div>
            <span className="eyebrow">Catálogo</span>
            <h2 style={{ fontSize: '1.5rem' }}>{productos.length} productos</h2>
          </div>
          <div className="chips">
            <span className="muted" style={{ fontSize: '.74rem', alignSelf: 'center' }}>Ordenar:</span>
            <Link className="chip" href={href(searchParams, { orden: undefined })}>Relevancia</Link>
            <Link className="chip" href={href(searchParams, { orden: 'precio_asc' })}>Precio ↑</Link>
            <Link className="chip" href={href(searchParams, { orden: 'precio_desc' })}>Precio ↓</Link>
          </div>
        </div>

        {activos.length > 0 && (
          <div className="chips" style={{ marginBottom: 18 }}>
            {activos.map(([k, v]) => (
              <span className="chip" key={k}>
                {k}: {v} <Link href={href(searchParams, { [k]: undefined })}>✕</Link>
              </span>
            ))}
            <Link className="chip" href="/catalogo" style={{ borderColor: 'var(--teal)' }}>Limpiar todo</Link>
          </div>
        )}

        {productos.length === 0 ? (
          <div className="empty">No hay productos para ese filtro. <Link href="/catalogo" style={{ color: 'var(--teal-bright)' }}>Ver todo</Link>.</div>
        ) : (
          <div className="grid">
            {productos.map((p) => <ProductCard key={p.id_producto} p={p} />)}
          </div>
        )}
      </div>
    </div>
  );
}
