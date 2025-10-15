# 📖 User Guide - Local Voice AI Agent

This comprehensive guide will walk you through setting up and using the Local Voice AI Agent step by step.

## 🎯 What This Guide Covers

- Complete setup process from scratch
- Troubleshooting common issues
- How to use the application effectively
- Tips for getting the best results

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- ✅ **macOS** (required for FastRTC)
- ✅ **Python 3.13+** installed
- ✅ **Homebrew** package manager
- ✅ **At least 8GB RAM** (for AI models)
- ✅ **Microphone and speakers** working

## 🚀 Step-by-Step Setup

### Step 1: Install System Dependencies

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ollama for AI models
brew install ollama

# Install uv for Python package management
brew install uv
```

### Step 2: Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd local-voice-ai-agent

# Create Python virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install all dependencies
uv sync
```

### Step 3: Download AI Model

Choose a model based on your system:

**For most users (recommended):**
```bash
ollama pull gemma3:4b
```

**For better quality (requires more RAM):**
```bash
ollama pull gemma3:12b
```

**Alternative options:**
```bash
ollama pull qwen3:4b          # Good balance
ollama pull llama3:latest      # Popular choice
```

### Step 4: Configure the Application

Edit `config/settings.py` to match your downloaded model:

```python
# Make sure this matches your downloaded model
AI_MODEL = "gemma3:4b"  # or "gemma3:12b", "qwen3:4b", etc.
```

### Step 5: Start the Application

```bash
# Make sure you're in the project directory
cd local-voice-ai-agent

# Activate virtual environment
source .venv/bin/activate

# Start Ollama service (in a separate terminal)
ollama serve

# Start the voice chat application
python local_voice_chat.py
```

## 🎮 Using the Application

### First Time Setup

1. **Open your browser** to the URL shown in terminal (usually `http://localhost:7860`)
2. **Grant microphone permissions** when prompted
3. **Test your microphone** by clicking the microphone button
4. **Start speaking** your QA questions

### Example Questions to Ask

**Test Case Creation:**
- "Create test cases for a login form"
- "Write test cases for an e-commerce checkout process"
- "Generate test scenarios for a user registration form"

**QA Best Practices:**
- "What are the different types of testing?"
- "How do I write effective test cases?"
- "What's the difference between unit and integration testing?"

**Automation Questions:**
- "How do I set up Selenium WebDriver?"
- "What's the best way to automate API testing?"
- "Explain the Page Object Model pattern"

**Tool-Specific Questions:**
- "How do I use Postman for API testing?"
- "What's the difference between Jest and Mocha?"
- "How do I set up continuous integration?"

## 🔧 Configuration Options

### Changing AI Model

Edit `config/settings.py`:

```python
# For faster responses
AI_MODEL = "gemma3:4b"

# For better quality (requires more resources)
AI_MODEL = "gemma3:12b"
```

### Adjusting Response Length

```python
# Shorter responses (faster)
AI_MAX_TOKENS = 100

# Longer responses (more detailed)
AI_MAX_TOKENS = 300
```

### Customizing Speech Enhancement

```python
# Modify how text is converted to speech
SPEECH_ENHANCEMENT = {
    "bold_pattern": r'\*\*(.*?)\*\*',
    "bold_replacement": r'IMPORTANT: \1',
    # Add your own patterns here
}
```

## 🐛 Common Issues and Solutions

### Issue: "ModuleNotFoundError: No module named 'fastrtc'"

**Solution:**
```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Reinstall dependencies
uv sync
```

### Issue: "Ollama connection failed"

**Solution:**
```bash
# Start Ollama service
ollama serve

# Check if model is downloaded
ollama list

# Download model if missing
ollama pull gemma3:4b
```

### Issue: "Microphone not working"

**Solution:**
1. **macOS**: System Preferences → Security & Privacy → Microphone → Allow your browser
2. **Browser**: Grant microphone permissions when prompted
3. **Test**: Try speaking and check if the microphone icon responds

### Issue: "No sound output"

**Solution:**
1. Check system audio is working
2. Try refreshing the web interface
3. Check browser audio permissions
4. Restart the application

### Issue: "Slow responses"

**Solution:**
1. Use a smaller model: `gemma3:4b` instead of `gemma3:12b`
2. Reduce `AI_MAX_TOKENS` in settings
3. Close other applications to free up RAM
4. Check system resources

## 💡 Tips for Best Results

### Voice Interaction Tips

1. **Speak clearly** and at a normal pace
2. **Pause briefly** between questions
3. **Use specific questions** rather than vague ones
4. **Wait for the AI to finish** before asking the next question

### Question Examples

**Good Questions:**
- "Create test cases for a login form with email and password fields"
- "Explain the difference between black box and white box testing"
- "How do I set up Selenium WebDriver with Python?"

**Avoid:**
- "Help me with testing" (too vague)
- "What is QA?" (too broad)
- "Tell me everything about automation" (too general)

### Performance Optimization

1. **Use smaller models** for faster responses
2. **Close unnecessary applications** to free up RAM
3. **Use wired internet** for better stability
4. **Keep the browser tab active** during conversations

## 🔍 Troubleshooting Checklist

If something isn't working, check these in order:

1. **Virtual environment activated?**
   ```bash
   which python
   # Should show: /path/to/project/.venv/bin/python
   ```

2. **Dependencies installed?**
   ```bash
   pip list | grep fastrtc
   # Should show: fastrtc 0.0.33
   ```

3. **Ollama running?**
   ```bash
   ollama list
   # Should show your downloaded models
   ```

4. **Model matches settings?**
   ```bash
   # Check config/settings.py
   AI_MODEL = "gemma3:4b"  # Should match your downloaded model
   ```

5. **Microphone permissions?**
   - macOS: System Preferences → Security & Privacy → Microphone
   - Browser: Check microphone permissions

6. **Audio working?**
   - Test system audio
   - Check browser audio permissions
   - Try refreshing the page

## 📞 Getting Help

If you're still having issues:

1. **Check the logs** in your terminal for error messages
2. **Try the basic setup** from scratch
3. **Check GitHub Issues** for similar problems
4. **Create a new issue** with your error details

## 🎯 Quick Start Commands

For experienced users, here's the quick setup:

```bash
# Clone and setup
git clone <your-repo>
cd local-voice-ai-agent
uv venv && source .venv/bin/activate
uv sync

# Download model
ollama pull gemma3:4b

# Start services
ollama serve &  # Run in background
python local_voice_chat.py
```

## 🚀 Next Steps

Once you have the application running:

1. **Explore different question types** to see what works best
2. **Customize the system prompt** in `config/settings.py` for your specific needs
3. **Try different AI models** to find your preferred balance of speed and quality
4. **Experiment with speech enhancement** settings for better audio output

---

**Happy Learning with your AI QA Teacher! 🎓**

*This guide covers the most common setup scenarios. For advanced configuration and troubleshooting, refer to the main README.md file.*
