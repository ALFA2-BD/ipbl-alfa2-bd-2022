import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from core.settings import DEBUG
from tqdm import tqdm
import os

class AudioHelper:
    def __init__(self) -> None:
        super.__init__()

    @staticmethod
    def transcribe_audio(audio_path)->str:
        r = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio,language='pt-BR')
        except sr.UnknownValueError:
            text = ''
        except sr.RequestError as e:
            text = ''
        return text

    @staticmethod
    def audio_to_text(audio_name:str, folder_audio_path:str)->str:

        audio_wav = '/'.join([folder_audio_path, audio_name])

        sound = AudioSegment.from_wav(audio_wav)
        sound.export(audio_wav, format='wav')

        audio_size = 30000
        segment = make_chunks (sound, audio_size)

        text = ''
        for i, portion in enumerate(tqdm(segment)):
            segment_path = '{}/segment_{}_{}.wav'.format(folder_audio_path, audio_name, i)
            portion.export(segment_path, format='wav')

            transcribed_audio = AudioHelper.transcribe_audio(segment_path)
            text = ' '.join([text, transcribed_audio])
            os.remove(segment_path)

        return text

    @staticmethod
    def mp3_to_wav(audio_name:str, folder_audio_path:str)->None:
        wav_audio_file = audio_name[:-3] + "wav"
        wav_path = "/".join([folder_audio_path, wav_audio_file])
        mp3_path = "/".join([folder_audio_path, audio_name])
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(wav_path, format="wav")
