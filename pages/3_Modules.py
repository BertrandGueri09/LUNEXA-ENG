import streamlit as st
import pandas as pd
from pathlib import Path

# Initialisation de sécurité
defaults = {
    "xp": 0,
    "streak": 1,
    "niveau": "Non évalué",
    "objectif": "Non défini",
    "badges": [],
    "journal_entries": [],
    "completed_lessons": 0,
    "vocab_progress": 25,
    "grammar_progress": 20,
    "pronunciation_progress": 15,
    "listening_progress": 10,
    "culture_progress": 10,
    "community_progress": 5
}

for key, value in defaults.items():
    st.session_state.setdefault(key, value)


st.title("📚 2. Modules d’apprentissage")

module = st.tabs(["Vocabulaire", "Grammaire", "Prononciation", "Compréhension orale"])

with module[0]:
    st.header("🧾 Vocabulaire")
    vocab_path = Path("data/vocabulaire.csv")
    df = pd.read_csv(vocab_path, sep=";")

    theme = st.selectbox("Choisir un thème", sorted(df["theme"].unique()))
    filtered = df[df["theme"] == theme]

    st.dataframe(filtered, use_container_width=True)

    mot = filtered.sample(1).iloc[0]
    st.subheader("Flashcard")

    with st.expander("Voir le mot"):
        st.write(f"**{mot['word']}**")

    with st.expander("Voir la traduction et l’exemple"):
        st.write(f"Traduction : **{mot['translation']}**")
        st.write(f"Exemple : {mot['example']}")

    if st.button("J’ai appris ce mot"):
        st.session_state["xp"] += 10
        st.session_state["vocab_progress"] = min(100, st.session_state["vocab_progress"] + 5)
        st.success("+10 XP")

    st.info("Méthode Anki simulée : les mots difficiles peuvent être revus plus souvent.")


with module[1]:
    st.header("📘 Grammaire")

    lesson = st.selectbox(
        "Choisir une leçon",
        [
            "Present Simple",
            "Past Simple",
            "Present Perfect",
            "Modal verbs",
            "Erreurs fréquentes des francophones"
        ]
    )

    if lesson == "Present Simple":
        st.write("Le Present Simple sert à parler des habitudes et vérités générales.")
        st.code("I work every day.\nShe works every day.")
    elif lesson == "Past Simple":
        st.write("Le Past Simple sert à parler d’une action terminée dans le passé.")
        st.code("I visited London last year.")
    elif lesson == "Present Perfect":
        st.write("Le Present Perfect relie le passé au présent.")
        st.code("I have lived here since 2020.")
    elif lesson == "Modal verbs":
        st.write("Les modaux expriment la capacité, l’obligation ou la possibilité.")
        st.code("I can speak English.\nYou should practice every day.")
    else:
        st.warning("Erreur fréquente : dire 'I have 20 years'.")
        st.success("Correction : 'I am 20 years old'.")

    answer = st.radio("Complétez : She ___ English every day.", ["study", "studies", "studying"])

    if st.button("Corriger l’exercice de grammaire"):
        if answer == "studies":
            st.session_state["xp"] += 10
            st.session_state["grammar_progress"] = min(100, st.session_state["grammar_progress"] + 5)
            st.success("Bonne réponse ! +10 XP")
        else:
            st.error("Incorrect. Avec 'she', on ajoute souvent -s : She studies.")


with module[2]:
    st.header("🎙️ Prononciation avec micro")

    from streamlit_mic_recorder import mic_recorder
    from utils.speech_api import transcribe_audio, pronunciation_score
    import tempfile

    st.write(
        "Enregistrez directement votre voix dans l’application, puis l’API transcrit votre audio "
        "et compare votre prononciation avec une phrase modèle."
    )

    st.subheader("Sons difficiles")
    st.table({
        "Mot": ["think", "this", "world", "through"],
        "IPA simplifié": ["/θɪŋk/", "/ðɪs/", "/wɜːld/", "/θruː/"],
        "Conseil": [
            "Langue entre les dents pour TH",
            "TH sonore",
            "Bien prononcer le R",
            "Ne pas prononcer GH"
        ]
    })

    phrase_modele = st.selectbox(
        "Choisissez une phrase à prononcer",
        [
            "The weather is wonderful today.",
            "I would like to book a room.",
            "Could you help me please?",
            "This is a very important meeting.",
            "I have been learning English for three months."
        ]
    )

    st.info(f"Phrase modèle : **{phrase_modele}**")

    st.subheader("🎤 Enregistrement vocal")

    audio = mic_recorder(
        start_prompt="▶️ Commencer l'enregistrement",
        stop_prompt="⏹️ Arrêter l'enregistrement",
        just_once=True,
        use_container_width=True,
        format="wav"
    )

    if audio:
        st.success("Audio enregistré avec succès.")
        st.audio(audio["bytes"], format="audio/wav")
        st.write("Audio reçu :", audio is not None)
         
         
         
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio["bytes"])
            audio_path = tmp_file.name

        if st.button("Analyser ma prononciation"):
            try:
                with st.spinner("Transcription en cours avec l’API..."):
                    try:
                        transcription = transcribe_audio(audio_path)

                        st.success("Transcription réussie")
                        st.subheader("📝 Transcription")
                        st.success(transcription)

                    except Exception as e:
                        st.error(f"Erreur OpenAI : {e}")
                        st.stop()

                        st.write("Type transcription :", type(transcription))
                        st.write("Contenu :", transcription)
                score, feedback = pronunciation_score(phrase_modele, transcription)

                st.subheader("Résultat de la reconnaissance vocale")
                st.write("**Transcription détectée :**")
                st.success(transcription)

                st.metric("Score de prononciation", f"{score}/100")
                st.info(feedback)

                if score >= 70:
                    st.session_state["xp"] += 15
                    st.session_state["pronunciation_progress"] = min(
                        100,
                        st.session_state["pronunciation_progress"] + 8
                    )
                    st.success("+15 XP pour la pratique vocale 🎉")
                else:
                    st.warning("Réessayez en parlant plus lentement et clairement.")

            except Exception as e:
                st.error("Erreur pendant la transcription.")
                st.code(str(e))
    else:
        st.warning("Cliquez sur le bouton micro pour commencer l’enregistrement.")
        st.caption("Votre navigateur doit autoriser l’accès au microphone.")


with module[3]:
    st.header("🎧 Compréhension orale")
    st.write("Dialogue du jour : At the restaurant")

    st.markdown("""
**Waiter:** Good evening. What would you like to order?  
**Customer:** I would like a chicken sandwich and a glass of water, please.  
**Waiter:** Sure. Anything else?  
**Customer:** No, thank you.
""")

    q = st.radio("Que commande le client ?", ["Un café", "Un sandwich au poulet", "Une pizza"])

    if st.button("Corriger la compréhension"):
        if q == "Un sandwich au poulet":
            st.session_state["xp"] += 10
            st.session_state["listening_progress"] = min(100, st.session_state["listening_progress"] + 5)
            st.success("Bonne réponse ! +10 XP")
        else:
            st.error("Réponse incorrecte. Relisez le dialogue.")
