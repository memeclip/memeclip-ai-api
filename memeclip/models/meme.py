"""
Meme model represents a meme created via the MemeClip API.
"""

import os
import json
import requests
from typing import Dict, Any, Optional
from datetime import datetime
from io import BytesIO
from PIL import Image


class Meme:
    """
    Represents a meme created via the MemeClip API.
    
    Attributes:
        id (str): Unique identifier for the meme
        url (str): Public URL to access the meme
        text (str): The original text used to generate the meme
        format (str): Format of the meme, either 'image' or 'video'
        style (str, optional): The style category used for the meme
        width (int): Width of the meme in pixels
        height (int): Height of the meme in pixels
        created_at (datetime): When the meme was created
    """
    
    def __init__(self, data: Dict[str, Any]):
        """
        Initialize a Meme object from API response data.
        
        Args:
            data (Dict[str, Any]): Response data from the API
        """
        self.id = data.get("id")
        self.url = data.get("url")
        self.text = data.get("text")
        self.format = data.get("format", "image")
        self.style = data.get("style")
        self.width = data.get("width")
        self.height = data.get("height")
        self.tags = data.get("tags", [])
        
        # Parse timestamps
        created_at = data.get("created_at")
        if created_at:
            self.created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        else:
            self.created_at = datetime.now()
        
        # Raw data for debugging
        self._raw_data = data
    
    def __repr__(self) -> str:
        """String representation of the meme."""
        return f"<Meme id={self.id} format={self.format}>"
    
    def download(self) -> bytes:
        """
        Download the meme content.
        
        Returns:
            bytes: The content of the meme as bytes
            
        Raises:
            IOError: If the download fails
        """
        response = requests.get(self.url)
        response.raise_for_status()
        return response.content
    
    def save(self, filepath: str) -> str:
        """
        Save the meme to a file.
        
        Args:
            filepath (str): Where to save the meme
            
        Returns:
            str: The path where the meme was saved
            
        Raises:
            IOError: If the download or save fails
        """
        content = self.download()
        
        # Ensure directory exists
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filepath, 'wb') as f:
            f.write(content)
            
        return filepath
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the meme to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the meme
        """
        return {
            "id": self.id,
            "url": self.url,
            "text": self.text,
            "format": self.format,
            "style": self.style,
            "width": self.width,
            "height": self.height,
            "tags": self.tags,
            "created_at": self.created_at.isoformat(),
        }
    
    def to_json(self) -> str:
        """
        Convert the meme to a JSON string.
        
        Returns:
            str: JSON representation of the meme
        """
        return json.dumps(self.to_dict())
    
    def display(self) -> Optional[Image.Image]:
        """
        Display the meme if it's an image and PIL is available.
        
        Returns:
            PIL.Image.Image or None: The image object if successful, None otherwise
            
        Note:
            This method only works for image memes, not video memes.
            The method returns the PIL Image object, which can be displayed
            in notebooks or saved in various formats.
        """
        if self.format != "image":
            print(f"Cannot display meme with format: {self.format}")
            return None
            
        try:
            content = self.download()
            return Image.open(BytesIO(content))
        except Exception as e:
            print(f"Failed to display image: {e}")
            return None 
