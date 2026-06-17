#!/usr/bin/env python3
# Genera la documentación PDF de la Actividad N.º 2 (RetroVerse) con estética synthwave.
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, NextPageTemplate, ListFlowable, ListItem
)

OUT = os.path.join(os.path.dirname(__file__), '..', '..',
                   'RetroVerse - Documentacion Actividad N2.pdf')
URL = "http://bore.pub:63304"

# Paleta synthwave
BG = colors.HexColor('#0a0a1f')
PINK = colors.HexColor('#ff2e97')
CYAN = colors.HexColor('#05d9e8')
VIOLET = colors.HexColor('#b537f2')
YELLOW = colors.HexColor('#ffe600')
INK = colors.HexColor('#16131f')
GREY = colors.HexColor('#555068')
SURF = colors.HexColor('#f3f0fb')
BORDER = colors.HexColor('#d9d2f0')

styles = getSampleStyleSheet()
H1 = ParagraphStyle('H1', parent=styles['Heading1'], textColor=VIOLET, fontSize=17,
                    spaceBefore=14, spaceAfter=8, fontName='Helvetica-Bold')
H2 = ParagraphStyle('H2', parent=styles['Heading2'], textColor=PINK, fontSize=12.5,
                    spaceBefore=10, spaceAfter=5, fontName='Helvetica-Bold')
BODY = ParagraphStyle('BODY', parent=styles['BodyText'], textColor=INK, fontSize=10.2,
                      leading=15, alignment=TA_JUSTIFY, spaceAfter=6)
SMALL = ParagraphStyle('SMALL', parent=BODY, fontSize=9, textColor=GREY, alignment=TA_LEFT)
CODE = ParagraphStyle('CODE', parent=BODY, fontName='Courier', fontSize=8.8, textColor=colors.HexColor('#0b6b75'),
                      alignment=TA_LEFT, leading=12)
CELL = ParagraphStyle('CELL', parent=BODY, fontSize=8.6, leading=11, alignment=TA_LEFT, spaceAfter=0)
CELLH = ParagraphStyle('CELLH', parent=CELL, textColor=colors.white, fontName='Helvetica-Bold')

# Cover styles
COVER_T = ParagraphStyle('COVER_T', fontName='Helvetica-Bold', fontSize=46, textColor=PINK,
                         alignment=TA_CENTER, leading=48)
COVER_S = ParagraphStyle('COVER_S', fontName='Helvetica', fontSize=14, textColor=CYAN,
                         alignment=TA_CENTER, leading=20, spaceBefore=10)
COVER_M = ParagraphStyle('COVER_M', fontName='Helvetica', fontSize=10.5, textColor=colors.HexColor('#cfc8ef'),
                         alignment=TA_CENTER, leading=16, spaceBefore=6)


def cover_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BG)
    canvas.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # grid floor
    canvas.setStrokeColor(colors.HexColor('#2a1c5e'))
    canvas.setLineWidth(0.6)
    for i in range(0, int(A4[0]), 22):
        canvas.line(i, 0, i, 150)
    for j in range(0, 150, 16):
        canvas.setStrokeColor(colors.HexColor('#3a2a6e'))
        canvas.line(0, j, A4[0], j)
    # neon horizon line
    canvas.setStrokeColor(PINK)
    canvas.setLineWidth(2)
    canvas.line(0, 150, A4[0], 150)
    canvas.setStrokeColor(CYAN)
    canvas.setLineWidth(0.8)
    canvas.line(0, 153, A4[0], 153)
    canvas.restoreState()


def content_bg(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(VIOLET)
    canvas.setLineWidth(1.4)
    canvas.line(18*mm, A4[1]-18*mm, A4[0]-18*mm, A4[1]-18*mm)
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(18*mm, 12*mm, "RetroVerse · Actividad Formativa N.º 2 · AyED · UTN-FRRe")
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
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, SURF]),
    ]
    if header:
        style += [('BACKGROUND', (0,0), (-1,0), VIOLET)]
    t.setStyle(TableStyle(style))
    return t


def P(t, s=BODY):
    return Paragraph(t, s)


story = []

