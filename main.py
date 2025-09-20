import whisper

model = whisper.load_model("tiny")
result = model.transcribe("dev-clean/LibriSpeech/dev-clean/174/84280/174-84280-0000.flac")

print(result["language"])
print(result["text"])
