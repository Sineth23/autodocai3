from nltk.tokenize import sent_tokenize

def handle_token_limit(text, max_tokens):
    """
    Function to handle the token limit of OpenAI.
    It tokenizes the text into sentences and then groups them into chunks. 
    Each chunk contains no more sentences than the maximum number of tokens allowed by OpenAI's API.
    """
    sentences = sent_tokenize(text)
    chunks = []
    chunk = []
    tokens = 0

    for sentence in sentences:
        sentence_tokens = len(sentence.split())
        if tokens + sentence_tokens > max_tokens:
            if chunk:  # add current chunk to chunks if it's not empty
                chunks.append(' '.join(chunk))
            chunk = [sentence]  # start a new chunk
            tokens = sentence_tokens
        else:
            chunk.append(sentence)
            tokens += sentence_tokens

    if chunk:  # add the last chunk if it's not empty
        chunks.append(' '.join(chunk))
    return chunks
