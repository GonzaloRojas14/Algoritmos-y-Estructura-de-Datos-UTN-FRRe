import Link from 'next/link';
import { notFound } from 'next/navigation';
import { getProducto, getRelacionados } from '@/lib/queries';
import { Price, RarityBadge } from '../../components/ui';
import AddToCart from '../../components/add-to-cart';
import ProductCard from '../../components/product-card';

export default function ProductoPage({ params }: { params: { id: string } }) {
  const p = getProducto(Number(params.id));
  if (!p) notFound();
  const esItem = p.familia_codigo === 'EQUIPO';
  const media = esItem ? p.imagen : `/img/splash/${p.ddragon_ref}.jpg`;
  const relacionados = getRelacionados(p, 4);

  return (
    <div className="container">
      <div className="breadcrumb">
        <Link href="/">Inicio</Link><span>›</span>
        <Link href={`/catalogo?familia=${p.familia_codigo}`}>{p.familia}</Link><span>›</span>
        <Link href={`/catalogo?categoria=${p.categoria_codigo}`}>{p.categoria}</Link><span>›</span>
        {p.nombre}
      </div>

      <div className="pdp">
        <div className={`pdp-media${esItem ? ' is-item' : ''}`}>
          {p.rareza_codigo !== 'COMUN' && <RarityBadge codigo={p.rareza_codigo} nombre={p.rareza} />}
          {media && <img src={media} alt={p.nombre} />}
        </div>

        <div className="pdp-info">
          <span className="eyebrow">{p.categoria} · {p.region_lore}</span>
          <h1 className="gold-text">{p.nombre}</h1>
          {p.subtitulo && <div className="sub">{p.subtitulo}</div>}

          <div className="spec-grid">
            <div className="spec"><div className="k">Familia</div><div className="v">{p.familia}</div></div>
            <div className="spec"><div className="k">Categoría</div><div className="v">{p.categoria}</div></div>
            <div className="spec"><div className="k">Rareza</div><div className="v" style={{ color: p.rareza_color ?? undefined }}>{p.rareza}</div></div>
            <div className="spec"><div className="k">Región (lore)</div><div className="v">{p.region_lore}</div></div>
            <div className="spec"><div className="k">SKU</div><div className="v" style={{ fontSize: '.9rem' }}>{p.sku}</div></div>
            <div className="spec"><div className="k">Stock</div><div className="v">{p.stock} u.</div></div>
          </div>

          {p.descripcion && <p className="desc">{p.descripcion}</p>}

          <div className="buybar">
            <Price precio={p.precio} moneda={p.moneda} />
            <AddToCart item={{ id: p.id_producto, sku: p.sku, nombre: p.nombre, imagen: p.imagen, precio: p.precio, moneda: p.moneda, esItem }} />
          </div>
        </div>
      </div>

      {relacionados.length > 0 && (
        <section className="block" style={{ paddingTop: 10 }}>
          <div className="section-head"><h2 style={{ fontSize: '1.4rem' }}>Más de {p.region_lore}</h2></div>
          <div className="divider"><span /></div>
          <div className="grid">{relacionados.map((r) => <ProductCard key={r.id_producto} p={r} />)}</div>
        </section>
      )}
    </div>
  );
}
