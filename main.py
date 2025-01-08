from openai import OpenAI
from modules import tools, math

client = OpenAI(api_key=tools.load_api_key())

def get_embedding(word, model="text-embedding-3-small"):
    """
    Get the embedding for a given word using the specified model.
    """
    response = client.embeddings.create(
        input=word,
        model=model
    )

    return response.data[0].embedding

def compare(content1, content2, method=3):
    """
    Compare two words using OpenAI embeddings and return their similarity score.
    """
    embedding1 = get_embedding(content1)
    embedding2 = get_embedding(content2)
    if method==1:
        print("Using Euclidean Distance.")
        similarity = math.euclidean_distance(embedding1, embedding2)
        print(f"Result: {similarity:.6f}")
    elif method==2:
        print("Using Cosine Similarity.")
        similarity = math.cosine_similarity(embedding1, embedding2)
        print(f"Result: {similarity:.6f}")
    else:
        print("Using Euclidean Distance and Cosine Similarity.")
        sim1, sim2 = math.euclidean_distance(embedding1, embedding2), math.cosine_similarity(embedding1, embedding2)
        print(f"Euclidean Distance: {sim1:.6f}")
        print(f"Cosine Similarity: {sim2:.6f}")

# Example usage
# load md files with tools.load_md_file("file_path")
content1 = "I want to go to tan on the beach with my friends"
content2 = "Nothing produces a better sound than a nuclear power"

compare(content1, content2)