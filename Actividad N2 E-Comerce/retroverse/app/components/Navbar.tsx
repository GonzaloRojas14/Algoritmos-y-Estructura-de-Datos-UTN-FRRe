import Link from 'next/link';
import CartBadge from './cart/CartBadge';

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="container navbar-inner">
        <Link href="/" className="logo gradient-text">RETROVERSE</Link>
        <div className="nav-links">
          <Link href="/">Catálogo</Link>
          <Link href="/#familias">Familias</Link>
          <Link href="/modelo">Modelo de datos</Link>
          <CartBadge />
        </div>
      </div>
    </nav>
  );
}
