# Discord Emo Bot

## Overview

This is a Discord bot with an AI-powered emo personality named Raven. The bot specializes in music recommendations, particularly punk, pop punk, metal, and emo genres, while maintaining a flirty, edgy personality through OpenAI integration.

## System Architecture

### Backend Architecture
- **Framework**: Discord.py - Python library for Discord bot development
- **AI Integration**: OpenAI API for personality-driven responses
- **Architecture Pattern**: Command-based bot with modular components
- **Language**: Python 3.x with async/await patterns

### Core Components
- **EmoBot Class**: Main bot controller extending `commands.Bot`
- **PersonalityEngine**: AI personality system using OpenAI
- **MusicKnowledge**: Static music database and recommendation system
- **Commands Module**: Discord command handlers
- **Configuration**: Environment-based configuration management

## Key Components

### 1. Bot Core (`bot.py`)
- Main Discord bot class with personality integration
- Handles Discord events and connection management
- Manages user interaction context tracking
- Sets up bot presence and status

### 2. Personality Engine (`personality.py`)
- OpenAI-powered AI personality system
- Maintains consistent "Raven" persona (emo, edgy, flirty)
- Handles conversation generation with personality traits
- Includes music knowledge and emotional intelligence

### 3. Music Knowledge (`music_knowledge.py`)
- Static database of punk, pop punk, metal, and emo music
- Band information with eras and vibes
- Song recommendations by genre
- Keyword-based music detection

### 4. Commands System (`commands.py`)
- Discord slash commands for music recommendations
- Vibe checking and mood responses
- Music genre-based recommendations
- Personality-driven command responses

### 5. Configuration (`config.py`)
- Environment variable management
- Discord and OpenAI API configuration
- Bot behavior settings
- Configuration validation

## Data Flow

1. **User Input**: Discord message received
2. **Command Processing**: Discord.py routes to appropriate command handler
3. **Music Analysis**: MusicKnowledge provides genre-specific recommendations
4. **Personality Response**: PersonalityEngine generates AI-driven responses
5. **Response Delivery**: Formatted message sent back to Discord

## External Dependencies

### Required Services
- **Discord API**: Bot hosting and message handling
- **OpenAI API**: AI personality generation
- **Python Environment**: Runtime with async support

### Python Packages
- `discord.py`: Discord API wrapper
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support
- `logging`: Application logging

### Environment Variables
- `DISCORD_TOKEN`: Discord bot authentication
- `OPENAI_API_KEY`: OpenAI API authentication
- `COMMAND_PREFIX`: Bot command prefix (default: "!")

## Deployment Strategy

### Development
- Local development with environment variables
- Python virtual environment recommended
- Direct execution via `main.py`

### Production Considerations
- Requires Discord bot token from Discord Developer Portal
- OpenAI API key for personality features
- Persistent hosting environment (VPS, cloud platform)
- Process monitoring for bot availability

### Scaling
- Single-instance bot suitable for small to medium servers
- Memory usage scales with music database size
- OpenAI API calls may have rate limits and costs

## Changelog

```
Changelog:
- July 03, 2025. Initial setup
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

## Technical Notes

### Design Decisions
- **Modular Architecture**: Separated concerns into distinct modules for maintainability
- **Static Music Database**: Chose local database over external API for reliability and speed
- **AI Personality**: OpenAI integration provides dynamic, context-aware responses
- **Command-Based Interface**: Discord slash commands provide familiar user experience

### Limitations
- Music database is static and requires manual updates
- OpenAI dependency creates external service requirement
- Single bot instance limits scalability across multiple servers
- No persistent user data storage implemented

### Future Enhancements
- Database integration for user preferences
- Music streaming service integration
- Multi-server support with shared personality
- Enhanced context tracking across conversations