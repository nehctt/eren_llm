import os
import whisper
import yt_dlp
import ffmpeg
import tempfile

class YouTubeProcessor:
    def __init__(self, model_size="base"):
        self.model = whisper.load_model(model_size)

    def download_and_transcribe(self, youtube_url):
        try:
            with tempfile.TemporaryDirectory() as tmp:
                # 1.  Download best-quality audio only
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": os.path.join(tmp, "audio.%(ext)s"),
                    "quiet": True,
                    "noplaylist": True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(youtube_url, download=True)
                    audio_path = ydl.prepare_filename(info)

                # 2.  Convert to WAV (Whisper prefers 16-bit wav)
                wav_path = os.path.join(tmp, "audio.wav")
                (
                    ffmpeg
                    .input(audio_path)
                    .output(wav_path, ac=1, ar="16k")
                    .overwrite_output()
                    .run(quiet=True)
                )

                # 3.  Transcribe
                result = self.model.transcribe(wav_path)

                return {
                    "title": info.get("title", "Unknown title"),
                    "transcription": result["text"],
                }

        except Exception as e:
            raise RuntimeError(f"Error processing YouTube video: {e}") from e