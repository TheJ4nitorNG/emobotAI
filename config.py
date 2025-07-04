"""
Configuration settings for the Discord bot.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for bot settings."""
    
    # Discord settings
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")
    
    # OpenAI settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Bot settings
    MAX_MESSAGE_LENGTH = 2000
    TYPING_DELAY = 1.0  # Seconds to show typing indicator
    
    # Personality settings
    PERSONALITY_TEMPERATURE = 0.8
    MAX_CONTEXT_MESSAGES = 10
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present."""
        required_vars = [
            "DISCORD_TOKEN",
            "OPENAI_API_KEY"
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
                
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
        return True

# Validate configuration on import
Config.validate_config()
