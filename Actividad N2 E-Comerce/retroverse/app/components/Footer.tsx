export default function Footer() {
  return (
    <footer className="footer">
      <div className="container">
        <div className="line" />
        <div className="row" style={{ flexWrap: 'wrap', gap: 12 }}>
          <span className="logo gradient-text">RETROVERSE</span>
          <span className="muted">
            Demo académica · Actividad Formativa N.º 2 · Algoritmos y Estructuras de Datos · UTN-FRRe
          </span>
        </div>
        <p className="muted" style={{ marginTop: 10 }}>
          ⚠️ Sitio de demostración: la navegación y el carrito son funcionales a nivel visual,
          pero <strong>no se procesan pagos reales</strong>.
        </p>
      </div>
    </footer>
  );
}
