import textstat

def extract_features(text):
    return {
        "flesch_reading_ease": textstat.flesch_reading_ease(text),
        "sentence_count": textstat.sentence_count(text),
        "syllable_count": textstat.syllable_count(text),
        "char_count": len(text),
        "word_count": len(text.split()),
        "avg_word_length": sum(len(word) for word in text.split()) / len(text.split())
    }