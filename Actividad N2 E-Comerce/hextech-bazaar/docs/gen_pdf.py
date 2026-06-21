#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el PDF de entrega de la Actividad N.º 2 — Hextech Bazaar.
Documento profesional y educativo, estructurado según lo que pide la cátedra:
objetivos, temática, uso de IA, diseño del registro y su clave, justificación del
diseño, entregables y criterios de evaluación. Tipos de dato conceptuales
(entero, real, cadena, booleano, fecha). Sin detalles de herramientas/infraestructura.

Uso:  python3 docs/gen_pdf.py  [URL_publica]
"""
import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, NextPageTemplate, Image, ListFlowable, ListItem, KeepTogether)

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', 'public', 'img')
OUT = os.path.join(HERE, '..', '..', 'Hextech Bazaar - Documentacion Actividad N2.pdf')
URL = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
    'HEXTECH_URL', 'https://transmission-deeper-obj-likes.trycloudflare.com')

# ---- Paleta Hextech ----
NAVY  = colors.HexColor('#0a1428'); NAVY2 = colors.HexColor('#102a43')
GOLD  = colors.HexColor('#c8aa6e'); GOLDD = colors.HexColor('#785a28'); GOLDL = colors.HexColor('#f0e6d2')
TEAL  = colors.HexColor('#0596aa'); INK   = colors.HexColor('#1f2733'); GREY = colors.HexColor('#5a6573')
PARCH = colors.HexColor('#f6f2e8'); BORDER = colors.HexColor('#d9cdb0'); TEALBG = colors.HexColor('#eafaf8')
CHK   = '<font name="ZapfDingbats" color="#3a7d44">4</font>'  # ✔ verde

def imgf(*p):
    f = os.path.join(IMG, *p)
    return f if os.path.exists(f) else None

H1   = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=15.5, textColor=GOLDD, spaceBefore=15, spaceAfter=6, leading=18)
H2   = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11, textColor=TEAL, spaceBefore=8, spaceAfter=3, leading=14)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=10, textColor=INK, leading=14.5, alignment=TA_JUSTIFY, spaceAfter=6)
LEAD = ParagraphStyle('LEAD', parent=BODY, textColor=GREY, fontSize=10.3)
SMALL= ParagraphStyle('SMALL', parent=BODY, fontSize=8.4, textColor=GREY, alignment=TA_LEFT)
QUOTE= ParagraphStyle('QUOTE', parent=BODY, fontName='Helvetica-Oblique', textColor=NAVY2, leftIndent=10, rightIndent=6, spaceBefore=1, spaceAfter=8, leading=14)
CELL = ParagraphStyle('CELL', fontName='Helvetica', fontSize=8.6, textColor=INK, leading=11)
CELLB= ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
CELLH= ParagraphStyle('CELLH', parent=CELL, fontName='Helvetica-Bold', textColor=GOLDL)
CELLC= ParagraphStyle('CELLC', fontName='Courier', fontSize=8.3, textColor=NAVY2, leading=11)
CALL = ParagraphStyle('CALL', parent=BODY, fontSize=9.6, leading=13.5, alignment=TA_LEFT, spaceAfter=2)

def P(t, s=BODY): return Paragraph(t, s)
def bullets(items, s=BODY):
    return ListFlowable([ListItem(P(t, s)) for t in items], bulletType='bullet', start='•', leftIndent=14)

def checklist(items):
    rows = [[P(CHK, CELL), P(t, CELL)] for t in items]
    t = Table(rows, colWidths=[8*mm, 162*mm])
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),2),
                           ('BOTTOMPADDING',(0,0),(-1,-1),2),('LEFTPADDING',(0,0),(0,-1),0)]))
    return t

def callout(parts, accent=TEAL, bg=TEALBG):
    body = [P(x, CALL) for x in parts]
    inner = Table([[body]], colWidths=[168*mm])
    inner.setStyle(TableStyle([('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),10),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('BACKGROUND',(0,0),(-1,-1),bg),('LINEBEFORE',(0,0),(0,-1),3,accent)]))
    return inner

def tbl(data, widths):
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('GRID',(0,0),(-1,-1),0.5,BORDER),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, PARCH]),
        ('BACKGROUND',(0,0),(-1,0),NAVY),('LINEBELOW',(0,0),(-1,0),1,GOLD)]))
    return t

def img_row():
    picks = [('loading','Ahri_0.jpg'), ('loading','Jinx_0.jpg'), ('loading','Yasuo_0.jpg'),
             ('item','3031.png'), ('item','3089.png')]
    row, widths = [], []
    for kind, name in picks:
        f = imgf(kind, name)
        if not f: continue
        h = 33*mm if kind == 'loading' else 21*mm
        w = h * (0.55 if kind == 'loading' else 1.0)
        row.append(Image(f, width=w, height=h)); widths.append(w + 4*mm)
    if not row: return None
    t = Table([row], colWidths=widths)
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'BOTTOM'),
                           ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2)]))
    return t

# ----------------------------- PORTADA -----------------------------
def cover(c, doc):
    W, Hh = A4
    c.saveState(); c.setFillColor(NAVY); c.rect(0, 0, W, Hh, fill=1, stroke=0)
    sp = imgf('splash', 'Aatrox_0.jpg') or imgf('splash', 'Kaisa_0.jpg')
    if sp:
        ir = ImageReader(sp); iw, ih = ir.getSize()
        bandh = Hh * 0.46; scale = max(W/iw, bandh/ih); dw, dh = iw*scale, ih*scale
        c.drawImage(ir, (W-dw)/2, Hh-bandh + (bandh-dh)/2, dw, dh, mask='auto', preserveAspectRatio=False)
        c.setFillColor(NAVY)
        for i in range(28):
            c.setFillAlpha(i/40.0); c.rect(0, Hh-bandh + i*(bandh/28), W, bandh/28+1, fill=1, stroke=0)
        c.setFillAlpha(1)
    c.setStrokeColor(GOLD); c.setLineWidth(1.4); c.line(20*mm, Hh*0.50, W-20*mm, Hh*0.50)
    c.setStrokeColor(TEAL); c.setLineWidth(0.6); c.line(20*mm, Hh*0.50-2, W-20*mm, Hh*0.50-2)
    c.saveState(); c.translate(W/2, Hh*0.50); c.rotate(45); c.setFillColor(GOLD); c.rect(-4,-4,8,8,fill=1,stroke=0); c.restoreState()
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 9)
    c.drawCentredString(W/2, Hh*0.45, 'F A N T A S Y   S H O P   ·   R U N E T E R R A')
    c.setFillColor(GOLDL); c.setFont('Helvetica-Bold', 40); c.drawCentredString(W/2, Hh*0.385, 'HEXTECH BAZAAR')
    c.setFillColor(colors.white); c.setFont('Helvetica', 13); c.drawCentredString(W/2, Hh*0.335, 'e-Commerce temático de League of Legends')
    c.setFillColor(GREY); c.setFont('Helvetica', 10)
    c.drawCentredString(W/2, Hh*0.30, 'Actividad Formativa N.º 2 — Diseñando un e-Commerce con IA')
    c.drawCentredString(W/2, Hh*0.275, 'Algoritmos y Estructuras de Datos · UTN-FRRe · ISI 2026')
    c.setStrokeColor(GOLD); c.setLineWidth(1); c.roundRect(W/2-78*mm, Hh*0.165, 156*mm, 18*mm, 3, fill=0, stroke=1)
    c.setFillColor(GOLD); c.setFont('Helvetica-Bold', 8.5); c.drawCentredString(W/2, Hh*0.205, 'URL DE LA APLICACIÓN PUBLICADA')
    c.setFillColor(colors.white); c.setFont('Courier-Bold', 11); c.drawCentredString(W/2, Hh*0.178, URL)
    c.setFillColor(GREY); c.setFont('Helvetica-Oblique', 7.5)
    c.drawCentredString(W/2, Hh*0.072, 'Demo académica — no procesa pagos reales. Modelo para demostrar los conceptos de registro y clave (Unidad 2).')
    c.drawCentredString(W/2, Hh*0.052, 'Imágenes y datos de League of Legends © Riot Games — uso educativo, sin fines de lucro.')
    c.restoreState()

def content_page(c, doc):
    W, Hh = A4
    c.saveState()
    c.setStrokeColor(GOLD); c.setLineWidth(1.1); c.line(18*mm, Hh-16*mm, W-18*mm, Hh-16*mm)
    c.setFillColor(GOLDD); c.setFont('Helvetica-Bold', 7.5); c.drawString(18*mm, Hh-14.4*mm, 'HEXTECH BAZAAR')
    c.setFillColor(GREY); c.setFont('Helvetica', 7.5); c.drawRightString(W-18*mm, Hh-14.4*mm, 'Actividad Formativa N.º 2 · UTN-FRRe')
    c.setStrokeColor(BORDER); c.setLineWidth(0.6); c.line(18*mm, 15*mm, W-18*mm, 15*mm)
    c.setFillColor(GREY); c.setFont('Helvetica', 8); c.drawCentredString(W/2, 11*mm, f'— {doc.page} —')
    c.restoreState()

# ----------------------------- CONTENIDO -----------------------------
def build():
    S = [NextPageTemplate('content'), PageBreak()]

    # Guía + recordatorio
    S += [P('Cómo leer este documento', H1),
        P('Esta documentación acompaña a <b>Hextech Bazaar</b>, el e-commerce diseñado para la '
          'Actividad Formativa N.º 2. Se recomienda leer todos los apartados:'),
        checklist([
            '<b>Objetivos</b> de la actividad.',
            '<b>Temática</b> elegida (entre las propuestas y la opción libre).',
            '<b>Requisitos obligatorios</b> de uso de IA.',
            '<b>Diseño del registro principal</b> y su <b>clave</b> (eje de la evaluación).',
            '<b>Entregables solicitados</b> y <b>criterios de evaluación</b>.',
        ]),
        Spacer(1,6),
        callout([
            '<b>Importante.</b> La entrega reúne en un mismo enlace la información que muestra: '
            '(1) la <b>URL de la aplicación</b> generada, (2) un <b>video demostrativo</b>, '
            '(3) el <b>diseño del registro principal con su clave</b> correspondiente, y '
            '(4) los <b>prompts</b> utilizados durante el proceso.'],
            accent=GOLD, bg=PARCH)]

    # 1. Objetivos
    S += [P('1 · Objetivos de la actividad', H1),
        P('La actividad aplica los conceptos de la <b>Unidad 2</b>. En concreto, se busca demostrar:'),
        bullets([
            'La definición y el uso de <b>estructuras tipo registro</b>.',
            'La identificación y el diseño de una <b>clave</b> para organizar y diferenciar datos.',
            'La comprensión de cómo <b>modelar información</b> para resolver un problema real (una tienda).',
        ])]

    # 2. Temática
    S += [P('2 · Temática elegida', H1),
        P('La consigna propone temáticas creativas (EcoSwap, MundialMarket, RetroVerse, PetMatch, '
          '<b>Fantasy Shop</b> y tema libre). Se eligió la <b>Opción 5 — Fantasy Shop</b>: un mercado '
          'inspirado en mundos de fantasía y <i>gaming</i>. La ambientación concreta es el videojuego '
          '<b>League of Legends</b> y su universo, <b>Runeterra</b>.')]

    # 3. El e-commerce
    S += [P('3 · El e-commerce: Hextech Bazaar', H1),
        P('<b>Hextech Bazaar</b> es una tienda del universo de Runeterra que ofrece dos <b>familias</b> '
          'de productos: <b>Coleccionables</b> (campeones y aspectos/<i>skins</i>) y <b>Equipo</b> '
          '(ítems de juego). Los productos usan datos e imágenes <b>oficiales del juego</b>. El sitio es '
          'navegable entre vistas (portada, catálogo con filtros, detalle de producto y carrito) y '
          '<b>no procesa pagos reales</b>: su objetivo es demostrar los conceptos de registro y clave.')]
    r = img_row()
    if r: S += [Spacer(1,4), r, P('Muestra del catálogo: campeones (coleccionables) e ítems de juego (equipo).', SMALL)]

    # 4. Uso de IA
    S += [P('4 · Requisitos obligatorios de uso de IA', H1),
        P('Se utilizó una herramienta de Inteligencia Artificial (<b>Claude</b>) para generar ideas, '
          'diseñar la aplicación y definir el registro. Cumpliendo la consigna:'),
        bullets([
            'Se <b>presentan todos los prompts</b> utilizados, en orden (apartado 9).',
            'El prompt principal incluye <b>explícitamente</b> el pedido del <b>diseño del registro</b> '
            'y la <b>definición de la clave</b>.',
            'Se incluyen también las <b>mejoras</b> y nuevos prompts realizados durante el proceso.',
        ])]

    # 5. Registro principal
    sec5 = [P('5 · Diseño del registro principal', H1),
        P('El <b>registro maestro</b> es <b>dim_comprador</b>, orientado al <b>cliente-comprador</b> '
          '(el <i>Invocador</i>). Es una estructura que agrupa <b>campos heterogéneos</b>; cada campo se '
          'define por <b>nombre</b>, <b>tipo de dato</b> y <b>tamaño</b>. Los tipos se expresan de forma '
          'conceptual (entero, real, cadena, booleano, fecha), como en la Unidad 2.')]
    reg = [[P('Nombre del campo', CELLH), P('Tipo de dato', CELLH), P('Tam.', CELLH), P('Contenido/Continente', CELLH), P('Rol de clave', CELLH)]]
    for a,b,cc,d,e in [
        ('id_comprador','Entero (autoincremental)','4 b','Contenido','PK — Primaria, Simple'),
        ('email','Cadena','120','Contenido','Candidata UNIQUE, Simple'),
        ('nick_invocador','Cadena','30','Contenido','Riot ID → clave compuesta'),
        ('riot_tag','Cadena','8','Contenido','Riot ID → clave compuesta'),
        ('nombre','Cadena','60','Contenido','—'),
        ('apellido','Cadena','60','Contenido','Secundaria (índice)'),
        ('fecha_nacimiento','Fecha','10','Continente (D/M/A)','—'),
        ('fecha_alta','Fecha','10','Contenido','—'),
        ('nivel_invocador','Entero','4 b','Contenido','—'),
        ('horas_jugadas','Real','8 b','Contenido','—'),
        ('cuenta_premium','Booleano','1 b','Contenido','—'),
        ('id_servidor','Entero','4 b','Contenido','FK — Foránea → dim_servidor (N:1)'),
    ]:
        reg.append([P(a,CELLC),P(b,CELLB),P(cc,CELL),P(d,CELL),P(e,CELL)])
    sec5 += [tbl(reg, [33*mm, 33*mm, 11*mm, 33*mm, 43*mm]),
        P('<b>Campo continente:</b> <font name="Courier">fecha_nacimiento</font> agrupa los subcampos '
          'Día / Mes / Año; el <i>selector de campo</i> (<font name="Courier">Registro.Campo</font>) '
          'permite acceder a cada uno. El registro incluye además un campo <b>real</b> '
          '(<font name="Courier">horas_jugadas</font>) y uno <b>booleano</b> '
          '(<font name="Courier">cuenta_premium</font>) para mostrar la variedad de tipos de dato.', SMALL)]
    S += [KeepTogether(sec5)]

    # 6. Clave
    S += [P('6 · Identificación y justificación de la clave', H1),
        P('Se elige como <b>clave primaria</b> el campo <font name="Courier">id_comprador</font> '
          '(entero, autoincremental). El razonamiento, frente a las otras claves candidatas:'),
        bullets([
            'El <b>email</b> es único, pero <b>cambia con frecuencia</b> (la persona migra de proveedor): '
            'es inestable como identificador permanente.',
            'El <b>Riot ID</b> (<font name="Courier">nick_invocador#riot_tag</font>) es único, pero es '
            '<b>compuesto</b> y el jugador puede <b>renombrarlo</b>, lo que obligaría a propagar el cambio.',
            'El campo <font name="Courier">id_comprador</font> es <b>estable, único, compacto, nunca nulo '
            'y desacoplado del negocio</b>: es la mejor opción para identificar el registro de forma '
            'permanente y para ser referenciado por otras tablas.',
        ]),
        P('El email y el Riot ID se conservan como <b>claves candidatas</b> '
          '(<font name="Courier">UNIQUE</font>) para garantizar la unicidad de negocio sin ser la PK.')]

    # 7. Modelo de datos
    S += [P('7 · El modelo de datos (coherencia con la tienda)', H1),
        P('El registro maestro se integra en un <b>modelo relacional</b> donde una tabla central de '
          '<b>compras</b> se relaciona con dimensiones (producto, comprador, fecha, medio de pago). '
          'Las jerarquías se <b>normalizan en cadena</b>, lo que produce <b>claves foráneas '
          'encadenadas</b>:'),
        bullets([
            'Rama producto: <font name="Courier">producto → categoría → familia</font>.',
            'Rama comprador: <font name="Courier">comprador → servidor → región</font>.',
        ]),
        P('Cada relación tiene su <b>cardinalidad</b>; la del registro maestro es <b>N:1</b> '
          '(muchos compradores pertenecen a un servidor). Así, el modelo demuestra los <b>cinco tipos '
          'de clave</b> de la Unidad 2:')]
    kt = [[P('Tipo de clave', CELLH), P('Definición', CELLH), P('Ejemplo en Hextech Bazaar', CELLH)]]
    for a,b,cc in [
        ('Primaria (PK)','Identifica de forma única e irrepetible','id_comprador; todos los identificadores id_*'),
        ('Foránea (FK)','Puente hacia otro registro/tabla','comprador→servidor; categoría→familia (encadenada)'),
        ('Secundaria','No única; agrupa, ordena o busca','índice por apellido; índice por categoría'),
        ('Simple','Formada por un único campo','id_comprador; email'),
        ('Compleja/compuesta','Campo continente o varias columnas','Riot ID (nick + tag); fecha (día/mes/año)'),
    ]:
        kt.append([P(a,CELLB),P(b,CELL),P(cc,CELL)])
    S += [tbl(kt, [33*mm, 56*mm, 64*mm])]

    # 8. Justificación del diseño
    S += [P('8 · Justificación del diseño utilizado', H1),
        P('<b>Por qué este registro y esta clave.</b> El eje del negocio es el <b>cliente-comprador</b>; '
          'por eso el registro maestro lo describe y se lo identifica con una clave estable. La elección '
          'de una clave surrogate sobre las naturales prioriza la <b>permanencia</b> del identificador.'),
        P('<b>Por qué este modelo.</b> La normalización en cadena permite mostrar de forma clara los '
          'distintos tipos de clave y mantener los datos consistentes (sin repetir nombres de familia, '
          'región, etc.). El modelo es <b>coherente</b> con la tienda: cada dimensión corresponde a algo '
          'que el usuario realmente ve y filtra.'),
        P('<b>Por qué este diseño visual.</b> La estética toma la identidad del juego (tonos dorados y '
          'celestes sobre fondo azul-noche) para lograr <b>coherencia temática</b> y una propuesta '
          'original. La navegación (portada → catálogo → detalle → carrito) es directa, y los <b>filtros</b> '
          'del catálogo (familia, categoría, rareza, región) reflejan exactamente los atributos del '
          'modelo de datos: la estructura diseñada se vuelve visible en la experiencia de uso.')]

    # 9. Entregables
    S += [PageBreak(), P('9 · Entregables solicitados', H1),
        P('El trabajo incluye todo lo pedido por la consigna:'),
        checklist([
            '<b>Nombre y descripción</b> del e-commerce (apartado 3).',
            '<b>Diseño del registro principal</b> con nombre, tipo de dato y tamaño de cada campo (apartado 5).',
            '<b>Identificación y explicación de la clave</b> (apartado 6).',
            '<b>Prompts</b> utilizados con la IA (apartado 11).',
            '<b>Video demostrativo</b> de la app, con tutorial de uso y qué muestra (guion en el apartado 12).',
            '<b>Aplicación con URL publicada</b> (ver portada).',
            '<b>Reflexión</b> sobre cómo la IA ayudó en el diseño (apartado 13).',
        ])]

    # 10. Criterios
    S += [P('10 · Criterios de evaluación y cómo se abordan', H1)]
    cri = [[P('Criterio', CELLH), P('Cómo se aborda en este trabajo', CELLH)]]
    for a,b in [
        ('Correcta definición del registro','Registro maestro con campos, tipos de dato y tamaños explícitos (ap. 5).'),
        ('Selección y justificación de la clave','PK surrogate justificada frente a email y Riot ID (ap. 6).'),
        ('Coherencia e-commerce ↔ estructura','Las vistas y filtros reflejan las dimensiones del modelo (ap. 7 y 8).'),
        ('Calidad y claridad de los prompts','Prompts ordenados, con pedido explícito de registro y clave (ap. 11).'),
        ('Creatividad y originalidad','Temática de Runeterra con catálogo y estética propias del juego.'),
        ('Presentación y fundamentación','Documento estructurado y app navegable publicada.'),
    ]:
        cri.append([P(a,CELLB),P(b,CELL)])
    S += [tbl(cri, [55*mm, 98*mm])]

    # 11. Prompts
    S += [P('11 · Prompts utilizados con la IA (en orden)', H1),
        P('IA utilizada: <b>Claude</b>. El prompt principal incluye explícitamente el pedido del diseño '
          'del registro y la definición de la clave.', LEAD)]
    for t, body in [
        ('Prompt 0 — Contexto teórico (Unidad 2)',
         'Se aportó la teoría de registros (campos contenidos y continentes, selector de campo) y los '
         'tipos de clave (simple, compuesta, primaria, secundaria, foránea), para que la IA modele sobre '
         'esos conceptos.'),
        ('Prompt 1 — Encargo general',
         '“El e-commerce será la Opción 5 – Fantasy Shop. Diseñá el modelo de datos; el registro maestro '
         'orientado a cliente-comprador. Generá la estructura del registro (nombre de campo, tipo de '
         'dato) y justificá teóricamente la elección de claves. En lo visual, sobre League of Legends: '
         'incorporá ítems/productos del juego. Prototipo funcional (navegación, catálogo, vista de '
         'producto). Publicá la app en una URL pública. Documentá y generá un PDF; guardá los prompts en '
         'orden.”'),
        ('Prompt 2 — Definiciones de diseño',
         'Productos: mezcla de campeones/aspectos e ítems de juego. Estética: identidad visual del juego '
         '(dorado y celeste sobre azul-noche).'),
        ('Prompt 3 — Registro y clave (pedido explícito)',
         '“Diseñá el registro principal orientado al cliente-comprador, indicando nombre de cada campo, '
         'tipo de dato y tamaño, e identificá la clave justificando su elección; integralo a un modelo '
         'que muestre los cinco tipos de clave.”'),
        ('Prompt 4 — Productos e imágenes del juego',
         '“Incorporá ítems/productos del juego League of Legends con sus imágenes.” Se poblaron campeones, '
         'aspectos e ítems con su categoría, rareza y región de Runeterra.'),
        ('Prompt 5 — Prototipo funcional + publicación',
         '“Armá el prototipo (portada, catálogo con filtros, detalle de producto y carrito) y publicá la '
         'app en una URL pública.”'),
        ('Prompt 6 — Documentación',
         '“Documentá lo relevante según el PDF y generá un PDF de entrega profesional y educativo; guardá '
         'los prompts en orden.”'),
    ]:
        S += [P(t, H2), P(body, QUOTE)]

    # 12. Recorrido
    S += [P('12 · Qué muestra la app (guion del video)', H1),
        bullets([
            '<b>Portada:</b> presentación de la tienda, las dos familias de productos y una selección de destacados.',
            '<b>Catálogo:</b> grilla de productos con <b>filtros</b> por familia, categoría, rareza y región, '
            'búsqueda por nombre y orden por precio.',
            '<b>Detalle de producto:</b> imagen grande, ficha (familia, categoría, rareza, región, código y stock), '
            'descripción y botón “Añadir al carrito”.',
            '<b>Carrito:</b> productos agregados, cantidades, totales y cierre de compra simulado (sin pago real).',
        ])]

    # 13. Reflexión
    S += [P('13 · Reflexión: cómo ayudó la IA', H1),
        P('La IA fue una asistente de diseño en todas las etapas. Primero ayudó a ordenar la <b>teoría de '
          'la Unidad 2</b> (registro y clave) y a traducirla en un <b>modelo coherente</b> con la temática, '
          'eligiendo y <b>justificando</b> la clave primaria frente a las candidatas naturales. Luego '
          'aceleró la incorporación de <b>productos reales</b> del juego y la construcción de un '
          '<b>prototipo navegable</b> donde la estructura de datos se refleja en los filtros y las vistas. '
          'Mi aporte fue decidir la temática, la dirección del diseño y validar que todo respetara los '
          'conceptos de la cátedra. El mayor valor de la IA fue <b>convertir un pedido conceptual en una '
          'propuesta concreta y documentada</b>, manteniendo el foco en lo evaluado: la correcta '
          'definición del <b>registro</b> y su <b>clave</b>.')]

    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=20*mm, bottomMargin=18*mm,
        pageTemplates=[
            PageTemplate(id='cover', frames=[Frame(0,0,A4[0],A4[1], id='c')], onPage=cover),
            PageTemplate(id='content', frames=[Frame(18*mm, 17*mm, A4[0]-36*mm, A4[1]-37*mm, id='f')], onPage=content_page),
        ])
    doc.build(S)
    print('PDF generado →', os.path.abspath(OUT))

if __name__ == '__main__':
    build()
