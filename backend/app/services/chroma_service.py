import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def store_chunks(chunks, embeddings, source):

    ids = []
    metadatas = []

    for i in range(len(chunks)):
        ids.append(f"{source}_chunk_{i}")
        metadatas.append({"source": source, "chunk_index": i})

    # Remove old chunks of this PDF first, in case a re-upload has fewer chunks
    collection.delete(where={"source": source})

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )


def count_chunks(source):

    result = collection.get(where={"source": source})

    return len(result["ids"])