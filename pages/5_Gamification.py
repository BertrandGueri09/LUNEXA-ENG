import streamlit as st

st.title("🎮 4. Gamification")

xp = st.session_state["xp"]

col1, col2, col3 = st.columns(3)
col1.metric("XP total", xp)
col2.metric("Streak quotidien", f"{st.session_state['streak']} 🔥")
col3.metric("Leçons terminées", st.session_state["completed_lessons"])

st.header("🏅 Badges")

badges = []
if xp >= 30:
    badges.append("Starter")
if xp >= 80:
    badges.append("Vocabulary Hero")
if xp >= 150:
    badges.append("Grammar Master")
if st.session_state["streak"] >= 5:
    badges.append("Streak Champion")

st.session_state["badges"] = badges

if badges:
    for badge in badges:
        st.success(f"🏅 {badge}")
else:
    st.info("Aucun badge pour le moment. Continuez à apprendre !")

st.header("🏆 Classement entre amis")
ranking = {
    "Utilisateur": ["Vous", "Amina", "Kevin", "Sara", "Yao"],
    "XP": [xp, 180, 150, 120, 95]
}
st.table(ranking)

st.header("📅 Défis hebdomadaires")
st.checkbox("Apprendre 20 nouveaux mots")
st.checkbox("Faire 3 exercices de grammaire")
st.checkbox("Écrire 5 phrases dans le journal")
st.checkbox("Faire une simulation de conversation")
