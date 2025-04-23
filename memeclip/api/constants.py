"""
Constants for the MemeClip API.
"""

# API version
API_VERSION = "v1"

# Base URL for API requests
API_BASE_URL = "https://memeclip.ai"

# Default request timeout in seconds
DEFAULT_TIMEOUT = 30

# Maximum file size for uploads (in bytes, 10MB)
MAX_UPLOAD_SIZE = 10 * 1024 * 1024

# Supported meme formats
SUPPORTED_FORMATS = ["image", "video"]

# Valid style categories
VALID_STYLES = [
    "tech",
    "gaming",
    "pets",
    "reaction",
    "trending",
    "classic",
    "movies",
    "tv",
    "sports",
    "politics",
    "business",
    "science",
    "food",
    "fashion",
    "music",
    "random"
] 
