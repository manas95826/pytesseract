import streamlit as st
from PIL import Image
import pytesseract
from pytesseract import Output

st.title("OCR with Bounding Box and Layout Analysis")

# Upload an image or PDF file
uploaded_file = st.file_uploader("Upload an image or PDF file", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    # Display the uploaded image
    if uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    elif uploaded_file.type == "application/pdf":
        st.warning("PDF support is under development. Please upload an image instead.")

    # Perform OCR
    if st.button("Run OCR"):
        text = pytesseract.image_to_string(image, output_type=Output.DICT)
        st.write("Extracted Text:")
        st.write(text['text'])

        # Visualize bounding boxes (optional)
        for i, word in enumerate(text['text']):
            left, top, width, height = text['left'][i], text['top'][i], text['width'][i], text['height'][i]
            st.image(image.crop((left, top, left + width, top + height)))

        # Add layout analysis or table detection here
        st.write("Layout Analysis / Table Detection Results:")


