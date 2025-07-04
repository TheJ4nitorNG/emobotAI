"""
Main Discord bot class with AI personality integration.
"""

import discord
from discord.ext import commands
import asyncio
import logging
from personality import PersonalityEngine
from music_knowledge import MusicKnowledge
from commands import setup_commands
from config import Config

# Set up logging
logger = logging.getLogger(__name__)

class EmoBot(commands.Bot):
    def __init__(self):
        # Use minimal intents that don't require privileged access
        intents = discord.Intents.default()
        # Only enable message_content if it's available (needs to be enabled in Discord Developer Portal)
        # For now, we'll work with default intents only
        
        super().__init__(
            command_prefix=Config.COMMAND_PREFIX,
            intents=intents,
            help_command=None
        )
        
        self.personality = PersonalityEngine()
        self.music_knowledge = MusicKnowledge()
        self.last_interactions = {}  # Track user interactions for context
        
    async def setup_hook(self):
        """Called when the bot is starting up."""
        logger.info("Setting up bot...")
        await setup_commands(self)
        logger.info("Bot setup complete")
        
    async def on_ready(self):
        """Called when the bot has connected to Discord."""
        logger.info(f'{self.user} has connected to Discord!')
        logger.info(f'Connected to {len(self.guilds)} guilds')
        
        # Set bot status
        activity = discord.Activity(
            type=discord.ActivityType.listening,
            name="My Chemical Romance 🖤"
        )
        await self.change_presence(activity=activity)
        
    async def on_message(self, message):
        """Handle incoming messages."""
        if message.author == self.user:
            return
            
        # Process commands first
        await self.process_commands(message)
        
        # Only respond to DMs or mentions in servers, or if message starts with bot prefix
        is_dm = isinstance(message.channel, discord.DMChannel)
        is_mentioned = self.user and self.user in message.mentions
        is_command_like = message.content.startswith(Config.COMMAND_PREFIX)
        
        if is_dm or is_mentioned or (not is_command_like and len(message.content) > 3):
            await self.handle_conversation(message)
            
    async def handle_conversation(self, message):
        """Handle AI conversation with personality."""
        try:
            # Show typing indicator
            async with message.channel.typing():
                # Get user context
                user_id = message.author.id
                user_context = self.last_interactions.get(user_id, {})
                
                # Check if message is about music
                is_music_related = self.music_knowledge.is_music_related(message.content)
                
                # Generate response with personality
                response = await self.personality.generate_response(
                    message.content,
                    user_context,
                    is_music_related,
                    message.author.display_name
                )
                
                # Add music knowledge if relevant
                if is_music_related:
                    music_info = await self.music_knowledge.get_music_response(message.content)
                    if music_info:
                        response += f"\n\n{music_info}"
                
                # Update user context
                self.last_interactions[user_id] = {
                    'last_message': message.content,
                    'last_response': response,
                    'message_count': user_context.get('message_count', 0) + 1
                }
                
                # Send response
                await message.channel.send(response)
                
        except Exception as e:
            logger.error(f"Error handling conversation: {e}")
            await message.channel.send(
                "Ugh, my brain's all scrambled right now... try again? 😵‍💫"
            )
            
    async def start_bot(self):
        """Start the bot with proper error handling."""
        try:
            if not Config.DISCORD_TOKEN:
                raise ValueError("Discord token is required")
            await self.start(Config.DISCORD_TOKEN)
        except discord.LoginFailure:
            logger.error("Invalid Discord token")
            raise
        except Exception as e:
            logger.error(f"Failed to start bot: {e}")
            raise
