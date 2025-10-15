"""
Local Voice AI Agent - QA Teacher
Author: Shanaka Fernando
Description: Real-time voice chat application powered by local AI models,
             specifically designed as a software quality assurance and automation teacher.
"""

import sys

from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
from loguru import logger
from ollama import chat
from config.settings import (
    AI_MODEL, AI_MAX_TOKENS, SYSTEM_PROMPT, SPEECH_ENHANCEMENT, STREAM_CONFIG
)
from utils.speech_enhancer import SpeechEnhancer

stt_model = get_stt_model()  # moonshine/base
tts_model = get_tts_model()  # kokoro

logger.remove(0)
logger.add(sys.stderr, level="DEBUG")


# Initialize speech enhancer with configuration
speech_enhancer = SpeechEnhancer(SPEECH_ENHANCEMENT)


def echo(audio):
    transcript = stt_model.stt(audio)
    logger.debug(f"🎤 Transcript: {transcript}")
    
    response = chat(
        model=AI_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {"role": "user", "content": transcript},
        ],
        options={"num_predict": AI_MAX_TOKENS},
    )
    
    response_text = response["message"]["content"]
    
    # Enhance text for natural speech with emphasis and pauses
    enhanced_text = speech_enhancer.enhance_text(response_text)
    logger.debug(f"🎵 Enhanced for speech: {enhanced_text}")
    
    for audio_chunk in tts_model.stream_tts_sync(enhanced_text):
        yield audio_chunk

if __name__ == "__main__":
    logger.info("🚀 Starting QA Voice Chat Agent...")
    
    stream = Stream(
        ReplyOnPause(echo), 
        modality=STREAM_CONFIG["modality"], 
        mode=STREAM_CONFIG["mode"]
    )
    
    logger.info("🎤 QA Voice Chat Agent is ready! Open your browser to start chatting.")
    stream.ui.launch()
