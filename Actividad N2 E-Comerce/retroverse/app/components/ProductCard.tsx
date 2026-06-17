import Link from 'next/link';
import { Producto } from '@/lib/queries';
import { money, thumbGradient } from '@/lib/format';

export default function ProductCard({ p }: { p: Producto }) {
  return (
    <Link href={`/producto/${p.id_producto}`} className="card">
      <div className="card-thumb" style={{ background: thumbGradient(p.id_producto) }}>
        {p.imagen_url && (
          /* eslint-disable-next-line @next/next/no-img-element */
          <img className="thumb-img" src={p.imagen_url} alt={p.nombre} loading="lazy" />
        )}
        <span className="decade-tag">{p.decada}</span>
        <span className="badge" style={{ background: 'rgba(10,10,31,0.55)', borderColor: 'rgba(255,255,255,0.4)', color: '#fff' }}>
          {p.condicion}
        </span>
      </div>
      <div className="card-body">
        <span className="card-meta">{p.marca} · {p.categoria}</span>
        <span className="card-title">{p.nombre}</span>
        <div className="row" style={{ marginTop: 'auto' }}>
          <span className="price">{money(p.precio)}</span>
          <span className="card-meta">{p.stock > 0 ? `Stock: ${p.stock}` : 'Agotado'}</span>
        </div>
      </div>
    </Link>
  );
}
