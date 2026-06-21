import Link from 'next/link';
import { getDestacados, getFamilias, getCategorias, getConteoTablas } from '@/lib/queries';
import ProductCard from './components/product-card';

export default function Home() {
  const destacados = getDestacados(10);
  const familias = getFamilias();
  const categorias = getCategorias();
  const conteo = getConteoTablas();
  const totalProductos = conteo.find((c) => c.tabla === 'dim_producto')?.filas ?? 0;

  return (
    <>
      <section className="hero">
        <div className="hero-bg" style={{ backgroundImage: 'url(/img/splash/Aatrox_0.jpg)' }} />
        <div className="container">
          <div className="hero-inner">
            <span className="eyebrow">Mercado de Runeterra</span>
            <h1 className="gold-text">El bazar Hextech de League&nbsp;of&nbsp;Legends</h1>
            <p>
              Coleccioná campeones y aspectos legendarios, o equipá tu inventario con los
              ítems más codiciados de la Grieta. {totalProductos} productos con datos e
              imágenes oficiales de Riot.
            </p>
            <div className="hero-cta">
              <Link href="/catalogo" className="btn btn-primary">Explorar catálogo</Link>
              <Link href="/catalogo?familia=COLECCIONABLE" className="btn btn-teal">Campeones &amp; Skins</Link>
            </div>
          </div>
        </div>
      </section>

      <section className="block">
        <div className="container">
          <span className="eyebrow">Dos familias</span>
          <h2 style={{ fontSize: '1.9rem', margin: '6px 0 4px' }}>Qué vas a encontrar</h2>
          <div className="divider"><span /></div>
          <div className="fam-grid">
            {familias.map((f) => (
              <div className="fam-card" key={f.codigo}>
                <h3>{f.nombre}</h3>
                <p>
                  {f.codigo === 'COLECCIONABLE'
                    ? 'Campeones y aspectos del universo de Runeterra, comprables con RP.'
                    : 'Ítems de juego de la Grieta del Invocador, comprables con oro.'}{' '}
                  <strong className="muted">({f.total} productos)</strong>
                </p>
                <div className="cats">
                  <Link href={`/catalogo?familia=${f.codigo}`}>Ver todo →</Link>
                  {categorias.filter((c) => c.familia === f.codigo).map((c) => (
                    <Link key={c.codigo} href={`/catalogo?categoria=${c.codigo}`}>{c.nombre} ({c.total})</Link>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="block" style={{ paddingTop: 0 }}>
        <div className="container">
          <div className="section-head">
            <div>
              <span className="eyebrow">Selección del bazar</span>
              <h2>Productos destacados</h2>
            </div>
            <Link href="/catalogo">Ver catálogo completo →</Link>
          </div>
          <div className="divider"><span /></div>
          <div className="grid">
            {destacados.map((p) => <ProductCard key={p.id_producto} p={p} />)}
          </div>
        </div>
      </section>
    </>
  );
}
