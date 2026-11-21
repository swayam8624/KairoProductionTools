# KairoProductionTools — teaching source reading order

Start with the [README](../README.md), then follow this **workflow-oriented** path. These repositories integrate with [KairoPipelineCore](https://github.com/swayam8624/KairoPipelineCore), the host-neutral Python contracts. The order below describes how a user action reaches validated, publishable data—not the import/build order.

1. [README.md](../README.md) — read API inputs, output contracts, errors and downstream caller.
2. [portfolio/projects.json](../portfolio/projects.json) — read API inputs, output contracts, errors and downstream caller.
3. [scripts/build_portfolio.py](../scripts/build_portfolio.py) — read API inputs, output contracts, errors and downstream caller.
4. [tests/test_portfolio_contract.py](../tests/test_portfolio_contract.py) — read API inputs, output contracts, errors and downstream caller.
5. [docs/DEMO_SCRIPT.md](../docs/DEMO_SCRIPT.md) — read API inputs, output contracts, errors and downstream caller.
6. [docs/INSTALLATION.md](../docs/INSTALLATION.md) — read API inputs, output contracts, errors and downstream caller.
7. [docs/NATIVE_VERIFICATION.md](../docs/NATIVE_VERIFICATION.md) — read API inputs, output contracts, errors and downstream caller.
8. [requirements-portfolio.txt](../requirements-portfolio.txt) — read API inputs, output contracts, errors and downstream caller.

## Data flow

Each DCC host adapter emits KairoPipelineCore-compliant diagnostics and immutable publishes. portfolio/projects.json captures per-project evidence and routes reviewers to the respective repositories. build_portfolio.py renders a PDF from that evidence and local supported images; tests check the evidence contract. No PDF build in this documentation-only pass.

## Boundary of the tests

The existing generated PDF is a published artifact, not source code. Do not regenerate it or imply a fresh native DCC verification merely because repository documentation changed.

## Teaching exercises

1. Trace one host action or command into a pure validation function and its structured diagnostic.
2. Identify where filesystem paths are normalized and hashed before publishing.
3. Feed malformed/missing files to the host-neutral path and locate the specific failure/diagnostic.
4. Run the portable tests; then read the native verification checklist before claiming host support.
5. Explain why a dry-run plan, a completed atomic publish, and a native host import are three different events.

## Licensing

Preserve the repository's existing [LICENSE](../LICENSE). The original source and documentation permit learning and development according to that file; external DCC SDKs, plugins, images and example assets retain their own terms.
