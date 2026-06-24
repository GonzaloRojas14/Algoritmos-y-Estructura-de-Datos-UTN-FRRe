#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el PDF de entrega de la Actividad N.º 2 (Hextech Bazaar).
Estilo formal y monocromo (negro, negrita y grises), redactado en primera persona.
Uso:  python3 docs/gen_pdf.py  [URL_publica]
"""
import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, NextPageTemplate)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '..', 'Hextech Bazaar - Documentacion Actividad N2.pdf')
URL = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
    'HEXTECH_URL', 'https://leslie-entities-cartoons-attorney.trycloudflare.com')

# Paleta monocroma
BLACK  = colors.HexColor('#000000')
INK    = colors.HexColor('#1a1a1a')
DGREY  = colors.HexColor('#333333')
GREY   = colors.HexColor('#666666')
LIGHT  = colors.HexColor('#f2f2f2')
BORDER = colors.HexColor('#c4c4c4')
HEAD   = colors.HexColor('#2b2b2b')
ACCENT = colors.HexColor('#284b73')      # azul sobrio: un toque de color
ACCENT_LT = colors.HexColor('#eef2f7')   # tinte muy suave para filas

styles = getSampleStyleSheet()
H1   = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=13.5, textColor=ACCENT, spaceBefore=16, spaceAfter=7, leading=16)
H2   = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=10.5, textColor=DGREY, spaceBefore=8, spaceAfter=3, leading=13)
BODY = ParagraphStyle('BODY', fontName='Helvetica', fontSize=10.3, textColor=INK, leading=15.5, alignment=TA_JUSTIFY, spaceAfter=8)
TOC  = ParagraphStyle('TOC', fontName='Helvetica', fontSize=11, textColor=INK, leading=20)
CELL = ParagraphStyle('CELL', fontName='Helvetica', fontSize=8.8, textColor=INK, leading=11.5)
CELLB= ParagraphStyle('CELLB', parent=CELL, fontName='Helvetica-Bold')
CELLM= ParagraphStyle('CELLM', fontName='Courier', fontSize=8.6, textColor=INK, leading=11.5)
CELLH= ParagraphStyle('CELLH', parent=CELL, fontName='Helvetica-Bold', textColor=colors.white)
QUOTE= ParagraphStyle('QUOTE', parent=BODY, fontName='Helvetica-Oblique', textColor=DGREY, leftIndent=12, spaceAfter=7, leading=14)

def P(t, s=BODY): return Paragraph(t, s)
def m(t): return f'<font name="Courier">{t}</font>'   # nombre de campo en minúscula_con_guion

def tbl(data, widths):
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER),
        ('LEFTPADDING',(0,0),(-1,-1),6), ('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),4), ('BOTTOMPADDING',(0,0),(-1,-1),4),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, ACCENT_LT]),
        ('BACKGROUND',(0,0),(-1,0), ACCENT)]))
    return t

# ---------------------------- PORTADA ----------------------------
def cover(c, doc):
    W, H = A4
    c.saveState()
    c.setFillColor(colors.white); c.rect(0, 0, W, H, fill=1, stroke=0)
    # marco superior
    c.setStrokeColor(ACCENT); c.setLineWidth(2.4); c.line(22*mm, H-28*mm, W-22*mm, H-28*mm)
    c.setStrokeColor(GREY); c.setLineWidth(0.5); c.line(22*mm, H-29.2*mm, W-22*mm, H-29.2*mm)
    c.setFillColor(DGREY); c.setFont('Helvetica-Bold', 9.5)
    c.drawCentredString(W/2, H-24*mm, 'UNIVERSIDAD TECNOLÓGICA NACIONAL — FACULTAD REGIONAL RESISTENCIA')
    c.setFillColor(GREY); c.setFont('Helvetica', 9)
    c.drawCentredString(W/2, H-33.5*mm, 'Ingeniería en Sistemas de Información')
    # título
    c.setFillColor(ACCENT); c.setFont('Helvetica-Bold', 34)
    c.drawCentredString(W/2, H*0.595, 'Hextech Bazaar')
    c.setFillColor(DGREY); c.setFont('Helvetica', 13.5)
    c.drawCentredString(W/2, H*0.555, 'Diseño de un e-Commerce con Inteligencia Artificial')
    c.setFillColor(GREY); c.setFont('Helvetica-Oblique', 11)
    c.drawCentredString(W/2, H*0.527, 'Actividad Formativa N.º 2')
    # divisor
    c.setStrokeColor(ACCENT); c.setLineWidth(0.8); c.line(W/2-40*mm, H*0.495, W/2+40*mm, H*0.495)
    # datos
    c.setFillColor(INK); c.setFont('Helvetica-Bold', 12)
    c.drawCentredString(W/2, H*0.44, 'Alumna: Zárate, Brisa')
    c.setFillColor(DGREY); c.setFont('Helvetica', 11)
    c.drawCentredString(W/2, H*0.405, 'Materia: Algoritmos y Estructuras de Datos')
    c.drawCentredString(W/2, H*0.378, 'Año: 2026')
    # link
    c.setFillColor(GREY); c.setFont('Helvetica-Bold', 9.5)
    c.drawCentredString(W/2, H*0.30, 'APLICACIÓN PUBLICADA')
    c.setFillColor(INK); c.setFont('Courier', 11)
    c.drawCentredString(W/2, H*0.275, URL)
    # pie
    c.setStrokeColor(ACCENT); c.setLineWidth(1); c.line(22*mm, 22*mm, W-22*mm, 22*mm)
    c.setFillColor(GREY); c.setFont('Helvetica', 8)
    c.drawCentredString(W/2, 17*mm, 'Trabajo académico. La aplicación es un modelo para demostrar los conceptos de registro y clave (Unidad 2); no procesa pagos reales.')
    c.restoreState()

def content_page(c, doc):
    W, H = A4
    c.saveState()
    c.setStrokeColor(ACCENT); c.setLineWidth(0.9); c.line(20*mm, H-16*mm, W-20*mm, H-16*mm)
    c.setFillColor(GREY); c.setFont('Helvetica', 7.6)
    c.drawString(20*mm, H-14.4*mm, 'Hextech Bazaar — Actividad Formativa N.º 2')
    c.drawRightString(W-20*mm, H-14.4*mm, 'Zárate, Brisa')
    c.setStrokeColor(BORDER); c.setLineWidth(0.5); c.line(20*mm, 15*mm, W-20*mm, 15*mm)
    c.setFillColor(GREY); c.setFont('Helvetica', 8)
    c.drawCentredString(W/2, 11*mm, str(doc.page))
    c.restoreState()

# ---------------------------- CONTENIDO ----------------------------
def build():
    S = [NextPageTemplate('content'), PageBreak()]

    # ----- Índice -----
    S += [P('Índice', H1)]
    temas = [
        'Introducción',
        'Marco teórico: registros y claves',
        'Diseño del registro principal',
        'Identificación y justificación de la clave',
        'Modelo de datos y relaciones',
        'Reflexión sobre el uso de inteligencia artificial',
        'Prompts utilizados',
    ]
    for i, t in enumerate(temas, 1):
        S.append(P(f'{i}.&nbsp;&nbsp;&nbsp;{t}', TOC))
    S += [PageBreak()]

    # ----- 1. Introducción -----
    S += [P('1. Introducción', H1),
        P('Para esta actividad elegí desarrollar Hextech Bazaar, una tienda en línea ambientada en el '
          'videojuego League of Legends y su universo, Runeterra. La tienda ofrece dos familias de '
          'productos: los coleccionables (campeones y aspectos) y el equipo (los ítems del juego). '
          'Más allá de la tienda en sí, lo que me propuse con este trabajo fue aplicar los conceptos de '
          'la Unidad 2: la estructura de tipo registro y el diseño de una clave que permita identificar y '
          'organizar los datos. La aplicación quedó publicada y se puede visitar en la dirección que figura '
          'en la portada.')]

    # ----- 2. Marco teórico -----
    S += [P('2. Marco teórico: registros y claves', H1),
        P('Un registro es una estructura que agrupa un conjunto de campos heterogéneos y representa una '
          'entidad del mundo real, como puede ser un comprador o un producto. Cada campo es la unidad '
          'mínima de información y se define por tres elementos: su nombre, su tipo de dato y su tamaño. '
          'Además, un campo puede ser de tipo contenido, cuando guarda un dato elemental, o de tipo '
          'continente, cuando agrupa en su interior varios subcampos; el ejemplo clásico es una fecha, '
          'que contiene día, mes y año.'),
        P('Los tipos de dato que utilicé son los siguientes: entero, para números sin parte decimal; '
          'real, para números con decimales; alfanumérico, para texto, que se mide en cantidad de '
          'caracteres; booleano, para valores de verdadero o falso; y fecha. Los tipos numéricos, '
          'booleanos y de fecha se miden en bytes (B).'),
        P('Una clave es un campo, o un conjunto de campos, que permite identificar o diferenciar los '
          'registros. Según la teoría de la cátedra distingo los siguientes tipos. La clave primaria '
          'identifica de manera única e irrepetible a cada registro. La clave foránea es un campo que '
          'actúa como enlace hacia el registro de otra tabla. La clave secundaria no identifica de forma '
          'única, sino que se usa para ordenar o agrupar los registros. Según la cantidad de campos que la '
          'forman, una clave es simple cuando está formada por un único campo, o compuesta cuando está '
          'formada por más de uno.')]

    # ----- 3. Registro principal -----
    S += [P('3. Diseño del registro principal', H1),
        P('El registro principal de la tienda es el del comprador (en el juego, el invocador), porque es '
          'la entidad central del negocio. A continuación detallo cada uno de sus campos con su nombre, '
          'su tipo de dato, su tamaño y su función dentro del registro.')]
    reg = [[P('Nombre del campo', CELLH), P('Tipo de dato', CELLH), P('Tamaño', CELLH),
            P('Contenido / Continente', CELLH), P('Rol de clave', CELLH)]]
    filas = [
        ('id_comprador',     'Entero',       '4 B',            'Contenido',                'clave primaria (simple)'),
        ('email',            'Alfanumérico', '120 caracteres', 'Contenido',                'dato único (simple)'),
        ('nick_invocador',   'Alfanumérico', '30 caracteres',  'Contenido',                'clave compuesta (riot id)'),
        ('riot_tag',         'Alfanumérico', '8 caracteres',   'Contenido',                'clave compuesta (riot id)'),
        ('nombre',           'Alfanumérico', '60 caracteres',  'Contenido',                '—'),
        ('apellido',         'Alfanumérico', '60 caracteres',  'Contenido',                'clave secundaria (ordenar)'),
        ('fecha_nacimiento', 'Fecha',        '4 B',            'Continente (día/mes/año)', '—'),
        ('fecha_alta',       'Fecha',        '4 B',            'Contenido',                '—'),
        ('nivel_invocador',  'Entero',       '4 B',            'Contenido',                '—'),
        ('horas_jugadas',    'Real',         '8 B',            'Contenido',                '—'),
        ('cuenta_premium',   'Booleano',     '1 B',            'Contenido',                '—'),
        ('id_servidor',      'Entero',       '4 B',            'Contenido',                'clave foránea'),
    ]
    for a,b,cc,d,e in filas:
        reg.append([P(a,CELLM),P(b,CELL),P(cc,CELL),P(d,CELL),P(e,CELL)])
    S += [tbl(reg, [33*mm, 26*mm, 28*mm, 35*mm, 48*mm])]

    # ----- 4. Clave -----
    S += [P('4. Identificación y justificación de la clave', H1),
        P('Como clave primaria del registro elegí el campo ' + m('id_comprador') + ', un número entero '
          'que se asigna automáticamente a cada comprador. Lo elegí porque es una clave estable y propia '
          'del sistema: no cambia y no depende de los datos del negocio, así que permite identificar cada '
          'registro de forma permanente y enlazarlo desde otras tablas.'),
        P('Los campos ' + m('email') + ', ' + m('nick_invocador') + ' y ' + m('riot_tag') + ' también '
          'permiten distinguir a un comprador, por lo que los declaré como dato único para que no se '
          'repitan. En particular, ' + m('nick_invocador') + ' y ' + m('riot_tag') + ' forman juntos una '
          'clave compuesta (el riot id), que tampoco puede repetirse en combinación.')]

    # ----- 5. Modelo de datos -----
    S += [P('5. Modelo de datos y relaciones', H1),
        P('Los registros se relacionan entre sí formando dos jerarquías. Del lado del comprador la '
          'jerarquía es comprador → servidor → país: cada comprador pertenece a un servidor de juego y '
          'cada servidor a un país. Del lado del producto la jerarquía es producto → categoría → familia. '
          'La relación entre el comprador y el servidor es de tipo N:1, es decir, muchos compradores '
          'pertenecen a un mismo servidor; ese enlace se realiza con la clave foránea ' + m('id_servidor') + '.'),
        P('De esta manera, en el modelo aparecen los distintos tipos de clave vistos en la materia, '
          'con un ejemplo concreto de cada uno:')]
    kt = [[P('Tipo de clave', CELLH), P('Ejemplo en el modelo', CELLH)]]
    for a,b in [
        ('clave primaria (simple)', m('id_comprador')),
        ('clave foránea', m('id_servidor') + ' (enlaza comprador con servidor)'),
        ('clave secundaria (ordenar)', m('apellido') + ' (permite ordenar los compradores)'),
        ('clave simple', m('id_comprador') + ' (un único campo)'),
        ('clave compuesta', m('nick_invocador') + ' + ' + m('riot_tag') + ' (juntos forman el Riot ID del jugador)'),
    ]:
        kt.append([P(a,CELLB),P(b,CELL)])
    S += [tbl(kt, [55*mm, 115*mm])]

    # ----- 6. Reflexión -----
    S += [P('6. Reflexión sobre el uso de inteligencia artificial', H1),
        P('La verdad es que usar Claude me ayudó bastante a construir la tienda. Yo tenía claro el modelo '
          'que quería (el registro del comprador, sus campos y la clave), pero pasarlo a una página '
          'funcional sola me hubiera llevado mucho más tiempo. Con la IA pude ver rápido cómo esos datos '
          'que diseñé se mostraban en el catálogo y en la vista de cada producto, y eso me ayudó a entender '
          'mejor cómo se conectan los registros entre sí a través de las claves. Me sirvió mucho trabajar '
          'con los datos de la materia (los campos, sus tipos de dato y las claves primaria y foránea), '
          'porque así la teoría de la Unidad 2 dejó de ser algo abstracto y la vi funcionando en una '
          'aplicación de verdad. Las decisiones del modelo las tomé yo; la IA me ayudó a llevarlas a la '
          'práctica y a darme cuenta de algunos errores.')]

    # ----- 7. Prompts -----
    S += [P('7. Prompts utilizados', H1),
        P('A continuación incluyo, en orden, los prompts que utilicé con la inteligencia artificial. El '
          'primero plantea el trabajo en general y el tercero pide de forma puntual el diseño del registro '
          'y la definición de la clave.')]
    prompts = [
        ('Prompt 1 — Encargo general', QUOTE,
         '«Necesito que el e-commerce sea el de la opción 5 – Fantasy Shop. Siguiendo las consignas del PDF '
         'y los conceptos de la Unidad 2, diseñá el modelo de datos en un esquema snowflake; el registro '
         'maestro tiene que estar orientado a cliente-comprador. Generá la estructura del registro '
         'detallando: nombre del campo, tipo de dato, y justificá teóricamente la elección de claves. '
         'Después, pasando a lo visual, necesito que sea sobre el juego League of Legends: para eso descargá '
         'ítems o productos del juego y agregalos a la página. Además tiene que ser un prototipo funcional '
         'visualmente (navegación entre ventanas, catálogo, vista de un producto). El e-commerce debe '
         'contar estrictamente con todo lo que pide el PDF. Usá un túnel de Cloudflare para tener una URL '
         'gratis y poder visualizar el trabajo; acordate de que es una página modelo para un ejercicio. '
         'Mientras desarrollás, documentá lo que sea relevante y guardá los prompts en orden.»'),
        ('Prompt 2 — Definiciones de diseño', BODY,
         'Cuando la IA repreguntó, definí implementar el modelo en una base de datos real, con una '
         'aplicación que la consulta; que los productos fueran una mezcla de coleccionables (campeones y '
         'aspectos) e ítems del juego; y una estética acorde a la temática del juego (la línea Hextech, con '
         'tonos oscuros, dorados y celestes).'),
        ('Prompt 3 — Diseño del registro y la clave (pedido puntual)', QUOTE,
         '«Diseñá el registro principal del comprador y detallame, para cada campo, su nombre, su tipo de '
         'dato y su tamaño. Después identificá cuál es la clave del registro y explicá por qué elegís esa y '
         'no otra.»'),
        ('Prompt 4 — Imágenes de los productos', BODY,
         '«Ponele imágenes a los productos; usá los campeones, aspectos e ítems reales del juego.» Para eso, '
         'la IA tomó las imágenes oficiales del juego (los campeones, sus aspectos y los íconos de los '
         'ítems) y las sumó al catálogo.'),
    ]
    for t, st, body in prompts:
        S += [P(t, H2), P(body, st)]

    doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=20*mm, bottomMargin=18*mm,
        pageTemplates=[
            PageTemplate(id='cover', frames=[Frame(0,0,A4[0],A4[1], id='c')], onPage=cover),
            PageTemplate(id='content', frames=[Frame(20*mm, 17*mm, A4[0]-40*mm, A4[1]-37*mm, id='f')], onPage=content_page),
        ])
    doc.build(S)
    print('PDF generado ->', os.path.abspath(OUT))

if __name__ == '__main__':
    build()
