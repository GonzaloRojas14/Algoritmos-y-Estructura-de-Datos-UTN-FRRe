import Link from 'next/link';
import type { Producto } from '@/lib/queries';
import { Price, RarityBadge } from './ui';

export default function ProductCard({ p }: { p: Producto }) {
  const esItem = p.familia_codigo === 'EQUIPO';
  return (
    <Link href={`/producto/${p.id_producto}`} className="card">
      <div className={`card-imgwrap${esItem ? ' is-item' : ''}`}>
        {p.rareza_codigo !== 'COMUN' && <RarityBadge codigo={p.rareza_codigo} nombre={p.rareza} />}
        <span className="region-tag">{p.region_lore}</span>
        {p.imagen && <img className="card-img" src={p.imagen} alt={p.nombre} loading="lazy" />}
      </div>
      <div className="card-body">
        <span className="card-cat">{p.categoria}</span>
        <span className="card-name">{p.nombre}</span>
        <span className="card-sub">{p.subtitulo}</span>
        <div className="card-foot">
          <Price precio={p.precio} moneda={p.moneda} small />
          <span className="muted" style={{ fontSize: '.7rem' }}>Stock: {p.stock}</span>
        </div>
      </div>
    </Link>
  );
}
