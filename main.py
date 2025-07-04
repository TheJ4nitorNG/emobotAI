#!/usr/bin/env python3
"""
Entry point for the Discord bot.
Handles bot initialization and startup.
"""

import asyncio
import logging
from bot import EmoBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    """Main entry point for the bot."""
    bot = EmoBot()
    try:
        await bot.start_bot()
    except KeyboardInterrupt:
        logging.info("Bot shutdown requested by user")
    except Exception as e:
        logging.error(f"Fatal error: {e}")
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
