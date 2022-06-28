import os
from utils.AudioHelper import AudioHelper
import pytest

@pytest.mark.skip(reason="this test is long and need audios")
def test_audios_files():
    audios = os.listdir('audios')
    for audio in audios:
        complete_audio_text = AudioHelper.audio_to_text(audio, 'audios')
        assert isinstance(complete_audio_text, str)
