from utils.StringHelper import StringHelper
from utils.AudioHelper import AudioHelper
import os

def test_audio_similarity():

    test_text = "teste 123"
    audio = 'teste123.wav'

    audio_text = AudioHelper.audio_to_text(audio, 'audios').strip()
    point = StringHelper.levenshtein_simlarity(test_text, audio_text)
    assert point > 0.8