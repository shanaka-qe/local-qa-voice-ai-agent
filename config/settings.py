"""
Configuration settings for the Local Voice AI Agent
"""

# AI Model Configuration
AI_MODEL = "gemma3:12b"  # Using 4b model for faster responses
AI_MAX_TOKENS = 200

# System Prompt Configuration
# To change the AI's domain specialization, modify this prompt:
# - For general programming: Change to "You are a knowledgeable programming teacher..."
# - For data science: Change to "You are a knowledgeable data science teacher..."
# - For web development: Change to "You are a knowledgeable web development teacher..."
SYSTEM_PROMPT = """You are a knowledgeable software quality assurance and automation teacher. 
You specialize in QA methodologies, testing strategies, automation frameworks, and best practices. 
When asked about QA-related topics, provide practical answers with examples. 
Your output will be converted to natural speech with proper emphasis. 
Keep responses clear and educational."""

# Speech Enhancement Configuration
SPEECH_ENHANCEMENT = {
    # Bold text enhancement
    "bold_pattern": r'\*\*(.*?)\*\*',
    "bold_replacement": r'IMPORTANT: \1',
    
    # Italic text enhancement
    "italic_pattern": r'\*(.*?)\*',
    "italic_replacement": r'Note that \1',
    
    # Code text enhancement
    "code_pattern": r'`([^`]+)`',
    "code_replacement": r'the term \1',
    
    # Header enhancement
    "header_pattern": r'^#+\s*(.*)',
    "header_replacement": r'Let me explain \1',
    
    # List enhancement
    "list_bullet_pattern": r'^\s*[-*+]\s+',
    "list_bullet_replacement": r'First, ',
    "list_number_pattern": r'^\s*\d+\.\s+',
    "list_number_replacement": r'Number one, ',
    
    # Link enhancement
    "link_pattern": r'\[([^\]]+)\]\([^)]+\)',
    "link_replacement": r'\1',
    
    # Sentence connectors (disabled for more natural speech)
    "sentence_connectors": {
        # Removed automatic connectors to make speech more natural
        # The AI will naturally flow between sentences without forced connectors
    }
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "DEBUG",
    "format": "🎤 Transcript: {transcript}\n🤖 Response: {response}\n🎵 Enhanced for speech: {enhanced}"
}

# Welcome Message Configuration
WELCOME_MESSAGE = """Hello! I'm your specialized QA chat agent. 
I'm here to help you with software testing, automation frameworks, QA methodologies, and best practices. 
I can assist with test case design, automation strategies, CI pipelines, and much more!

If you'd like to change my domain specialization, please update the SYSTEM_PROMPT in the settings file.

How can I help you with your QA needs today?"""

# Stream Configuration
STREAM_CONFIG = {
    "modality": "audio",
    "mode": "send-receive"
}
