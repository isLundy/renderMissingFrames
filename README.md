# Render Missing Frames ( testing )

A python script for Nuke.

> Requirements: Nuke 12 or later

### Method:

Select a Write node, then run the script.

### Install example:

init.py

```python
import nuke

nuke.pluginAddPath('./PythonScripts/renderMissingFrames')
```

menu.py

```python
import nuke
import openExploreDir

s = nuke.menu("Nuke").addMenu("PythonScripts")
h = s.addMenu("renderMissingFrames")
h.addCommand("Render Missin gFrames", "renderMissingFrames")
```

