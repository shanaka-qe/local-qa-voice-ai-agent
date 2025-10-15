"""
Speech enhancement utilities for converting markdown to natural speech
"""
import re
from typing import Dict, Any


class SpeechEnhancer:
    """
    A utility class for enhancing text to sound more natural when spoken by TTS engines.
    Converts markdown formatting to speech-friendly patterns.
    """
    
    def __init__(self, enhancement_config: Dict[str, Any]):
        """
        Initialize the speech enhancer with configuration.
        
        Args:
            enhancement_config: Dictionary containing speech enhancement patterns and replacements
        """
        self.config = enhancement_config
    
    def enhance_text(self, text: str) -> str:
        """
        Convert markdown formatting to natural speech patterns.
        
        Args:
            text: Input text with markdown formatting
            
        Returns:
            Enhanced text optimized for speech synthesis
        """
        # Apply bold text enhancement
        text = re.sub(
            self.config["bold_pattern"], 
            self.config["bold_replacement"], 
            text
        )
        
        # Apply italic text enhancement
        text = re.sub(
            self.config["italic_pattern"], 
            self.config["italic_replacement"], 
            text
        )
        
        # Apply code text enhancement
        text = re.sub(
            self.config["code_pattern"], 
            self.config["code_replacement"], 
            text
        )
        
        # Apply header enhancement
        text = re.sub(
            self.config["header_pattern"], 
            self.config["header_replacement"], 
            text, 
            flags=re.MULTILINE
        )
        
        # Apply list enhancements
        text = re.sub(
            self.config["list_bullet_pattern"], 
            self.config["list_bullet_replacement"], 
            text, 
            flags=re.MULTILINE
        )
        text = re.sub(
            self.config["list_number_pattern"], 
            self.config["list_number_replacement"], 
            text, 
            flags=re.MULTILINE
        )
        
        # Apply link enhancement
        text = re.sub(
            self.config["link_pattern"], 
            self.config["link_replacement"], 
            text
        )
        
        # Apply sentence connectors
        for pattern, replacement in self.config["sentence_connectors"].items():
            text = re.sub(pattern, replacement, text)
        
        # Clean up multiple spaces
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()
    
    def enhance_bold_text(self, text: str) -> str:
        """
        Apply only bold text enhancement.
        
        Args:
            text: Input text
            
        Returns:
            Text with bold enhancement applied
        """
        return re.sub(
            self.config["bold_pattern"], 
            self.config["bold_replacement"], 
            text
        )
    
    def enhance_code_text(self, text: str) -> str:
        """
        Apply only code text enhancement.
        
        Args:
            text: Input text
            
        Returns:
            Text with code enhancement applied
        """
        return re.sub(
            self.config["code_pattern"], 
            self.config["code_replacement"], 
            text
        )
