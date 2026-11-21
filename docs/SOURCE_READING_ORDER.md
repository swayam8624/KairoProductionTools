# Teaching source map — KairoProductionTools

Multi-DCC workflow and verifiable publication packaging, not an engine runtime.

Read these source links in order, identify the caller and callee for each public API, then check the error/ownership contract and its tests.

## Reading order

1. [`README.md`](README.md)
2. [`portfolio`](portfolio)
3. [`scripts`](scripts)
4. [`docs`](docs)
5. [`tests`](tests)

## Repository integration and API contracts

Houdini, Maya, Blender and Nuke connect to KairoPipelineCore's verified manifests and KairoAssets' import checks; each native host has different available verification.

## Teaching standards

- Comments explain invariants, decision reasons, lifetime, prerequisites and cross-file effects; they do not narrate obvious statements.
- Follow upstream interfaces before implementation details; distinguish implemented, host-verified and planned features.
- Run available tests at a pinned commit and consult [STATUS.md](STATUS.md) / [STATUS.yaml](STATUS.yaml) before declaring completion.
- Reuse original contributions under [LICENSE](LICENSE), subject to third-party code and asset terms.
