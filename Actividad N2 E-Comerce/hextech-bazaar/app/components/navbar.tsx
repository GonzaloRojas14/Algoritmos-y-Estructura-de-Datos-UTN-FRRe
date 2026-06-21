'use client';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useCart } from './cart-context';
import { HexMark } from './ui';

const LINKS = [
  ['/', 'Inicio'],
  ['/catalogo', 'Catálogo'],
  ['/catalogo?familia=COLECCIONABLE', 'Campeones & Skins'],
  ['/catalogo?familia=EQUIPO', 'Ítems'],
];

export default function Navbar() {
  const path = usePathname();
  const { count } = useCart();
  return (
    <nav className="nav">
      <div className="container nav-inner">
        <Link href="/" className="brand">
          <HexMark />
          <b>Hextech Bazaar<small>Fantasy Shop · Runeterra</small></b>
        </Link>
        <div className="nav-links">
          {LINKS.map(([href, label]) => (
            <Link key={href} href={href} className={path === href ? 'active' : ''}>{label}</Link>
          ))}
          <Link href="/carrito" className="cart-pill">
            🛒 Carrito {count > 0 && <span className="cart-count">{count}</span>}
          </Link>
        </div>
      </div>
    </nav>
  );
}
