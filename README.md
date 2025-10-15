# Local Voice AI Agent - QA Teacher

A real-time voice chat application powered by local AI models, specifically designed as a software quality assurance and automation teacher. This project allows you to have natural voice conversations with an AI specialized in QA methodologies, testing strategies, and automation frameworks.

## 🎯 Features

- **Real-time Speech-to-Text**: Convert your voice to text using Moonshine
- **Local AI Processing**: Powered by Ollama with Gemma models running locally
- **Natural Speech Synthesis**: Convert AI responses to speech using Kokoro
- **QA Specialized**: AI teacher focused on software quality assurance and automation
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

## 🚀 Installation

### 1. Install Prerequisites

```bash
# Install Ollama for local LLM inference
brew install ollama

# Install uv for fast Python package management
brew install uv
```

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd local-voice-ai-agent
```

### 3. Set Up Python Environment

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv sync
```

### 4. Download AI Models

The application supports multiple models. Choose based on your system capabilities:

**For faster responses (recommended):**
```bash
ollama pull gemma3:4b
```

**For better quality (requires more resources):**
```bash
ollama pull gemma3:12b
```

**Alternative models:**
```bash
ollama pull qwen3:4b          # Good balance of speed and quality
ollama pull llama3:latest     # Popular alternative
```

### 5. Configure the Model

Edit `config/settings.py` to change the AI model:

```python
# Change this line to use a different model
AI_MODEL = "gemma3:4b"  # or "gemma3:12b", "qwen3:4b", etc.
```

## 🎮 Usage

### Start the Voice Chat

```bash
# Make sure you're in the project directory
cd local-voice-ai-agent

# Activate virtual environment
source .venv/bin/activate

# Start the application
python local_voice_chat.py
```

### Using the Application

1. **Open your browser** to the URL shown in the terminal (usually `http://localhost:7860`)
2. **Click the microphone button** to start speaking
3. **Ask QA-related questions** like:
   - "What is Selenium?"
   - "How do I write good test cases?"
   - "Explain the difference between unit and integration testing"
   - "What are the benefits of CI/CD?"
4. **Listen to the AI's response** - it will speak back to you with natural emphasis

## ⚙️ Configuration

### AI Model Settings

Edit `config/settings.py` to customize:

```python
# AI Model Configuration
AI_MODEL = "gemma3:4b"        # Change the model
AI_MAX_TOKENS = 200           # Adjust response length

# System Prompt
SYSTEM_PROMPT = """Your custom prompt here..."""
```

### Speech Enhancement

Customize how markdown formatting is converted to speech in `config/settings.py`:

```python
SPEECH_ENHANCEMENT = {
    "bold_pattern": r'\*\*(.*?)\*\*',
    "bold_replacement": r'IMPORTANT: \1',
    # ... other patterns
}
```

### Available Models

Based on your system, you can use:

| Model | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| `gemma3:4b` | 3.3 GB | Fast | Good | Quick responses |
| `gemma3:12b` | 8.1 GB | Slower | Better | Detailed explanations |
| `qwen3:4b` | 2.5 GB | Fast | Good | Alternative option |
| `llama3:latest` | 4.7 GB | Medium | Good | Popular choice |

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

### Common Issues

1. **"Module not found" errors**:
   ```bash
   # Make sure virtual environment is activated
   source .venv/bin/activate
   uv sync
   ```

2. **Model not found**:
   ```bash
   # Check available models
   ollama list
   
   # Pull the required model
   ollama pull gemma3:4b
   ```

3. **Audio issues**:
   - Check browser permissions for microphone access
   - Ensure your system audio is working
   - Try refreshing the web interface

4. **Performance issues**:
   - Use a smaller model like `gemma3:4b`
   - Reduce `AI_MAX_TOKENS` in settings
   - Close other applications to free up resources

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