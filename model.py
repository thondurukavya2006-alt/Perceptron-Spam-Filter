
import re
import numpy as np

class PerceptronSpamFilter:
    def __init__(self, weights=None, bias=0):
        if weights is None:
            weights = [0, 0, 0, 0]
        self.weights = np.array(weights, dtype=float)
        self.bias = float(bias)

    def extract_features(self, text):
        text_lower = text.lower()
        contains_free = 1 if "free" in text_lower else 0
        contains_offer = 1 if "offer" in text_lower else 0
        length = len(text_lower)
        contains_link = 1 if re.search(r"http|www", text_lower) else 0
        return np.array([contains_free, contains_offer, length, contains_link])

    def predict(self, text):
        x = self.extract_features(text)
        y = np.dot(self.weights, x) + self.bias
        return 1 if y > 0 else 0, x, y
