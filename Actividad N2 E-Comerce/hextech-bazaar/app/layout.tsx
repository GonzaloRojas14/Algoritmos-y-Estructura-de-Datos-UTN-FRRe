import './globals.css';
import type { Metadata } from 'next';
import { Cinzel, Inter } from 'next/font/google';
import fs from 'node:fs';
import path from 'node:path';
import { CartProvider } from './components/cart-context';
import Navbar from './components/navbar';
import Footer from './components/footer';

const cinzel = Cinzel({ subsets: ['latin'], weight: ['600', '700'], variable: '--font-display' });
const inter = Inter({ subsets: ['latin'], variable: '--font-body' });

export const metadata: Metadata = {
  title: 'Hextech Bazaar · Fantasy Shop de League of Legends',
  description:
    'Tienda temática de campeones, aspectos e ítems de League of Legends. Demo académica (registro y clave, Unidad 2 — UTN-FRRe).',
};

function ddragonVersion(): string {
  try {
    return fs.readFileSync(path.join(process.cwd(), 'public', 'ddragon-version.txt'), 'utf8').trim();
  } catch {
    return '16.12.1';
  }
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es" className={`${cinzel.variable} ${inter.variable}`}>
      <body>
        <CartProvider>
          <Navbar />
          <main className="site">{children}</main>
          <Footer version={ddragonVersion()} />
        </CartProvider>
      </body>
    </html>
  );
}
