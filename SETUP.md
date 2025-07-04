# Discord Bot Setup Guide

## Bot Setup Instructions

Your AI Discord bot "Raven" is now running and ready to connect! Here's how to get it working on Discord:

### Step 1: Generate Bot Invite Link (Required)

1. Go to https://discord.com/developers/applications
2. Find your application (the one you created to get the DISCORD_TOKEN)
3. Click on your application
4. Go to the "OAuth2" → "URL Generator" section

### Step 2: Optional - Enable Enhanced Features

For full message reading capabilities:
1. Go to the "Bot" section in the left sidebar
2. Scroll down to "Privileged Gateway Intents"
3. **Enable these intents:**
   - ✅ Message Content Intent (allows bot to read all message content)
   - ✅ Server Members Intent (optional, but recommended)

### Step 3: Generate Bot Invite Link

2. **Select ONLY this scope:**
   - ✅ bot

3. **Select these bot permissions:**
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Add Reactions
   - ✅ Embed Links
   - ✅ Use External Emojis

4. Copy the generated URL at the bottom

**Note:** Don't select "applications.commands" if you're getting an "invalid scopes" error - just use "bot" scope only.

### Step 4: Invite Bot to Your Server

1. Open the URL you copied in a new browser tab
2. Select the Discord server where you want to add the bot
3. Click "Authorize"

### Step 4: Test Your Bot

Once invited, you can test the bot with these commands:

- `!help` - See all available commands
- `!recommend punk` - Get punk music recommendations
- `!vibe` - Check Raven's current mood
- `!lyrics` - Get random emo/punk lyrics
- `!playlist heartbreak` - Create a themed playlist

You can also:
- **DM the bot directly** for private conversations
- **Mention the bot** in server channels (like @Raven) for responses

## Bot Features

- **Flirty, Edgy Personality**: Raven has a romantic, emo personality with attitude
- **Deep Music Knowledge**: Specializes in punk, pop punk, metal, and emo genres
- **Natural Conversations**: Uses AI to have real conversations about music and life
- **Music Commands**: Recommendations, playlists, lyrics, and mood responses

## Troubleshooting

If the bot doesn't respond:
1. Make sure Message Content Intent is enabled in Discord Developer Portal
2. Check that the bot has permissions to read and send messages in your server
3. Try DMing the bot directly first to test basic functionality

The bot is currently running and ready to connect once you complete the Discord setup!