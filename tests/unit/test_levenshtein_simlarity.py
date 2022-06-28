from matplotlib.pyplot import text
from utils.StringHelper import StringHelper
from faker import Faker
import string
from random import randint, sample

fake = Faker()

def test_small_same_texts():
    text1 = fake.sentence()
    text2 = text1
    assert StringHelper.levenshtein_simlarity(text1, text2) == 1.0

def test_bigger_same_texts():
    text1 = fake.text()
    text2 = text1
    assert StringHelper.levenshtein_simlarity(text1, text2) == 1.0

def test_texts_smalls_with_one_difference():

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    alphabet_size = len(alphabet)
    random_index = randint(0, alphabet_size)
    random_letter = alphabet[random_index]

    text1 = fake.sentence()
    text1_size = len(text1)
    random_index_to_add = randint(0, text1_size)

    text2 = text1[:random_index_to_add] + random_letter + text1[random_index_to_add:]
    assert StringHelper.levenshtein_simlarity(text1, text2) > 0.7

def test_texts_bigest_with_one_difference():
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    alphabet_size = len(alphabet)
    random_index = randint(0, alphabet_size)
    random_letter = alphabet[random_index]

    text1 = fake.text()
    text1_size = len(text1)
    random_index_to_add = randint(0, text1_size)

    text2 = text1[:random_index_to_add] + random_letter + text1[random_index_to_add:]
    assert StringHelper.levenshtein_simlarity(text1, text2) > 0.9

def test_shuffle_text():
    text1 = fake.text()
    text2 = ''.join(sample(text1, len(text1)))
    assert StringHelper.levenshtein_simlarity(text1, text2) < 0.5