# ---------------- COVER ----------------
story.append(NextPageTemplate('content'))
story.append(Spacer(1, 150))
story.append(Paragraph("RETROVERSE", COVER_T))
story.append(Paragraph("Diseñando un e-Commerce con Inteligencia Artificial", COVER_S))
story.append(Spacer(1, 18))
story.append(Paragraph("Actividad Formativa N.º 2", COVER_M))
story.append(Paragraph("Algoritmos y Estructuras de Datos · ISI · UTN-FRRe · 2026", COVER_M))
story.append(Paragraph("Unidad 2 — Registros y Claves", COVER_M))
story.append(Spacer(1, 40))
story.append(Paragraph("IA utilizada: Claude (Claude Code · Opus 4.8)", COVER_M))
story.append(Paragraph("App publicada:", COVER_M))
story.append(Paragraph('<font color="#05d9e8">%s</font>' % URL, COVER_M))
story.append(PageBreak())

# ---------------- 1. e-commerce ----------------
story.append(P("1. El e-commerce elegido: RetroVerse", H1))
story.append(P("<b>RetroVerse</b> es una tienda digital de objetos vintage, coleccionables y "
               "tecnología retro: computadoras hogareñas, consolas, walkmans, discmans, vinilos, "
               "cartuchos y accesorios gamer de los años 70, 80 y 90. Se plantea como un "
               "<b>marketplace curado</b>, donde cada comprador opera asociado a una tienda/vendedor."))
story.append(P("La consigna pide diseñar el <b>registro principal</b> relacionado con los productos/"
               "servicios, indicando el nombre de cada campo, su tipo de dato y la clave elegida con su "
               "justificación. En este trabajo se va más allá: se construye un <b>modelo relacional "
               "completo en esquema snowflake</b> y una <b>aplicación funcional</b> que lo consume, "
               "publicada en línea mediante un túnel a internet (ver Sección 5)."))
story.append(P("Aclaración: la página es funcional a nivel de <b>navegación entre vistas e ítems y "
               "carrito</b>, pero <b>no procesa pagos reales</b>. Es un modelo académico, no un sistema "
               "de producción.", SMALL))

# ---------------- 2. registro principal ----------------
story.append(P("2. Registro principal: <font face='Courier'>dim_comprador</font> (cliente-comprador)", H1))
story.append(P("El registro maestro está <b>orientado al cliente-comprador</b>. Reúne campos "
               "<b>heterogéneos</b> (texto, fechas, enteros) que describen a la entidad “Comprador”. "
               "La cardinalidad pedida es <b>N:1</b>: muchos compradores compran a un (1) vendedor, lo "
               "que se implementa con la clave foránea <font face='Courier'>id_vendedor</font>."))
data = [[P("Campo", CELLH), P("Tipo (SQL)", CELLH), P("Tam.", CELLH),
         P("Contenido / Continente", CELLH), P("Rol de clave", CELLH)]]
rows = [
    ("id_comprador", "SERIAL", "4 B", "Contenido", "PK — Primaria, Simple"),
    ("dni", "VARCHAR", "11", "Contenido", "Candidata natural, Simple (UNIQUE)"),
    ("email", "VARCHAR", "120", "Contenido", "Candidata natural, Simple (UNIQUE)"),
    ("nombre", "VARCHAR", "60", "Contenido", "—"),
    ("apellido", "VARCHAR", "60", "Contenido", "Secundaria (índice: ordenar/agrupar)"),
    ("fecha_nacimiento", "DATE", "4 B", "Continente (Día/Mes/Año)", "—"),
    ("fecha_alta", "DATE", "4 B", "Contenido", "—"),
    ("id_ciudad", "INT", "4 B", "Contenido", "FK → dim_ciudad"),
    ("id_vendedor", "INT", "4 B", "Contenido", "FK → dim_vendedor (N:1)"),
]
for r in rows:
    data.append([P(r[0], CODE), P(r[1], CELL), P(r[2], CELL), P(r[3], CELL), P(r[4], CELL)])
story.append(tbl(data, [33*mm, 22*mm, 12*mm, 42*mm, 53*mm]))
story.append(Spacer(1, 4))
story.append(P("El campo <font face='Courier'>fecha_nacimiento</font> ilustra el concepto de "
               "<b>campo continente</b>: internamente agrupa los subcampos Día, Mes y Año, que la "
               "aplicación puede descomponer mediante el selector de campo.", SMALL))

# ---------------- 3. clave ----------------
story.append(P("3. Identificación y justificación de la clave", H1))
story.append(P("<b>Clave primaria elegida:</b> <font face='Courier'>id_comprador</font> "
               "(surrogate entera, autoincremental).", BODY))
