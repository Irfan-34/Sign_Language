
from translator_engine import GlossTranslator

def test_translator():
    translator = GlossTranslator()
    
    # Test 1: Gloss to English
    gloss = "ME STORE GO"
    res = translator.gloss_to_sentence(gloss, "en")
    print(f"Gloss: {gloss} -> English: {res}")
    
    # Test 2: Gloss to Hindi (requires internet usually, but let's see if googletrans works or falls back)
    # The utils file has fallback.
    res_hi = translator.gloss_to_sentence(gloss, "hi")
    # Hint: Hindi might print as unicode chars
    print(f"Gloss: {gloss} -> Hindi: {res_hi}")
    
    # Test 3: Sentence to Gloss
    sent = "How are you?"
    gloss_rev = translator.sentence_to_gloss(sent)
    print(f"Sentence: {sent} -> Gloss: {gloss_rev}")

if __name__ == "__main__":
    test_translator()
