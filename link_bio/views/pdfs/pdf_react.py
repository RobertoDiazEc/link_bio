import reflex as rx

#import { Document, Page, Text, View, StyleSheet } from '@react-pdf/renderer';

class Document(rx.Component):
    library = "@react-pdf/renderer"
    tag = "Document"


class Page(rx.Component):
    library = "@react-pdf/renderer"
    tag = "Page"
    size: rx.Var[str]
    # here we are wrapping style prop but as style is a reserved name in Reflex we must name it something else and then change this name with rename props method
    theme: rx.Var[dict]
    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class Text(rx.Component):
    library = "@react-pdf/renderer"
    tag = "Text"


class View(rx.Component):
    library = "@react-pdf/renderer"
    tag = "View"
    # here we are wrapping style prop but as style is a reserved name in Reflex we must name it something else and then change this name with rename props method
    theme: rx.Var[dict]
    _rename_props: dict[str, str] = {
        "theme": "style",
    }


class StyleSheet(rx.Component):
    library = "@react-pdf/renderer"
    tag = "StyleSheet"
    page: rx.Var[dict] = {
        "flexDirection": "row",
        "backgroundColor": "#E4E4E4",
    }
    section: rx.Var[dict] = {
    "margin": 10,
    "padding": 10,
    "flexGrow": 1,
  }


class PDFViewer(rx.NoSSRComponent):
    library = "@react-pdf/renderer"
    tag = "PDFViewer"


document = Document.create
page = Page.create
text = Text.create
view = View.create
style_sheet = StyleSheet.create
pdf_viewer = PDFViewer.create

# style_props = {
#     "style": {"_hover": {"opacity": 0.75},
#               "section": {
#                     "margin": 10,
#                     "padding": 10,
#                     "flexGrow": 1,
#                 },
#                "page": {
#                     "flexDirection": "row",
#                     "backgroundColor": "#E4E4E4",
#                 }, 
#             },
# }

# styles = style_sheet(
#     {
#         "page": {
#             "flexDirection": "row",
#             "backgroundColor": "#E4E4E4",
#         },
#         "section": {
#             "margin": 10,
#             "padding": 10,
#             "flexGrow": 1,
#         },
#     }
# )


def pdf_react() -> rx.Component:
    return pdf_viewer(
        document(
            page(
                view(
                    text("Hello, World!"),
                ),
                view(
                    text("Hello, 2!"),
                ),
                size="A4",
            ),
            
        ),
        width="100%",
        height="80vh",
    )



