# SubCook

> *"SubCook be cooking up subtitles "*

SubCook generates high-quality subtitles for any video format using OpenAI Whisper AI transcription. Supports multiple languages, streaming sources, and outputs clean `.srt` files compatible with all major media players.

---

## Installation & Setup

### 1. Install FFmpeg

**FFmpeg** is required for audio extraction and streaming:
- Download from: https://ffmpeg.org/download.html
- Or install via:
  ```bash
  # Windows via Chocolatey
  choco install ffmpeg

  # macOS via Homebrew
  brew install ffmpeg

  # Linux (Debian-based)
  sudo apt install ffmpeg
  ```

Verify it's working:

```bash
ffmpeg -version
```

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:

```txt
openai-whisper
ffmpeg-python
torch
```

---

## 🧪 How to Use

### Option 1: Using `.mp4` directly

Edit the `input_file` path in `transcribe.py`:

```python
input_file = r"F:\Videos\your_video.mp4"
```

Whisper will **automatically extract the audio** and generate subtitles.

---

### Option 2: Manually convert `.mp4`/`.m3u8` to `.wav` first

Extract audio:

```bash
ffmpeg -i your_video.mp4 -ar 16000 -ac 1 -c:a pcm_s16le audio.wav
```

Or for `.m3u8`:

```bash
ffmpeg -headers "Referer: https://vidsrc.vip\r\nOrigin: https://vidsrc.vip\r\n" \
-i "https://example.com/stream.m3u8" -ar 16000 -ac 1 -c:a pcm_s16le audio.wav
```

Then in `transcribe.py`, set:

```python
input_file = r"F:\Videos\audio.wav"
```

---

### 👇 Run the Script

No arguments, just run:

```bash
python transcribe.py
```

You'll get:

* `translated_output1.txt` — full text.
* `translated_output1.srt` — subtitle file.

---

## 🎞️ How to Watch with Subtitles

### Option 1: VLC Player

Open your video and **drag `translated_output1.srt` into VLC** or name it exactly like the video:

```
output.mp4
output.srt
```

### Option 2: FFplay (Real-Time Playback)

```bash
ffplay output.mp4 -vf subtitles=translated_output1.srt
```

### Option 3: Burn Subtitles into the Video (Optional)

```bash
ffmpeg -i output.mp4 -vf subtitles=translated_output1.srt output_with_subs.mp4
```

---

## ⚙️ Other Tools Explored

* `ffplay` – for fast playback with subtitles.
* `ffmpeg` – to extract audio or stream `.m3u8`.
* `VLC` – for desktop playback.
* Whisper models: `base`, `small`, `medium`, `large` for performance vs. speed.

---

## 📁 Project Structure

```
📁 Subtitle-Generator-AI
├── transcribe.py
├── requirements.txt
├── translated_output1.txt
├── translated_output1.srt
└── README.md
```

---

## 🧠 Powered By

* [OpenAI Whisper](https://github.com/openai/whisper)
* [FFmpeg](https://ffmpeg.org/)
* [VLC Media Player](https://www.videolan.org/vlc/)
* [Python](https://www.python.org/)

---

## 🙌 Author

Built by [@Sufiyan71](https://github.com/Sufiyan71) — because subtitles should never block your binge-watch.

---

## 🌍 License

MIT License
