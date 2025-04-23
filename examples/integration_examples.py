#!/usr/bin/env python
"""
Advanced integration examples for the MemeClip API.
Shows how to integrate MemeClip into various applications.
"""

import os
import sys
import time
from pathlib import Path

# Add the parent directory to the path if running as a script
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent))

from memeclip import MemeClip
from memeclip.models import MemeClipError

# Get API key from environment variable
api_key = os.environ.get("MEMECLIP_API_KEY")

if not api_key:
    print("Please set the MEMECLIP_API_KEY environment variable")
    print("You can get an API key at https://memeclip.ai/api")
    sys.exit(1)

# Initialize the MemeClip client
api = MemeClip(api_key=api_key)


def social_media_scheduling_example():
    """
    Example of creating a batch of memes for social media scheduling.
    """
    print("\n=== Social Media Scheduling Example ===")
    
    # List of content ideas for the week
    content_ideas = [
        {"text": "When the Monday meeting could have been an email", "style": "business"},
        {"text": "Tuesday motivation be like...", "style": "trending"},
        {"text": "That mid-week feeling when you're out of coffee", "style": "reaction"},
        {"text": "When it's Thursday but feels like Friday", "style": "random"},
        {"text": "Friday plans vs. reality", "style": "random"},
    ]
    
    # Create a meme for each content idea
    print("Creating a week's worth of social media content...")
    memes = []
    
    for idea in content_ideas:
        try:
            meme = api.create_meme(text=idea["text"], style=idea["style"])
            memes.append(meme)
            print(f"✓ Created meme: {idea['text']}")
            
            # Save the meme
            day = idea["text"].split()[1].lower()  # Extract day from text
            output_file = f"output/scheduled/{day}_meme.jpg"
            meme.save(output_file)
            
            # Be nice to the API with a short delay between requests
            time.sleep(1)
        except MemeClipError as e:
            print(f"✗ Failed to create meme: {e}")
    
    print(f"Created {len(memes)} memes for social media scheduling")
    return memes


def customer_support_example():
    """
    Example of using memes in customer support responses.
    """
    print("\n=== Customer Support Example ===")
    
    # Simulate a customer inquiry
    customer_issue = "My account is locked and I can't log in"
    
    # Generate a friendly meme response
    print(f"Customer issue: {customer_issue}")
    print("Generating friendly response meme...")
    
    try:
        meme = api.create_meme(
            text="Hang in there! Our support team is unlocking your account right now",
            style="reaction",
            tags=["support", "friendly", "helpful"]
        )
        
        print(f"✓ Created support response meme: {meme.id}")
        meme.save("output/support_response.jpg")
        
        # In a real app, you might attach this to a support ticket or email
        print(f"Support response meme URL: {meme.url}")
        return meme
    except MemeClipError as e:
        print(f"✗ Failed to create support meme: {e}")
        return None


def content_marketing_example():
    """
    Example of creating memes for content marketing.
    """
    print("\n=== Content Marketing Example ===")
    
    # Product features to highlight
    product_features = [
        "Our app loads 5x faster than competitors",
        "Save 20 hours per week with our automation tools",
        "Unlimited storage with our premium plan"
    ]
    
    print("Creating memes to highlight product features...")
    
    for i, feature in enumerate(product_features):
        try:
            # Create a meme highlighting the feature
            meme = api.create_meme(
                text=f"When you discover {feature.lower()}", 
                style="reaction",
                tags=["marketing", "product"]
            )
            
            print(f"✓ Created marketing meme for feature {i+1}")
            meme.save(f"output/marketing_feature_{i+1}.jpg")
            
            # In a real app, you might post these to social media or use in ads
            time.sleep(1)
        except MemeClipError as e:
            print(f"✗ Failed to create marketing meme: {e}")
    
    print("Content marketing memes completed")


if __name__ == "__main__":
    # Create output directories
    os.makedirs("output/scheduled", exist_ok=True)
    
    try:
        # Run examples
        social_media_scheduling_example()
        customer_support_example()
        content_marketing_example()
        
        print("\nAll examples completed successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}") 
