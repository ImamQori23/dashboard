import streamlit as st
from PIL import Image
st.markdown("<p style='text-align:center; font-size:32px; font-weight:bold; color:black;'>Cerita di Balik Data: Narasi Visual dari Global Terrorism Database</p>", unsafe_allow_html=True)
image_2=Image.open("Picture2.png")
image_4=Image.open("Picture4.png")
tempat_image_4, tempat_image_2 = st.columns(2)
with tempat_image_2:
    st.write("")  
    st.image(
        image_2,
        caption=""
    )

st.markdown("""
Berdasarkan hasil visualisasi didapatkan bahwa timur tengah dan afrika utara menjadi tempat paling banyak kasus terorisme
""")

with tempat_image_4:
    st.image(
        image_4,  
    )
   
image_1=Image.open("Picture1.png") 
st.image(image_1)
st.markdown(""" Berdasarkan hasil analisis didapatkan hasil 20 negara dengan jumlah serangan terbanyak dan yang berada diposisi pertama adalah irak""")


image_2=Image.open(r"C:\Users\hp\.vscode\capstone\Screenshot_(841)-transformed.png") 
st.image(image_2)

image_3=Image.open(r"C:\Users\hp\.vscode\capstone\Screenshot_(849)-transformed.png") 
st.image(image_3)
st.markdown(""" 
Tahun 2014 diwarnai dengan 16.071 serangan teror  yang merenggut
34.749 nyawa. Ini merupakan statistik yang sangat mencekam, 
menunjukkan dampak devastating  terorisme di dunia.
Serangan: Terjadi rata-rata 44 serangan teror setiap hari di tahun 2014.
Korban: Lebih dari 34.000 orang kehilangan nyawa akibat terorisme, 
         setara dengan rata-rata 95 korban jiwa setiap hari.
Lokasi: Irak, Suriah, Nigeria, Pakistan, dan Afghanistan adalah
         negara-negara yang paling terkena dampak terorisme.

""")
