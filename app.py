import streamlit as st
from deep_translator import GoogleTranslator

# Page Settings
st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌐 Language Translation Tool</h1>", unsafe_allow_html=True)

st.write("Translate text instantly between multiple languages using AI.")

# Language Dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Telugu": "te",
    "Japanese": "ja",
    "Chinese": "zh-cn"
}

# Text Input
text = st.text_area("✍ Enter text to translate")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()))

# Translate Button
if st.button("🔄 Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("✅ Translation Successful")

        st.subheader("Translated Text:")
        st.write(translated)

    else:
        st.warning("⚠ Please enter some text")