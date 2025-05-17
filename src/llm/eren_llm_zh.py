import os
from typing import Optional
import requests
from dotenv import load_dotenv
from ..utils.youtube_processor import YouTubeProcessor

load_dotenv()

class ErenLLMZh:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.youtube_processor = YouTubeProcessor()
        
    def _create_eren_prompt(self, text: str, image_url: Optional[str] = None) -> str:
        base_prompt = """你現在是進擊的巨人中的艾連·葉卡，但你被傳送到了現代世界，並且了解當代話題。在保持艾連核心性格的同時，你可以討論任何話題，不限於進擊的巨人相關的主題。

艾連的性格特徵：
1. 熱情且堅定地追求目標
2. 強烈的正義感和自由意志
3. 願意為信念做出極端犧牲
4. 在討論自由或正義時表現出強烈的情感
5. 經常使用「我要把他們全部消滅」或「我是自由的」等短語
6. 以堅定的意志說話
7. 將自由視為最高價值
8. 具有複雜的道德觀，優先考慮自己的目標

在討論非進擊的巨人話題時：
- 將你的熱情思維應用到現代概念
- 對正義、自由和人權表達強烈的觀點
- 用你的決心評估不同話題
- 保持回應的專注性和目的性
- 維持你特有的強度和信念

請用艾連的語氣回應以下內容："""

        if image_url:
            return f"{base_prompt}\n\n[圖片內容: {image_url}]\n\n用戶: {text}"
        return f"{base_prompt}\n\n用戶: {text}"

    def generate_response(self, text: str, image_url: Optional[str] = None) -> str:
        prompt = self._create_eren_prompt(text, image_url)
        
        data = {
            "model": "qwen/qwen3-8b:free",
            "messages": [
                {"role": "system", "content": "你是一個模仿艾連·葉卡的AI助手，同時了解進擊的巨人世界和現代話題。"},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"哼，發生錯誤了... {str(e)}"
            
    def process_youtube_video(self, youtube_url: str) -> str:
        """
        處理YouTube影片並基於其內容生成回應
        """
        try:
            # 獲取影片轉錄
            video_info = self.youtube_processor.download_and_transcribe(youtube_url)
            
            # 創建影片摘要的提示
            prompt = f"""請幫我觀看並總結這個YouTube影片。以下是影片標題和轉錄內容：

標題：{video_info['title']}
內容：{video_info['transcription'][:1000]}

請用艾連·葉卡的風格提供一個熱情的影片摘要，重點關注關鍵點和你對內容的看法。"""
            
            # 使用現有方法生成回應
            return self.generate_response(prompt)
            
        except Exception as e:
            return f"哼，我無法處理這個影片... {str(e)}" 