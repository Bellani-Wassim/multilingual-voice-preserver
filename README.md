# multilingual-voice-preserver
This project is an open-source system that performs speech-to-speech translation with voice preservation.
It takes spoken input in one language, translates it into another (e.g., English → Spanish), and outputs the translated sentence in the same voice as the original speaker.

The pipeline combines:

ASR (Whisper) → convert speech to text.

MT (M2M100 / MarianMT) → translate text into the target language.

Voice Cloning (RVC / OpenVoice) → generate speech in the speaker’s original voice.

✨ Key Features:

Real-time or batch speech-to-speech translation.

Natural-sounding, identity-preserving voice cloning.

Modular design (swap models for ASR, MT, or TTS).

Extensible for multiple languages and voices.

🚀 Goal: Break language barriers while keeping your authentic voice.
