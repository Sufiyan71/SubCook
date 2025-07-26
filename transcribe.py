import whisper
import time
import os

# Path to your video file
input_file = r"F:\Videos\audio1.wav"

# Load Whisper model (you can use 'base', 'small', 'medium', or 'large')
print("Loading model...")
model = whisper.load_model("medium")

# Start timing
start_time = time.time()

# Transcribe + translate Korean to English
print("Transcribing and translating...")
result = model.transcribe(
    input_file,
    task="translate",
    language="Korean",  # You can use "ko" as well
    verbose=True,
    fp16=False  # Force CPU precision mode to avoid FP16 warnings
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

# Final print
print("\n✅ Translation complete!")
print(f"⤷ Text output saved to: {os.path.abspath(text_output_path)}")
print(f"⤷ Subtitles saved to:   {os.path.abspath(srt_output_path)}")
print(f"⏱️ Total time: {round(time.time() - start_time, 2)} seconds")
