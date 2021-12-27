# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yYnGyKzgTxdPiHOeI5FQS-2PTO2Vranr
"""

import streamlit as st
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

def main():
    
    # Set page title and favicon.
    st.set_page_config(
    page_title="BreastCancerDetector"
    )

    st.title('Breast Cancer Detector')
    st.write("by Breast Cancer Everywhere group")
    st.image("app_pic.jpg", width=600)
    st.write('This project was made by ITI-AI Pro students to help people detect breast cancer')

    image_input = st.file_uploader(label='Upload Breast Mammogram (PGM)', type=['pgm'])
    detect = st.button("Detect Breast Cancer")
    np.set_printoptions(suppress=True)

    model = tensorflow.keras.models.load_model('Final_model.h5') # Change it
    
    if image_input is not None:
        
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(image_input, mode='r')
        image = image.convert('RGB')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        data[0] = image_array

#     image = Image.open(image_input,mode='r')
#     image = image.convert('RGB')
#     image = image.resize((224, 224))
#     image_array = np.asarray(image)
    
        size = st.slider("Adjust Image Size: ", 300, 1000)
        st.image(image, width=size)
        st.write("------------------------------------------------------")

    if detect:
        prediction = model.predict(data)
        class1 = prediction[0,0]
        class2 = prediction[0,1]
        if class1 > class2:
            st.info(" This is a **Benign Tumor** by {:.2f}%".format(class1 * 100) )
        elif class2 > class1:
            st.info(" This is **Malignant Tumor** by {:.2f}%".format(class2 * 100))
        else:
            st.write("We encountered an ERROR. This should be temporary, please try again with a better quality image. Cheers!")


if __name__ == '__main__':
    main()
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)