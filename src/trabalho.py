import numpy as np
import streamlit as st
from PIL import Image

st.title("Código do trabalho")

foto = Image.open("./imagens/gato_redbull.jpg")
img = np.array(foto)

st.write("Imagem original: ")
st.image(img)

# ------------------------------------------------------------------

st.header("Espelhamento")
col1, col2, col3 = st.columns(3)

espelho_horizontal = img[:, ::-1]
espelho_vertical = img[::-1, :]

col1.image(img, caption="Original")

col2.image(espelho_horizontal, caption="Espelho horizontal")
col3.image(espelho_vertical, caption="Espelho vertical")


# ------------------------------------------------------------------

st.header("Recorte")
col1, col2, col3 = st.columns(3)

altura, largura = img.shape[0], img.shape[1]
y = col1.slider("y", 0, altura - 1, altura // 4)
x = col1.slider("x", 0, largura - 1, largura // 4)
tamanho = col1.slider("tamanho", 10, largura, largura // 3)

recorte = img[y:y + tamanho, x:x + tamanho]

col2.image(img, caption="Original")
col3.image(recorte, caption="Recorte")


# ------------------------------------------------------------------

st.header("Negativo")
col1, col2 = st.columns(2)

negativo = 255 - img

col1.image(img, caption="Original")
col2.image(negativo, caption="Negativo")


# ------------------------------------------------------------------

st.header("Troca de cor")
col1, col2 = st.columns(2)

troca_de_cor = img[:, :, ::-1]

col1.image(img, caption="Original")
col2.image(troca_de_cor, caption="Canais trocados (R e B)")


# ------------------------------------------------------------------

st.header("Pixel art")
col1, col2 = st.columns(2)

bloco = col1.slider("Tamanho do bloco", 1, 50, 10)

reduzida = img[::bloco, ::bloco]
pixel_art = reduzida.repeat(bloco, axis=0).repeat(bloco, axis=1)

col1.image(img, caption="Original")
col2.image(pixel_art, caption="Pixel art")

