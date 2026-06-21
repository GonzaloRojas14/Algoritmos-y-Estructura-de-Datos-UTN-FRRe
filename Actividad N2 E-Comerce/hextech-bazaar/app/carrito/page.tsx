'use client';
import { useState } from 'react';
import Link from 'next/link';
import { useCart } from '../components/cart-context';
import { Price } from '../components/ui';
import { fmt } from '@/lib/format';

export default function Carrito() {
  const { items, setQty, remove, clear, count } = useCart();
  const [confirmado, setConfirmado] = useState(false);

  const totales = items.reduce<Record<string, number>>((acc, it) => {
    acc[it.moneda] = (acc[it.moneda] ?? 0) + it.precio * it.qty;
    return acc;
  }, {});

  if (confirmado) {
    return (
      <div className="container empty">
        <h1 className="gold-text" style={{ fontSize: '2rem' }}>¡Orden confirmada! ✦</h1>
        <p style={{ margin: '14px 0' }}>
          Esto es una <strong>demo académica</strong>: no se procesó ningún pago real.
          Tu pedido habría generado filas en la tabla de hechos <code>hecho_compra</code>.
        </p>
        <Link href="/catalogo" className="btn btn-primary">Seguir explorando</Link>
      </div>
    );
  }

  if (count === 0) {
    return (
      <div className="container empty">
        <h1 className="gold-text" style={{ fontSize: '1.8rem' }}>Tu carrito está vacío</h1>
        <p style={{ margin: '14px 0' }}>Agregá campeones, aspectos o ítems desde el catálogo.</p>
        <Link href="/catalogo" className="btn btn-primary">Ir al catálogo</Link>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '30px 24px 60px' }}>
      <span className="eyebrow">Carrito de compra</span>
      <h1 className="gold-text" style={{ fontSize: '2rem', margin: '6px 0 4px' }}>Tu botín ({count})</h1>
      <div className="divider"><span /></div>

      <div className="catalog" style={{ gridTemplateColumns: '1fr 320px', padding: 0 }}>
        <div>
          {items.map((it) => (
            <div className="cart-row" key={it.id}>
              <div className={it.esItem ? 'cart-thumb-item' : ''} style={{ borderRadius: 3, overflow: 'hidden' }}>
                {it.imagen && <img src={it.imagen} alt={it.nombre} />}
              </div>
              <div>
                <Link href={`/producto/${it.id}`} style={{ fontFamily: 'var(--display)', color: 'var(--gold-bright)' }}>{it.nombre}</Link>
                <div className="muted" style={{ fontSize: '.78rem' }}>{it.sku}</div>
                <button className="link-remove" onClick={() => remove(it.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', marginTop: 4 }}>Quitar</button>
              </div>
              <div className="qty">
                <button onClick={() => setQty(it.id, it.qty - 1)}>−</button>
                <span>{it.qty}</span>
                <button onClick={() => setQty(it.id, it.qty + 1)}>+</button>
              </div>
              <Price precio={it.precio * it.qty} moneda={it.moneda} small />
            </div>
          ))}
        </div>

        <aside className="cart-summary">
          <h3 style={{ fontFamily: 'var(--display)', color: 'var(--gold)', marginBottom: 10 }}>Resumen</h3>
          {Object.entries(totales).map(([moneda, total]) => (
            <div className="line" key={moneda}><span>Total en {moneda}</span><strong style={{ color: 'var(--gold-bright)' }}>{fmt(total)}</strong></div>
          ))}
          <div className="line total"><span>Ítems</span><span>{count}</span></div>
          <button className="btn btn-primary" style={{ width: '100%', marginTop: 16 }} onClick={() => { setConfirmado(true); clear(); }}>
            Finalizar compra
          </button>
          <button className="btn" style={{ width: '100%', marginTop: 10 }} onClick={clear}>Vaciar carrito</button>
          <p className="muted" style={{ fontSize: '.74rem', marginTop: 12, textAlign: 'center' }}>Demo — no se cobra dinero real.</p>
        </aside>
      </div>
    </div>
  );
}
