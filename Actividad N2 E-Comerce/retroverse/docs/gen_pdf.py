#!/usr/bin/env python3
# Genera la documentación PDF del Trabajo Práctico N.º 2 (RetroVerse).
# Estilo monocromo: negro, negrita y grises.
import os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, NextPageTemplate, ListFlowable, ListItem, KeepTogether
)
from reportlab.platypus.tableofcontents import TableOfContents

OUT = os.path.join(os.path.dirname(__file__), '..', '..',
                   'RetroVerse - Documentacion Actividad N2.pdf')
URL = sys.argv[1] if len(sys.argv) > 1 else "https://mails-deals-restricted-tops.trycloudflare.com"

# Paleta monocroma (negro / grises)
BLACK  = colors.HexColor('#000000')
INK    = colors.HexColor('#1a1a1a')   # cuerpo de texto
DGREY  = colors.HexColor('#3a3a3a')   # subtítulos
GREY   = colors.HexColor('#6a6a6a')   # texto secundario
LIGHT  = colors.HexColor('#f3f3f3')   # fondo de filas alternas / citas
BORDER = colors.HexColor('#c8c8c8')   # líneas de tabla
HEADBG = colors.HexColor('#262626')   # fondo de encabezado de tabla

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], textColor=BLACK, fontSize=16.5,
                    spaceBefore=22, spaceAfter=8, fontName='Helvetica-Bold', keepWithNext=1)
H2 = ParagraphStyle('H2', parent=styles['Heading2'], textColor=DGREY, fontSize=12,
                    spaceBefore=13, spaceAfter=5, fontName='Helvetica-Bold', keepWithNext=1)
HIDX = ParagraphStyle('HIDX', parent=styles['Heading1'], textColor=BLACK, fontSize=16.5,
                      spaceBefore=0, spaceAfter=14, fontName='Helvetica-Bold')
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], textColor=INK, fontSize=10.4,
                      leading=15.5, alignment=TA_JUSTIFY, spaceAfter=7)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=9, textColor=GREY, alignment=TA_LEFT)
CODE = ParagraphStyle('CODE', parent=BODY, fontName='Courier', fontSize=8.8, textColor=DGREY,
                      alignment=TA_LEFT, leading=12)
CELL = ParagraphStyle('CELL', parent=BODY, fontSize=8.7, leading=11.5, alignment=TA_LEFT, spaceAfter=0)
CELLH = ParagraphStyle('CELLH', parent=CELL, textColor=colors.white, fontName='Helvetica-Bold')

# Estilos de portada
COVER_T = ParagraphStyle('COVER_T', fontName='Helvetica-Bold', fontSize=30, textColor=BLACK,
                         alignment=TA_CENTER, leading=36)
COVER_S = ParagraphStyle('COVER_S', fontName='Helvetica', fontSize=13, textColor=DGREY,
                         alignment=TA_CENTER, leading=18, spaceBefore=8)
COVER_M = ParagraphStyle('COVER_M', fontName='Helvetica', fontSize=10.5, textColor=GREY,
                         alignment=TA_CENTER, leading=16, spaceBefore=6)
COVER_B = ParagraphStyle('COVER_B', parent=COVER_M, fontName='Helvetica-Bold', textColor=INK)


def cover_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.white)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # divisor superior (negro grueso + gris fino)
    canvas.setStrokeColor(BLACK); canvas.setLineWidth(3)
    canvas.line(18*mm, A4[1]-26*mm, A4[0]-18*mm, A4[1]-26*mm)
    canvas.setStrokeColor(GREY); canvas.setLineWidth(0.6)
    canvas.line(18*mm, A4[1]-27.4*mm, A4[0]-18*mm, A4[1]-27.4*mm)
    # divisor inferior
    canvas.setStrokeColor(BLACK); canvas.setLineWidth(1.2)
    canvas.line(18*mm, 24*mm, A4[0]-18*mm, 24*mm)
    canvas.restoreState()


