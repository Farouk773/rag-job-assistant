from pathlib import Path
def load_documents(folder_path):
    documents=[]
    dossier=Path(folder_path)
    for fichier in dossier.glob("*.txt"):
        contenu=fichier.read_text(encoding="utf-8")
        documents.append(
            {
                "source":fichier.name,
                "text":contenu
            }
        )
    return documents

if __name__=="__main__":
    docs=load_documents("data/job_listings")
    print(len(docs))
    print(docs[0]["text"][:200])