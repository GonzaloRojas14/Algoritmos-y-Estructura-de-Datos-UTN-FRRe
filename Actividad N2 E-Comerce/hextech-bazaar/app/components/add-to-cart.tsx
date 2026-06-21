'use client';
import { useState } from 'react';
import { useCart, CartItem } from './cart-context';

export default function AddToCart({ item }: { item: Omit<CartItem, 'qty'> }) {
  const { add } = useCart();
  const [done, setDone] = useState(false);
  return (
    <button
      className="btn btn-primary"
      onClick={() => { add(item); setDone(true); setTimeout(() => setDone(false), 1600); }}
    >
      {done ? '✓ Añadido' : 'Añadir al carrito'}
    </button>
  );
}
