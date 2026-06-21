import Database from 'better-sqlite3';
import fs from 'node:fs';
import path from 'node:path';

// Conexión SQLite única (cacheada en globalThis para sobrevivir el HMR de Next dev).
// En el primer acceso aplica el esquema snowflake y, si está vacío, carga los seeds.
const g = globalThis as unknown as { __hextechDb?: Database.Database };

function bootstrap(db: Database.Database) {
  const dir = path.join(process.cwd(), 'db');
  db.exec(fs.readFileSync(path.join(dir, 'schema.sql'), 'utf8')); // idempotente (IF NOT EXISTS)
  const { n } = db.prepare('SELECT COUNT(*) AS n FROM dim_producto').get() as { n: number };
  if (n === 0) {
    db.exec(fs.readFileSync(path.join(dir, 'seed-dimensiones.sql'), 'utf8'));
    db.exec(fs.readFileSync(path.join(dir, 'seed-productos.sql'), 'utf8'));
  }
}

export function getDb(): Database.Database {
  if (g.__hextechDb) return g.__hextechDb;
  const db = new Database(path.join(process.cwd(), 'db', 'hextech.sqlite'));
  db.pragma('journal_mode = WAL');
  db.pragma('foreign_keys = ON');
  bootstrap(db);
  g.__hextechDb = db;
  return db;
}
