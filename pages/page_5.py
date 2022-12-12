# Contents of ~/my_app/pages/page_3.py
# import libs
import pytesseract
from pytesseract import Output
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path
import PyPDF2
import cv2
from tabula import read_pdf

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

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
    
uploaded_file=r'/home/frederic/Documents/Python/SDG/Github Clone/Python-Public/TEST_OCR/2019_2020_Reg.pdf'
images = convert_from_path(uploaded_file)
pdf_writer = PyPDF2.PdfFileWriter()


file=r'/home/frederic/Documents/Python/SDG/Github Clone/Python-Public/TEST_OCR/2042_3926.pdf'
df = read_pdf(file,pages='all')
st.write(df)


st.markdown("# Page 4 🎉")
st.sidebar.markdown("# Pa
