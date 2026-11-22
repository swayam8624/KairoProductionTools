# Production portfolio — a report is not a DCC acceptance test

KairoProductionTools assembles human-readable evidence about workflows that span Blender, Maya, Houdini, Nuke and the Kairo engine. Its principal generator is [`scripts/build_portfolio.py`](../scripts/build_portfolio.py), using ReportLab to create a PDF. The report may be useful for a technical review, but creating a beautiful PDF does not establish that the cited tools ran successfully.

## 1. Distinguish source, generated artifact and tested claim

A source DCC scene (`.blend`, `.ma`, `.hip`, `.nk`) records authoring state. A *publish manifest* records a version, intended files and content hashes. A *consumer validation* checks the actual bytes against the manifest. A *portfolio page* explains or displays those results.

The [KairoPipelineCore publication walkthrough](https://github.com/swayam8624/KairoPipelineCore/blob/docs/teaching-walkthrough-20261121/docs/CROSS_DCC_PUBLICATION_WALKTHROUGH.md) covers producer/consumer fingerprint verification. A static screenshot in the portfolio does not substitute for that stage.

## 2. Read the builder in execution order

The script configures fixed A4 dimensions, typographic colors, margins and output locations; reusable functions `wrap`, `text_block`, `title`, `card`, `link` and `page_base` place content on a ReportLab Canvas. Section functions such as `draw_architecture`, `draw_blender`, `draw_houdini`, `draw_nuke`, `draw_maya` and `draw_closing` create pages in a controlled order.

The `build()` entry point coordinates those pages and writes the final PDF. Because coordinates, page dimensions and media references are partly fixed, inspect page clipping and missing image handling before treating the output as publication-ready.

**Exercise:** take a known-valid evidence image, remove it temporarily, and observe how the builder handles the missing file. Confirm the PDF still clearly identifies which verification evidence was unavailable rather than implying success.

## 3. Make claims inspectable

For each illustrated workflow, attach its exact source repo/commit, DCC version and OS, input scene, export command, package manifest hash, native-host test result and independent consumer readback. For performance claims, record dataset, measurement method, host and repetition count.

Use clear evidence labels: *source-present*, *unit-tested*, *native-host verified*, *benchmark-evidenced* or *not yet verified*. A concept rendering or manually prepared screenshot should not be captioned as proof of a complete import/export pipeline.

## 4. Licensing and provenance

The code license for a report generator may permit others to learn and extend its layout logic. It does **not** automatically allow public redistribution of source photographs, third-party logos, screenshots from proprietary software, fonts, media assets or external datasets. Preserve a per-asset attribution and permissions register before publishing downloadable media.

Do not attach unrelated model or texture licenses to material merely because it appears on the same page.

## 5. Tests and release process

Read [`tests/test_portfolio_contract.py`](../tests/test_portfolio_contract.py) and [`docs/SOURCE_READING_ORDER.md`](SOURCE_READING_ORDER.md). Validate that links remain correct, references exist, text does not overflow page boundaries, and the generated PDF can be opened on another machine. Then inspect the actual visual output before distributing it.

A ReportLab build succeeding proves that a document file was generated, not that Maya or Houdini produced its source data correctly.

*Evidence note: source-derived teaching document only; no native DCC test or new portfolio PDF was produced in this documentation pass.*
