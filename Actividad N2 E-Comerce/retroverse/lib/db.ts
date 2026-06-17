import { Pool } from 'pg';

// Pool único reutilizado entre requests (evita agotar conexiones en dev/HMR).
const globalForPg = globalThis as unknown as { pgPool?: Pool };

export const pool =
  globalForPg.pgPool ??
  new Pool({
    connectionString:
      process.env.DATABASE_URL ??
      'postgresql://retroverse:retroverse@localhost:5432/retroverse',
    // Fija el search_path al esquema snowflake del proyecto.
    options: '-c search_path=retroverse',
    max: 5,
  });

if (process.env.NODE_ENV !== 'production') globalForPg.pgPool = pool;

export async function query<T = any>(text: string, params?: any[]): Promise<T[]> {
  const res = await pool.query(text, params);
  return res.rows as T[];
}
