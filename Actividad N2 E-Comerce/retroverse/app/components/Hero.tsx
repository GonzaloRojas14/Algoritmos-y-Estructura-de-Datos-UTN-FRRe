import Link from 'next/link';

export default function Hero() {
  return (
    <section className="hero">
      <div className="sun" />
      <div className="container">
        <h1>
          Viajá al pasado <br />
          <span className="gradient-text">en tecnología retro</span>
        </h1>
        <p>
          Computadoras hogareñas, consolas, walkmans y vinilos. Piezas restauradas y de
          colección de los 70s, 80s y 90s. Bienvenido a RetroVerse.
        </p>
        <div style={{ marginTop: 26, display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
          <Link href="#catalogo" className="btn btn-primary">Explorar catálogo</Link>
          <Link href="/modelo" className="btn btn-ghost">Ver modelo de datos</Link>
        </div>
      </div>
      <div className="grid-floor" />
    </section>
  );
}
