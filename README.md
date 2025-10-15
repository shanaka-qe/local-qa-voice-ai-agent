# AI Voice Assistant for Quality Assurance - QA Teacher

**Author:** Shanaka Fernando

A real-time voice chat application powered by local AI models, specifically designed as a software quality assurance and automation teacher. This project allows you to have natural voice conversations with an AI specialized in QA methodologies, testing strategies, and automation frameworks.

**Perfect for creating test cases, asking QA questions, and learning automation frameworks through natural voice interaction.**

> 📖 **New to this project?** Check out our [**User Guide**](USER_GUIDE.md) for a complete step-by-step setup walkthrough!


## 🎯 Features

- **Real-time Speech-to-Text**: Convert your voice to text using Moonshine
- **Local AI Processing**: Powered by Ollama with Gemma models running locally
- **Natural Speech Synthesis**: Convert AI responses to speech using Kokoro
- **QA Specialized**: AI teacher focused on software quality assurance and automation
- **Test Case Creation**: Get help creating comprehensive test cases for your applications
- **QA Question Answering**: Ask questions about testing strategies, automation frameworks, and best practices
- **Smart Speech Enhancement**: Converts markdown formatting to natural speech patterns
- **Web Interface**: Easy-to-use web interface for voice interactions
- **Modular Architecture**: Clean, organized codebase with configurable settings

## 🏗️ Project Structure

```
local-voice-ai-agent/
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration settings
├── utils/
│   ├── __init__.py
│   └── speech_enhancer.py   # Speech enhancement utilities
├── local_voice_chat.py      # Main application
├── pyproject.toml           # Dependencies
├── README.md               # This file
└── uv.lock                 # Dependency lock file
```

## 📋 Prerequisites

- **macOS** (required for FastRTC)
- **Python 3.13+**
- **Ollama** - For running local LLMs
- **uv** - Fast Python package manager

## 🚀 Quick Start

### Basic Setup

```bash
# Clone and setup
git clone <your-repo-url>
cd local-voice-ai-agent
uv venv && source .venv/bin/activate
uv sync

# Download AI model
ollama pull gemma3:4b

# Start the application
ollama serve &  # Run in background
python local_voice_chat.py
```

### Using the Application

1. **Open your browser** to the URL shown in the terminal (usually `http://localhost:7860`)
2. **Click the microphone button** to start speaking
3. **Ask QA-related questions** like:
   - "Create test cases for a login form"
   - "What is Selenium?"
   - "How do I write good test cases?"
   - "Explain the difference between unit and integration testing"
4. **Listen to the AI's response** - it will speak back to you with natural emphasis

## ⚙️ Configuration

Edit `config/settings.py` to customize:

```python
# AI Model Configuration
AI_MODEL = "gemma3:4b"        # Change the model
AI_MAX_TOKENS = 200           # Adjust response length

# System Prompt
SYSTEM_PROMPT = """Your custom prompt here..."""
```

## 🔧 How It Works

### Technical Flow

1. **Speech Input**: Your voice is captured by the web interface
2. **Speech-to-Text**: Moonshine converts your speech to text
3. **AI Processing**: Ollama processes the text using your chosen LLM
4. **Speech Enhancement**: Markdown formatting is converted to natural speech patterns
5. **Text-to-Speech**: Kokoro converts the enhanced text to speech
6. **Audio Output**: You hear the AI's response through your speakers

### Key Components

- **FastRTC**: WebRTC communication for real-time audio
- **Moonshine**: Local speech-to-text conversion
- **Kokoro**: Text-to-speech synthesis
- **Ollama**: Local LLM inference
- **SpeechEnhancer**: Converts markdown to natural speech

## 🛠️ Development

### Project Structure

- **`config/settings.py`**: All configuration settings
- **`utils/speech_enhancer.py`**: Speech enhancement utilities
- **`local_voice_chat.py`**: Main application logic

### Adding New Speech Patterns

Edit `config/settings.py` to add new speech enhancement patterns:

```python
SPEECH_ENHANCEMENT = {
    "your_pattern": r'your_regex_pattern',
    "your_replacement": r'your_replacement_text',
    # ... add to the sentence_connectors if needed
}
```

### Testing

```bash
# Test the project structure
python -c "from config.settings import AI_MODEL; print(f'Using model: {AI_MODEL}')"

# Test speech enhancement
python -c "
from utils.speech_enhancer import SpeechEnhancer
from config.settings import SPEECH_ENHANCEMENT
enhancer = SpeechEnhancer(SPEECH_ENHANCEMENT)
result = enhancer.enhance_text('**Test** this *text*')
print(result)
"
```

## 🐛 Troubleshooting

**Most common issues:**
- **Dependencies not installed**: `uv sync`
- **Ollama not running**: `ollama serve`
- **Model not found**: `ollama pull gemma3:4b`
- **Microphone permissions**: Check macOS System Preferences

**Need detailed help?** See our [**User Guide**](USER_GUIDE.md) for comprehensive troubleshooting.

## 📝 License

This project is open source. Please check the license file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section
2. Review the logs in the terminal
3. Ensure all prerequisites are installed
4. Verify your model is downloaded and working

---

**Happy Learning with your AI QA Teacher! 🎓**