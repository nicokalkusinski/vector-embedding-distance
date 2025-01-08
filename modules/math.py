import numpy as np

def euclidean_distance(vec1, vec2):
    """
    Calculate the Euclidean distance between two vectors.

    Parameters:
        vec1 (list or numpy.ndarray): First vector.
        vec2 (list or numpy.ndarray): Second vector.

    Returns:
        float: Euclidean distance between the two vectors.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.linalg.norm(vec1 - vec2)

def cosine_similarity(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors.

    Parameters:
        vec1 (list or numpy.ndarray): First vector.
        vec2 (list or numpy.ndarray): Second vector.

    Returns:
        float: Cosine similarity between the two vectors.
    """
    # Ensure the vectors are numpy arrays
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    # Calculate cosine similarity
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)

    return dot_product / (norm_vec1 * norm_vec2)