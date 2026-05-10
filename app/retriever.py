import pandas as pd
import pickle
import faiss

from sentence_transformers import SentenceTransformer

# Load dataset
df = pd.read_csv("data/shl_catalog.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Combine searchable text
documents = (
    df["name"].fillna("") + " " +
    df["description"].fillna("")
).tolist()

# Generate embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "data/faiss_index.index")

# Save metadata
with open("data/metadata.pkl", "wb") as f:
    pickle.dump(df.to_dict("records"), f)

print("\nEmbeddings + FAISS index created successfully!")

# ---------------- SEARCH FUNCTION ---------------- #

def search_assessments(query, top_k=5):

    # Load saved index
    index = faiss.read_index("data/faiss_index.index")

    # Load metadata
    with open("data/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    # Encode query
    query_embedding = model.encode([query])

    # Search
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        item = metadata[idx]

        results.append({
            "name": item["name"],
            "url": item["url"],
            "description": item["description"]
        })

    return results


# ---------------- TEST SEARCH ---------------- #

if __name__ == "__main__":

    results = search_assessments("Java backend developer")

    print("\nSearch Results:\n")

    for r in results:

        print("NAME:", r["name"])
        print("URL:", r["url"])
        print("DESCRIPTION:", r["description"])
        print("-" * 50)