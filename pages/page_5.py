# Contents of ~/my_app/pages/page_3.py
# import libs
import pytesseract
from pytesseract import Output
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path
import PyPDF2
import streamlit as st
import os.path
import pathlib

@st.cache
def Reader_Function(uploaded_file,FName):
    
    images = convert_from_path(uploaded_file)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    ## Convert a screened pdf '2019_2020_Reg.pdf' into a searchable pdf called 'searchable.pdf'
    for image in images:
        page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
        pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
        pdf_writer.addPage(pdf.getPage(0))
    
    # export the searchable PDF to searchable.pdf
    with open(FName & "_search.pdf", "wb") as f:
        pdf_writer.write(f)
  

    return st.markdown("Done")

def upload():
    if uploaded_file is None:
        st.session_state["upload_state"] = "Upload a file first!"
    else:
        data = uploaded_file.getvalue().decode('utf-8')
        parent_path = pathlib.Path(__file__).parent.parent.resolve()           
        save_path = os.path.join(parent_path, "data")
        complete_name = os.path.join(save_path, uploaded_file.name)
        destination_file = open(complete_name, "w")
        destination_file.write(data)
        destination_file.close()
        st.session_state["upload_state"] = "Saved " + complete_name + " successfully!"
                       

st.set_page_config(
    page_title="Hello Fred",
    page_icon="👋",
    menu_items={
    'Get Help':'https://www.yahoo.fr',
   'Report a bug': 'https://www.boursotama.com',
}
)

uploaded_file = st.file_uploader("Choose a file",type=["pdf"])

if uploaded_file is not None:
        
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)
    parent_path = pathlib.Path(__file__).parent.parent.resolve()           
    save_path = os.path.join(parent_path, "data")
    complete_name = os.path.join(save_path, uploaded_file.name)
    Reader_Function(complete_name,uploaded_file.name)
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

st.button("Upload file to Sandbox", on_click=upload)
    
    
st.markdown("# Page 5 🎉")
st.sidebar.markdown("# Test OCR")
