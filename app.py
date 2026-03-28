import streamlit as st
from PIL import Image
import io

from utils.remover import remove_background

st.set_page_config(page_title="AI Background Remover", page_icon="🖼️")

st.title("🖼️ AI Background Remover")

uploaded = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded:
    img = Image.open(uploaded)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    output = remove_background(img)

    st.subheader("Background Removed")
    st.image(output, use_container_width=True)

    buf = io.BytesIO()
    output.save(buf, format="PNG")

    st.download_button(
        label="⬇ Download Image",
        data=buf.getvalue(),
        file_name="removed_background.png",
        mime="image/png"
    )