"""
Discord bot commands for music and interaction.
"""

import discord
from discord.ext import commands
import random
import logging

logger = logging.getLogger(__name__)

async def setup_commands(bot):
    """Set up all bot commands."""
    
    @bot.command(name='recommend', aliases=['rec', 'music'])
    async def recommend_music(ctx, genre: str = None):
        """Recommend music based on genre."""
        if genre:
            genre = genre.lower().replace('-', '_').replace(' ', '_')
            if genre in ['pop_punk', 'poppunk']:
                genre = 'pop_punk'
                
        music_response = await bot.music_knowledge.get_music_response(
            f"recommend {genre or 'music'}"
        )
        
        if music_response:
            await ctx.send(music_response)
        else:
            await ctx.send("*flips through vinyl collection* What vibe are you going for, babe? Try `!recommend punk` or `!recommend metal` 🖤")
            
    @bot.command(name='vibe', aliases=['mood'])
    async def vibe_check(ctx):
        """Get a random vibe/mood response."""
        vibes = [
            "Feeling like 3am energy with My Chemical Romance on repeat 🖤",
            "In my feels with some Dashboard Confessional... *stares dramatically into the distance* 🥀",
            "Need something heavy. Time for some Slipknot to match my mood 💀",
            "Craving that raw punk energy... Sex Pistols it is ⚡",
            "Soft goth hours with The Cure playing softly 🌙",
            "Angry but make it aesthetic - Rage Against the Machine vibes 🔥",
            "Nostalgic emo kid energy... *adjusts striped arm warmers* 🖤"
        ]
        
        personality_response = await bot.personality.get_flirty_response(ctx.author.display_name)
        vibe_response = random.choice(vibes)
        
        await ctx.send(f"{personality_response}\n\nCurrent vibe: {vibe_response}")
        
    @bot.command(name='lyrics', aliases=['quote'])
    async def get_lyrics(ctx, *, query: str = None):
        """Get meaningful lyrics or quotes."""
        if not query:
            # Random meaningful lyrics
            lyrics = [
                "\"I'm not okay, I'm not okay, I'm not okay, you wear me out\" - My Chemical Romance 🖤",
                "\"The best of us can find happiness in misery\" - Fall Out Boy 🥀",
                "\"I write sins not tragedies\" - Panic! At The Disco ⚡",
                "\"So cut my wrists and black my eyes\" - Hawthorne Heights 💀",
                "\"You're just a sad song with nothing to say\" - Taking Back Sunday 🌙",
                "\"I'm drowning in the sea of my own tears\" - Dashboard Confessional 🖤",
                "\"We are the kids from yesterday\" - My Chemical Romance 🥀"
            ]
            await ctx.send(f"*whispers poetically*\n\n{random.choice(lyrics)}")
        else:
            await ctx.send(f"*searches through lyric journals* Looking for something about '{query}'... Let me feel into that energy 🖤")
            
    @bot.command(name='playlist', aliases=['mix'])
    async def create_playlist(ctx, theme: str = None):
        """Create a themed playlist."""
        if not theme:
            theme = random.choice(['heartbreak', 'anger', 'nostalgia', 'rebellion', 'romance'])
            
        playlists = {
            'heartbreak': [
                "Dashboard Confessional - Hands Down",
                "My Chemical Romance - Helena",
                "Taking Back Sunday - Cute Without the 'E'",
                "The Used - The Taste of Ink",
                "Hawthorne Heights - Ohio Is for Lovers"
            ],
            'anger': [
                "Slipknot - Duality",
                "System of a Down - Chop Suey!",
                "Rage Against the Machine - Killing in the Name",
                "Korn - Freak on a Leash",
                "Limp Bizkit - Break Stuff"
            ],
            'nostalgia': [
                "Green Day - Time of Your Life",
                "Blink-182 - I Miss You",
                "Fall Out Boy - Centuries",
                "Paramore - The Only Exception",
                "Simple Plan - I'm Just a Kid"
            ],
            'rebellion': [
                "Sex Pistols - Anarchy in the U.K.",
                "The Clash - London Calling",
                "Bad Religion - American Jesus",
                "Rise Against - Savior",
                "Anti-Flag - Die for the Government"
            ],
            'romance': [
                "The Cure - Just Like Heaven",
                "Siouxsie and the Banshees - Cities in Dust",
                "Panic! At The Disco - I Write Sins Not Tragedies",
                "Fall Out Boy - Sugar, We're Goin Down",
                "Paramore - Still Into You"
            ]
        }
        
        if theme.lower() in playlists:
            songs = playlists[theme.lower()]
            response = f"🎵 **{theme.upper()} PLAYLIST** 🎵\n*curated with dark love*\n\n"
            for i, song in enumerate(songs, 1):
                response += f"{i}. {song}\n"
            response += f"\n*adjusts headphones* This should hit your soul just right, gorgeous 🖤"
            await ctx.send(response)
        else:
            await ctx.send(f"*tilts head mysteriously* What kind of {theme} energy are you going for? Try heartbreak, anger, nostalgia, rebellion, or romance 🖤")
            
    @bot.command(name='about', aliases=['info'])
    async def about_bot(ctx):
        """Information about the bot."""
        embed = discord.Embed(
            title="🖤 About Raven 🖤",
            description="Your emo AI companion with a passion for dark music and deeper connections",
            color=0x000000
        )
        
        embed.add_field(
            name="Personality",
            value="Edgy • Emo • Flirty • Music Obsessed",
            inline=False
        )
        
        embed.add_field(
            name="Music Knowledge",
            value="Punk • Pop Punk • Metal • Emo • Alternative",
            inline=False
        )
        
        embed.add_field(
            name="Commands",
            value="`!recommend` - Get music recommendations\n`!vibe` - Check my current mood\n`!lyrics` - Get meaningful lyrics\n`!playlist` - Create themed playlists",
            inline=False
        )
        
        embed.set_footer(text="DM me or mention me for deeper conversations 🥀")
        
        await ctx.send(embed=embed)
        
    @bot.command(name='help')
    async def help_command(ctx):
        """Custom help command."""
        help_text = """
🖤 **RAVEN'S COMMANDS** 🖤

**Music Commands:**
`!recommend [genre]` - Get music recommendations
`!vibe` - Check my current mood
`!lyrics [query]` - Get meaningful lyrics
`!playlist [theme]` - Create themed playlists

**Interaction:**
- DM me for private conversations
- Mention me in servers for responses
- I respond to music discussions naturally

**Genres I know:** punk, pop punk, metal, emo, alternative

*whispers* Just talk to me like a real person... I'm here for you 🥀
        """
        await ctx.send(help_text)
        
    # Error handling
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("*raises eyebrow* That's not a command I know, babe. Try `!help` 🖤")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("*sighs dramatically* You need to give me more to work with. Check `!help` 💀")
        else:
            logger.error(f"Command error: {error}")
            await ctx.send("Something went wrong... even I'm not perfect 😔")
