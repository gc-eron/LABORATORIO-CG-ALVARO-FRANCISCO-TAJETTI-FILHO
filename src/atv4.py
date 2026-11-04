import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

foto = Image.open("imagens/gato.jpg")
img = np.array(foto)
st.image(img)

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)
col1.image(img)
col2.text(img[100, 100])

# 2. Canais
st.header("2. Canais")
col1, col2, col3 = st.columns(3)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0
col1.image(so_r, caption="Só R")

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0
col2.image(so_g, caption="Só G")

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0
col3.image(so_b, caption="Só B")

# Lógica do so_r, so_b e so_g: Cada variável so_r, so_g e so_b é uma cópia da imagem original, mas com os canais desejados destacados e os outros zerados, mas por que no red é 1 e 2, enquanto no g é 0 e 2? Porque o canal vermelho é o primeiro canal (índice 0), o verde é o segundo (índice 1) e o azul é o terceiro (índice 2). Portanto, para destacar o canal vermelho, zeramos os canais verde e azul (índices 1 e 2), para destacar o canal verde, zeramos os canais vermelho e azul (índices 0 e 2), e para destacar o canal azul, zeramos os canais vermelho e verde (índices 0 e 1).

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)
# faça você: mais três vértices do cubo na col1
amarelo = np.zeros((80, 80, 3), dtype=np.uint8)
ciano = np.zeros((80, 80, 3), dtype=np.uint8)
magenta = np.zeros((80, 80, 3), dtype=np.uint8)

amarelo[:, :] = (255, 255, 0)
ciano[:, :] = (0, 255, 255)
magenta[:, :] = (255, 0, 255)

col1.image(amarelo, caption="amarelo")
col1.image(ciano, caption="ciano")
col1.image(magenta, caption="magenta")

# faça você: a foto com channels="BGR" na col2
quadrado = np.zeros((100, 100, 3), dtype=np.uint8)
quadrado[:, :, 0] = 255
col2.image(img, channels="BGR")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2, col3 = st.columns(3)

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
media_poderada = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)
col1.image(img, caption="original")
col2.image(media, caption="média")
col3.image(media_poderada, caption="média ponderada")