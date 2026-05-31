import streamlit as st

st.title("LX LUNEXA ENG")
st.subheader("Application complète pour apprendre l’anglais")

st.write("""
Cette application accompagne l’utilisateur dans son apprentissage de l’anglais grâce à un parcours structuré :
évaluation de niveau, modules d’apprentissage, pratique quotidienne, gamification, immersion culturelle,
suivi des progrès et communauté.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧠 Évaluation initiale\n\nTest de niveau A1 à C2 et choix des objectifs.")
with col2:
    st.success("📚 Modules\n\nVocabulaire, grammaire, prononciation et écoute.")
with col3:
    st.warning("🎮 Motivation\n\nXP, badges, streaks et défis hebdomadaires.")

st.markdown("---")

st.header("✅ Les 7 aspects du cahier de charge")
st.table({
    "Aspect": [
        "1. Évaluation initiale",
        "2. Modules d’apprentissage",
        "3. Pratique quotidienne",
        "4. Gamification",
        "5. Immersion & Culture",
        "6. Suivi des progrès",
        "7. Communauté"
    ],
    "Statut": ["Intégré"] * 7
})
