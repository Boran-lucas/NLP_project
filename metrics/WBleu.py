import math
from collections import Counter
from nltk.util import ngrams
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from scipy.stats import entropy

class WeightedEntropyBLEU:
    def __init__(self, reference_corpus):
        self.reference_corpus = reference_corpus
        self.ngram_entropies = self.calculate_ngram_entropies()

    def calculate_ngram_entropies(self):
        ngram_counts = Counter()
        total_ngrams = 0

        for sentence in self.reference_corpus:
            for n in range(1, 5):  # On calcule les n-grammes de 1 à 4
                ngram_counts.update(ngrams(sentence, n))
                total_ngrams += len(sentence) - n + 1

        ngram_probabilities = {ngram: count / total_ngrams for ngram, count in ngram_counts.items()}
        return {ngram: -prob * math.log2(prob) for ngram, prob in ngram_probabilities.items()}

    def score(self, reference_sentences, candidate_sentence):
        weights = [self.ngram_entropies.get(ngram, 0.0) for ngram in ngrams(candidate_sentence, 1)]
        return sentence_bleu(reference_sentences, candidate_sentence, weights=weights, smoothing_function=SmoothingFunction().method1)


# Code pour tester la métrique
if __name__ == "__main__":
    reference_corpus = [
        "Le chat est sur le tapis".split(),
        "Le chien joue dans le jardin".split(),
        "Il fait beau aujourd'hui".split(),
    ]

    candidate_sentence = "Le chat est sur le jardin".split()
    reference_sentences = [
        "Le chat est dans le jardin".split(),
        "Le chat est sur le sol".split(),
    ]

    weighted_bleu = WeightedEntropyBLEU(reference_corpus)
    bleu_score = weighted_bleu.score(reference_sentences, candidate_sentence)
    print(f"Weighted Entropy BLEU Score: {bleu_score:.4f}")
