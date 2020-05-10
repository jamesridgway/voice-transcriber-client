from assertpy import assert_that
import os
import vcr
from voice_transcriber.voice_transcriber import VoiceTranscriber

class TestVoiceTranscriber:

    @vcr.use_cassette('tests/fixtures/transcribe.yaml')
    def test_transcribe(self):
        sample_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../fixtures/sample_audio.m4a')
        voice_transcriber = VoiceTranscriber('mydoma.in', 'letmein')
        assert_that(voice_transcriber.transcribe('intro', sample_filename)).is_true()
