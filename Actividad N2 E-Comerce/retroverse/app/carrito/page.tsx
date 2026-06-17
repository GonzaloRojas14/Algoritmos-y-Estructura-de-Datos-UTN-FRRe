'use client';

import Link from 'next/link';
import { useState } from 'react';
import { useCart } from '../components/cart/CartProvider';
import { money } from '@/lib/format';

export default function CarritoPage() {
  const { items, setQty, remove, clear, total, count } = useCart();
  const [done, setDone] = useState(false);

  return (
    <div className="container" style={{ marginTop: 24 }}>
      <div className="section-title"><h2>Tu carrito</h2><span className="line" /></div>

      {items.length === 0 ? (
        <p className="muted" style={{ margin: '30px 0' }}>
          El carrito está vacío. <Link href="/" style={{ color: 'var(--neon-cyan)' }}>Volver al catálogo →</Link>
        </p>
      ) : (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: 24, marginTop: 18 }}>
          <div>
            {items.map((i) => (
              <div className="cart-row" key={i.id}>
                <div style={{ width: 60, height: 48, borderRadius: 8, background: 'var(--grad-main)' }} />
                <div>
                  <div className="card-title">{i.nombre}</div>
                  <div className="card-meta">{money(i.precio)} c/u</div>
                </div>
                <div className="qty">
                  <button onClick={() => setQty(i.id, i.cantidad - 1)}>−</button>
                  <span>{i.cantidad}</span>
                  <button onClick={() => setQty(i.id, i.cantidad + 1)}>+</button>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div className="price" style={{ fontSize: '1.05rem' }}>{money(i.precio * i.cantidad)}</div>
                  <button onClick={() => remove(i.id)} className="muted"
                    style={{ background: 'none', border: 'none', cursor: 'pointer', fontSize: '0.8rem' }}>
                    Quitar
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <div className="row"><span className="muted">Ítems</span><span>{count}</span></div>
            <div className="row" style={{ margin: '12px 0', fontSize: '1.3rem' }}>
              <span>Total</span><span className="price">{money(total)}</span>
            </div>
            <button className="btn btn-primary" style={{ width: '100%' }} onClick={() => setDone(true)}>
              Finalizar compra
            </button>
            <button className="btn btn-ghost" style={{ width: '100%', marginTop: 10 }} onClick={clear}>
              Vaciar carrito
            </button>
            <p className="muted" style={{ marginTop: 12, fontSize: '0.8rem' }}>
              RetroVerse es una demo: no se solicitan datos de pago ni se cobra nada.
            </p>
          </div>
        </div>
      )}

      {done && (
        <div className="modal-backdrop" onClick={() => setDone(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <h2 className="gradient-text">¡Compra simulada! 🎉</h2>
            <p className="muted" style={{ margin: '14px 0' }}>
              Esta es una página de demostración académica. No se procesó ningún pago real
              ni se almacenó información sensible.
            </p>
            <button className="btn btn-primary" onClick={() => { clear(); setDone(false); }}>
              Entendido
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