story.append(P("¿Por qué no usar el DNI o el email como clave primaria?", H2))
story.append(ListFlowable([
    ListItem(P("El <b>DNI</b> es una clave candidata natural y simple, pero puede no existir para "
               "compradores extranjeros, puede cargarse con error y, si cambiara, obligaría a "
               "actualizar todas las tablas que lo referencian.")),
    ListItem(P("El <b>email</b> también es único, pero <b>cambia con frecuencia</b> (la persona migra "
               "de proveedor), lo que lo hace inestable como identificador permanente.")),
    ListItem(P("<font face='Courier'>id_comprador</font> es <b>estable, compacto, nunca nulo y "
               "desacoplado del negocio</b>: ideal como clave primaria y como destino de las claves "
               "foráneas de la tabla de hechos.")),
], bulletType='bullet', leftIndent=14))
story.append(P("DNI y email se conservan como <b>claves candidatas</b> (restricción UNIQUE) para "
               "garantizar unicidad de negocio sin ser la clave primaria.", BODY))

story.append(PageBreak())

# ---------------- 4. modelo snowflake ----------------
story.append(P("4. Modelo de datos: esquema Snowflake", H1))
story.append(P("El modelo es <b>dimensional snowflake</b>: una <b>tabla de hechos</b> central "
               "(<font face='Courier'>hecho_venta</font>, grano = 1 ítem de un pedido) rodeada de "
               "<b>dimensiones normalizadas en cadena</b>. Esa normalización (las “ramas” del copo de "
               "nieve) es lo que distingue al snowflake del star schema y permite mostrar "
               "<b>claves foráneas encadenadas</b>:"))
story.append(ListFlowable([
    ListItem(P("Producto → categoría → familia")),
    ListItem(P("Comprador / Vendedor → ciudad → provincia → país")),
], bulletType='bullet', leftIndent=14))
story.append(P("Tipos de clave presentes en el modelo", H2))
data = [[P("Tipo de clave", CELLH), P("Definición (Unidad 2)", CELLH), P("Ejemplo en RetroVerse", CELLH)]]
krows = [
    ("Primaria (PK)", "Identifica de forma única e irrepetible", "dim_comprador.id_comprador (y todas las id_*)"),
    ("Foránea (FK)", "Puente hacia otro registro / archivo", "dim_comprador.id_vendedor, dim_categoria.id_familia"),
    ("Secundaria", "No única; sirve para agrupar / ordenar / buscar", "idx_comprador_apellido, idx_producto_categoria"),
    ("Simple", "Formada por un único campo contenido", "dni, sku, codigo_iso"),
    ("Compleja / compuesta", "Campo continente / varias columnas", "hecho_venta (nro_pedido, nro_linea) UNIQUE"),
]
for r in krows:
    data.append([P(r[0], CELL), P(r[1], CELL), P(r[2], CODE)])
story.append(tbl(data, [33*mm, 62*mm, 67*mm]))
story.append(Spacer(1, 6))
story.append(P("Tablas del esquema", H2))
story.append(P("<b>Hechos:</b> hecho_venta. &nbsp; <b>Dimensiones:</b> dim_comprador (maestro), "
               "dim_vendedor, dim_producto, dim_categoria, dim_familia, dim_marca, dim_condicion, "
               "dim_decada, dim_ciudad, dim_provincia, dim_pais, dim_tiempo, dim_medio_pago. "
               "El DDL completo y los datos de ejemplo están en los archivos "
               "<font face='Courier'>db/schema.sql</font> y <font face='Courier'>db/seed.sql</font>.", BODY))
story.append(P("Conexión con corte de control", H2))
story.append(P("La tabla de hechos está indexada por tiempo, comprador y (vía comprador) por vendedor. "
               "Ordenando físicamente por la jerarquía <b>vendedor → comprador → fecha</b> se puede "
               "aplicar un <b>corte de control</b> que emita subtotales por vendedor y por comprador. "
               "La clave de corte sería la clave compleja (id_vendedor, id_comprador, fecha).", BODY))

story.append(PageBreak())

# ---------------- 5. arquitectura ----------------
story.append(P("5. Arquitectura y publicación", H1))
story.append(P("La aplicación se construyó con <b>Next.js 14</b> (App Router, React, TypeScript) y "
               "<b>PostgreSQL</b> real: las vistas se renderizan en el servidor y consultan el esquema "
               "<font face='Courier'>retroverse</font> en vivo. El diseño aplica una estética "
               "<b>Synthwave / Y2K neón</b> (fondos oscuros, gradientes magenta-cyan, grid en "
               "perspectiva, glow)."))
