# RAG Job Assistant

Petit projet perso pour apprendre à construire un système RAG (Retrieval-Augmented Generation) de zéro, sans LangChain.

Le but : pouvoir poser des questions sur un ensemble d'offres d'emploi (IA, data, dev) et avoir une réponse qui cite ses sources, sans inventer de réponse quand l'info n'existe pas dans les documents.

## Stack

- Python 3.10+
- ChromaDB pour la base vectorielle (locale)
- API Claude (Anthropic) pour la génération de réponses
- Streamlit pour l'interface

## Structure

```
rag-job-assistant/
├── data/
│   └── job_listings/     # 26 offres d'emploi au format .txt
├── src/                   # le code du pipeline
├── requirements.txt
└── .env                   # clé API, non versionné
```

## Où j'en suis

Terminé : environnement Python, structure du projet, corpus de 26 offres, ingestion des documents (`load_documents`), découpage en chunks (`chunk_documents`).
En cours : génération des embeddings et stockage dans ChromaDB.

## Pour lancer le projet

```bash
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

Puis créer un fichier `.env` avec :
```
ANTHROPIC_API_KEY=ta_cle_ici
```