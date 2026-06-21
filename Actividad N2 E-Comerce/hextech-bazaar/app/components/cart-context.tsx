'use client';
import { createContext, useContext, useEffect, useState, ReactNode } from 'react';

export type CartItem = {
  id: number; sku: string; nombre: string; imagen: string | null;
  precio: number; moneda: string; esItem: boolean; qty: number;
};

type CartCtx = {
  items: CartItem[];
  add: (it: Omit<CartItem, 'qty'>) => void;
  setQty: (id: number, qty: number) => void;
  remove: (id: number) => void;
  clear: () => void;
  count: number;
};

const Ctx = createContext<CartCtx | null>(null);
const KEY = 'hextech-cart-v1';

export function CartProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<CartItem[]>([]);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    try { const raw = localStorage.getItem(KEY); if (raw) setItems(JSON.parse(raw)); } catch {}
    setReady(true);
  }, []);
  useEffect(() => { if (ready) localStorage.setItem(KEY, JSON.stringify(items)); }, [items, ready]);

  const add: CartCtx['add'] = (it) =>
    setItems((prev) => {
      const found = prev.find((p) => p.id === it.id);
      if (found) return prev.map((p) => (p.id === it.id ? { ...p, qty: p.qty + 1 } : p));
      return [...prev, { ...it, qty: 1 }];
    });
  const setQty: CartCtx['setQty'] = (id, qty) =>
    setItems((prev) => prev.map((p) => (p.id === id ? { ...p, qty: Math.max(1, qty) } : p)));
  const remove: CartCtx['remove'] = (id) => setItems((prev) => prev.filter((p) => p.id !== id));
  const clear = () => setItems([]);
  const count = items.reduce((a, p) => a + p.qty, 0);

  return <Ctx.Provider value={{ items, add, setQty, remove, clear, count }}>{children}</Ctx.Provider>;
}

export function useCart() {
  const c = useContext(Ctx);
  if (!c) throw new Error('useCart fuera de CartProvider');
  return c;
}
