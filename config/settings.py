"""
Configuration settings for the Local Voice AI Agent
"""

# AI Model Configuration
AI_MODEL = "gemma3:4b"  # Using 4b model for faster responses
AI_MAX_TOKENS = 200

# System Prompt Configuration
SYSTEM_PROMPT = """You are a knowledgeable software quality assurance and automation teacher. 
You specialize in QA methodologies, testing strategies, automation frameworks, and best practices. 
When asked about QA-related topics, provide detailed, practical answers with examples. 
Use markdown formatting like **bold** for important concepts, *italic* for emphasis, and `code` for technical terms. 
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
    
    # Sentence connectors
    "sentence_connectors": {
        r'\.\s+([A-Z])': r'. Additionally, \1',
        r'\?\s+([A-Z])': r'? Now, \1',
        r'!\s+([A-Z])': r'! Furthermore, \1'
    }
}

# Logging Configuration
LOGGING_CONFIG = {
    "level": "DEBUG",
    "format": "🎤 Transcript: {transcript}\n🤖 Response: {response}\n🎵 Enhanced for speech: {enhanced}"
}

# Stream Configuration
STREAM_CONFIG = {
    "modality": "audio",
    "mode": "send-receive"
}