def content_bg(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(BLACK)
    canvas.setLineWidth(1.2)
    canvas.line(18*mm, A4[1]-18*mm, A4[0]-18*mm, A4[1]-18*mm)
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18*mm, 12*mm, "Algoritmos y Estructuras de Datos · UTN-FRRe · Rojas, Gonzalo")
    canvas.drawRightString(A4[0]-18*mm, 12*mm, "Pág. %d" % doc.page)
    canvas.restoreState()


def tbl(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ('GRID', (0,0), (-1,-1), 0.5, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
    ]
    if header:
        style += [('BACKGROUND', (0,0), (-1,0), HEADBG)]
    t.setStyle(TableStyle(style))
    return t


def P(t, s=BODY):
    return Paragraph(t, s)


def prompt_block(title, text):
    quote = Paragraph(text, ParagraphStyle('pq', parent=BODY, leftIndent=10, fontName='Helvetica-Oblique',
                                           textColor=DGREY, backColor=LIGHT,
                                           borderColor=BORDER, borderWidth=0.5, borderPadding=6, spaceAfter=8))
    story.append(KeepTogether([P(title, H2), quote]))


story = []

# ---------------- PORTADA ----------------
story.append(NextPageTemplate('content'))
story.append(Spacer(1, 120))
story.append(Paragraph("Algoritmos y Estructuras de Datos", COVER_T))
story.append(Paragraph("Universidad Tecnológica Nacional · Facultad Regional Resistencia", COVER_S))
story.append(Spacer(1, 40))
story.append(Paragraph("Trabajo Práctico N.º 2", COVER_B))
story.append(Paragraph("Diseñando un e-Commerce con Inteligencia Artificial", COVER_M))
story.append(Spacer(1, 8))
story.append(Paragraph("RetroVerse — tienda de objetos vintage y tecnología retro", COVER_M))
story.append(Spacer(1, 44))
story.append(Paragraph("Alumno: Rojas, Gonzalo", COVER_B))
story.append(Paragraph("Legajo: 28838", COVER_B))
story.append(Spacer(1, 22))
story.append(Paragraph("Aplicación publicada en:", COVER_M))
story.append(Paragraph('<b><font color="#000000">%s</font></b>' % URL, COVER_M))
story.append(PageBreak())

# ---------------- ÍNDICE ----------------
story.append(P("Índice", HIDX))
story.append(Spacer(1, 10))
toc = TableOfContents()
toc.dotsMinLevel = 1   # sin puntos suspensivos en las secciones (más limpio)
toc.levelStyles = [
    ParagraphStyle('TOC1', fontName='Helvetica', fontSize=12, leading=28, textColor=INK),
]
story.append(toc)
story.append(PageBreak())

# ---------------- 1. OBJETIVOS ----------------
story.append(P("1. Objetivo del trabajo", H1))
story.append(P("Este trabajo corresponde al Trabajo Práctico N.º 2 de la materia y pone en práctica los "
               "temas de la Unidad 2. La idea fue tomar la teoría de registros y claves y aplicarla a un "
               "caso concreto: el diseño de una aplicación de e-Commerce."))
story.append(P("En concreto, me propuse mostrar tres cosas: cómo se define y se usa una estructura de tipo "
               "registro para representar algo del mundo real; cómo se elige una clave que permita "
               "identificar y diferenciar los datos; y cómo, a partir de esa estructura, se puede modelar "
               "la información para resolver un problema real."))

# ---------------- 2. TEMÁTICA Y DESCRIPCIÓN ----------------
story.append(P("2. La temática elegida: RetroVerse", H1))
story.append(P("La consigna pedía elegir una temática que se saliera de lo común. Entre las opciones "
               "propuestas elegí la Opción 3, <b>RetroVerse</b>, una tienda digital de objetos vintage, "
               "coleccionables y tecnología retro."))
story.append(P("RetroVerse es un mercado de tecnología y objetos retro de los años 70, 80 y 90: "
               "computadoras hogareñas, consolas, walkmans, discmans, vinilos, cartuchos y accesorios. "
               "Cada comprador está asociado a una tienda o vendedor, así que muchos compradores terminan "
               "comprándole a un mismo vendedor."))
story.append(P("Elegí esta temática por dos razones. La primera es que se aleja de los e-commerce típicos "
               "(supermercados, ropa o electrónica común), que es justamente lo que pedía la consigna. La "
               "segunda es que es un rubro con bastantes datos que se relacionan entre sí (marca, "
               "categoría, década, condición), y eso lo hace cómodo para practicar el diseño de registros "
               "y claves."))

# ---------------- 3. REGISTRO PRINCIPAL Y CLAVE ----------------
story.append(P("3. El registro principal y su clave", H1))
story.append(P("El registro principal que pide la consigna lo diseñé orientado al cliente-comprador; en el "
               "modelo lo llamé <font face='Courier'>Comprador</font>. Un registro es una estructura que "
               "junta, bajo una misma entidad, campos de distinto tipo (texto, fechas, números). Esa es su "
               "característica más importante, la heterogeneidad: a diferencia de un arreglo, donde todo es "
               "del mismo tipo, acá conviven datos distintos que describen a una misma cosa, en este caso "
               "una persona que compra."))

story.append(P("3.1 Campos del registro", H2))
data = [[P("Campo", CELLH), P("Tipo de dato", CELLH), P("Tam.", CELLH),
         P("Contenido / Continente", CELLH), P("Rol de la clave", CELLH)]]
rows = [
    ("id_comprador", "Entero", "4 B", "Contenido", "Clave primaria (simple)"),
    ("dni", "Texto", "11", "Contenido", "Dato único (clave simple natural)"),
    ("email", "Texto", "120", "Contenido", "Dato único (clave simple natural)"),
    ("nombre", "Texto", "60", "Contenido", "—"),
    ("apellido", "Texto", "60", "Contenido", "Clave secundaria (ordenar / agrupar)"),
    ("fecha_nacimiento", "Fecha", "4 B", "Continente (Día/Mes/Año)", "—"),
    ("fecha_alta", "Fecha", "4 B", "Contenido", "—"),
    ("id_ciudad", "Entero", "4 B", "Contenido", "Clave foránea (hacia Ciudad)"),
    ("id_vendedor", "Entero", "4 B", "Contenido", "Clave foránea (hacia Vendedor)"),
]
for r in rows:
    data.append([P(r[0], CODE), P(r[1], CELL), P(r[2], CELL), P(r[3], CELL), P(r[4], CELL)])
story.append(tbl(data, [33*mm, 22*mm, 12*mm, 41*mm, 54*mm]))
story.append(Spacer(1, 6))

story.append(P("3.2 La clave del registro", H2))
story.append(P("Como clave principal elegí <font face='Courier'>id_comprador</font>, un identificador "
               "numérico propio del registro. La razón es sencilla: la clave tiene que ser un dato que no "
               "se repita nunca y que no cambie con el tiempo."))
story.append(P("El DNI y el email también sirven para reconocer a una persona, pero no me cerraban como "
               "clave principal: el DNI puede faltar (por ejemplo en un comprador extranjero) o cargarse "
               "mal, y el email se cambia bastante seguido. Por eso los dejé como datos que no se pueden "
               "repetir, pero el campo que ordena e identifica todo el registro es "
               "<font face='Courier'>id_comprador</font>."))

# ---------------- 4. CONCEPTOS DE LA UNIDAD 2 APLICADOS ----------------
story.append(P("4. Los conceptos de la Unidad 2 aplicados a RetroVerse", H1))
story.append(P("Más que quedarme en un registro suelto, traté de que el diseño se apoyara en los conceptos "
               "que vimos en la Unidad 2. En este apartado los repaso y muestro dónde aparecen en el "
               "trabajo."))

story.append(P("4.1 Campos contenidos y continentes", H2))
story.append(P("Un campo contenido guarda un único dato indivisible, como el nombre o el DNI del comprador. "
               "Un campo continente, en cambio, está formado por otros campos más simples: el ejemplo "
               "típico es la fecha de nacimiento, que por dentro se separa en día, mes y año. En el registro "
               "del comprador esa distinción aparece tal cual: casi todos sus campos son contenidos y la "
               "fecha de nacimiento es el campo continente."))

story.append(P("4.2 Los tipos de clave que aparecen en el modelo", H2))
story.append(P("Quise que el modelo mostrara los distintos tipos de clave que da la teoría, mirados desde "
               "sus dos clasificaciones: por su formato y por su función."))
data = [[P("Tipo de clave", CELLH), P("Qué es (Unidad 2)", CELLH), P("Ejemplo en RetroVerse", CELLH)]]
krows = [
    ("Simple", "Un solo campo contenido", "el DNI de un comprador"),
    ("Compleja", "Varios campos agrupados (continente)", "n.º de pedido + n.º de línea de una venta"),
    ("Primaria", "Identifica de forma única e irrepetible", "id_comprador"),
    ("Secundaria", "No es única; sirve para ordenar o agrupar", "el apellido del comprador"),
    ("Foránea", "Puente para relacionarse con otro archivo", "id_vendedor (del comprador hacia su vendedor)"),
]
for r in krows:
    data.append([P(r[0], CELL), P(r[1], CELL), P(r[2], CELL)])
story.append(tbl(data, [28*mm, 64*mm, 70*mm]))
story.append(Spacer(1, 10))

# ---------------- 5. JUSTIFICACIÓN DEL DISEÑO ----------------
story.append(P("5. Por qué diseñé el modelo de esta manera", H1))

story.append(P("5.1 Que la estructura se parezca al negocio", H2))
story.append(P("Puse al comprador en el centro porque, en una tienda como esta, lo que más interesa "
               "identificar y diferenciar es al cliente. La regla “muchos compradores le compran a un "
               "mismo vendedor” quedó representada con la clave foránea "
               "<font face='Courier'>id_vendedor</font>, que es una relación de muchos a uno. De esta "
               "manera, la estructura de datos se parece a cómo funciona realmente el e-commerce."))

story.append(P("5.2 No repetir datos", H2))
story.append(P("En lugar de repetir el nombre de la categoría o de la provincia en cada producto, separé "
               "esa información en tablas relacionadas y las uní con claves foráneas. Así los datos no se "
               "repiten y, si algo cambia, se corrige en un solo lugar. Esta forma de ordenar las tablas "
               "en cadena tiene un nombre técnico (esquema en copo de nieve), pero lo importante para este "
               "trabajo no es el nombre del esquema sino el uso de las claves para relacionar la "
               "información."))

story.append(P("5.3 El diseño visual", H2))
story.append(P("La parte visual acompaña a la temática: una estética retro, una navegación clara entre el "
               "catálogo, la ficha de cada producto, la tienda del vendedor y el carrito, y una foto real "
               "de cada objeto para que se reconozca enseguida de qué producto se trata."))

# ---------------- 6. PROMPTS ----------------
story.append(P("6. Prompts utilizados con la IA", H1))
story.append(P("Dejo los prompts en orden, tal como fue el proceso. La IA que usé fue Claude; el pedido "
               "puntual del diseño del registro y la clave es el Prompt 3."))

prompt_block("Prompt 0 — Contexto teórico",
             "Antes de pedir nada, le pasé a la IA la teoría de la Unidad 2 (registros, campos contenidos "
             "y continentes, y los tipos de clave: simple, compleja, primaria, secundaria y foránea) para "
             "que el diseño partiera de esos conceptos y no de algo genérico.")
prompt_block("Prompt 1 — Encargo general",
             "“El e-commerce elegido es RetroVerse. Quiero que apliques la teoría de la Unidad 2 que te "
             "pasé: pensá el registro principal como una estructura de datos con campos heterogéneos, "
             "distinguiendo los campos contenidos de los continentes, y definí una clave que identifique "
             "de forma única a cada registro. El registro principal tiene que estar orientado al "
             "cliente-comprador, con una relación de muchos a uno (muchos compradores le compran a un "
             "mismo vendedor) resuelta con una clave foránea. Armá un modelo de datos relacional con "
             "varias tablas relacionadas que use los distintos tipos de clave (simple, compleja, primaria, "
             "secundaria y foránea), conectando las tablas entre sí con esas claves para no repetir "
             "información. La página tiene que ser funcional visualmente entre pantallas e ítems, pero sin "
             "pago real. Documentá el proceso y guardá los prompts en orden.”")
prompt_block("Prompt 2 — Definiciones de diseño",
             "Cuando la IA repreguntó, definí implementar el modelo en una base de datos real, con una "
             "aplicación que la consulta, y una estética acorde a la temática retro.")
prompt_block("Prompt 3 — Diseño del registro y la clave (pedido puntual)",
             "“Diseñá el registro principal de RetroVerse orientado al cliente-comprador, indicando el "
             "nombre de cada campo, su tipo de dato y su tamaño, e identificá la clave del registro "
             "justificando por qué la elegís; integralo a un modelo con tablas relacionadas que muestre "
             "claves primaria, foránea, secundaria, simple y compleja.”")
prompt_block("Prompt 4 — Imágenes de los productos",
             "“Ponele imágenes a las publicaciones; buscá los objetos en internet y usalos para los ítems.” "
             "La IA buscó una foto representativa de cada producto en repositorios de uso educativo y las "
             "sumó al catálogo.")

# ---------------- 7. REFLEXIÓN ----------------
story.append(P("7. Reflexión sobre el uso de la IA", H1))
story.append(P("La IA me sirvió de apoyo durante todo el trabajo, pero las decisiones las fui tomando yo a "
               "partir de la teoría. Después de pasarle los conceptos de la Unidad 2, me ayudó a bajarlos "
               "a un caso concreto: cómo quedaría el registro del comprador, qué tipos de clave convenía "
               "mostrar y cómo relacionar las tablas entre sí."))
story.append(P("Donde más me ahorró tiempo fue en las partes mecánicas (escribir la estructura, armar "
               "datos de ejemplo, preparar las pantallas), y eso me dejó concentrarme en lo importante: "
               "por qué elegir un identificador propio como clave, cómo representar la relación de muchos a "
               "uno con el vendedor y cómo evitar repetir datos. Lo más útil fue poder probar ideas rápido "
               "y mantener todo coherente entre la teoría, el modelo y la aplicación."))

# ---------------- build ----------------
class DocTemplate(BaseDocTemplate):
    """Registra los títulos en el índice (TOC). H1 = nivel 0; subsecciones numeradas = nivel 1."""
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            name = flowable.style.name
            text = flowable.getPlainText()
            if name == 'H1':
                self.notify('TOCEntry', (0, text, self.page))


doc = DocTemplate(os.path.abspath(OUT), pagesize=A4,
                  leftMargin=18*mm, rightMargin=18*mm, topMargin=24*mm, bottomMargin=20*mm,
                  title="Algoritmos y Estructuras de Datos - TP N.º 2 - RetroVerse",
                  author="Rojas, Gonzalo")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
doc.addPageTemplates([
    PageTemplate(id='cover', frames=[frame], onPage=cover_bg),
    PageTemplate(id='content', frames=[frame], onPage=content_bg),
])
doc.multiBuild(story)
print("PDF generado en:", os.path.abspath(OUT))
