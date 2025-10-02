from transformers import pipeline
# Load a pre-trained text classification model (toxic content)
classifier = pipeline('text-classification', model='unitary/toxic-bert')
def analyze_text(content: str):
    result = classifier(content)
    return result
