#!/usr/bin/env python3
"""Markdown (subconjunto) -> PDF con reportlab. Sin dependencias externas."""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, KeepTogether,
                                Preformatted, HRFlowable, CondPageBreak)

pdfmetrics.registerFont(TTFont("Body", "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"))
pdfmetrics.registerFont(TTFont("Mono", "/System/Library/Fonts/Monaco.ttf"))
pdfmetrics.registerFont(TTFont("BodyB", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("BodyI", "/System/Library/Fonts/Supplemental/Arial Italic.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="BodyB", italic="BodyI")

INK   = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#5b6472")
ACC   = colors.HexColor("#0f5c8c")
CODEB = colors.HexColor("#f4f6f8")
CODEE = colors.HexColor("#d5dbe2")
NOTEB = colors.HexColor("#fdf6e3")
NOTEE = colors.HexColor("#d9c88f")

S = {
 "h1": ParagraphStyle("h1", fontName="BodyB", fontSize=21, leading=26, textColor=ACC,
                      spaceBefore=0, spaceAfter=10),
 "h2": ParagraphStyle("h2", fontName="BodyB", fontSize=14.5, leading=19, textColor=INK,
                      spaceBefore=15, spaceAfter=6),
 "h3": ParagraphStyle("h3", fontName="BodyB", fontSize=11.5, leading=15, textColor=ACC,
                      spaceBefore=11, spaceAfter=4),
 "p":  ParagraphStyle("p", fontName="Body", fontSize=9.6, leading=14, textColor=INK,
                      spaceAfter=6, alignment=TA_LEFT),
 "li": ParagraphStyle("li", fontName="Body", fontSize=9.6, leading=13.5, textColor=INK,
                      leftIndent=11, bulletIndent=2, spaceAfter=2.5),
 "th": ParagraphStyle("th", fontName="BodyB", fontSize=8.4, leading=11, textColor=colors.white),
 "td": ParagraphStyle("td", fontName="Body", fontSize=8.4, leading=11, textColor=INK),
 "note": ParagraphStyle("note", fontName="Body", fontSize=9.2, leading=13.2, textColor=INK),
 "cover_t": ParagraphStyle("ct", fontName="BodyB", fontSize=30, leading=36, textColor=ACC,
                           alignment=TA_CENTER, spaceAfter=10),
 "cover_s": ParagraphStyle("cs", fontName="Body", fontSize=13, leading=19, textColor=MUTED,
                           alignment=TA_CENTER),
 "toc": ParagraphStyle("toc", fontName="Body", fontSize=9.6, leading=15, textColor=INK,
                       leftIndent=8),
}

def inline(t):
    t = (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    t = re.sub(r"`([^`]+)`",
               r'<font name="Mono" size="8.8" backColor="#eef1f4">\1</font>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", t)
    return t

def code_block(lines, avail):
    """Una fila por línea, para que el bloque pueda partirse entre páginas."""
    txt = [l.rstrip() for l in lines]
    while txt and not txt[-1]: txt.pop()
    while txt and not txt[0]:  txt.pop(0)
    longest = max((len(l) for l in txt), default=0)
    size = 8.3
    while longest * size * 0.6 > avail - 16 and size > 4.8:
        size -= 0.15
    st = ParagraphStyle("code", fontName="Mono", fontSize=size,
                        leading=size * 1.32, textColor=INK)
    rows = [[Preformatted(l if l else " ", st)] for l in txt]
    t = Table(rows, colWidths=[avail], splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), CODEB),
        ("BOX", (0,0), (-1,-1), 0.6, CODEE),
        ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 0), ("BOTTOMPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,0), 6), ("BOTTOMPADDING", (0,-1), (-1,-1), 6),
    ]))
    return t

def note_block(lines, avail):
    paras = [Paragraph(inline(l), S["note"]) for l in lines if l.strip()]
    t = Table([[paras]], colWidths=[avail])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), NOTEB),
        ("BOX", (0,0), (-1,-1), 0.6, NOTEE),
        ("LINEBEFORE", (0,0), (0,-1), 2.6, colors.HexColor("#c9a227")),
        ("LEFTPADDING", (0,0), (-1,-1), 9), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    return t

def table_block(rows, avail):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    cells = [c for c in cells if not all(re.fullmatch(r":?-{2,}:?", x or "-") for x in c)]
    if not cells: return None
    ncol = max(len(r) for r in cells)
    cells = [r + [""] * (ncol - len(r)) for r in cells]
    data = [[Paragraph(inline(c), S["th"] if i == 0 else S["td"]) for c in row]
            for i, row in enumerate(cells)]
    widths = []
    raw = [[len(c) for c in row] for row in cells]
    tot = [max(col) for col in zip(*raw)]
    ssum = sum(tot) or 1
    for w in tot:
        widths.append(max(avail * 0.07, avail * w / ssum))
    scale = avail / sum(widths)
    widths = [w * scale for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ACC),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f2f5f8")]),
        ("GRID", (0,0), (-1,-1), 0.45, colors.HexColor("#c6cdd6")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 5), ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 3.5), ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
    ]))
    return t

