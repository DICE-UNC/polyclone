#!/bin/sh
#FreeCAD
#model
#igs, stp
#stp, stl, igs

#Write Python script

echo "import FreeCAD" >> convert.py
echo "import Part" >> convert.py
echo "import Mesh" >> convert.py



echo "Part.open('$PWD/$1')" >> convert.py
echo "o = [ FreeCAD.getDocument('Unnamed').findObjects()[0] ]" >> convert.py
echo "Mesh.export(o, '$PWD/$2')" >> convert.py

/usr/lib/freecad/bin/FreeCADCmd < convert.py





