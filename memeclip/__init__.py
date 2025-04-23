"""
MemeClip AI API - Official Python SDK
====================================

MemeClip is an AI-powered meme generation platform.
This package provides a Python interface to the MemeClip API.

Basic usage:
   >>> from memeclip import MemeClip
   >>> api = MemeClip(api_key="your_api_key")
   >>> meme = api.create_meme(text="When the code works on the first try")
   >>> meme.save("awesome_meme.jpg")
"""

import os
from .client import MemeClip

__version__ = "0.1.0"
__all__ = ["MemeClip"]

# Allow setting API key via environment variable
MEMECLIP_API_KEY = os.environ.get("MEMECLIP_API_KEY", None) 
