# Discord Eren Bot

一個基於 Discord.py 的聊天機器人，模仿進擊的巨人中的艾連·葉卡角色。這個機器人支持英文和中文對話，並且可以處理圖片和 YouTube 影片內容。

## 功能特點

- 雙語支持（英文和中文）
- 圖片分析功能
- YouTube 影片內容分析
- 角色扮演：模仿艾連·葉卡的性格和說話方式
- 使用 Qwen 和 LLaMA 模型進行自然語言處理

## 安裝要求

- Python 3.8+
- FFmpeg
- Discord Bot Token
- OpenRouter API Key

## 安裝步驟

1. 克隆專案：
```bash
git clone https://github.com/yourusername/discord_vlm.git
cd discord_vlm
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

3. 安裝 FFmpeg：
- macOS: `brew install ffmpeg`
- Ubuntu: `sudo apt-get install ffmpeg`
- Windows: 從 [FFmpeg 官網](https://ffmpeg.org/download.html) 下載

4. 設置環境變數：
創建 `.env` 文件並添加以下內容：
```
DISCORD_TOKEN=your_discord_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
```

## 使用方法

啟動機器人：
```bash
python main.py
```

### 可用命令

英文版命令：
- `!chat [text]` - 與艾連對話
- `!chat_with_image [text]` - 與艾連對話（包含圖片）
- `!chat_with_youtube [youtube_url]` - 與艾連討論 YouTube 影片內容

中文版命令：
- `!chat_zh [text]` - 與中文版艾連對話
- `!chat_with_image_zh [text]` - 與中文版艾連對話（包含圖片）
- `!chat_with_youtube_zh [youtube_url]` - 與中文版艾連討論 YouTube 影片內容

通用命令：
- `!ping` - 測試機器人延遲

## 專案結構

```
discord_vlm/
├── src/
│   ├── bot/
│   │   ├── commands.py
│   │   └── discord_bot.py
│   ├── llm/
│   │   ├── eren_llm.py
│   │   └── eren_llm_zh.py
│   └── utils/
│       └── youtube_processor.py
├── main.py
├── requirements.txt
└── .env
```

## 技術細節

- 使用 Discord.py 框架
- 使用 OpenRouter API 進行 LLM 調用
- 使用 Qwen 模型進行中文處理
- 使用 LLaMA 模型進行英文處理
- 使用 Whisper 進行語音轉文字
- 使用 FFmpeg 進行音頻處理

## 注意事項

- 確保有足夠的磁盤空間用於下載和處理 YouTube 影片
- 影片處理可能需要一些時間，請耐心等待
- 建議使用較短的影片進行測試