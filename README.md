# multilingual-voice-preserver
This project is an open-source system that performs speech-to-speech translation with voice preservation.
It takes spoken input in English, translates it into Spanish, and outputs the translated sentence in the same voice as the original speaker.

The pipeline combines:
- ASR (Whisper) → convert speech to text.
- MT (M2M100 / MarianMT) → translate text into the target language.
- Voice Cloning (RVC / OpenVoice) → generate speech in the speaker’s original voice.

🚀 Goal: Break language barriers while keeping your authentic voice.
