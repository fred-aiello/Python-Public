# Contents of ~/my_app/pages/page_3.py
# import libs
import pytesseract
from pytesseract import Output
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path
import PyPDF2
import streamlit as st



st.set_page_config(
    page_title="Hello Fred",
    page_icon="👋",
    menu_items={
    'Get Help':'https://www.yahoo.fr',
   'Report a bug': 'https://www.boursotama.com',
}
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    '''
    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

    '''   
    images = convert_from_path(uploaded_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Convert a screened pdf '2019_2020_Reg.pdf' into a searchable pdf called 'searchable.pdf'
    for image in images:
        page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
        pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
        pdf_writer.addPage(pdf.getPage(0))# export the searchable PDF to searchable.pdf
    with open("searchable.pdf", "wb") as f:
        pdf_writer.write(f)

    '''

    st.markdown("Done")

st.markdown("# Page 5 🎉")
st.sidebar.markdown("# Test OCR")
