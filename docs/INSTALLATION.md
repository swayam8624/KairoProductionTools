# Installation map

All tools share `KairoPipelineCore`; install its wheel into the DCC Python
environment or use each adapter's bundled/package layout.

- Blender: install the versioned extension zip from KairoBlender.
- Houdini: link `packages/kairo_houdini.json` into the user package directory.
- Nuke: add the KairoNuke repository root to `NUKE_PATH`.
- Maya: add the KairoMaya `modules` directory to `MAYA_MODULE_PATH`.
- KairoAssets: update the engine component pin and rebuild with CMake/Ninja.

Each repository README contains its exact host-neutral command and native
release checklist.
