from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

def gerar_pdf(nome, email, telefone, objetivo, formacao, cursos, projetos):

    pdf = SimpleDocTemplate("curriculo.pdf")

    estilos = getSampleStyleSheet()

    elementos = []

    elementos.append(
        Paragraph(nome, estilos["Title"])
    )

    elementos.append(
        Paragraph(email, estilos["BodyText"])
    )

    elementos.append(
        Paragraph(telefone, estilos["BodyText"])
    )

    elementos.append(
        Spacer(1, 20)
    )

    elementos.append(
        Paragraph("Objetivo Profissional", estilos["Heading2"])
    )

    elementos.append(
        Paragraph(objetivo, estilos["BodyText"])
    )

    elementos.append(
        Paragraph("Formação", estilos["Heading2"])
    )

    elementos.append(
        Paragraph(formacao, estilos["BodyText"])
    )

    elementos.append(
        Paragraph("Cursos", estilos["Heading2"])
    )

    elementos.append(
        Paragraph(cursos, estilos["BodyText"])
    )

    elementos.append(
        Paragraph("Projetos", estilos["Heading2"])
    )

    elementos.append(
        Paragraph(projetos, estilos["BodyText"])
    )

    pdf.build(elementos)