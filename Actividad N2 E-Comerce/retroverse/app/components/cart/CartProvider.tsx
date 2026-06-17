'use client';

import { createContext, useContext, useEffect, useState, ReactNode } from 'react';

export type CartItem = {
  id: number;
  nombre: string;
  precio: number;
  cantidad: number;
};

type CartCtx = {
  items: CartItem[];
  add: (item: Omit<CartItem, 'cantidad'>) => void;
  remove: (id: number) => void;
  setQty: (id: number, cantidad: number) => void;
  clear: () => void;
  count: number;
  total: number;
};

const Ctx = createContext<CartCtx | null>(null);
const KEY = 'retroverse-cart';

export function CartProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<CartItem[]>([]);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    try {
      const raw = localStorage.getItem(KEY);
      if (raw) setItems(JSON.parse(raw));
    } catch {}
    setReady(true);
  }, []);

  useEffect(() => {
    if (ready) localStorage.setItem(KEY, JSON.stringify(items));
  }, [items, ready]);

  const add: CartCtx['add'] = (item) =>
    setItems((prev) => {
      const found = prev.find((i) => i.id === item.id);
      if (found) return prev.map((i) => (i.id === item.id ? { ...i, cantidad: i.cantidad + 1 } : i));
      return [...prev, { ...item, cantidad: 1 }];
    });

  const remove: CartCtx['remove'] = (id) => setItems((prev) => prev.filter((i) => i.id !== id));
  const setQty: CartCtx['setQty'] = (id, cantidad) =>
    setItems((prev) =>
      cantidad <= 0 ? prev.filter((i) => i.id !== id) : prev.map((i) => (i.id === id ? { ...i, cantidad } : i)),
    );
  const clear = () => setItems([]);

  const count = items.reduce((s, i) => s + i.cantidad, 0);
  const total = items.reduce((s, i) => s + i.precio * i.cantidad, 0);

  return (
    <Ctx.Provider value={{ items, add, remove, setQty, clear, count, total }}>{children}</Ctx.Provider>
  );
}

export function useCart() {
  const ctx = useContext(Ctx);
  if (!ctx) throw new Error('useCart must be used within CartProvider');
  return ctx;
}
