import streamlit as st

st.title("🌍 5. Immersion & Culture")

tab1, tab2, tab3 = st.tabs(["Actualités simplifiées", "Slang & expressions", "Quiz culturel"])

with tab1:
    st.header("📰 Actualité simplifiée")
    st.write("""
**Simple English News**

Today, many students use mobile apps to learn languages.
These apps help them practice vocabulary, grammar, listening and speaking every day.
""")
    st.info("Objectif : lire de courts textes en anglais accessible.")

with tab2:
    st.header("🎬 Slang et expressions populaires")
    st.table({
        "Expression": ["What's up?", "No worries", "Hang out", "I'm into it", "That's awesome"],
        "Sens": [
            "Quoi de neuf ?",
            "Pas de souci",
            "Passer du temps avec quelqu’un",
            "Ça m’intéresse",
            "C’est génial"
        ],
        "Contexte": ["Conversation", "Politesse", "Amis", "Goûts", "Enthousiasme"]
    })

    if st.button("J’ai révisé les expressions"):
        st.session_state["xp"] += 10
        st.session_state["culture_progress"] = min(100, st.session_state["culture_progress"] + 5)
        st.success("+10 XP")

with tab3:
    st.header("🎵 Quiz culturel anglophone")
    q1 = st.radio("Quelle ville est associée à Hollywood ?", ["New York", "Los Angeles", "Chicago"])
    q2 = st.radio("Quel pays utilise principalement l’accent RP traditionnel ?", ["Royaume-Uni", "Canada", "Australie"])

    if st.button("Valider le quiz culturel"):
        score = 0
        if q1 == "Los Angeles":
            score += 1
        if q2 == "Royaume-Uni":
            score += 1

        st.write(f"Score : {score}/2")
        if score == 2:
            st.session_state["xp"] += 15
            st.success("Excellent ! +15 XP")
        else:
            st.info("Continuez à découvrir la culture anglophone.")
