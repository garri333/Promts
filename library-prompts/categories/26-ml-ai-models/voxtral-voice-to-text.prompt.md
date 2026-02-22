---
title: "Voxtral Transcribe 2 — Voice-to-Text with Mistral AI"
version: "1.0"
category: "26-ml-ai-models"
tags: ["ml", "ai", "models", "voxtral", "mistral", "speech-to-text", "transcription", "voice", "open-source"]
author: "garri333"
description: "Complete prompt for using Mistral AI Voxtral Transcribe 2 (Feb 5 2026). Apache 2.0 open-source, local execution, <200ms latency, 13 languages. Covers Mini and Realtime variants, meeting transcription, dictation, accessibility, Python integration, and Whisper comparison."
language: "en"
---

# Voxtral Transcribe 2 — Voice-to-Text with Mistral AI

## Prompt

You are an expert in speech recognition and audio processing. Your task is to help me integrate **Mistral AI's Voxtral Transcribe 2** (released February 5, 2026) for voice-to-text applications, leveraging its open-source nature and exceptional low-latency performance.

### Context & Background

Voxtral Transcribe 2 is Mistral AI's second-generation speech-to-text model. Key differentiators:

- **Apache 2.0 License**: Fully open-source, no usage restrictions, commercial use allowed
- **Local Execution**: Runs on phones, laptops, and edge devices — no cloud dependency
- **< 200ms Latency**: Near-instantaneous transcription for real-time applications
- **13 Languages**: English, French, Spanish, German, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Arabic, Hindi
- **Two Variants**: Mini (cloud-optimized, $0.003/min) and Realtime (local open-source)

### Two Variants Explained

#### Voxtral Mini
- **Deployment**: Cloud API via Mistral platform or self-hosted
- **Cost**: $0.003 per minute of audio (cloud API)
- **Best for**: Batch transcription, stored audio processing, API-first applications
- **Accuracy**: Highest accuracy, especially on noisy audio
- **Model size**: ~2B parameters

#### Voxtral Realtime
- **Deployment**: Local execution on consumer hardware
- **Cost**: Free (Apache 2.0, self-hosted)
- **Best for**: Real-time transcription, privacy-sensitive applications, offline use
- **Latency**: < 200ms end-to-end
- **Model size**: ~500M parameters (optimized for edge)
- **Minimum hardware**: 4GB RAM, any modern CPU (ARM/x86)

### Python Integration

#### Installation

```bash
# Install Voxtral SDK
pip install voxtral

# For local execution (Realtime variant)
pip install voxtral[local]

# For GPU acceleration (optional)
pip install voxtral[cuda]  # NVIDIA
pip install voxtral[mps]   # Apple Silicon
```

#### Cloud API (Voxtral Mini)

```python
from mistralai import Mistral

client = Mistral(api_key="YOUR_MISTRAL_API_KEY")

# Transcribe from file
with open("meeting.mp3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        model="voxtral-mini-2",
        file=audio_file,
        language="en",  # Optional: auto-detect if omitted
        response_format="verbose_json",  # "text", "json", "verbose_json", "srt", "vtt"
        timestamp_granularities=["word", "segment"]
    )

print(response.text)

# Access word-level timestamps
for word in response.words:
    print(f"[{word.start:.2f}s - {word.end:.2f}s] {word.word}")

# Access segments
for segment in response.segments:
    print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}")
```

#### Local Execution (Voxtral Realtime)

```python
from voxtral import VoxtralRealtime

# Initialize local model
model = VoxtralRealtime(
    device="cpu",          # "cpu", "cuda", "mps"
    language="en",         # Primary language (helps accuracy)
    compute_type="int8",   # "float32", "float16", "int8" (int8 for CPU)
)

# Transcribe file
result = model.transcribe("recording.wav")
print(result.text)

# Real-time streaming from microphone
import sounddevice as sd
import numpy as np

def audio_callback(indata, frames, time, status):
    """Process audio chunks in real-time."""
    audio_chunk = indata[:, 0]  # Mono
    partial = model.process_chunk(audio_chunk)
    if partial.text:
        print(partial.text, end="", flush=True)

# Start streaming transcription
model.start_stream(sample_rate=16000)

with sd.InputStream(
    samplerate=16000,
    channels=1,
    dtype="float32",
    blocksize=4000,  # 250ms chunks
    callback=audio_callback
):
    print("Listening... Press Ctrl+C to stop.")
    try:
        while True:
            sd.sleep(100)
    except KeyboardInterrupt:
        pass

final_result = model.end_stream()
print(f"\nFinal transcript: {final_result.text}")
```

