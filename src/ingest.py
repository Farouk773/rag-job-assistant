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

def chunk_documents(documents, chunk_size=500,overlap=50):
    chunks=[]
    for doc in documents:
        texte=doc["text"]
        source=doc["source"]
        start=0
        while start<len(texte):
            end=start+chunk_size
            morceau=texte[start:end]
            chunks.append(
                {
                    "text":morceau,
                    "source":source
                }
            )

            start+=chunk_size-overlap
    return chunks

if __name__=="__main__":
    docs=load_documents("data/job_listings")
    print(len(docs))
    print(docs[0]["text"][:200])
    print("////////////////////////////////")
    chunks=chunk_documents(docs)
    print(len(chunks))
    print(chunks[0]["source"])
