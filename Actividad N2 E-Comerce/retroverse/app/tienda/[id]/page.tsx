import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getVendedor, getProductosDeVendedor, getCompradoresPorVendedor } from '@/lib/queries';
import ProductCard from '@/app/components/ProductCard';

export const dynamic = 'force-dynamic';

export default async function TiendaPage({ params }: { params: { id: string } }) {
  const id = Number(params.id);
  if (Number.isNaN(id)) notFound();

  const [v, productos, compradores] = await Promise.all([
    getVendedor(id),
    getProductosDeVendedor(id),
    getCompradoresPorVendedor(id),
  ]);
  if (!v) notFound();

  return (
    <div className="container">
      <p className="breadcrumb"><Link href="/">Catálogo</Link> / Tienda / <span className="muted">{v.nombre_tienda}</span></p>

      <div className="cart-summary" style={{ marginTop: 18 }}>
        <h1 className="gradient-text" style={{ fontSize: '1.8rem' }}>{v.nombre_tienda}</h1>
        <p className="muted" style={{ marginTop: 8 }}>{v.descripcion}</p>
        <ul className="spec-list" style={{ maxWidth: 480 }}>
          <li><span className="k">CUIT</span><span>{v.cuit}</span></li>
          <li><span className="k">Ubicación</span><span>{v.ciudad}, {v.provincia} ({v.pais})</span></li>
          <li><span className="k">Reputación</span><span>⭐ {v.reputacion} / 5.0</span></li>
          <li><span className="k">Compradores asociados</span><span>{compradores}</span></li>
        </ul>
        <div className="note">
          🔗 Relación <strong>N:1</strong>: estos <strong>{compradores}</strong> compradores
          están asociados a este único vendedor (registro maestro <code>dim_comprador.id_vendedor</code>).
        </div>
      </div>

      <div className="section-title"><h2>Productos de la tienda</h2><span className="line" /></div>
      <div className="grid" style={{ marginTop: 18 }}>
        {productos.map((p) => <ProductCard key={p.id_producto} p={p} />)}
      </div>
    </div>
  );
}
