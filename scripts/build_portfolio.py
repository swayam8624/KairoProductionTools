#!/usr/bin/env python3
"""Generate the versioned UTS Technical Direction portfolio PDF."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/Swayam_Singal_UTS_Technical_Direction_Portfolio.pdf"
BLENDER_IMAGE = ROOT.parent / "KairoBlender/docs/images/blender-asset-result.png"
W, H = A4

INK = HexColor("#101827")
MUTED = HexColor("#5B6475")
PAPER = HexColor("#F5F7FB")
CARD = white
NAVY = HexColor("#0D1526")
BLUE = HexColor("#4F8EF7")
CYAN = HexColor("#18B6A4")
AMBER = HexColor("#F59E0B")
RED = HexColor("#E45656")
LINE = HexColor("#DDE3EC")


def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def text_block(c: Canvas, text: str, x: float, y: float, width: float,
               *, font: str = "Helvetica", size: float = 9.5,
               color=INK, leading: float | None = None,
               max_lines: int | None = None) -> float:
    leading = leading or size * 1.35
    lines = wrap(text, font, size, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    c.setFont(font, size)
    c.setFillColor(color)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def label(c: Canvas, text: str, x: float, y: float, color=CYAN) -> None:
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(x, y, text.upper())


def title(c: Canvas, text: str, x: float, y: float, width: float = 500) -> float:
    return text_block(c, text, x, y, width, font="Helvetica-Bold", size=24,
                      leading=28, color=INK)


def page_base(c: Canvas, page: int, section: str) -> None:
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(42, H - 40, W - 42, H - 40)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(MUTED)
    c.drawString(42, H - 30, "SWAYAM SINGAL / TECHNICAL DIRECTION")
    c.drawRightString(W - 42, H - 30, section.upper())
    c.line(42, 36, W - 42, 36)
    c.setFont("Helvetica", 7.5)
    c.drawString(42, 23, "Kairo Production Tools / UTS portfolio / August 2026")
    c.drawRightString(W - 42, 23, f"{page} / 8")


def pill(c: Canvas, text: str, x: float, y: float, color=CYAN) -> float:
    width = stringWidth(text, "Helvetica-Bold", 7.5) + 18
    c.setFillColor(color)
    c.roundRect(x, y - 13, width, 19, 9, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawString(x + 9, y - 7, text)
    return x + width + 7


def card(c: Canvas, x: float, y: float, w: float, h: float,
         heading: str, body: str, *, accent=BLUE, metric: str = "") -> None:
    c.setFillColor(CARD)
    c.roundRect(x, y - h, w, h, 10, fill=1, stroke=0)
    c.setFillColor(accent)
    c.roundRect(x, y - h, 5, h, 2.5, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x + 16, y - 22, heading)
    if metric:
        c.setFillColor(accent)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(x + w - 14, y - h + 13, metric)
    text_block(c, body, x + 16, y - 40, w - 30, size=8.5, color=MUTED, leading=11)


def link(c: Canvas, label_text: str, url: str, x: float, y: float,
         *, size: float = 9, color=BLUE) -> None:
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(color)
    c.drawString(x, y, label_text)
    width = stringWidth(label_text, "Helvetica-Bold", size)
    c.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0)


def arrow(c: Canvas, x1: float, y1: float, x2: float, y2: float, color=LINE) -> None:
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.line(x1, y1, x2, y2)
    c.setFillColor(color)
    c.line(x2, y2, x2 - 7, y2 + 4)
    c.line(x2, y2, x2 - 7, y2 - 4)


def box(c: Canvas, x: float, y: float, w: float, h: float,
        heading: str, sub: str, color=BLUE) -> None:
    c.setFillColor(CARD)
    c.setStrokeColor(color)
    c.setLineWidth(1.2)
    c.roundRect(x, y - h, w, h, 8, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 9)
    c.setFillColor(INK)
    c.drawCentredString(x + w / 2, y - 21, heading)
    c.setFont("Helvetica", 7.5)
    c.setFillColor(MUTED)
    c.drawCentredString(x + w / 2, y - 36, sub)


def draw_cover(c: Canvas) -> None:
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.circle(W - 78, H - 100, 88, fill=1, stroke=0)
    c.setFillColor(BLUE)
    c.circle(W - 20, H - 186, 53, fill=1, stroke=0)
    c.setFillColor(AMBER)
    c.circle(W - 34, 68, 30, fill=1, stroke=0)
    label(c, "UTS Animal Logic Academy / Technical Direction", 52, H - 90, CYAN)
    text_block(c, "KAIRO\nPRODUCTION\nTOOLS", 52, H - 150, 440,
               font="Helvetica-Bold", size=40, leading=43, color=white)
    text_block(c, "A multi-DCC artist pipeline from Python validation to C++ engine ingest.",
               54, H - 305, 420, font="Helvetica", size=15, leading=20,
               color=HexColor("#C7D2E6"))
    y = H - 378
    for heading, body in (
        ("4 creative applications", "Blender, Houdini, Nuke, Maya"),
        ("1 production contract", "diagnose -> dry-run -> publish -> verify"),
        ("2 language layers", "Python artist tools + C++23 engine integration"),
    ):
        c.setFillColor(HexColor("#18243B"))
        c.roundRect(52, y - 50, 350, 58, 9, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(68, y - 13, heading)
        c.setFillColor(HexColor("#9EABC1"))
        c.setFont("Helvetica", 9)
        c.drawString(68, y - 32, body)
        y -= 72
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(52, 107, "Swayam Singal")
    c.setFillColor(HexColor("#9EABC1"))
    c.setFont("Helvetica", 9)
    c.drawString(52, 89, "Graphics / engine programmer extending into production technical direction")
    link(c, "github.com/swayam8624/KairoProductionTools",
         "https://github.com/swayam8624/KairoProductionTools", 52, 58,
         size=8.5, color=CYAN)
    c.setFillColor(HexColor("#72809A"))
    c.setFont("Helvetica", 7.5)
    c.drawRightString(W - 40, 27, "Portfolio PDF / 8 pages")
    c.showPage()


def draw_architecture(c: Canvas) -> None:
    page_base(c, 2, "Production architecture")
    label(c, "The system", 42, H - 76)
    title(c, "One contract, many creative hosts", 42, H - 112)
    text_block(c, "Each application keeps its native workflow. The shared layer standardises diagnostics, portable paths, fingerprints, frame sequences, and immutable publication.",
               42, H - 148, 500, size=9.5, color=MUTED)
    y = H - 215
    hosts = [("BLENDER", "asset publish"), ("HOUDINI", "cache publish"),
             ("MAYA", "scene package"), ("NUKE", "shot preflight")]
    x = 42
    for heading, sub in hosts:
        box(c, x, y, 113, 54, heading, sub, CYAN)
        x += 127
    arrow(c, 298, y - 68, 298, y - 98, CYAN)
    box(c, 180, y - 104, 236, 66, "KairoPipelineCore", "strict kairo.publish.v1 / atomic transaction", BLUE)
    arrow(c, 298, y - 180, 298, y - 210, BLUE)
    box(c, 180, y - 216, 236, 66, "IMMUTABLE VERSION", "payloads + provenance + SHA-256", AMBER)
    arrow(c, 180, y - 297, 120, y - 327, LINE)
    arrow(c, 416, y - 297, 476, y - 327, LINE)
    box(c, 42, y - 333, 180, 60, "Nuke downstream check", "missing / mutated output rejection", RED)
    box(c, 374, y - 333, 180, 60, "KairoAssets C++ ingest", "verify / register glTF scene", RED)
    card(c, 42, 178, 158, 92, "Artist feedback", "Errors carry stable codes, severity, suggestions, and a host location for navigation.", accent=CYAN)
    card(c, 218, 178, 158, 92, "Safe mutation", "Dry-run creates nothing. Publication becomes visible only after full staging and verification.", accent=BLUE)
    card(c, 394, 178, 158, 92, "Downstream trust", "Consumers recalculate fingerprints instead of trusting timestamps or filenames.", accent=AMBER)
    c.showPage()


def draw_blender(c: Canvas) -> None:
    page_base(c, 3, "Flagship project")
    label(c, "Project 01 / Native verified", 42, H - 76, CYAN)
    title(c, "Blender to Kairo asset pipeline", 42, H - 112)
    text_block(c, "An artist can find a production problem, navigate to it, apply a bounded fix, and publish a real glTF package without leaving Blender.",
               42, H - 155, 500, size=9.5, color=MUTED)
    image = ImageReader(str(BLENDER_IMAGE))
    c.setFillColor(CARD)
    c.roundRect(42, H - 468, 511, 287, 10, fill=1, stroke=0)
    c.drawImage(image, 50, H - 458, width=495, height=278, preserveAspectRatio=True, anchor="c")
    c.setFillColor(NAVY)
    c.roundRect(52, H - 447, 160, 30, 7, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 8)
    c.setFillColor(white)
    c.drawString(64, H - 435, "NATIVE BLENDER RENDER RESULT")
    y = H - 500
    x = pill(c, "VALIDATE", 42, y, CYAN)
    x = pill(c, "NAVIGATE", x, y, BLUE)
    x = pill(c, "SAFE FIX", x, y, AMBER)
    x = pill(c, "DRY-RUN", x, y, BLUE)
    pill(c, "PUBLISH", x, y, CYAN)
    card(c, 42, H - 545, 158, 112, "Artist surface", "Blender panel, diagnostics list, property navigation, scale fix, selected/all scope, version controls.", accent=CYAN)
    card(c, 218, H - 545, 158, 112, "Production output", "Separate glTF, binary buffer, textures, source provenance, per-file SHA-256, atomic version directory.", accent=BLUE)
    card(c, 394, H - 545, 158, 112, "Evidence", "Blender 5.2 LTS: 4 native tests, 4 pure tests, fresh-profile install, package validation, 1280x720 render.", accent=AMBER)
    link(c, "GitHub: KairoBlender", "https://github.com/swayam8624/KairoBlender", 42, 73)
    c.showPage()


def draw_contract(c: Canvas) -> None:
    page_base(c, 4, "Python and C++")
    label(c, "Shared infrastructure", 42, H - 76, BLUE)
    title(c, "A handoff that can prove what it consumed", 42, H - 112)
    text_block(c, "The engine does not trust that a DCC publish stayed unchanged. Python records the contract; C++ reloads it strictly and verifies every byte before registry mutation.",
               42, H - 145, 500, size=9.5, color=MUTED)
    c.setFillColor(NAVY)
    c.roundRect(42, H - 390, 246, 202, 10, fill=1, stroke=0)
    label(c, "Python publication", 58, H - 212, CYAN)
    code = [
        "manifest = PublishManifest(",
        "  kind=ASSET, source_host='blender',",
        "  outputs=(scene,), dependencies=files)",
        "",
        "plan_publish(...)       # no writes",
        "publish_bundle(...)     # stage + verify",
        "os.replace(staging, target)",
    ]
    c.setFillColor(HexColor("#D8E3F4"))
    c.setFont("Courier", 7.8)
    yy = H - 238
    for line_text in code:
        c.drawString(58, yy, line_text)
        yy -= 17
    c.setFillColor(NAVY)
    c.roundRect(306, H - 390, 246, 202, 10, fill=1, stroke=0)
    label(c, "C++23 ingestion", 322, H - 212, AMBER)
    code = [
        "auto manifest = LoadPipelinePublishManifest(path);",
        "ValidatePipelinePublishBundle(path, manifest);",
        "",
        "AssetID id = RegisterBlenderPublish(",
        "  projectRoot, path, registry);",
        "",
        "// rejects tamper / escape / symlink",
    ]
    c.setFillColor(HexColor("#D8E3F4"))
    c.setFont("Courier", 7.4)
    yy = H - 238
    for line_text in code:
        c.drawString(322, yy, line_text)
        yy -= 17
    card(c, 42, H - 430, 158, 108, "Portable schema", "Exact keys and types, bounded arrays/text, project-relative paths, deterministic canonical JSON.", accent=CYAN, metric="v1")
    card(c, 218, H - 430, 158, 108, "Transaction safety", "Fingerprint before staging, copy without symlink following, verify staged bytes, atomic rename, rollback on failure.", accent=BLUE, metric="32 TESTS")
    card(c, 394, H - 430, 158, 108, "Engine trust gate", "Strict JSON, bundle containment, regular-file checks, SHA-256 replay, exact glTF candidate selection.", accent=AMBER, metric="2/2 CTEST")
    text_block(c, "Problem solved: timestamp checks and ad-hoc exporters cannot prove that the engine is loading the artist-approved version. Content identity and an immutable contract can.",
               42, 180, 510, font="Helvetica-Bold", size=10.5, color=INK, leading=15)
    link(c, "KairoPipelineCore", "https://github.com/swayam8624/KairoPipelineCore", 42, 100)
    link(c, "KairoAssets", "https://github.com/swayam8624/KairoAssets", 190, 100)
    link(c, "KairoGameEngine", "https://github.com/swayam8624/KairoGameEngine", 292, 100)
    c.showPage()


def draw_houdini(c: Canvas) -> None:
    page_base(c, 5, "FX pipeline support")
    label(c, "Project 02 / Host-neutral verified", 42, H - 76, AMBER)
    title(c, "Houdini CacheGuard", 42, H - 112)
    text_block(c, "A cache assistant for the expensive moment before, during, and after simulation. It turns a failed sequence into an exact resume plan instead of another full recook.",
               42, H - 155, 500, size=9.5, color=MUTED)
    stages = [
        ("BEFORE COOK", "Validate $F tokens, project containment, frame range, free space, and cache budget."),
        ("AFTER INTERRUPTION", "Scan the directory and compress missing frames into resumable ranges."),
        ("BEFORE PUBLISH", "Compare upstream graph fingerprint, reject stale or incomplete frames."),
        ("AT HANDOFF", "Publish every cache frame with provenance and immutable SHA-256 identity."),
    ]
    y = H - 210
    for index, (heading, body) in enumerate(stages, 1):
        c.setFillColor(AMBER if index < 4 else CYAN)
        c.circle(65, y - 18, 16, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(65, y - 21, str(index))
        c.setFillColor(CARD)
        c.roundRect(96, y - 54, 456, 62, 9, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(INK)
        c.drawString(112, y - 13, heading)
        text_block(c, body, 112, y - 31, 420, size=8.3, color=MUTED, leading=10.5)
        if index < 4:
            c.setStrokeColor(LINE)
            c.setLineWidth(2)
            c.line(65, y - 35, 65, y - 72)
        y -= 82
    card(c, 42, 210, 246, 103, "Failure made actionable", "Example: frames 1005-1008 missing; cache changed upstream; estimated completion exceeds configured free-space reserve.", accent=RED)
    card(c, 306, 210, 246, 103, "Verification", "10 unit tests plus compile, JSON package validation, shelf XML validation, and green GitHub CI. Native HOM/hython is license-gated.", accent=AMBER)
    link(c, "GitHub: KairoHoudini", "https://github.com/swayam8624/KairoHoudini", 42, 73)
    c.showPage()


def draw_nuke(c: Canvas) -> None:
    page_base(c, 6, "Compositing preflight")
    label(c, "Project 03 / Host-neutral verified", 42, H - 76, RED)
    title(c, "Nuke ShotDoctor", 42, H - 112)
    text_block(c, "A Read/Write preflight that catches plate, range, colorspace, connection, path, and overwrite errors before render submission.",
               42, H - 145, 500, size=9.5, color=MUTED)
    y = H - 228
    box(c, 42, y, 120, 62, "READ", "plates/main.####.exr", BLUE)
    arrow(c, 162, y - 31, 232, y - 31, BLUE)
    box(c, 232, y, 120, 62, "COMP TREE", "groups included", CYAN)
    arrow(c, 352, y - 31, 422, y - 31, BLUE)
    box(c, 422, y, 130, 62, "WRITE", "renders/v003/####", AMBER)
    diagnostics = [
        ("NUKE_READ_FRAMES_MISSING", "Frames 1007-1010 are absent from the plate.", RED),
        ("NUKE_READ_COLORSPACE", "Read colorspace is outside the approved show profile.", AMBER),
        ("NUKE_WRITE_DISCONNECTED", "The render output has no input branch.", RED),
        ("NUKE_WRITE_OVERWRITE", "14 frames already exist in this version.", AMBER),
    ]
    yy = H - 335
    for code, message, color in diagnostics:
        c.setFillColor(CARD)
        c.roundRect(42, yy - 46, 510, 53, 8, fill=1, stroke=0)
        c.setFillColor(color)
        c.roundRect(42, yy - 46, 5, 53, 2, fill=1, stroke=0)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(color)
        c.drawString(58, yy - 12, code)
        c.setFont("Helvetica", 8.5)
        c.setFillColor(MUTED)
        c.drawString(58, yy - 30, message)
        yy -= 64
    card(c, 42, 230, 246, 108, "Cross-DCC trust", "Load Houdini cache or render manifests, check allowed kind, output presence, byte count, and SHA-256 before ingest.", accent=CYAN)
    card(c, 306, 230, 246, 108, "Verification", "10 tests cover rules, grouped-node adapter shape, controlled no-host behavior, valid ingest, missing output, and mutation rejection. CI is green.", accent=RED)
    link(c, "GitHub: KairoNuke", "https://github.com/swayam8624/KairoNuke", 42, 73)
    c.showPage()


def draw_maya(c: Canvas) -> None:
    page_base(c, 7, "Scene assembly")
    label(c, "Project 04 / Host-neutral verified", 42, H - 76, BLUE)
    title(c, "Maya SceneDoctor", 42, H - 112)
    text_block(c, "A dockable scene handoff panel backed by Maya API 2.0 mesh inspection and command-layer project diagnostics.",
               42, H - 155, 500, size=9.5, color=MUTED)
    items = [
        ("REFERENCES", "Missing/unloaded files, external paths, duplicate or reserved namespaces.", CYAN),
        ("TRANSFORMS", "Dirty export roots and zero/negative scale without silent artistic fixes.", AMBER),
        ("GEOMETRY", "Empty meshes, missing UVs/materials, nonmanifold edges, lamina faces.", RED),
        ("TEXTURES", "Missing/external files and colorspaces outside the project profile.", BLUE),
    ]
    positions = [(42, H - 215), (306, H - 215), (42, H - 360), (306, H - 360)]
    for (heading, body, color), (x, y) in zip(items, positions):
        card(c, x, y, 246, 120, heading, body, accent=color)
    c.setFillColor(NAVY)
    c.roundRect(42, H - 650, 510, 142, 10, fill=1, stroke=0)
    label(c, "Dockable artist loop", 60, H - 535, CYAN)
    text_block(c, "OPEN PANEL  ->  VALIDATE SCENE  ->  DOUBLE-CLICK DIAGNOSTIC  ->  FIX IN CONTEXT  ->  REVALIDATE",
               60, H - 565, 470, font="Courier-Bold", size=9, leading=14, color=white)
    text_block(c, "Once preflight is clear, the package publisher stages the .ma/.mb scene, project references, and textures, verifies them, and exposes the version atomically.",
               60, H - 602, 470, size=8.5, color=HexColor("#B7C2D6"), leading=12)
    pill(c, "8 TESTS", 42, 157, BLUE)
    pill(c, "API 2.0 ADAPTER", 112, 157, CYAN)
    pill(c, "ATOMIC PACKAGE", 224, 157, AMBER)
    pill(c, "GREEN CI", 341, 157, CYAN)
    text_block(c, "Native Maya panel/API execution remains an explicit install and license gate.",
               42, 116, 500, size=8.5, color=MUTED)
    link(c, "GitHub: KairoMaya", "https://github.com/swayam8624/KairoMaya", 42, 73)
    c.showPage()


def draw_closing(c: Canvas) -> None:
    page_base(c, 8, "Evidence and fit")
    label(c, "Application summary", 42, H - 76, CYAN)
    title(c, "Production engineering in service of artists", 42, H - 112)
    text_block(c, "This suite is a solo engineering portfolio built around an artist review loop: visible diagnostics, navigable failures, bounded fixes, repeatable demos, and explicit host gates. It is ready for collaborative usability testing rather than presented as unverified group work.",
               42, H - 145, 510, size=9.3, color=MUTED, leading=12.5)
    c.setFillColor(CARD)
    c.roundRect(42, H - 390, 510, 192, 10, fill=1, stroke=0)
    headers = ["Surface", "Evidence", "Status"]
    xs = [58, 213, 462]
    for header, x in zip(headers, xs):
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(MUTED)
        c.drawString(x, H - 220, header.upper())
    rows = [
        ("Pipeline core", "32 tests / multi-platform CI", "GREEN"),
        ("Blender", "8 tests / native host + render", "NATIVE"),
        ("Houdini", "10 tests / package + CI", "HOST GATE"),
        ("Nuke", "10 tests / adapter + CI", "HOST GATE"),
        ("Maya", "8 tests / publisher + CI", "HOST GATE"),
        ("KairoAssets", "C++23 build / 2 of 2 CTest", "NATIVE"),
    ]
    yy = H - 246
    for surface, evidence, status in rows:
        c.setStrokeColor(LINE)
        c.line(58, yy - 9, 536, yy - 9)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 8.3)
        c.drawString(58, yy, surface)
        c.setFont("Helvetica", 8.3)
        c.setFillColor(MUTED)
        c.drawString(213, yy, evidence)
        color = CYAN if status in {"GREEN", "NATIVE"} else AMBER
        c.setFillColor(color)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(462, yy, status)
        yy -= 25
    card(c, 42, H - 430, 158, 118, "Python", "Shared package plus four DCC adapters. Pure rules are isolated from host APIs for fast feedback and CI.", accent=CYAN)
    card(c, 218, H - 430, 158, 118, "C++23", "Strict engine-side consumer integrated into KairoAssets and pinned in KairoGameEngine.", accent=BLUE)
    card(c, 394, H - 430, 158, 118, "Problem solving", "Late failures become precise actions: resume ranges, path fixes, integrity rejection, and rollback.", accent=AMBER)
    label(c, "Repository index", 42, 216, BLUE)
    repos = [
        ("Portfolio hub", "https://github.com/swayam8624/KairoProductionTools"),
        ("Core", "https://github.com/swayam8624/KairoPipelineCore"),
        ("Blender", "https://github.com/swayam8624/KairoBlender"),
        ("Houdini", "https://github.com/swayam8624/KairoHoudini"),
        ("Nuke", "https://github.com/swayam8624/KairoNuke"),
        ("Maya", "https://github.com/swayam8624/KairoMaya"),
        ("C++ engine assets", "https://github.com/swayam8624/KairoAssets"),
    ]
    x, y = 42, 190
    for index, (name, url) in enumerate(repos):
        link(c, name, url, x, y, size=8.5)
        if index == 3:
            x, y = 306, 190
        else:
            y -= 24
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(INK)
    c.drawRightString(W - 42, 69, "Prepared for UTS Master of Animation and Visualisation")
    c.showPage()


def build() -> None:
    if not BLENDER_IMAGE.is_file():
        raise FileNotFoundError(f"Blender visual evidence is missing: {BLENDER_IMAGE}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Swayam Singal - UTS Technical Direction Portfolio")
    c.setAuthor("Swayam Singal")
    c.setSubject("Artist-facing Python DCC tools and C++ engine pipeline")
    draw_cover(c)
    draw_architecture(c)
    draw_blender(c)
    draw_contract(c)
    draw_houdini(c)
    draw_nuke(c)
    draw_maya(c)
    draw_closing(c)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
