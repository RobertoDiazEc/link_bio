from fpdf import FPDF
import reflex as rx
import io
from ..backend.backend import backState


class PDFWorker(rx.Component):
    """PDF Worker Component."""
    library = "@react-pdf-viewer/core@3.12.0"
    lib_dependencies: list[str] = ["pdfjs-dist@3.4.120"]
    tag = "Worker"
    workerUrl: rx.Var[str] = (
        "https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js"
    )
pdfworker = PDFWorker.create

class defaultLayoutPlugin(rx.Component):
    """PDF Worker Component."""
    library = "@react-pdf-viewer/default-layout@3.12.0"
    tag = "defaultLayoutPlugin"


class PDFViewer(rx.Component):
    """PDF Viewer Component."""
    library = "@react-pdf-viewer/core@3.12.0"
    plugins: rx.Var[list] 
    tag = "Viewer"
    fileUrl: rx.Var[str]



pdfviewer = PDFViewer.create   



# class PDF(FPDF):
#     def header(self):
#         self.set_font('Arial', 'B', 12)
#         self.cell(0, 10, 'Factura', 0, 1, 'C')

#     def footer(self):
#         self.set_y(-15)
#         self.set_font('Arial', 'I', 8)
#         self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')


# def generar_pdf():
#     pdf = PDF()
#     pdf.add_page()
#     pdf.set_font('Arial', size=12)
#     pdf.cell(200, 10, txt="Este es un ejemplo de factura.", ln=True)

#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output, 'F')
#     pdf.output("public/pdfs/invoice.pdf", dest='S')
#     pdf_output.seek(0)
#     return pdf_output


#@rx.route('/mostrar_pdf')
# def mostrar_pdf_page() -> rx.Component:
#     pdf_stream = generar_pdf()
#     return rx.box(
#         rx.vstack(
#             pdfworker(
#             pdfviewer(),
#             fileUrl="/pdfs/Leasing.pdf",
#         ),
#     width="100%", 
#     height="100%",
#     ),
#         # content=pdf_stream.read(), 
#         # media_type='/pdfs'
# )

def mostrar_pdf_page() -> rx.Component:
    return pdfworker(
        pdfviewer(
            fileUrl=backState.outfilepdf,
        ),
        width="100%",
        height="100%",
    )