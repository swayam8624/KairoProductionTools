# KairoProductionTools: linked source-reading order

This repo coordinates the DCC portfolio and emits a versioned evidence/portfolio deliverable. Begin with the portfolio builder and its tests, then follow each documented bridge into independently versioned KairoPipelineCore/Blender/Houdini/Maya/Nuke repos.

## APIs and boundaries

The builder reads declared source evidence, packages reproducible artifacts and checks the output contract; it should not invent unexecuted validation. The underlying pipeline APIs are in KairoPipelineCore and each host-specific bridge.

## Read these files (2)

1. [`scripts/build_portfolio.py`](scripts/build_portfolio.py) — inspect the host API dependencies, validation, returned evidence and failure handling; compare its callers to corresponding tests.
2. [`tests/test_portfolio_contract.py`](tests/test_portfolio_contract.py) — inspect the host API dependencies, validation, returned evidence and failure handling; compare its callers to corresponding tests.

## License and verification

This repository preserves its existing [LICENSE](LICENSE) for original work; external artist tools, SDKs, output media and third-party assets keep their own terms. Educational reuse and further development are encouraged within those licenses. Use [README](README.md) for actual host configuration. A source guide or passing pure-Python unit tests do not imply a successful native-host integration run.
