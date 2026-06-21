import { fmt } from '@/lib/format';

// Marca hexagonal Hextech (logo).
export function HexMark({ size = 34 }: { size?: number }) {
  return (
    <svg className="mark" width={size} height={size * 1.12} viewBox="0 0 56 64" fill="none" aria-hidden>
      <path d="M28 1l26 15v32L28 63 2 48V16z" stroke="#c8aa6e" strokeWidth="2" fill="rgba(10,200,185,.08)" />
      <path d="M28 13l15 9v18l-15 9-15-9V22z" stroke="#0ac8b9" strokeWidth="1.5" fill="none" />
      <circle cx="28" cy="32" r="4.5" fill="#c8aa6e" />
    </svg>
  );
}

// Moneda: RP (azul/teal) u Oro (dorado).
export function Coin({ moneda }: { moneda: string }) {
  const oro = moneda === 'Oro';
  return (
    <svg className="coin" viewBox="0 0 24 24" aria-hidden>
      <circle cx="12" cy="12" r="10" fill={oro ? '#c8aa6e' : '#0ac8b9'} stroke={oro ? '#785a28' : '#0596aa'} strokeWidth="2" />
      <circle cx="12" cy="12" r="5" fill="none" stroke={oro ? '#785a28' : '#04222a'} strokeWidth="2" />
    </svg>
  );
}

export function Price({ precio, moneda, small }: { precio: number; moneda: string; small?: boolean }) {
  return (
    <span className="price">
      <Coin moneda={moneda} />
      {fmt(precio)} {!small && <small>{moneda}</small>}
    </span>
  );
}

const RAREZA_COLOR: Record<string, string> = {
  COMUN: '#9aa4af', EPICO: '#3b82f6', LEGENDARIO: '#a855f7', MITICO: '#f59e0b', ULTIMATE: '#ef4444',
};
export function RarityBadge({ codigo, nombre }: { codigo: string; nombre: string }) {
  return <span className="badge" style={{ color: RAREZA_COLOR[codigo] ?? '#9aa4af' }}>{nombre}</span>;
}
