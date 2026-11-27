#!/usr/bin/env python3
"""Export the SRS, use cases and traceability appendix as a printable PDF.

Run: uv run --with reportlab --with markdown --with beautifulsoup4 scripts/course_pdf.py
"""

import argparse
import html
import re
from pathlib import Path
from urllib.parse import urljoin

import markdown
from bs4 import BeautifulSoup
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    LongTable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "docs/course"
PAGE_WIDTH, PAGE_HEIGHT = A4
WIDTH = PAGE_WIDTH - 80


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path)
    parser.add_argument("--output", type=Path, default=COURSE / "deliverables/AgentCloud-SRS-v1.0.pdf")
    args = parser.parse_args()
    candidates = [args.font, Path('/mnt/c/Windows/Fonts/simhei.ttf')]
    font_path = next((p for p in candidates if p and p.is_file()), None)
    if font_path:
        pdfmetrics.registerFont(TTFont("CourseText", str(font_path)))
        font = "CourseText"
    else:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        font = "STSong-Light"
    pdfmetrics.registerFontFamily(font, normal=font, bold=font, italic=font, boldItalic=font)
    base = dict(fontName=font, wordWrap="CJK", textColor=colors.HexColor("#24302E"))
    body = ParagraphStyle("Body", fontSize=9, leading=15, spaceAfter=8, **base)
    cell = ParagraphStyle("Cell", fontSize=8, leading=12, **base)
    headings = {
        1: ParagraphStyle("Title", fontSize=22, leading=30, spaceAfter=18, keepWithNext=True, **base),
        2: ParagraphStyle("Heading", fontSize=15, leading=22, spaceBefore=12, spaceAfter=9, keepWithNext=True, **base),
        3: ParagraphStyle("Subheading", fontSize=11, leading=17, spaceBefore=9, spaceAfter=7, keepWithNext=True, **base),
    }
    story = []

    def inline(node):
        text = str(node)
        text = re.sub(r"</?code>", "", text)
        text = re.sub(r"</?p>", "", text)
        text = re.sub(r"<strong>", "<b>", text)
        text = text.replace("</strong>", "</b>")
        text = text.replace("<em>", "<i>").replace("</em>", "</i>")
        return text

    for index, source in enumerate(["SRS.md", "USE_CASES.md", "TRACEABILITY.md"]):
        if index:
            story.append(PageBreak())
        document = BeautifulSoup(markdown.markdown((COURSE / source).read_text(), extensions=["tables"]), "html.parser")
        for link in document.find_all("a", href=True):
            link["href"] = urljoin(
                f"https://github.com/lilong555/agentcloud-course/blob/main/docs/course/{source}",
                link["href"],
            )
        for element in document.children:
            if not getattr(element, "name", None):
                continue
            if element.name in ("h1", "h2", "h3"):
                story.append(Paragraph(inline(element).replace(f"<{element.name}>", "").replace(f"</{element.name}>", ""), headings[int(element.name[1])]))
            elif element.name == "p":
                image = element.find("img")
                if image:
                    path = COURSE / image["src"]
                    figure = Image(str(path))
                    scale = min(WIDTH / figure.imageWidth, 630 / figure.imageHeight)
                    figure.drawWidth = figure.imageWidth * scale
                    figure.drawHeight = figure.imageHeight * scale
                    story.append(figure)
                    story.append(Spacer(1, 10))
                else:
                    story.append(Paragraph(inline(element), body))
            elif element.name == "table":
                rows = []
                for row in element.find_all("tr"):
                    rows.append([
                        Paragraph(inline(td).replace("<th>", "").replace("</th>", "").replace("<td>", "").replace("</td>", ""), cell)
                        for td in row.find_all(["th", "td"])
                    ])
                columns = len(rows[0])
                weights = {2: [1, 4], 3: [1, 2, 3], 4: [1.1, 2.1, 1.1, 3.2], 5: [1.3, 1.3, 1.8, 1.2, 1.3]}.get(columns, [1] * columns)
                table = LongTable(rows, colWidths=[WIDTH * w / sum(weights) for w in weights], repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E5F1EC")),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9F8")]),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LINEBELOW", (0, 0), (-1, 0), 0.6, colors.HexColor("#4F8C78")),
                    ("LINEBELOW", (0, 1), (-1, -1), 0.25, colors.HexColor("#D8E0DC")),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ]))
                story.extend([table, Spacer(1, 10)])
            elif element.name in ("ul", "ol"):
                for number, item in enumerate(element.find_all("li", recursive=False), 1):
                    prefix = f"{number}. " if element.name == "ol" else "• "
                    story.append(Paragraph(html.escape(prefix) + inline(item).replace("<li>", "").replace("</li>", ""), body))

    def page_frame(canvas, document):
        canvas.setStrokeColor(colors.HexColor("#C9D8D1"))
        canvas.line(40, PAGE_HEIGHT - 27, PAGE_WIDTH - 40, PAGE_HEIGHT - 27)
        canvas.setFont(font, 8)
        canvas.setFillColor(colors.HexColor("#56665F"))
        canvas.drawString(40, PAGE_HEIGHT - 21, "AgentCloud | SRS v1.0 | 2026-11-27")
        canvas.drawRightString(PAGE_WIDTH - 40, 24, f"{document.page}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(args.output), pagesize=A4, leftMargin=40, rightMargin=40,
                                 topMargin=42, bottomMargin=42, title="AgentCloud SRS v1.0",
                                 author="AgentCloud Course", pageCompression=1)
    document.build(story, onFirstPage=page_frame, onLaterPages=page_frame)
    print(args.output)


if __name__ == "__main__":
    main()
