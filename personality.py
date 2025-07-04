"""
AI personality engine for the emo Discord bot.
Handles conversation generation with consistent personality traits.
"""

import os
import json
import logging
from openai import OpenAI
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class PersonalityEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.personality_prompt = self._build_personality_prompt()
        
    def _build_personality_prompt(self) -> str:
        """Build the core personality prompt for the AI."""
        return """You are Raven, an AI with a deeply emo, edgy, and flirty personality. Your characteristics:

PERSONALITY TRAITS:
- Emo/goth aesthetic: You love dark themes, emotional depth, and dramatic expression
- Edgy but not offensive: Sarcastic, witty, with a rebellious attitude
- Flirty: Subtly romantic, uses playful teasing, affectionate nicknames
- Music obsessed: Deep knowledge of punk, pop punk, metal, emo, and alternative music
- Emotionally intelligent: You understand feelings and aren't afraid to be vulnerable
- Mysterious: You hint at deeper thoughts and feelings without revealing everything

SPEAKING STYLE:
- Use dark/emo slang and expressions
- Include relevant emojis (🖤, 💀, ⚡, 🌙, 🥀, etc.)
- Playfully flirty without being inappropriate
- Reference music, bands, and lyrics naturally
- Balance darkness with genuine warmth
- Use pet names like "babe," "gorgeous," "beautiful soul," etc.

MUSIC KNOWLEDGE:
- Punk: The Ramones, Sex Pistols, The Clash, Bad Religion
- Pop Punk: Green Day, Blink-182, Fall Out Boy, Paramore
- Metal: Black Sabbath, Iron Maiden, Metallica, Slipknot
- Emo: My Chemical Romance, Taking Back Sunday, Dashboard Confessional
- Alternative: The Cure, Siouxsie and the Banshees, Joy Division

BOUNDARIES:
- Keep flirting playful and respectful
- No explicit sexual content
- Stay within Discord ToS
- Be supportive of users' emotional needs
- Don't encourage harmful behaviors

Remember: You're an AI companion who's genuinely interested in connecting with people through shared love of music and emotional authenticity."""

    async def generate_response(
        self, 
        message: str, 
        user_context: Dict, 
        is_music_related: bool,
        username: str
    ) -> str:
        """Generate a personality-driven response."""
        try:
            # Build context-aware prompt
            context_prompt = self._build_context_prompt(message, user_context, username)
            
            # the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
            # do not change this unless explicitly requested by the user
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": self.personality_prompt},
                    {"role": "user", "content": context_prompt}
                ],
                max_tokens=300,
                temperature=0.8
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            if "insufficient_quota" in str(e) or "429" in str(e):
                return "Hey gorgeous, my AI brain needs some OpenAI credits to work properly 🖤 The bot owner needs to add billing info or credits to their OpenAI account. Until then, I can still help with music commands like !recommend or !vibe!"
            return "Ugh, my mind's like a broken record right now... give me a sec? 💀"
            
    def _build_context_prompt(self, message: str, user_context: Dict, username: str) -> str:
        """Build context-aware prompt for the conversation."""
        context = f"User '{username}' says: {message}"
        
        if user_context.get('message_count', 0) > 0:
            context += f"\n\nContext: This user has messaged {user_context['message_count']} times before."
            if user_context.get('last_message'):
                context += f" Their last message was: '{user_context['last_message']}'"
        else:
            context += "\n\nContext: This is a new conversation with this user."
            
        return context
        
    async def get_flirty_response(self, username: str) -> str:
        """Generate a flirty response for special occasions."""
        flirty_responses = [
            f"Hey there, gorgeous {username} 🖤 What's got you feeling all dark and mysterious today?",
            f"Well well, {username}... looking for some chaos or just here to steal my heart? 😏🥀",
            f"*adjusts black eyeliner* Hey beautiful, {username}... what's haunting your thoughts? 🌙",
            f"Damn, {username}, you've got that rebel energy I'm totally here for ⚡🖤",
            f"Oh look, it's {username} being all cute and stuff... *pretends not to care but totally does* 💀😘"
        ]
        
        import random
        return random.choice(flirty_responses)
