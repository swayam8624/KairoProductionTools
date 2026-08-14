# Verification matrix

| Surface | Current evidence | Native gate |
|---|---|---|
| Shared core | Python unit suite and multi-platform GitHub CI | Not host-specific |
| Blender 5.2 LTS | Native headless registration, navigation, safe fix, glTF export, dry-run, atomic publish, fresh-profile install, rendered result | Passed |
| Houdini | Host-neutral cache, HOM-shape, and publisher tests | Houdini/hython install and license required |
| Nuke | Host-neutral Read/Write, adapter-shape, and publish-integrity tests | Nuke install and license required |
| Maya | Host-neutral scene, adapter-path, and publisher tests | Maya install and license required |
| KairoAssets | Full Clang C++23 build and CTest, including tamper/traversal regression tests | Passed |

“Host-neutral” means the production rules and data transactions ran without the
commercial DCC process. It does not mean the UI/API integration ran natively.
