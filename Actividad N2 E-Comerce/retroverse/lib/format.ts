export function money(value: string | number): string {
  const n = typeof value === 'string' ? parseFloat(value) : value;
  return new Intl.NumberFormat('es-AR', {
    style: 'currency',
    currency: 'ARS',
    maximumFractionDigits: 0,
  }).format(n);
}

// Gradiente neón determinístico a partir de un id (placeholder sin imágenes externas).
const PALETTES = [
  ['#ff2e97', '#b537f2'],
  ['#05d9e8', '#b537f2'],
  ['#ff2e97', '#05d9e8'],
  ['#ffe600', '#ff2e97'],
  ['#b537f2', '#05d9e8'],
  ['#05d9e8', '#0a0a1f'],
];

export function thumbGradient(id: number): string {
  const [a, b] = PALETTES[id % PALETTES.length];
  return `linear-gradient(135deg, ${a} 0%, ${b} 100%)`;
}
