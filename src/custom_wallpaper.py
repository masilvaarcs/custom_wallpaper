import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Definir dimensões da página A4 em pixels (considerando 96 DPI)
A4_WIDTH = int(8.27 * 96)
A4_HEIGHT = int(11.69 * 96)
A4_SIZE = (A4_WIDTH, A4_HEIGHT)


def resize_to_a4(par_image):
    """Redimensiona a imagem para o tamanho A4."""
    return par_image.resize(A4_SIZE, Image.Resampling.LANCZOS)


def draw_text_on_image(par_image, text, position):
    """Desenha texto em uma imagem na posição especificada."""
    draw = ImageDraw.Draw(par_image)
    font_size = 40
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calcular o tamanho do texto
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    if position == "top":
        x = (par_image.width - text_width) // 2
        y = 10  # Margem superior
    elif position == "center":
        x = (par_image.width - text_width) // 2
        y = (par_image.height - text_height) // 2
    elif position == "bottom":
        x = (par_image.width - text_width) // 2
        y = par_image.height - text_height - 10  # Margem inferior

    draw.text((x, y), text, font=font, fill="black")
    return par_image


# Título do app
st.title("Editor de Texto em Imagem A4")

# Upload de imagem
uploaded_file = st.file_uploader("Selecione uma imagem", type=["jpg", "jpeg", "png"])
if uploaded_file:
    # Abrir a imagem
    image = Image.open(uploaded_file)

    # Redimensionar para tamanho A4
    image = resize_to_a4(image)

    # Exibir pré-visualização da imagem
    st.image(image, caption="Pré-visualização da imagem", use_container_width=True)

    # Campos de entrada para os textos
    text_top = st.text_input("Texto para o Topo")
    text_center = st.text_input("Texto para o Centro")
    text_bottom = st.text_input("Texto para a Parte Inferior")

    if st.button("Aplicar Texto"):
        # Fazer cópia da imagem para desenhar texto
        image_with_text = image.copy()

        # Adicionar textos nas posições
        if text_top:
            image_with_text = draw_text_on_image(image_with_text, text_top, "top")
        if text_center:
            image_with_text = draw_text_on_image(image_with_text, text_center, "center")
        if text_bottom:
            image_with_text = draw_text_on_image(image_with_text, text_bottom, "bottom")

        # Exibir imagem com texto
        st.image(image_with_text, caption="Imagem com Texto", use_container_width=True)

        # Opção para baixar a imagem
        buf = io.BytesIO()
        image_with_text.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button(
            label="Baixar Imagem",
            data=byte_im,
            file_name="imagem_editada.png",
            mime="image/png",
        )
