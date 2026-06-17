'use client';

import Link from 'next/link';
import { useCart } from './CartProvider';

export default function CartBadge() {
  const { count } = useCart();
  return (
    <Link href="/carrito" className="cart-pill">
      🛒 Carrito
      <span className="cart-count">{count}</span>
    </Link>
  );
}
