import chromadb

from ingest import load_documents , chunk_documents

def store_chunks(chunks):
    client=chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(name="job_listings")
    ids=[]
    for i in range(len(chunks)):
        ids.append(str(i))
    documents=[]
    for chunk in chunks:
        documents.append(chunk["text"])

    metadata=[]
    for chunk in chunks:
        metadata.append({"source":chunk["source"]})

    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadata
    )
    return collection

if __name__=="__main__":
    docs= load_documents("data/job_listings")
    chunks = chunk_documents(docs)
    collection= store_chunks(chunks)
    print(collection.count())