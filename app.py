import streamlit as st

st.set_page_config(
    page_title="LUNEXA ENG",
    page_icon="LE",
    layout="wide"
)

def init_state():
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
        if key not in st.session_state:
            st.session_state[key] = value

init_state()

st.sidebar.title("LUNEXA ENG")
st.sidebar.caption("Apprendre l’anglais étape par étape")

st.sidebar.metric("XP", st.session_state["xp"])
st.sidebar.metric("Streak", f"{st.session_state['streak']} jour(s) 🔥")
st.sidebar.write(f"**Niveau :** {st.session_state['niveau']}")
st.sidebar.write(f"**Objectif :** {st.session_state['objectif']}")

pages = {
    "Accueil": "pages/1_Accueil.py",
    "Évaluation initiale": "pages/2_Evaluation.py",
    "Modules d’apprentissage": "pages/3_Modules.py",
    "Pratique quotidienne": "pages/4_Pratique.py",
    "Gamification": "pages/5_Gamification.py",
    "Immersion & Culture": "pages/6_Immersion_Culture.py",
    "Suivi des progrès": "pages/7_Progression.py",
    "Communauté": "pages/8_Communaute.py"
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))

with open(pages[selection], encoding="utf-8") as f:
    code = f.read()
    exec(code)
