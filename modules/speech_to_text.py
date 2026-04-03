from faster_whisper import WhisperModel

model = WhisperModel("tiny", compute_type="int8")

def transcribe(audio_file):

    segments, _ = model.transcribe(audio_file)

    text = " ".join([seg.text for seg in segments])

    return text.lower()