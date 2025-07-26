import whisper
import time
import os

# Path to your video/audio file
input_file = r"your_video_file.mp4"  # Replace with your actual video file path(mp4, mp3, wav, etc.)

# Load Whisper model (you can use 'base', 'small', 'medium', or 'large')
print("Loading model...")
model = whisper.load_model("medium") 

# Start timing
start_time = time.time()

# Transcribe + translate your_language to English
print("Transcribing and translating...")
result = model.transcribe(
    input_file,
    task="translate",
    language="your_language",  #enter the language in which the video/audio is 
    verbose=True,
    fp16=False  
)

# Save the full translation text
text_output_path = "translated_output1.txt"
with open(text_output_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

# Optional: Save as SRT subtitles
def write_srt(segments, output_path):
    def format_timestamp(seconds: float) -> str:
        hrs = int(seconds // 3600)
        mins = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds - int(seconds)) * 1000)
        return f"{hrs:02}:{mins:02}:{secs:02},{millis:03}"

    with open(output_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            f.write(f"{i}\n")
            f.write(f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n")
            f.write(f"{segment['text'].strip()}\n\n")

srt_output_path = "translated_output1.srt"
write_srt(result["segments"], srt_output_path)

print(f" Text output saved to: {os.path.abspath(text_output_path)}")
print(f"saved to:   {os.path.abspath(srt_output_path)}")
print(f"Total time: {round(time.time() - start_time, 2)} seconds")
