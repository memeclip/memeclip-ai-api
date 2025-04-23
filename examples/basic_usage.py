#!/usr/bin/env python
"""
Basic usage examples for the MemeClip API.
"""

import os
import sys
from pathlib import Path

# Add the parent directory to the path if running as a script
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

from memeclip import MemeClip

# Get API key from environment variable
api_key = os.environ.get("MEMECLIP_API_KEY")

if not api_key:
    print("Please set the MEMECLIP_API_KEY environment variable")
    print("You can get an API key at https://memeclip.ai/api")
    sys.exit(1)

# Initialize the MemeClip client
api = MemeClip(api_key=api_key)

print("Creating a meme...")
# Create a simple meme
meme = api.create_meme(
    text="When you're debugging for hours and find a typo in your code",
    style="tech"
)

print(f"Meme created with ID: {meme.id}")
print(f"Meme URL: {meme.url}")

# Save the meme to a file
output_file = "output/debug_meme.jpg"
meme.save(output_file)
print(f"Saved meme to {output_file}")

# Create a video meme
print("\nCreating a video meme...")
video_meme = api.create_meme(
    text="When your code compiles on the first try",
    style="tech",
    format="video",
    duration=5
)

print(f"Video meme created with ID: {video_meme.id}")
print(f"Video URL: {video_meme.url}")

# Save the video meme
video_output = "output/happy_programmer.mp4"
video_meme.save(video_output)
print(f"Saved video meme to {video_output}")

# List recent memes
print("\nListing recent memes...")
memes = api.list_memes(limit=5)
print(f"Found {len(memes)} recent memes:")

for i, meme in enumerate(memes, 1):
    print(f"{i}. ID: {meme.id}, Text: {meme.text[:40]}{'...' if len(meme.text) > 40 else ''}")

print("\nDone!") 
