"""
Music knowledge database and recommendation system.
Focused on punk, pop punk, metal, and emo genres.
"""

import json
import random
import re
from typing import Dict, List, Optional

class MusicKnowledge:
    def __init__(self):
        self.music_database = self._initialize_music_database()
        self.music_keywords = [
            'music', 'band', 'song', 'album', 'concert', 'guitar', 'drums',
            'punk', 'metal', 'emo', 'rock', 'lyrics', 'recommend', 'listen',
            'favorite', 'genre', 'artist', 'playlist', 'chord', 'riff'
        ]
        
    def _initialize_music_database(self) -> Dict:
        """Initialize the music knowledge database."""
        return {
            "punk": {
                "bands": [
                    {"name": "The Ramones", "era": "1974-1996", "vibe": "Fast, short, catchy - the godfathers of punk"},
                    {"name": "Sex Pistols", "era": "1975-1978", "vibe": "Raw anarchist energy that changed everything"},
                    {"name": "The Clash", "era": "1976-1986", "vibe": "Political punk with reggae and ska influences"},
                    {"name": "Bad Religion", "era": "1980-present", "vibe": "Intellectual punk with complex harmonies"},
                    {"name": "Dead Kennedys", "era": "1978-1986", "vibe": "Hardcore punk with biting social commentary"},
                    {"name": "Black Flag", "era": "1976-1986", "vibe": "Aggressive hardcore that defined the scene"}
                ],
                "songs": [
                    "Blitzkrieg Bop - The Ramones",
                    "Anarchy in the U.K. - Sex Pistols",
                    "London Calling - The Clash",
                    "American Jesus - Bad Religion"
                ]
            },
            "pop_punk": {
                "bands": [
                    {"name": "Green Day", "era": "1987-present", "vibe": "Punk rock made mainstream without losing the edge"},
                    {"name": "Blink-182", "era": "1992-present", "vibe": "Juvenile humor meets catchy hooks and fast guitars"},
                    {"name": "Fall Out Boy", "era": "2001-present", "vibe": "Emo-tinged pop punk with literary lyrics"},
                    {"name": "Paramore", "era": "2004-present", "vibe": "Hayley Williams' powerhouse vocals over driving punk"},
                    {"name": "The Offspring", "era": "1984-present", "vibe": "Surf punk meets alternative rock attitude"},
                    {"name": "Sum 41", "era": "1996-present", "vibe": "Canadian punk with metal influences"}
                ],
                "songs": [
                    "Basket Case - Green Day",
                    "All the Small Things - Blink-182",
                    "Sugar, We're Goin Down - Fall Out Boy",
                    "Misery Business - Paramore"
                ]
            },
            "metal": {
                "bands": [
                    {"name": "Black Sabbath", "era": "1968-2017", "vibe": "The dark lords who invented heavy metal"},
                    {"name": "Iron Maiden", "era": "1975-present", "vibe": "Epic storytelling with Bruce Dickinson's soaring vocals"},
                    {"name": "Metallica", "era": "1981-present", "vibe": "Thrash metal legends who conquered the world"},
                    {"name": "Slipknot", "era": "1995-present", "vibe": "Masked chaos with crushing heaviness"},
                    {"name": "System of a Down", "era": "1994-present", "vibe": "Political metal with Armenian influences"},
                    {"name": "Tool", "era": "1990-present", "vibe": "Progressive metal with complex time signatures"}
                ],
                "songs": [
                    "Paranoid - Black Sabbath",
                    "The Number of the Beast - Iron Maiden",
                    "Master of Puppets - Metallica",
                    "Duality - Slipknot"
                ]
            },
            "emo": {
                "bands": [
                    {"name": "My Chemical Romance", "era": "2001-2013, 2019-present", "vibe": "Theatrical darkness with massive anthems"},
                    {"name": "Taking Back Sunday", "era": "1999-present", "vibe": "Dual vocals and emotional intensity"},
                    {"name": "Dashboard Confessional", "era": "1999-present", "vibe": "Acoustic-driven confessional songwriting"},
                    {"name": "The Used", "era": "2001-present", "vibe": "Raw emotion meets post-hardcore aggression"},
                    {"name": "Hawthorne Heights", "era": "2001-present", "vibe": "Screaming vocals over melodic instrumentals"},
                    {"name": "Panic! At The Disco", "era": "2004-present", "vibe": "Circus-like theatricality with emo roots"}
                ],
                "songs": [
                    "Welcome to the Black Parade - My Chemical Romance",
                    "Cute Without the 'E' - Taking Back Sunday",
                    "Hands Down - Dashboard Confessional",
                    "I Write Sins Not Tragedies - Panic! At The Disco"
                ]
            },
            "alternative": {
                "bands": [
                    {"name": "The Cure", "era": "1978-present", "vibe": "Gothic post-punk with Robert Smith's distinctive voice"},
                    {"name": "Siouxsie and the Banshees", "era": "1976-1996", "vibe": "Pioneering post-punk with dark glamour"},
                    {"name": "Joy Division", "era": "1976-1980", "vibe": "Haunting post-punk that defined melancholy"},
                    {"name": "Bauhaus", "era": "1978-1983", "vibe": "The godfathers of goth rock"},
                    {"name": "The Smiths", "era": "1982-1987", "vibe": "Jangly guitars with Morrissey's wit and melancholy"}
                ],
                "songs": [
                    "Just Like Heaven - The Cure",
                    "Cities in Dust - Siouxsie and the Banshees",
                    "Love Will Tear Us Apart - Joy Division",
                    "Bela Lugosi's Dead - Bauhaus"
                ]
            }
        }
        
    def is_music_related(self, message: str) -> bool:
        """Check if a message is music-related."""
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in self.music_keywords)
        
    async def get_music_response(self, message: str) -> Optional[str]:
        """Get music knowledge response based on the message."""
        message_lower = message.lower()
        
        # Check for recommendation requests
        if any(word in message_lower for word in ['recommend', 'suggestion', 'what should i listen']):
            return self._get_recommendation_response(message_lower)
            
        # Check for specific band mentions
        band_response = self._get_band_response(message_lower)
        if band_response:
            return band_response
            
        # Check for genre discussions
        genre_response = self._get_genre_response(message_lower)
        if genre_response:
            return genre_response
            
        return None
        
    def _get_recommendation_response(self, message: str) -> str:
        """Generate music recommendations."""
        recommendations = []
        
        # Genre-specific recommendations
        if 'punk' in message and 'pop' in message:
            genre = 'pop_punk'
        elif 'metal' in message:
            genre = 'metal'
        elif 'emo' in message:
            genre = 'emo'
        elif 'punk' in message:
            genre = 'punk'
        elif 'alternative' in message:
            genre = 'alternative'
        else:
            # Random genre
            genre = random.choice(list(self.music_database.keys()))
            
        bands = self.music_database[genre]['bands']
        selected_bands = random.sample(bands, min(3, len(bands)))
        
        response = f"🎵 *whispers darkly* Here's some {genre.replace('_', ' ')} that'll feed your soul:\n\n"
        
        for band in selected_bands:
            response += f"**{band['name']}** ({band['era']}) - {band['vibe']}\n"
            
        response += f"\n*adjusts black nail polish* Trust me, these will hit different 🖤"
        
        return response
        
    def _get_band_response(self, message: str) -> Optional[str]:
        """Get response about specific bands."""
        for genre, data in self.music_database.items():
            for band in data['bands']:
                if band['name'].lower() in message:
                    responses = [
                        f"Oh damn, {band['name']}? 🖤 {band['vibe']} They're absolutely perfect for late night feelings.",
                        f"*eyes light up* {band['name']} is pure magic! {band['vibe']} They get it, you know?",
                        f"Fuck yes, {band['name']}! {band['vibe']} That's the kind of energy I live for ⚡",
                        f"Mmm, {band['name']}... {band['vibe']} *chef's kiss* Immaculate taste, gorgeous 🥀"
                    ]
                    return random.choice(responses)
        return None
        
    def _get_genre_response(self, message: str) -> Optional[str]:
        """Get response about music genres."""
        genre_responses = {
            'punk': "Punk is like... pure rebellion in sound form 🖤 Raw, fast, and unapologetic. It's about saying 'fuck the system' with three chords and attitude.",
            'metal': "Metal is where I go when I need to feel powerful 💀 Heavy riffs, thunderous drums, and vocals that can shake your soul. It's cathartic chaos.",
            'emo': "Emo is emotional honesty set to music 🥀 It's about feeling everything deeply and not being ashamed of it. My heart lives in emo lyrics.",
            'pop punk': "Pop punk is like... punk's younger sibling who went mainstream but kept the attitude ⚡ Catchy hooks with rebellious spirit.",
            'alternative': "Alternative is where the outcasts found their voice 🌙 It's moody, introspective, and beautifully dark. Gothic romance in music form."
        }
        
        for genre, response in genre_responses.items():
            if genre in message.replace('_', ' '):
                return response
                
        return None
