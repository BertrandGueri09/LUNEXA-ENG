import streamlit as st

st.title("👥 7. Communauté")

tab1, tab2, tab3 = st.tabs(["Tandem", "Forum", "Sessions live"])

with tab1:
    st.header("🤝 Tandem avec locuteurs natifs")
    st.write("Trouvez un partenaire linguistique pour pratiquer l’anglais.")
    st.table({
        "Nom": ["Emily", "James", "Sophia"],
        "Pays": ["USA", "UK", "Canada"],
        "Disponibilité": ["Lundi soir", "Mercredi après-midi", "Samedi matin"]
    })

    if st.button("Demander un tandem"):
        st.session_state["community_progress"] = min(100, st.session_state["community_progress"] + 10)
        st.success("Demande envoyée en mode prototype.")

with tab2:
    st.header("💬 Forum d’entraide")
    question = st.text_input("Posez une question à la communauté")
    if st.button("Publier"):
        if question.strip():
            st.success("Question publiée en mode prototype.")
            st.write(f"Votre question : {question}")
        else:
            st.warning("Veuillez écrire une question.")

    st.subheader("Questions récentes")
    st.write("- Quelle est la différence entre **since** et **for** ?")
    st.write("- Comment prononcer le son **TH** ?")
    st.write("- Quels mots apprendre pour voyager ?")

with tab3:
    st.header("👨‍🏫 Sessions live avec des profs")
    st.table({
        "Session": ["Speaking Club", "Grammar Booster", "Business English"],
        "Jour": ["Mardi", "Jeudi", "Samedi"],
        "Heure": ["18:00", "19:00", "10:00"]
    })

    choice = st.selectbox("Choisir une session", ["Speaking Club", "Grammar Booster", "Business English"])
    if st.button("S’inscrire"):
        st.session_state["xp"] += 10
        st.success(f"Inscription confirmée pour {choice}. +10 XP")
