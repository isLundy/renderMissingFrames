# Render Missing Frames ( testing )

A python script for Nuke.

> Requirements: Nuke 12 or later

<br />

### Method:

Select a `Write` node, then run the script.

- The file type must be `sequence` and must follow the rules `<path>/<name>.<frame number variable>.<extension>`

  > example: `<path>/final_comp_v01.%04d.exr` or `<path>/final_comp_v01.####.exr`

<br />

### Install example

You can put the code in [`W_hotbox`](https://www.nukepedia.com/python/ui/w_hotbox).

<img src="/images/W_hotbox_RenderMissingFrames.png">
<img src="/images/W_hotbox_RenderMissingFrames_02.png">