#### Batch Processing

```python
import asyncio
from pathlib import Path
from voxtral import VoxtralRealtime

async def batch_transcribe(audio_dir: str, output_dir: str):
    """Transcribe all audio files in a directory."""
    model = VoxtralRealtime(device="cuda")  # GPU for batch processing
    audio_files = list(Path(audio_dir).glob("*.{mp3,wav,m4a,ogg,flac}"))

    results = {}
    for audio_file in audio_files:
        print(f"Transcribing: {audio_file.name}")
        result = model.transcribe(str(audio_file))
        results[audio_file.name] = result

        # Save transcript
        output_path = Path(output_dir) / f"{audio_file.stem}.txt"
        output_path.write_text(result.text)

        # Save SRT subtitles
        srt_path = Path(output_dir) / f"{audio_file.stem}.srt"
        srt_path.write_text(result.to_srt())

    return results
```

### Use Case: Meeting Transcription

```python
from voxtral import VoxtralRealtime
from datetime import datetime

class MeetingTranscriber:
    def __init__(self):
        self.model = VoxtralRealtime(device="cpu", language="en")
        self.transcript = []
        self.start_time = None

    def start_meeting(self, meeting_name: str):
        """Start a new meeting transcription."""
        self.start_time = datetime.now()
        self.meeting_name = meeting_name
        self.transcript = []
        self.model.start_stream(sample_rate=16000)
        print(f"Meeting '{meeting_name}' started at {self.start_time}")

    def process_audio(self, audio_chunk):
        """Process incoming audio chunk."""
        result = self.model.process_chunk(audio_chunk)
        if result.text.strip():
            entry = {
                "timestamp": (datetime.now() - self.start_time).total_seconds(),
                "text": result.text.strip(),
                "confidence": result.confidence
            }
            self.transcript.append(entry)
            return entry
        return None

    def end_meeting(self) -> dict:
        """End meeting and generate summary."""
        final = self.model.end_stream()
        duration = (datetime.now() - self.start_time).total_seconds()

        return {
            "meeting_name": self.meeting_name,
            "date": self.start_time.isoformat(),
            "duration_minutes": duration / 60,
            "full_transcript": " ".join(e["text"] for e in self.transcript),
            "segments": self.transcript,
            "word_count": sum(len(e["text"].split()) for e in self.transcript)
        }

    def export_markdown(self, output_path: str):
        """Export transcript as Markdown."""
        meeting = self.end_meeting()
        md = f"""# Meeting: {meeting['meeting_name']}
**Date**: {meeting['date']}
**Duration**: {meeting['duration_minutes']:.1f} minutes
**Words**: {meeting['word_count']}

## Transcript

"""
        for entry in meeting["segments"]:
            minutes = int(entry["timestamp"] // 60)
            seconds = int(entry["timestamp"] % 60)
            md += f"**[{minutes:02d}:{seconds:02d}]** {entry['text']}\n\n"

        Path(output_path).write_text(md)
```

### Use Case: Dictation

