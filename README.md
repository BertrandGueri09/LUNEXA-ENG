# English Learning Coach

Application Streamlit complète pour l'apprentissage de l'anglais avec reconnaissance vocale directe au micro.

## Fonctionnalités

1. Évaluation initiale
2. Modules d’apprentissage
3. Pratique quotidienne
4. Gamification
5. Immersion & Culture
6. Suivi des progrès
7. Communauté
8. Reconnaissance vocale directe avec microphone

## Installation

```bash
pip install -r requirements.txt
```

## Configuration de la clé API OpenAI

Créez un fichier `.env` à la racine du projet :

```env
OPENAI_API_KEY=votre_cle_api_openai_ici
```

Ou créez un fichier `.streamlit/secrets.toml` :

```toml
OPENAI_API_KEY = "votre_cle_api_openai_ici"
```

## Lancement

```bash
streamlit run app.py
```

## Utilisation du micro

1. Ouvrir `Modules d’apprentissage`
2. Aller dans l’onglet `Prononciation`
3. Choisir une phrase modèle
4. Cliquer sur `Commencer l'enregistrement`
5. Parler
6. Cliquer sur `Arrêter l'enregistrement`
7. Cliquer sur `Analyser ma prononciation`

Le navigateur demandera l’autorisation d’utiliser le micro. Cliquez sur `Autoriser`.

## Remarque

La transcription utilise l’API OpenAI. Il faut donc une clé API valide et une connexion Internet.
