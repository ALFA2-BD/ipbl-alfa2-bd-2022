import jellyfish as jf
from math import exp

class StringHelper:
    def __init__(self) -> None:
        super.__init__()

    @staticmethod
    def levenshtein_simlarity(text_original, text_generated)->int:
        bigger_text = len(text_original) if len(text_original) > len(text_generated) else len(text_generated)
        return 1/exp(jf.levenshtein_distance(text_original,text_generated)/bigger_text)