import os
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

BASE = os.path.expanduser("~/ELearning-NS2/documentation")
MD_FILE = os.path.join(BASE, "project_report.md")
FIGURE_DIR = os.path.join(BASE, "figures")
OUTPUT = os.path.join(BASE, "Network_Performance_Analysis_Report.docx")

doc = Document()

# Page layout
section = doc.sections[0]
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.75)
section.left_margin = Inches(0.85)
section.right_margin = Inches(0.85)

# Default font
styles = doc.styles
styles["Normal"].font.name = "Times New Roman"
styles["Normal"].font.size = Pt(11)

for style_name in ["Heading 1", "Heading 2", "Heading 3"]:
    styles[style_name].font.name = "Times New Roman"
    styles[style_name].font.color.rgb = RGBColor(31, 78, 121)

styles["Heading 1"].font.size = Pt(16)
styles["Heading 1"].font.bold = True
styles["Heading 2"].font.size = Pt(13)
styles["Heading 2"].font.bold = True
styles["Heading 3"].font.size = Pt(12)

# Page number footer
for sec in doc.sections:
    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run("Page ")
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)

# Cover page
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(65)
r = p.add_run("PROJECT REPORT")
r.bold = True
r.font.size = Pt(22)
r.font.name = "Times New Roman"
r.font.color.rgb = RGBColor(31, 78, 121)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(35)
r = p.add_run(
    "NETWORK PERFORMANCE ANALYSIS\n"
    "OF A UNIVERSITY E-LEARNING SYSTEM"
)
r.bold = True
r.font.size = Pt(19)
r.font.name = "Times New Roman"

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(35)
r = p.add_run("Submitted by")
r.bold = True
r.font.size = Pt(14)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("KANDLAPALLI BHARATH KUMAR")
r.bold = True
r.font.size = Pt(16)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(30)
p.add_run("Department of Computer Science and Engineering\n")
p.add_run("Madanapalle Institute of Technology & Science\n")
p.add_run("Academic Year: 2026–2027")

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.paragraph_format.space_before = Pt(35)
r = p.add_run(
    "Project Guide: __________________________\n"
    "Roll Number: __________________________"
)
r.font.size = Pt(11)

doc.add_page_break()

# Inline Markdown formatting
def add_formatted_text(paragraph, text):
    parts = re.split(r'(\*\*.*?\*\*|\*.*?\*)', text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        elif part.startswith("*") and part.endswith("*"):
            run = paragraph.add_run(part[1:-1])
            run.italic = True
        else:
            paragraph.add_run(part)

def add_table(rows):
    if not rows:
        return
    cleaned = []
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells):
            continue
        cleaned.append(cells)

    if not cleaned:
        return

    cols = max(len(r) for r in cleaned)
    table = doc.add_table(rows=0, cols=cols)
    table.style = "Table Grid"

    for row_index, values in enumerate(cleaned):
        cells = table.add_row().cells
        for i in range(cols):
            value = values[i] if i < len(values) else ""
            cells[i].text = value
            for paragraph in cells[i].paragraphs:
                for run in paragraph.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(9)
                    if row_index == 0:
                        run.bold = True
            if row_index == 0:
                shading = OxmlElement("w:shd")
                shading.set(qn("w:fill"), "D9EAF7")
                cells[i]._tc.get_or_add_tcPr().append(shading)

    doc.add_paragraph()

# Read Markdown
with open(MD_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

paragraph_buffer = []
table_buffer = []
list_buffer = []

def flush_paragraph():
    global paragraph_buffer
    if paragraph_buffer:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        add_formatted_text(p, " ".join(x.strip() for x in paragraph_buffer))
        paragraph_buffer = []

def flush_table():
    global table_buffer
    if table_buffer:
        add_table(table_buffer)
        table_buffer = []

def flush_lists():
    global list_buffer
    for item, ordered in list_buffer:
        style = "List Number" if ordered else "List Bullet"
        p = doc.add_paragraph(style=style)
        add_formatted_text(p, item)
    list_buffer = []

for line in lines:
    stripped = line.strip()

    # Skip empty lines after flushing content
    if not stripped:
        flush_paragraph()
        flush_table()
        flush_lists()
        continue

    # Markdown table
    if stripped.startswith("|") and stripped.endswith("|"):
        flush_paragraph()
        flush_lists()
        table_buffer.append(stripped)
        continue
    else:
        flush_table()

    # Headings
    heading_match = re.match(r"^(#{1,3})\s+(.*)", stripped)
    if heading_match:
        flush_paragraph()
        flush_lists()
        level = len(heading_match.group(1))
        title = heading_match.group(2).strip()
        doc.add_heading(title, level=level)
        continue

    # Numbered and bulleted lists
    numbered = re.match(r"^\d+\.\s+(.*)", stripped)
    bullet = re.match(r"^[-*]\s+(.*)", stripped)

    if numbered:
        flush_paragraph()
        list_buffer.append((numbered.group(1), True))
        continue
    elif bullet:
        flush_paragraph()
        list_buffer.append((bullet.group(1), False))
        continue
    else:
        flush_lists()

    paragraph_buffer.append(stripped)

flush_paragraph()
flush_table()
flush_lists()

# Add actual graphs in a dedicated section
doc.add_page_break()
doc.add_heading("APPENDIX: SIMULATION GRAPHS", level=1)

graphs = [
    ("pdr_comparison.png", "Figure 1: Packet Delivery Ratio Comparison"),
    ("plr_comparison.png", "Figure 2: Packet Loss Ratio Comparison"),
    ("throughput_comparison.png", "Figure 3: Throughput Comparison"),
    ("delay_comparison.png", "Figure 4: Average Delay Comparison"),
    ("congestion_pdr.png", "Figure 5: Congestion - Packet Delivery Ratio"),
    ("congestion_plr.png", "Figure 6: Congestion - Packet Loss Ratio"),
    ("congestion_throughput.png", "Figure 7: Congestion - Throughput"),
    ("congestion_delay.png", "Figure 8: Congestion - Average Delay"),
    ("sliding_window_throughput.png", "Figure 9: TCP Sliding Window Throughput"),
    ("sliding_window_delay.png", "Figure 10: TCP Sliding Window Average Delay"),
]

for filename, caption in graphs:
    path = os.path.join(FIGURE_DIR, filename)
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Inches(5.8))
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption)
        r.italic = True
        r.font.size = Pt(10)
        doc.add_paragraph()
    else:
        print("WARNING: Missing graph:", filename)

doc.save(OUTPUT)
print("Word report generated successfully:")
print(OUTPUT)
