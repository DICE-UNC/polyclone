#!/bin/sh
#BRL-CAD
#model
#euclid, dxf, igs, stl
#acad, dxf, euclid, igs, stl, vrml, x3d


case "$3" in
	euclid)
		/usr/brlcad/bin/euclid-g -i $1 -o temp.g
		;;
	dxf)
		/usr/brlcad/bin/dxf-g $1 temp.g
	        ;;
	igs)
		/usr/brlcad/bin/iges-g -n -o temp.g $1
	        ;;
	stl)
		/usr/brlcad/bin/stl-g $1 temp.g
	        ;;
	*)
                echo "Unsupporte input format $3"
		exit 1

esac



case "$4" in
	acad)
		/usr/brlcad/bin/g-acad -o $2 temp.g all
	        ;;
	dxf)
		/usr/brlcad/bin/g-dxf -o $2 temp.g all
	        ;;
	euclid)
		/usr/brlcad/bin/g-euclid -o $2 temp.g all
	        ;;
	igs)
		/usr/brlcad/bin/g-iges -o $2 temp.g all
	        ;;
	stl)
		/usr/brlcad/bin/g-stl -o $2 temp.g all
	        ;;
	vrml)
		/usr/brlcad/bin/g-vrml -o $2 temp.g all
	        ;;
	x3d)
		/usr/brlcad/bin/g-x3d -o $2 temp.g all
	        ;;
	*)
                echo "Unsupporte output format $4"
		exit 1
esac
