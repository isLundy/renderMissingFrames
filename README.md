<h1 align='center'>
  Render Missing Frames
</h1>

> Requirements: Nuke 13 or later

<br />

### Usage

Select a `Write` node, then run the script.

- The file type must be `sequence` and must follow the rules `<path>/<name>.<frame number variable>.<extension>`

  > example: `<path>/final_comp_v001.%04d.exr` or `<path>/final_comp_v001.####.exr`

<br />

### Install example

You can put the code in `W_hotbox`.

<img src="/images/W_hotbox_RenderMissingFrames.png">
<img src="/images/W_hotbox_RenderMissingFrames_02.png">
