import io
import streamlit as st
from google import genai
from PIL import Image

# Page Config
st.set_page_config(
    page_title="AI Media Generator", page_icon="🎨", layout="centered"
)

st.title("🎨 AI Image Generator Tool")
st.write("Apna Google AI Studio API key dalein aur AI images banayein!")

# Sidebar for Google API Key
st.sidebar.header("🔑 Settings")
google_api_key = st.sidebar.text_input(
    "Google AI Studio API Key",
    type="password",
    help="Yahan apni Google API key dalein",
)

prompt = st.text_area(
    "Apna Prompt Likhein:",
    placeholder="A futuristic city with flying cars, cyberpunk style...",
)

if st.button("Generate Image 🚀"):
  if not google_api_key:
    st.error("Barah-e-karam pehle sidebar mein apni Google API Key dalein!")
  elif not prompt:
    st.warning("Barah-e-karam prompt zaroor likhein!")
  else:
    with st.spinner("Google AI image generate kar raha hai..."):
      try:
        client = genai.Client(api_key=google_api_key)

        result = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=prompt,
            config=dict(number_of_images=1, output_mime_type="image/jpeg"),
        )

        for generated_image in result.generated_images:
          image = Image.open(io.BytesIO(generated_image.image.image_bytes))
          st.success("Image kamyabi se ban gayi!")
          st.image(image, caption=prompt, use_column_width=True)

      except Exception as e:
        st.error(f"Koi error aa gaya: {e}")
        
