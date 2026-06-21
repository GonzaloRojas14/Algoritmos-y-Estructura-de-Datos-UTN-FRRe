export default function Footer({ version }: { version: string }) {
  return (
    <footer className="footer">
      <div className="container">
        <div className="disc">
          <b>HEXTECH BAZAAR</b> — Fantasy Shop temático de League of Legends.<br />
          Demo académica · Actividad Formativa N.º 2, Algoritmos y Estructuras de Datos (UTN-FRRe, ISI 2026).
          Modelo de <b>registro</b> y <b>clave</b> (Unidad 2). <b>No procesa pagos reales.</b>
        </div>
        <div className="muted" style={{ textAlign: 'right', fontSize: '.78rem' }}>
          Datos e imágenes: Riot Data Dragon v{version}.<br />
          League of Legends © Riot Games. Uso educativo, sin fines de lucro.
        </div>
      </div>
    </footer>
  );
}
