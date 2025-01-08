def load_api_key() -> str:
    try:
        with open('api_key.txt', 'r') as f:
            api_key = f.read().strip()
        print("Loaded OpenAI API key.")
        return api_key
    except FileNotFoundError:
        print("No file named openai_api_key.txt found. Please create a file named openai_api_key.txt and add your OpenAI API key.")
        return ""
    
def load_md_file(file_path):
    """
    Loads a Markdown file and processes invalid escape sequences.

    Args:
        file_path (str): Path to the Markdown file.

    Returns:
        str: The sanitized content of the Markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"