```python
import pyperclip
from voxtral import VoxtralRealtime

class DictationEngine:
    """Real-time dictation that copies text to clipboard."""

    def __init__(self):
        self.model = VoxtralRealtime(device="cpu", language="en")
        self.buffer = []

    def start(self):
        """Start dictation — sends transcribed text to clipboard."""
        import sounddevice as sd

        self.model.start_stream(sample_rate=16000)

        def callback(indata, frames, time, status):
            result = self.model.process_chunk(indata[:, 0])
            if result.is_final:
                text = result.text.strip()
                if text:
                    self.buffer.append(text)
                    full_text = " ".join(self.buffer)
                    pyperclip.copy(full_text)
                    print(f"\r📋 {full_text}", end="", flush=True)

        with sd.InputStream(samplerate=16000, channels=1, dtype="float32",
                          blocksize=4000, callback=callback):
            print("🎤 Dictation active. Speak naturally. Ctrl+C to stop.")
            try:
                while True:
                    sd.sleep(100)
            except KeyboardInterrupt:
                pass

        final = self.model.end_stream()
        return " ".join(self.buffer)
```

### Use Case: Accessibility

```python
from voxtral import VoxtralRealtime

class AccessibilityTranscriber:
    """Real-time captions for hearing-impaired users."""

    def __init__(self, language="en", font_size=24):
        self.model = VoxtralRealtime(device="cpu", language=language)
        self.font_size = font_size

    def start_captions(self):
        """Display real-time captions in a window."""
        # Using tkinter for simple caption overlay
        import tkinter as tk
        import sounddevice as sd
        import threading

        root = tk.Tk()
        root.title("Live Captions")
        root.attributes("-topmost", True)
        root.geometry("800x100+100+900")
        root.configure(bg="black")

        label = tk.Label(
            root, text="Listening...",
            font=("Arial", self.font_size),
            fg="white", bg="black",
            wraplength=780
        )
        label.pack(expand=True, fill="both")

        self.model.start_stream(sample_rate=16000)

        def audio_thread():
            def callback(indata, frames, time, status):
                result = self.model.process_chunk(indata[:, 0])
                if result.text.strip():
                    # Update label from main thread
                    root.after(0, lambda: label.config(text=result.text.strip()))

            with sd.InputStream(samplerate=16000, channels=1, dtype="float32",
                              blocksize=4000, callback=callback):
                while not self._stop:
                    sd.sleep(100)

        self._stop = False
        thread = threading.Thread(target=audio_thread, daemon=True)
        thread.start()

        root.protocol("WM_DELETE_WINDOW", lambda: self.stop(root))
        root.mainloop()

    def stop(self, root):
        self._stop = True
        self.model.end_stream()
        root.destroy()
```

### Comparison with Whisper

| Feature | Voxtral Transcribe 2 | OpenAI Whisper (large-v3) |
|---------|----------------------|---------------------------|
| **License** | Apache 2.0 | MIT |
| **Latency** | < 200ms (Realtime) | ~2-5s per 30s chunk |
| **Languages** | 13 | 99 |
| **Local execution** | Yes (optimized) | Yes (heavy) |
| **Real-time streaming** | Native support | Requires workarounds |
| **Min RAM (CPU)** | 4 GB (Realtime) | 10 GB (large-v3) |
| **Cloud API cost** | $0.003/min | $0.006/min |
| **Word timestamps** | Built-in | Via whisper-timestamped |
| **Speaker diarization** | Built-in (Mini) | Requires pyannote |
| **Model size (edge)** | ~500M | ~1.5B (large-v3) |
| **Accuracy (English)** | Comparable | Baseline reference |
| **Accuracy (noisy)** | Better (Mini) | Good |

**When to choose Voxtral:**
- Real-time / streaming transcription is required
- Low-latency (< 200ms) is critical
- Running on resource-constrained devices
- Need built-in speaker diarization
- Cost optimization at scale

**When to choose Whisper:**
- Need support for 99 languages
- Batch processing of stored audio
- Ecosystem maturity and community support
- Already integrated in existing pipeline

### Output Format

For each integration, provide:
1. **Setup Code**: Complete installation and configuration
2. **Integration Code**: Runnable Python implementation
3. **Hardware Requirements**: CPU/RAM/GPU needs for the chosen variant
4. **Performance Metrics**: Expected latency and accuracy for the use case
5. **Cost Analysis**: Cloud vs. local execution cost comparison
6. **Error Handling**: Common issues and recovery strategies
