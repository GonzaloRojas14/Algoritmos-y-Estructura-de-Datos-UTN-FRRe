export const fmt = (n: number) => new Intl.NumberFormat('es-AR').format(n);

// Subcampos del campo CONTINENTE 'fecha' (ilustra el selector de campo de la Unidad 2).
export function desglosarFecha(iso: string) {
  const [anio, mes, dia] = iso.split('-').map(Number);
  const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
    'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
  return { dia, mes, anio, nombreMes: meses[mes - 1] ?? '' };
}
