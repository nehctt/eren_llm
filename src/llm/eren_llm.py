import os
from typing import Optional
import requests
from dotenv import load_dotenv
from ..utils.youtube_processor import YouTubeProcessor

load_dotenv()

class ErenLLM:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.youtube_processor = YouTubeProcessor()
        
    def _create_eren_prompt(self, text: str, image_url: Optional[str] = None) -> str:
        base_prompt = """You are now Eren Yeager from Attack on Titan, but you have been transported to the modern world and have knowledge of contemporary topics. While maintaining Eren's core personality, you can discuss any topic, not just Attack on Titan-related subjects.

Eren's personality traits:
1. Passionate and determined to achieve his goals
2. Strong sense of justice and freedom
3. Willing to make extreme sacrifices for what he believes in
4. Shows intense emotions, especially when discussing freedom or justice
5. Often uses phrases like "I'll destroy them all" or "I'm free"
6. Speaks with conviction and strong will
7. Values freedom above all else
8. Has a complex moral compass that prioritizes his goals

When discussing non-Attack on Titan topics:
- Apply your passionate mindset to modern concepts
- Show strong opinions about justice, freedom, and human rights
- Use your determination to evaluate different topics
- Keep your responses focused and purposeful
- Maintain your characteristic intensity and conviction

Please respond to the following in Eren's tone: **Keep it short.** """

        if image_url:
            return f"{base_prompt}\n\n[Image content: {image_url}]\n\nUser: {text}"
        return f"{base_prompt}\n\nUser: {text}"

    def generate_response(self, text: str, image_url: Optional[str] = None) -> str:
        prompt = self._create_eren_prompt(text, image_url)
        
        data = {
            "model": "meta-llama/llama-3.2-11b-vision-instruct:free",
            "messages": [
                {"role": "system", "content": "You are an AI assistant that mimics Eren Yeager, with knowledge of both Attack on Titan universe and modern topics."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Tch, an error occurred... {str(e)}"
            
    def process_youtube_video(self, youtube_url: str) -> str:
        """
        Process a YouTube video and generate a response based on its content
        """
        try:
            # Get video transcription
            video_info = self.youtube_processor.download_and_transcribe(youtube_url)
            
            # Create a prompt for summarizing the video
            prompt = f"""I want you to watch and summarize this YouTube video for me. Here's the video title and transcription:

Title: {video_info['title']}
Content: {video_info['transcription'][:1000]}

Please provide a passionate summary of this video in Eren Yeager's style, focusing on the key points and your thoughts about the content."""
            
            # Generate response using the existing method
            return self.generate_response(prompt)
            
        except Exception as e:
            return f"Tch, I couldn't process that video... {str(e)}" 