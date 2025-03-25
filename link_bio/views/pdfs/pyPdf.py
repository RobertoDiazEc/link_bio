#!/usr/bin/python3

from ...backend.PdfJS import PDFJavascript as FPDF

# This example shows how to open the print dialog when the document has loaded.

pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', '', 20)
pdf.text(90, 50, 'Print me!')
pdf.include_js('print(true);')
pdf.output('demo.pdf')