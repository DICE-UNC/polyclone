#!/bin/bash
#LibreOffice Writer (v4.0.2.2)
#document
#odt, ott, sxw, stw, fodt, uot, docx, xml, doc, html, rtf, txt
#odt, ott, sxw, stw, fodt, uot, docx, xml, doc, html, rtf, txt, pdf

echo $JAVA_HOME

/usr/bin/soffice --headless --convert-to $4 $1
