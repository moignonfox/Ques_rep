import PyPDF2

def pdf_to_text(pdf_path, txt_output):
    # Ouvrir le fichier PDF en mode binaire
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)  # Lire le PDF
        with open(txt_output, 'w', encoding='utf-8') as text_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_file.write(text)


pdf_to_text(r'C:\Users\moign\Ques_rep\Document\Le probleme a trois corps - Liu Cixin.pdf',
            r'C:\Users\moign\Ques_rep\File_converted\Le probleme a trois corps - Liu Cixin.txt')
pdf_to_text(r'C:\Users\moign\Ques_rep\Document\La foret sombre - Cixin Liu.pdf',
            r'C:\Users\moign\Ques_rep\File_converted\La foret sombre - Cixin Liu.txt')