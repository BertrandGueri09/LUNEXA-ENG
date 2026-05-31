import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 6. Suivi des progrès")

progress_data = pd.DataFrame({
    "Module": [
        "Vocabulaire",
        "Grammaire",
        "Prononciation",
        "Compréhension orale",
        "Culture",
        "Communauté"
    ],
    "Progression": [
        st.session_state["vocab_progress"],
        st.session_state["grammar_progress"],
        st.session_state["pronunciation_progress"],
        st.session_state["listening_progress"],
        st.session_state["culture_progress"],
        st.session_state["community_progress"]
    ]
})

fig = px.bar(
    progress_data,
    x="Module",
    y="Progression",
    title="Progression par module",
    range_y=[0, 100]
)
st.plotly_chart(fig, use_container_width=True)

col1, col2, col3 = st.columns(3)
col1.metric("Niveau", st.session_state["niveau"])
col2.metric("Objectif", st.session_state["objectif"])
col3.metric("XP", st.session_state["xp"])

st.header("📩 Rapport hebdomadaire")
st.write("""
Votre rapport hebdomadaire pourrait être envoyé par email avec :
- temps d’apprentissage ;
- XP gagnés ;
- mots appris ;
- erreurs fréquentes ;
- recommandations pour la semaine suivante.
""")

if st.button("Générer un rapport prototype"):
    st.success("Rapport généré en mode prototype.")
    st.code(f"""
Rapport hebdomadaire
Niveau : {st.session_state['niveau']}
Objectif : {st.session_state['objectif']}
XP : {st.session_state['xp']}
Recommandation : pratiquer 10 minutes par jour.
""")

st.header("📝 Simulation d’examens")
exam = st.selectbox("Choisir un examen", ["TOEIC", "IELTS", "TOEFL"])
st.write(f"Simulation disponible pour : {exam}")
st.info("Version prototype : ajout futur d’un vrai système de tests chronométrés.")
