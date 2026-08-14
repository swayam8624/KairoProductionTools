# Portfolio demonstration script

## Flagship: Blender to engine

1. Open the deliberately broken crate scene.
2. Run Kairo validation: show transformed geometry and production diagnostics.
3. Select a diagnostic to navigate to the object and property.
4. Apply the bounded scale fix and rerun validation.
5. Dry-run publication and show that no destination version was created.
6. Publish v001. Inspect glTF, buffer, textures, and `publish.kairo.json`.
7. In C++, load the manifest, verify every payload fingerprint, and register the
   published glTF with `kairo.gltf.scene`.
8. Mutate the buffer and rerun ingest to demonstrate explicit rejection.

## Supporting tools

- Houdini: remove frames 1005-1008 from a fixture and show the resumable range,
  stale-upstream warning, and disk-budget estimate.
- Nuke: point a Read at that incomplete sequence, then show missing-frame and
  colorspace diagnostics; mutate a publish and show hash rejection.
- Maya: show an external reference, negative root scale, missing UV set, and
  external texture, then navigate from panel entries to nodes.

Record host versions and license tiers on screen. Do not represent host-neutral
tests as native application execution.
