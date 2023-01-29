from pydub import AudioSegment
import os

def split_audio(wav_path, output_folder):
    # Load the WAV file
    audio = AudioSegment.from_wav(wav_path)
    file_name = os.path.basename(wav_path)
    # Get the length of the audio file in milliseconds
    audio_length = len(audio)
    # Calculate the number of chunks needed
    n_chunks = audio_length // 10000
    # If the file is shorter than 10 seconds, pad it with null data
    if n_chunks == 0:
        null_data = AudioSegment.silent(duration=10000)
        audio = audio + null_data
    # Split the audio file into chunks
    for i in range(n_chunks + 1):
        start = i * 10000
        end = start + 10000
        chunk = audio[start:end]
        chunk_file_name = file_name.split(".")[0] + f"_{i}.wav"
        chunk_path = os.path.join(output_folder, chunk_file_name)
        # Save the chunk to the output folder
        chunk.export(chunk_path, format="wav")
        print(f"{chunk_file_name} saved in {output_folder}")

# Example usage
split_audio("path/to/input.wav", "path/to/output_folder")