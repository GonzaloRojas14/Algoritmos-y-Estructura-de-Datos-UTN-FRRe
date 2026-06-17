import { query } from '@/lib/db';

export const dynamic = 'force-dynamic';

const REGISTRO_MAESTRO = [
  ['id_comprador', 'SERIAL', 'Contenido', 'PK — Primaria, Simple'],
  ['dni', 'VARCHAR(11)', 'Contenido', 'Candidata natural, Simple (UNIQUE)'],
  ['email', 'VARCHAR(120)', 'Contenido', 'Candidata natural, Simple (UNIQUE)'],
  ['nombre', 'VARCHAR(60)', 'Contenido', '—'],
  ['apellido', 'VARCHAR(60)', 'Contenido', 'Secundaria (índice)'],
  ['fecha_nacimiento', 'DATE', 'Continente (Día/Mes/Año)', '—'],
  ['fecha_alta', 'DATE', 'Contenido', '—'],
  ['id_ciudad', 'INT', 'Contenido', 'FK → dim_ciudad'],
  ['id_vendedor', 'INT', 'Contenido', 'FK → dim_vendedor (N:1)'],
];

const CLAVES = [
  ['Primaria (PK)', 'Identifica único e irrepetible', 'dim_comprador.id_comprador'],
  ['Foránea (FK)', 'Puente hacia otro registro/archivo', 'dim_comprador.id_vendedor'],
  ['Secundaria', 'No única; agrupa / ordena / busca', 'idx_comprador_apellido'],
  ['Simple', 'Un único campo contenido', 'dni, sku, codigo_iso'],
  ['Compleja / compuesta', 'Campo continente / varias columnas', 'hecho_venta (nro_pedido, nro_linea)'],
];

export default async function ModeloPage() {
  // Conteo en vivo de filas por tabla del esquema snowflake
  const counts = await query<{ tabla: string; n: string }>(`
    SELECT 'dim_comprador' AS tabla, COUNT(*)::text AS n FROM dim_comprador
    UNION ALL SELECT 'dim_vendedor', COUNT(*)::text FROM dim_vendedor
    UNION ALL SELECT 'dim_producto', COUNT(*)::text FROM dim_producto
    UNION ALL SELECT 'hecho_venta', COUNT(*)::text FROM hecho_venta
  `);

  return (
    <div className="container" style={{ marginTop: 24 }}>
      <div className="section-title"><h2>Modelo de datos · Esquema Snowflake</h2><span className="line" /></div>
      <p className="muted" style={{ maxWidth: 760 }}>
        RetroVerse usa un modelo dimensional <strong>snowflake</strong>: una tabla de hechos
        central (<code>hecho_venta</code>) rodeada de dimensiones <em>normalizadas en cadena</em>
        (producto → categoría → familia; comprador → ciudad → provincia → país).
      </p>

      <div className="note" style={{ marginTop: 16 }}>
        Registro maestro: <strong>dim_comprador</strong> (cliente-comprador). Cardinalidad
        <strong> N:1</strong> → muchos compradores compran a un vendedor.
      </div>

      <div className="section-title"><h2>Registro maestro: dim_comprador</h2><span className="line" /></div>
      <div style={{ overflowX: 'auto' }}>
        <table className="data-table">
          <thead><tr><th>Campo</th><th>Tipo</th><th>Contenido/Continente</th><th>Rol de clave</th></tr></thead>
          <tbody>
            {REGISTRO_MAESTRO.map((r) => (
              <tr key={r[0]}><td><code>{r[0]}</code></td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="section-title"><h2>Tipos de clave presentes</h2><span className="line" /></div>
      <div style={{ overflowX: 'auto' }}>
        <table className="data-table">
          <thead><tr><th>Tipo</th><th>Definición</th><th>Ejemplo en RetroVerse</th></tr></thead>
          <tbody>
            {CLAVES.map((r) => (
              <tr key={r[0]}><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td><code>{r[2]}</code></td></tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="section-title"><h2>Datos cargados (en vivo desde PostgreSQL)</h2><span className="line" /></div>
      <div className="filters">
        {counts.map((c) => (
          <span key={c.tabla} className="chip active">{c.tabla}: {c.n}</span>
        ))}
      </div>
      <p className="muted" style={{ marginTop: 10, marginBottom: 30 }}>
        Estos conteos se leen en tiempo real del esquema <code>retroverse</code> en PostgreSQL,
        demostrando que el modelo está vivo y la app lo consulta.
      </p>
    </div>
  );
}
