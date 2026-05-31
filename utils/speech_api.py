
import os, json, difflib, re
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_client():
    key = None
    try:
        key = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        pass
    key = key or os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("OPENAI_API_KEY introuvable.")
    return OpenAI(api_key=key)

def transcribe_audio(audio_path):
    client = get_client()
    with open(audio_path,"rb") as f:
        r = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language="en"
        )
    return r.text

def pronunciation_score(expected, spoken):

    import difflib

    score = round(
        difflib.SequenceMatcher(
            None,
            expected.lower(),
            spoken.lower()
        ).ratio() * 100
    )

    if score >= 85:
        feedback = "Excellente prononciation."
    elif score >= 70:
        feedback = "Bonne prononciation."
    elif score >= 50:
        feedback = "Prononciation correcte mais améliorable."
    else:
        feedback = "Travaille davantage la prononciation."

    return score, feedback

def analyse_english(text):
    client = get_client()
    prompt=f'''
Analyse ce texte anglais et retourne uniquement un JSON :
{{
"niveau":"A1",
"grammaire":0,
"vocabulaire":0,
"fluidite":0,
"correction":"",
"commentaire":""
}}

Texte:
{text}
'''
    r=client.responses.create(model="gpt-5-mini", input=prompt)
    try:
        return json.loads(r.output_text)
    except Exception:
        return {"niveau":"Indéterminé","grammaire":0,"vocabulaire":0,"fluidite":0,"correction":text,"commentaire":r.output_text}
