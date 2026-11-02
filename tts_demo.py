import pyttsx3

def synthesize_speech(text, voice_id=None):
    """Synthesizes speech from the given text using pyttsx3.

    Args:
        text (str): The text to convert to speech.
        voice_id (str, optional): The ID of the voice to use. If None, the default voice is used.
    """
    engine = pyttsx3.init()

    if voice_id:
        engine.setProperty('voice', voice_id)

    # You can adjust speaking rate and volume
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

    print(f"Synthesizing: '{text}'")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    # Example usage:
    sample_text = "Merhaba, bu yapay zeka ses sentezi örneğidir."

    # List available voices (optional, for demonstration)
    engine_for_listing = pyttsx3.init()
    voices = engine_for_listing.getProperty('voices')
    engine_for_listing.stop()

    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"  {i}: ID={voice.id}, Name={voice.name}, Lang={voice.languages}")

    # Synthesize with default voice
    print("\n--- Synthesizing with default voice ---")
    synthesize_speech(sample_text)

    # Synthesize with a specific voice (if available, e.g., the first one listed)
    if voices:
        first_voice_id = voices[0].id
        print(f"\n--- Synthesizing with voice ID: {first_voice_id} ---")
        synthesize_speech(sample_text, voice_id=first_voice_id)
    else:
        print("\nNo voices found to test with a specific ID.")
