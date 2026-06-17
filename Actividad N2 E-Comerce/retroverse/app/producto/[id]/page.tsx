import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getProducto } from '@/lib/queries';
import { money, thumbGradient } from '@/lib/format';
import AddToCartButton from '@/app/components/cart/AddToCartButton';

export const dynamic = 'force-dynamic';

export default async function ProductoPage({ params }: { params: { id: string } }) {
  const id = Number(params.id);
  if (Number.isNaN(id)) notFound();
  const p = await getProducto(id);
  if (!p) notFound();

  return (
    <div className="container">
      <p className="breadcrumb">
        <Link href="/">Catálogo</Link> / {p.familia} / <span className="muted">{p.nombre}</span>
      </p>

      <div className="detail">
        <div className="hero-img" style={{ background: thumbGradient(p.id_producto) }}>
          {p.imagen_url && (
            /* eslint-disable-next-line @next/next/no-img-element */
            <img className="thumb-img thumb-img--contain" src={p.imagen_url} alt={p.nombre} />
          )}
          <span className="display" style={{ fontSize: '3rem', color: '#fff', opacity: 0.92 }}>{p.decada}</span>
        </div>

        <div>
          <span className="badge">{p.condicion}</span>
          <h1 style={{ marginTop: 10 }}>{p.nombre}</h1>
          <p className="muted" style={{ marginTop: 8 }}>{p.descripcion}</p>

          <p className="price" style={{ fontSize: '2rem', margin: '18px 0' }}>{money(p.precio)}</p>

          <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            <AddToCartButton id={p.id_producto} nombre={p.nombre} precio={parseFloat(p.precio)} disabled={p.stock <= 0} />
            <Link href={`/tienda/${p.id_vendedor}`} className="btn btn-ghost">Ver tienda</Link>
          </div>

          <ul className="spec-list">
            <li><span className="k">SKU</span><span>{p.sku}</span></li>
            <li><span className="k">Familia</span><span>{p.familia}</span></li>
            <li><span className="k">Categoría</span><span>{p.categoria}</span></li>
            <li><span className="k">Marca</span><span>{p.marca}</span></li>
            <li><span className="k">Década</span><span>{p.decada}</span></li>
            <li><span className="k">Condición</span><span>{p.condicion}</span></li>
            <li><span className="k">Stock</span><span>{p.stock} unidad(es)</span></li>
            <li><span className="k">Vendedor</span><span>{p.nombre_tienda}</span></li>
          </ul>

          <div className="note">
            🛈 Demo académica: agregar al carrito es funcional, pero no se procesan pagos reales.
          </div>
        </div>
      </div>
    </div>
  );
}
