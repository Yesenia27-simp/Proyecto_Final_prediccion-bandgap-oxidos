import nbformat
import json
import base64
import os
from fpdf import FPDF
from PIL import Image
import io

class NotebookPDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'Tareas de Modelado IA - Nanotecnología', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

def convert_notebook_to_pdf(nb_path, pdf_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    pdf = NotebookPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Use a standard font that supports some basic symbols
    pdf.set_font("helvetica", size=10)

    for cell in nb.cells:
        if cell.cell_type == 'markdown':
            pdf.set_font("helvetica", 'B', 12)
            pdf.set_text_color(0, 51, 102) # Dark blue for headers
            # Simulating markdown headers by checking for #
            text = cell.source
            pdf.multi_cell(0, 8, text.encode('latin-1', 'replace').decode('latin-1'))
            pdf.ln(2)
            pdf.set_text_color(0, 0, 0)
            
        elif cell.cell_type == 'code':
            # Code block
            pdf.set_font("courier", size=9)
            pdf.set_fill_color(240, 240, 240)
            pdf.multi_cell(0, 5, cell.source.encode('latin-1', 'replace').decode('latin-1'), fill=True)
            pdf.ln(2)
            
            # Outputs
            for output in cell.get('outputs', []):
                if output.output_type == 'stream':
                    pdf.set_font("courier", 'I', 8)
                    pdf.set_fill_color(255, 255, 255)
                    pdf.multi_cell(0, 4, output.text.encode('latin-1', 'replace').decode('latin-1'))
                    pdf.ln(1)
                elif output.output_type == 'display_data' or output.output_type == 'execute_result':
                    if 'data' in output and 'image/png' in output.data:
                        img_data = base64.b64decode(output.data['image/png'])
                        img = Image.open(io.BytesIO(img_data))
                        
                        # Save temp image
                        img_path = "temp_plot.png"
                        img.save(img_path)
                        
                        # Calculate width to fit page
                        page_width = pdf.w - 2 * pdf.l_margin
                        img_w, img_h = img.size
                        ratio = min(page_width / img_w, 1.0)
                        
                        pdf.image(img_path, w=img_w * ratio)
                        pdf.ln(2)
                        os.remove(img_path)
                    elif 'data' in output and 'text/plain' in output.data:
                         pdf.set_font("courier", 'I', 8)
                         pdf.multi_cell(0, 4, output.data['text/plain'].encode('latin-1', 'replace').decode('latin-1'))
                         pdf.ln(1)

    pdf.output(pdf_path)
    print(f"PDF generated: {pdf_path}")

if __name__ == "__main__":
    convert_notebook_to_pdf("Merged_Tareas.ipynb", "Tareas_unidad_1_Modelado_YGZM.pdf")