story.append(P("Cada publicación muestra una <b>foto real del objeto</b>: las imágenes de los 14 "
               "productos se obtuvieron de Wikipedia / Wikimedia Commons (uso educativo) vía el endpoint "
               "<font face='Courier'>Special:FilePath</font> y se sirven localmente desde "
               "<font face='Courier'>public/img/</font>; el gradiente neón queda como <i>fallback</i> si "
               "faltara la imagen."))
story.append(P("Despliegue (contenedores)", H2))
story.append(ListFlowable([
    ListItem(P("<b>Proyecto Docker Compose aislado</b> (<font face='Courier'>retroverse</font>) con tres "
               "servicios: <font face='Courier'>db</font> (postgres:16-alpine), "
               "<font face='Courier'>app</font> (Next.js standalone) y "
               "<font face='Courier'>bore</font> (túnel HTTP a internet).")),
    ListItem(P("No publica puertos en el host, por lo que <b>no colisiona</b> con los servicios que ya "
               "corren en el servidor (otro Postgres en 5432, MinIO en 9000-9001, app en 3000).")),
    ListItem(P("El esquema y el seed se cargan automáticamente al inicializar la base "
               "(<font face='Courier'>/docker-entrypoint-initdb.d</font>).")),
    ListItem(P("<b>Túnel <font face='Courier'>bore</font></b>: expone la app con una URL pública gratuita "
               "(<font face='Courier'>bore.pub</font>) mediante una conexión <b>saliente</b>, sin abrir "
               "puertos ni necesitar dominio o cuenta. Se descartó el Quick Tunnel de Cloudflare porque el "
               "dominio <font face='Courier'>trycloudflare.com</font> es filtrado por algunos DNS/clientes "
               "(WARP, 1.1.1.1 for Families) del lado del usuario.")),
], bulletType='bullet', leftIndent=14))
story.append(P("URL pública (demo en vivo):", H2))
story.append(P('<font face="Courier" color="#0b6b75">%s</font>' % URL, BODY))
story.append(P("Nota: el puerto remoto del túnel está fijado, por lo que la URL es estable mientras el "
               "contenedor no se recree. Conviene grabar el video demo con la app en línea.", SMALL))

# ---------------- 6. prompts ----------------
story.append(P("6. Prompts utilizados con la IA (cronológico)", H1))
story.append(P("La consigna exige presentar los prompts, incluyendo explícitamente el pedido del diseño "
               "del registro y la definición de la clave. IA: <b>Claude (Claude Code · Opus 4.8)</b>.", SMALL))

def prompt_block(title, text):
    story.append(P(title, H2))
    story.append(Paragraph(text, ParagraphStyle('pq', parent=BODY, leftIndent=10, fontName='Helvetica-Oblique',
                                                 textColor=colors.HexColor('#3a3550'), backColor=SURF,
                                                 borderColor=BORDER, borderWidth=0.5, borderPadding=6, spaceAfter=8)))

prompt_block("Prompt 0 — Contexto teórico (2026-06-17)",
             "Se aportó a la IA la teoría de la Unidad 2 sobre la anatomía de los registros (campos "
             "contenidos/continentes, selector de campo) y el poder de las claves (simple, compleja, "
             "primaria, secundaria, foránea), con su aplicación en corte de control y archivos indexados, "
             "para que la IA modele en base a esos conceptos.")
prompt_block("Prompt 1 — Encargo general (2026-06-17)",
             "“En este workspace hay una carpeta ‘actividad dos’ con un PDF de requerimientos para crear "
             "un e-commerce con IA. Gestioná las skills necesarias (diseño front y modelaje), generalas e "
             "instalalas. El e-commerce elegido es RetroVerse. Armá un modelo de datos relacional en "
             "esquema snowflake para usar diferentes claves. En el server hay un Docker corriendo: armá un "
             "container distinto y, mientras tanto, usá un túnel Cloudflare para una URL random gratis. El "
             "registro maestro será orientado a cliente-comprador con cardinalidad N:1 (muchos compradores "
             "compran a un vendedor). La página debe ser funcional visualmente entre ventanas e ítems, pero "
             "sin pago real. Documentá en un PDF y guardá los prompts cronológicamente.”")
