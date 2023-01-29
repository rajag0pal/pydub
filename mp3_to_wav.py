from pydub import AudioSegment
import os

def mp3_to_wav(mp3_path, wav_path):
    # Load the MP3 file
    mp3_audio = AudioSegment.from_mp3(mp3_path)

    # Save the file as a WAV
    mp3_audio.export(wav_path, format="wav")
    print(f"{mp3_path} converted to {wav_path}")

# Example usage
mp3_to_wav(mp3_path,wav_path)