
import streamlit as st
from datetime import date
import tempfile
from utils.speech_api import transcribe_audio, pronunciation_score, analyse_english

st.title("💬 Pratique quotidienne")

tab1, tab2, tab3, tab4 = st.tabs(["Conversation IA","Journal","Défi","Pratique vocale"])

with tab4:
    st.header("🎤 Analyse vocale")
    phrase = st.text_input("Phrase modèle", "Hello, my name is John.")
    audio = st.audio_input("Enregistre ta voix")

    if audio:
        st.audio(audio)
        if st.button("Analyser l'audio"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(audio.getvalue())
                path = tmp.name

            transcription = transcribe_audio(path)
            score = pronunciation_score(phrase, transcription)
            analyse = analyse_english(transcription)

            st.subheader("Transcription")
            st.write(transcription)

            st.metric("Prononciation", f"{score}%")
            st.metric("Niveau", analyse.get("niveau","N/A"))
            st.metric("Grammaire", analyse.get("grammaire",0))
            st.metric("Vocabulaire", analyse.get("vocabulaire",0))
            st.metric("Fluidité", analyse.get("fluidite",0))

            st.info(analyse.get("commentaire",""))
            st.success(analyse.get("correction",""))
