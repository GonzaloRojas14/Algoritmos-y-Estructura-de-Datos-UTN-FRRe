import Link from 'next/link';
import Hero from './components/Hero';
import ProductCard from './components/ProductCard';
import { getCatalogo, getFamilias, getDecadas } from '@/lib/queries';

export const dynamic = 'force-dynamic';

type SP = { familia?: string; decada?: string; q?: string };

function buildHref(base: SP, patch: Partial<SP>) {
  const merged = { ...base, ...patch };
  const params = new URLSearchParams();
  if (merged.familia) params.set('familia', merged.familia);
  if (merged.decada) params.set('decada', merged.decada);
  if (merged.q) params.set('q', merged.q);
  const qs = params.toString();
  return `/${qs ? `?${qs}` : ''}#catalogo`;
}

export default async function Home({ searchParams }: { searchParams: SP }) {
  const sp: SP = {
    familia: searchParams.familia,
    decada: searchParams.decada,
    q: searchParams.q,
  };
  const [productos, familias, decadas] = await Promise.all([
    getCatalogo(sp),
    getFamilias(),
    getDecadas(),
  ]);

  return (
    <>
      <Hero />

      <section className="container" id="catalogo">
        <div className="section-title" id="familias">
          <h2>Catálogo</h2>
          <span className="line" />
        </div>

        {/* Filtro por familia */}
        <form className="filters" method="get" action="/">
          <Link href={buildHref({}, {})} className={`chip ${!sp.familia && !sp.decada ? 'active' : ''}`}>
            Todo
          </Link>
          {familias.map((f) => (
            <Link key={f} href={buildHref(sp, { familia: sp.familia === f ? undefined : f })}
              className={`chip ${sp.familia === f ? 'active' : ''}`}>
              {f}
            </Link>
          ))}
          <span style={{ width: 1, height: 24, background: 'var(--border)' }} />
          {decadas.map((d) => (
            <Link key={d} href={buildHref(sp, { decada: sp.decada === d ? undefined : d })}
              className={`chip ${sp.decada === d ? 'active' : ''}`}>
              {d}
            </Link>
          ))}
        </form>

        {/* Búsqueda */}
        <form className="filters" method="get" action="/">
          {sp.familia && <input type="hidden" name="familia" value={sp.familia} />}
          {sp.decada && <input type="hidden" name="decada" value={sp.decada} />}
          <input className="search-input" type="text" name="q" defaultValue={sp.q ?? ''}
            placeholder="Buscar por nombre o marca…" />
          <button className="btn btn-ghost" type="submit">Buscar</button>
        </form>

        {productos.length === 0 ? (
          <p className="muted" style={{ margin: '30px 0' }}>No se encontraron productos con esos filtros.</p>
        ) : (
          <div className="grid" style={{ marginTop: 18 }}>
            {productos.map((p) => (
              <ProductCard key={p.id_producto} p={p} />
            ))}
          </div>
        )}

        <p className="muted" style={{ marginTop: 22 }}>{productos.length} producto(s) en catálogo.</p>
      </section>
    </>
  );
}
