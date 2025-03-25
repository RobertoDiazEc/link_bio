import reflex as rx


class PDFWorker(rx.Component):
    """PDF Worker Component."""
    library = "@react-pdf-viewer/core@3.12.0"
    lib_dependencies: list[str] = ["pdfjs-dist@3.4.120"]
    tag = "Worker"
    workerUrl: rx.Var[str] = (
        "https://unpkg.com/pdfjs-dist@3.4.120/build/pdf.worker.min.js"
    )

class PDFViewer(PDFWorker):
    """PDF Viewer Component."""
    library = "@react-pdf-viewer/core@3.12.0"
    plugins: rx.Var[list] = [
        rx.Var.create("defaultLayoutPlugin()", _var_is_local=False),
    ]
    tag = "Viewer"
    fileUrl: rx.Var[str]


pdfworker = PDFWorker.create
pdfviewer = PDFViewer.create   


    