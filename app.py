import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Media Generator", page_icon="🎨", layout="centered"
)

st.title("🎨 AI Image Generator Tool")
st.write(
    "Apna pasandeeda prompt likhein aur aik hi click mein AI image banayein!"
)

prompt = st.text_area(
    "Apna Prompt Likhein:",
    placeholder="A futuristic city with flying cars, cyberpunk style...",
)

if st.button("Generate Image 🚀"):
  if not prompt:
    st.warning("Barah-e-karam koi prompt zaroor likhein!")
  else:
    with st.spinner(
        "AI image tayar kar raha hai, thora intezar karein..."
    ):
      try:
        # URL encode prompt for safe usage
        import urllib.parse

        encoded_prompt = urllib.parse.quote(prompt)

        # Pollinations free image URL
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        st.success("Image kamyabi se ban gayi!")
        st.image(image_url, caption=prompt, use_column_width=True)

      except Exception as e:
        st.error(f"Koi error aa gaya: {e}")
