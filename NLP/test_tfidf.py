from tfifd import (inverse_document_frequency, document_frequency, term_frequency)
import sys
sys.path.append('.')

documents = ["Sweet sweet nurse! Love?", 
             "Sweet sorrow",
             "How sweet is love?",
             "Nurse!"]

query = "sweet love"

def test_inverse_document_frequency():
    pass
    
def test_term_frequency():
    result = document_frequency(documents, query)
    assert(result, 6)

def test_document_frequency():
    result = term_frequency(documents, query)
    assert(result, 5)

test_term_frequency()
test_document_frequency()