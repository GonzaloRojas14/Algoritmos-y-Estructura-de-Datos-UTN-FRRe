'use client';

import { useState } from 'react';
import { useCart } from './CartProvider';

type Props = { id: number; nombre: string; precio: number; disabled?: boolean };

export default function AddToCartButton({ id, nombre, precio, disabled }: Props) {
  const { add } = useCart();
  const [added, setAdded] = useState(false);

  const onClick = () => {
    add({ id, nombre, precio });
    setAdded(true);
    setTimeout(() => setAdded(false), 1400);
  };

  return (
    <button className="btn btn-primary" onClick={onClick} disabled={disabled}>
      {disabled ? 'Sin stock' : added ? '✓ Agregado' : 'Agregar al carrito'}
    </button>
  );
}
