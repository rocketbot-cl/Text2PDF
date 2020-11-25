from fpdf import FPDF


class TxtToPdfService:
    def __init__(self):
        self.pdf = FPDF()
        self.text = []

    def open_txt(self, path_txt):
        with open(path_txt) as file_txt:
            for line in file_txt:
                self.text.append(line)

    def write_into_pdf(self, path_pdf, height_line):
        self.pdf.add_page()
        for line in self.text:
            self.pdf.write(height_line, line)
        self.pdf.output(path_pdf)

    def set_font(self, data):
        family = data['family']
        style = data['style']
        size = data['size']
        self.pdf.set_font(family=family, style=style, size=size)

    def set_margins(self, margins):
        left = margins['left']
        right = margins['right']
        top = margins['top']
        self.pdf.set_margins(left=left, top=top, right=right)
