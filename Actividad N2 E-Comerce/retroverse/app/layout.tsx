import type { Metadata } from 'next';
import { Orbitron, Inter } from 'next/font/google';
import './globals.css';
import { CartProvider } from './components/cart/CartProvider';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

const orbitron = Orbitron({ subsets: ['latin'], variable: '--font-display', display: 'swap' });
const inter = Inter({ subsets: ['latin'], variable: '--font-body', display: 'swap' });

export const metadata: Metadata = {
  title: 'RetroVerse — Tienda de tecnología y objetos retro',
  description: 'Marketplace de objetos vintage, coleccionables y tecnología retro. Demo académica (Actividad N.º 2 — AyED UTN-FRRe).',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es" className={`${orbitron.variable} ${inter.variable}`}>
      <body>
        <CartProvider>
          <Navbar />
          <main>{children}</main>
          <Footer />
        </CartProvider>
      </body>
    </html>
  );
}
