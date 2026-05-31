import streamlit as st

st.title("🧠 1. Évaluation initiale")

st.write("Répondez à ce mini-test pour estimer votre niveau d’anglais.")

score = 0

questions = [
    {
        "q": "Choose the correct sentence:",
        "options": ["She go to school.", "She goes to school.", "She going to school."],
        "answer": "She goes to school."
    },
    {
        "q": "What does 'I am hungry' mean?",
        "options": ["Je suis fatigué", "J’ai faim", "Je suis en retard"],
        "answer": "J’ai faim"
    },
    {
        "q": "Complete: I have lived here ___ 2020.",
        "options": ["for", "since", "during"],
        "answer": "since"
    },
    {
        "q": "What is the past tense of 'go'?",
        "options": ["goed", "went", "gone"],
        "answer": "went"
    },
    {
        "q": "Choose the best translation: 'Je voudrais réserver une chambre.'",
        "options": [
            "I want eating a room.",
            "I would like to book a room.",
            "I am booking food."
        ],
        "answer": "I would like to book a room."
    }
]

for i, item in enumerate(questions, 1):
    user_answer = st.radio(f"{i}. {item['q']}", item["options"], key=f"eval_{i}")
    if user_answer == item["answer"]:
        score += 1

objectif = st.selectbox(
    "Quel est votre objectif principal ?",
    ["Voyage", "Travail", "Examen TOEIC/IELTS/TOEFL", "Conversation", "Culture anglophone"]
)

if st.button("Valider mon évaluation"):
    if score <= 1:
        niveau = "A1 - Débutant"
    elif score == 2:
        niveau = "A2 - Élémentaire"
    elif score == 3:
        niveau = "B1 - Intermédiaire"
    elif score == 4:
        niveau = "B2 - Intermédiaire avancé"
    else:
        niveau = "C1/C2 - Avancé"

    st.session_state["niveau"] = niveau
    st.session_state["objectif"] = objectif
    st.session_state["xp"] += 30
    st.session_state["completed_lessons"] += 1

    st.success(f"Niveau estimé : {niveau}")
    st.info(f"Objectif sélectionné : {objectif}")
    st.balloons()

st.markdown("---")
st.subheader("Parcours personnalisé recommandé")

if st.session_state["objectif"] == "Voyage":
    st.write("Priorité : vocabulaire de voyage, conversations à l’hôtel, restaurant et aéroport.")
elif st.session_state["objectif"] == "Travail":
    st.write("Priorité : anglais professionnel, réunions, emails et entretiens.")
elif "Examen" in st.session_state["objectif"]:
    st.write("Priorité : grammaire, compréhension orale, simulation d’examen et vocabulaire académique.")
else:
    st.write("Priorité : conversations du quotidien, culture, écoute et expressions naturelles.")