def build(md, out, title, subtitle):
    PW, PH = A4
    LM = RM = 17 * mm
    TM, BM = 17 * mm, 16 * mm
    avail = PW - LM - RM

    doc = BaseDocTemplate(out, pagesize=A4, leftMargin=LM, rightMargin=RM,
                          topMargin=TM, bottomMargin=BM, title=title,
                          author="Gonzalo Rojas")
    frame = Frame(LM, BM, avail, PH - TM - BM, id="n")

    def deco(canv, d):
        canv.saveState()
        n = canv.getPageNumber()
        if n > 1:
            canv.setFont("Body", 7.5); canv.setFillColor(MUTED)
            canv.drawString(LM, BM - 9 * mm, title)
            canv.drawRightString(PW - RM, BM - 9 * mm, str(n))
            canv.setStrokeColor(colors.HexColor("#dfe4ea")); canv.setLineWidth(0.4)
            canv.line(LM, BM - 6.5 * mm, PW - RM, BM - 6.5 * mm)
        canv.restoreState()

    doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=deco)])

    F = []
    # ── portada ──
    F += [Spacer(1, 52 * mm), Paragraph(title, S["cover_t"]),
          Spacer(1, 4 * mm), Paragraph(subtitle, S["cover_s"]), Spacer(1, 10*mm),
          HRFlowable(width="55%", thickness=1, color=CODEE, hAlign="CENTER")]

    lines = md.split("\n")
    i = 0
    first_h1 = True
    buf = []

    def flush():
        nonlocal buf
        if buf:
            txt = " ".join(buf).strip()
            if txt: F.append(Paragraph(inline(txt), S["p"]))
            buf = []

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()

        if s.startswith("```"):
            flush(); i += 1; blk = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                blk.append(lines[i]); i += 1
            i += 1
            F.append(code_block(blk, avail)); F.append(Spacer(1, 6)); continue

        if s.startswith("> "):
            flush(); blk = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                blk.append(lines[i].strip().lstrip(">").strip()); i += 1
            F.append(note_block(blk, avail)); F.append(Spacer(1, 6)); continue

        if s.startswith("|") and s.endswith("|"):
            flush(); blk = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                blk.append(lines[i]); i += 1
            t = table_block(blk, avail)
            if t: F.append(t); F.append(Spacer(1, 7))
            continue

        if s.startswith("# "):
            flush()
            if not first_h1:
                F.append(CondPageBreak(0.62 * (PH - TM - BM)))
                F.append(Spacer(1, 6))
            first_h1 = False
            F.append(Paragraph(inline(s[2:]), S["h1"]))
            F.append(HRFlowable(width="100%", thickness=1.1, color=ACC,
                                spaceBefore=1, spaceAfter=9))
            i += 1; continue
        if s.startswith("### "):
            flush(); F.append(Paragraph(inline(s[4:]), S["h3"])); i += 1; continue
        if s.startswith("## "):
            flush(); F.append(Paragraph(inline(s[3:]), S["h2"])); i += 1; continue

        def es_item(k):
            return k < len(lines) and re.match(r"^\s*((-|\*)|\d+\.)\s+", lines[k])

        def continua(k):
            """línea que sigue a un item: indentada, no vacía, y no un item nuevo"""
            if k >= len(lines): return False
            raw = lines[k]
            return (raw.startswith(("  ", "\t")) and raw.strip()
                    and not es_item(k)
                    and not raw.strip().startswith(("|", ">", "```", "#")))

        if es_item(i):
            flush()
            while es_item(i):
                m = re.match(r"^\s*((?:-|\*)|(\d+)\.)\s+(.*)", lines[i])
                bullet = "•" if m.group(2) is None else m.group(2) + "."
                partes = [m.group(3)]
                i += 1
                while continua(i):
                    partes.append(lines[i].strip()); i += 1
                F.append(Paragraph(inline(" ".join(partes)), S["li"], bulletText=bullet))
            F.append(Spacer(1, 4)); continue

        if s in ("---", "***"):
            flush(); F.append(Spacer(1, 3))
            F.append(HRFlowable(width="100%", thickness=0.5, color=CODEE))
            F.append(Spacer(1, 5)); i += 1; continue

        if not s:
            flush(); i += 1; continue

        buf.append(s); i += 1

    flush()
    doc.build(F)

if __name__ == "__main__":
    src, out, title, sub = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    build(open(src, encoding="utf-8").read(), out, title, sub)
    print("PDF:", out)