prompt_block("Prompt 2 — Definiciones de arquitectura (2026-06-17)",
             "Ante la repregunta de la IA, se eligió: stack Next.js + PostgreSQL real (esquema snowflake en "
             "base real, app que lee de la BD; contenedores app + db) y estética Synthwave / Y2K neón.")
prompt_block("Prompt 3 — Diseño del registro y la clave (entregado a la IA)",
             "“Diseñá el registro principal de RetroVerse orientado al cliente-comprador, indicando nombre "
             "de cada campo, su tipo de dato y tamaño, e identificá la clave del registro justificando su "
             "elección; integralo a un esquema snowflake con dimensiones normalizadas que muestre claves "
             "primaria, foránea, secundaria, simple y compleja.”")
prompt_block("Prompt 4 — Cambio de túnel por bloqueo de DNS (2026-06-17)",
             "“No me abre la URL del túnel, ni en wifi ni en datos móviles, pero a un amigo sí.” "
             "Diagnóstico de la IA: el dominio trycloudflare.com lo filtran a nivel DNS los clientes de "
             "Cloudflare del dispositivo (WARP / 1.1.1.1 for Families). Se reemplazó el túnel por "
             "bore (bore.pub, otro dominio), integrado al docker-compose con puerto fijo. URL estable.")
prompt_block("Prompt 5 — Imágenes reales en las publicaciones (2026-06-17)",
             "“Ponele imágenes a las publicaciones; buscá los objetos en internet y usalos para los "
             "items.” La IA descargó una foto representativa de cada uno de los 14 productos desde "
             "Wikipedia / Wikimedia Commons (uso educativo), las guardó en public/img/ y pobló "
             "dim_producto.imagen_url; el front muestra la foto con el gradiente neón como fallback.")

story.append(PageBreak())

# ---------------- 7. reflexión ----------------
story.append(P("7. Reflexión: cómo ayudó la IA", H1))
story.append(P("La inteligencia artificial funcionó como copiloto de diseño en todo el trayecto. A partir "
               "de la teoría de registros y claves de la Unidad 2, ayudó a traducir esos conceptos a un "
               "modelo relacional concreto en esquema snowflake, sugiriendo cómo representar cada tipo de "
               "clave (primaria, foránea, secundaria, simple y compleja) con ejemplos coherentes con el "
               "dominio retro. También aceleró tareas mecánicas —escribir el DDL, el seed, los componentes "
               "de la interfaz y la configuración de contenedores— permitiendo concentrarse en las "
               "decisiones de diseño: por qué elegir una surrogate key como clave primaria del comprador, "
               "cómo modelar la cardinalidad N:1 hacia el vendedor y cómo normalizar las jerarquías. "
               "Además, propuso una estética consistente y resolvió la publicación mediante un túnel "
               "a internet. El aporte clave de la IA fue mantener la <b>coherencia entre los conceptos "
               "teóricos, el modelo de datos y la aplicación visible</b>, reduciendo el tiempo de "
               "implementación sin perder el foco pedagógico."))

# ---------------- 8. checklist ----------------
story.append(P("8. Checklist de entrega", H1))
data = [[P("Requisito de la consigna", CELLH), P("Estado", CELLH)]]
checks = [
    ("Nombre y descripción del e-commerce (RetroVerse)", "Sección 1"),
    ("Diseño del registro principal (campos + tipos)", "Sección 2"),
    ("Identificación y explicación de la clave", "Sección 3"),
    ("Captura / registro de los prompts usados con la IA", "Sección 6 + docs/prompts.md"),
    ("App e-commerce con URL publicada", "Sección 5 (túnel bore)"),
    ("Reflexión (5–10 líneas) sobre el aporte de la IA", "Sección 7"),
    ("Video demo de la app (tutorial de uso)", "A grabar por el estudiante"),
]
for r in checks:
    data.append([P(r[0], CELL), P(r[1], CODE)])
story.append(tbl(data, [120*mm, 42*mm]))

# ---------------- build ----------------
doc = BaseDocTemplate(os.path.abspath(OUT), pagesize=A4,
                      leftMargin=18*mm, rightMargin=18*mm, topMargin=24*mm, bottomMargin=20*mm,
                      title="RetroVerse - Documentación Actividad N.º 2",
                      author="Gonzalo Rojas")
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='f')
doc.addPageTemplates([
    PageTemplate(id='cover', frames=[frame], onPage=cover_bg),
    PageTemplate(id='content', frames=[frame], onPage=content_bg),
])
doc.build(story)
print("PDF generado en:", os.path.abspath(OUT))
