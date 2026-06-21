// ============================================================================
//  fetch-ddragon.mjs
//  Descarga datos e imágenes OFICIALES de League of Legends desde Riot Data
//  Dragon (CDN público y gratuito) y genera db/seed-productos.sql para el
//  esquema snowflake de Hextech Bazaar.
//
//  Productos generados (mezcla skins + ítems):
//    · Campeones  → categoría CAMPEON  (familia COLECCIONABLE), moneda RP
//    · Aspectos   → categoría SKIN      (familia COLECCIONABLE), moneda RP
//    · Ítems      → ATAQUE/MAGIA/DEFENSA/BOTA (familia EQUIPO),  moneda Oro
//
//  Uso:  node scripts/fetch-ddragon.mjs
// ============================================================================

import { writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const DDRAGON = 'https://ddragon.leagueoflegends.com';
const LOCALE = 'es_ES';

const IMG = {
  loading: path.join(ROOT, 'public', 'img', 'loading'),
  splash:  path.join(ROOT, 'public', 'img', 'splash'),
  item:    path.join(ROOT, 'public', 'img', 'item'),
};

// Campeones curados con su región del lore de Runeterra y precio en RP.
const CHAMPS = [
  ['Ahri',        'IONIA',        6300], ['Yasuo',     'IONIA',        4800],
  ['Zed',         'IONIA',        4800], ['Irelia',    'IONIA',        4800],
  ['Darius',      'NOXUS',        4800], ['Katarina',  'NOXUS',        3150],
  ['Swain',       'NOXUS',        4800], ['Garen',     'DEMACIA',      3150],
  ['Lux',         'DEMACIA',      3150], ['Fiora',     'DEMACIA',      6300],
  ['Jinx',        'ZAUN',         4800], ['Ekko',      'ZAUN',         6300],
  ['Vi',          'PILTOVER',     4800], ['Caitlyn',   'PILTOVER',     4800],
  ['Jayce',       'PILTOVER',     4800], ['Ashe',      'FRELJORD',     1350],
  ['Sejuani',     'FRELJORD',     4800], ['Lissandra', 'FRELJORD',     4800],
  ['Azir',        'SHURIMA',      6300], ['Nasus',     'SHURIMA',      1350],
  ['Aatrox',      'SHURIMA',      4800], ['Thresh',    'SHADOW_ISLES', 6300],
  ['Senna',       'SHADOW_ISLES', 4800], ['MissFortune','BILGEWATER',  4800],
  ['Gangplank',   'BILGEWATER',   4800], ['Leona',     'TARGON',       4800],
  ['Kaisa',       'VOID',         6300],
];

const SKIN_TIERS = [
  { rareza: 'EPICO',      precio: 1350 },
  { rareza: 'LEGENDARIO', precio: 1820 },
];

const sqlStr = (v) => (v === null || v === undefined ? 'NULL' : `'${String(v).replace(/'/g, "''")}'`);
const stripHtml = (s) => (s || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const clamp = (s, n) => (s && s.length > n ? s.slice(0, n - 1).trimEnd() + '…' : s);

async function getJSON(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`HTTP ${r.status} ${url}`);
  return r.json();
}

async function download(url, dest) {
  if (existsSync(dest)) return true;
  try {
    const r = await fetch(url);
    if (!r.ok) return false;
    const buf = Buffer.from(await r.arrayBuffer());
    await writeFile(dest, buf);
    return true;
  } catch {
    return false;
  }
}

function itemCategoria(tags = []) {
  if (tags.includes('Boots')) return 'BOTA';
  if (tags.some((t) => ['SpellDamage', 'Mana', 'ManaRegen', 'CooldownReduction', 'AbilityHaste'].includes(t))) return 'MAGIA';
  if (tags.some((t) => ['CriticalStrike', 'AttackSpeed', 'Damage', 'LifeSteal'].includes(t))) return 'ATAQUE';
  if (tags.some((t) => ['Armor', 'Health', 'SpellBlock', 'HealthRegen'].includes(t))) return 'DEFENSA';
  return 'ATAQUE';
}

function itemRareza(total, esBota) {
  if (esBota) return 'COMUN';
  if (total >= 3300) return 'LEGENDARIO';
  if (total >= 2200) return 'EPICO';
  return 'COMUN';
}

async function main() {
  for (const dir of Object.values(IMG)) await mkdir(dir, { recursive: true });

  const versions = await getJSON(`${DDRAGON}/api/versions.json`);
  const V = versions[0];
  console.log(`Data Dragon versión: ${V} · locale ${LOCALE}`);

  const products = []; // {sku,nombre,subtitulo,desc,imagen,precio,moneda,stock,destacado,ref,cat,rar,reg}
  let destCount = 0;

  // -------- Campeones + aspectos --------
  for (const [id, region, precioChamp] of CHAMPS) {
    let detail;
    try {
      detail = await getJSON(`${DDRAGON}/cdn/${V}/data/${LOCALE}/champion/${id}.json`);
    } catch (e) {
      console.warn(`  ! sin detalle de ${id}: ${e.message}`);
      continue;
    }
    const c = detail.data[id];
    const ref0 = `${id}_0`;
    const okLoad = await download(`${DDRAGON}/cdn/img/champion/loading/${ref0}.jpg`, path.join(IMG.loading, `${ref0}.jpg`));
    await download(`${DDRAGON}/cdn/img/champion/splash/${ref0}.jpg`, path.join(IMG.splash, `${ref0}.jpg`));
    if (!okLoad) { console.warn(`  ! sin imagen de ${id}`); continue; }

    const champDestacado = destCount < 4 ? 1 : 0; if (champDestacado) destCount++;
    products.push({
      sku: `CHAMP-${c.key}`, nombre: c.name, subtitulo: c.title,
      desc: clamp(stripHtml(c.lore || c.blurb), 320),
      imagen: `/img/loading/${ref0}.jpg`, precio: precioChamp, moneda: 'RP',
      stock: ((Number(c.key) * 7) % 40) + 8, destacado: champDestacado,
      ref: ref0, cat: 'CAMPEON', rar: 'COMUN', reg: region,
    });
    console.log(`  ✓ campeón ${c.name}`);

    // hasta 2 aspectos no-default
    const skins = (c.skins || []).filter((s) => s.num > 0 && s.name && s.name !== 'default').slice(0, 2);
    for (let i = 0; i < skins.length; i++) {
      const s = skins[i];
      const ref = `${id}_${s.num}`;
      const ok = await download(`${DDRAGON}/cdn/img/champion/loading/${ref}.jpg`, path.join(IMG.loading, `${ref}.jpg`));
      await download(`${DDRAGON}/cdn/img/champion/splash/${ref}.jpg`, path.join(IMG.splash, `${ref}.jpg`));
      if (!ok) continue;
      const tier = SKIN_TIERS[Math.min(i, SKIN_TIERS.length - 1)];
      const skDest = destCount < 8 ? 1 : 0; if (skDest) destCount++;
      products.push({
        sku: `SKIN-${c.key}-${s.num}`, nombre: s.name, subtitulo: `Aspecto de ${c.name}`,
        desc: `Aspecto «${s.name}» para ${c.name}, ${c.title}. Coleccionable del universo de Runeterra.`,
        imagen: `/img/loading/${ref}.jpg`, precio: tier.precio, moneda: 'RP',
        stock: ((s.num * 13) % 30) + 5, destacado: skDest,
        ref, cat: 'SKIN', rar: tier.rareza, reg: region,
      });
      console.log(`    ✓ skin ${s.name}`);
    }
  }

  // -------- Ítems del juego --------
  const itemData = (await getJSON(`${DDRAGON}/cdn/${V}/data/${LOCALE}/item.json`)).data;
  const caps = { ATAQUE: 6, MAGIA: 6, DEFENSA: 6, BOTA: 4 };
  const count = { ATAQUE: 0, MAGIA: 0, DEFENSA: 0, BOTA: 0 };
  const entries = Object.entries(itemData)
    .filter(([, it]) => it.gold?.purchasable && it.maps?.['11'] && it.image?.full && !it.requiredChampion)
    .filter(([, it]) => !(it.tags || []).some((t) => ['Consumable', 'Trinket'].includes(t)))
    .sort((a, b) => (b[1].gold.total || 0) - (a[1].gold.total || 0));

  for (const [id, it] of entries) {
    const tags = it.tags || [];
    const cat = itemCategoria(tags);
    const esBota = cat === 'BOTA';
    const total = it.gold.total || 0;
    if (esBota) { if (total < 300 || total > 1500 || (it.depth || 1) < 2) continue; }
    else { if (total < 1300) continue; if (it.into && it.into.length > 0 && (it.depth || 1) < 3) continue; }
    if (count[cat] >= caps[cat]) continue;

    const ok = await download(`${DDRAGON}/cdn/${V}/img/item/${it.image.full}`, path.join(IMG.item, it.image.full));
    if (!ok) continue;
    count[cat]++;
    const itDest = destCount < 12 ? 1 : 0; if (itDest) destCount++;
    products.push({
      sku: `ITEM-${id}`, nombre: it.name, subtitulo: clamp(stripHtml(it.plaintext) || 'Ítem de la Grieta', 80),
      desc: clamp(stripHtml(it.description), 320),
      imagen: `/img/item/${it.image.full}`, precio: total, moneda: 'Oro',
      stock: ((Number(id) % 50) + 10), destacado: itDest,
      ref: id, cat, rar: itemRareza(total, esBota), reg: 'RUNETERRA',
    });
    console.log(`  ✓ ítem ${it.name} [${cat}]`);
    if (Object.keys(caps).every((k) => count[k] >= caps[k])) break;
  }

  // -------- Generar SQL --------
  const lines = [];
  lines.push('-- ============================================================================');
  lines.push(`-- HEXTECH BAZAAR · Seed de PRODUCTOS (autogenerado desde Data Dragon ${V})`);
  lines.push('-- NO editar a mano: regenerar con `node scripts/fetch-ddragon.mjs`.');
  lines.push('-- ============================================================================');
  lines.push('');
  for (const p of products) {
    lines.push(
      'INSERT OR IGNORE INTO dim_producto (sku,nombre,subtitulo,descripcion,imagen,precio,moneda,stock,destacado,ddragon_ref,id_categoria,id_rareza,id_region_lore) VALUES (' +
      `${sqlStr(p.sku)},${sqlStr(p.nombre)},${sqlStr(p.subtitulo)},${sqlStr(p.desc)},${sqlStr(p.imagen)},${p.precio},${sqlStr(p.moneda)},${p.stock},${p.destacado},${sqlStr(p.ref)},` +
      `(SELECT id_categoria FROM dim_categoria WHERE codigo=${sqlStr(p.cat)}),` +
      `(SELECT id_rareza FROM dim_rareza WHERE codigo=${sqlStr(p.rar)}),` +
      `(SELECT id_region_lore FROM dim_region_lore WHERE codigo=${sqlStr(p.reg)}));`
    );
  }

  // -------- Hechos de ejemplo (1 fila = 1 línea de una orden) --------
  const skus = products.map((p) => p.sku);
  const priceOf = Object.fromEntries(products.map((p) => [p.sku, p.precio]));
  const ordenes = [
    { orden: 1001, email: 'luna.rojas@hextech.gg',  fecha: '2026-06-05', medio: 'TARJETA',      items: [skus[0], skus[1]] },
    { orden: 1002, email: 'marco.vega@hextech.gg',  fecha: '2026-06-08', medio: 'RP_COMPRADO',  items: [skus[2], skus[3], skus[4]] },
    { orden: 1003, email: 'sofia.luz@hextech.gg',   fecha: '2026-06-12', medio: 'TARJETA',      items: [skus[5]] },
    { orden: 1004, email: 'diego.pena@hextech.gg',  fecha: '2026-06-18', medio: 'ESENCIA_AZUL', items: [skus[6], skus[7]] },
    { orden: 1005, email: 'faker.demo@hextech.gg',  fecha: '2026-06-20', medio: 'RP_COMPRADO',  items: [skus[8], skus[9]] },
  ];
  lines.push('');
  lines.push('-- Hechos de ejemplo (grano: 1 fila = 1 línea de una orden de compra)');
  for (const o of ordenes) {
    let linea = 0;
    for (const sku of o.items.filter(Boolean)) {
      linea++;
      const precio = priceOf[sku] || 0;
      lines.push(
        'INSERT OR IGNORE INTO hecho_compra (nro_orden,nro_linea,id_comprador,id_producto,id_tiempo,id_medio_pago,cantidad,precio_unitario,subtotal) VALUES (' +
        `${o.orden},${linea},` +
        `(SELECT id_comprador FROM dim_comprador WHERE email=${sqlStr(o.email)}),` +
        `(SELECT id_producto FROM dim_producto WHERE sku=${sqlStr(sku)}),` +
        `(SELECT id_tiempo FROM dim_tiempo WHERE fecha=${sqlStr(o.fecha)}),` +
        `(SELECT id_medio_pago FROM dim_medio_pago WHERE codigo=${sqlStr(o.medio)}),` +
        `1,${precio},${precio});`
      );
    }
  }

  await writeFile(path.join(ROOT, 'db', 'seed-productos.sql'), lines.join('\n') + '\n', 'utf8');
  await writeFile(path.join(ROOT, 'public', 'ddragon-version.txt'), V, 'utf8');
  console.log(`\nListo: ${products.length} productos (${destCount} destacados) → db/seed-productos.sql`);
}

main().catch((e) => { console.error(e); process.exit(1); });
