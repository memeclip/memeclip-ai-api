"""
Main client class for the MemeClip API.
"""

import os
import requests
from typing import Dict, List, Optional, Union

from .models.meme import Meme
from .models.error import MemeClipError
from . import MEMECLIP_API_KEY

class MemeClip:
    """
    The main class for interacting with the MemeClip API.
    
    Args:
        api_key (str, optional): Your MemeClip API key. If not provided, 
            will look for MEMECLIP_API_KEY environment variable.
        base_url (str, optional): Custom API base URL. Defaults to MemeClip production API.
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        base_url: str = "https://api.memeclip.ai"
    ):
        self.api_key = api_key or MEMECLIP_API_KEY
        if self.api_key is None:
            raise ValueError(
                "API key must be provided either as an argument or "
                "via the MEMECLIP_API_KEY environment variable"
            )
        
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "MemeClip Python SDK v0.1.0",
            "Accept": "application/json",
        })
    
    def create_meme(
        self, 
        text: str,
        style: Optional[str] = None,
        format: str = "image",
        duration: Optional[int] = None,
        tags: Optional[List[str]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> Meme:
        """
        Create a meme from text.
        
        Args:
            text (str): The text content for the meme
            style (str, optional): Category of meme style (e.g., "tech", "gaming", "pets")
            format (str, optional): Output format, either "image" or "video"
            duration (int, optional): For video memes, the duration in seconds
            tags (List[str], optional): List of tags to help match appropriate meme templates
            width (int, optional): Desired width of the output meme
            height (int, optional): Desired height of the output meme
            
        Returns:
            Meme: A Meme object with methods to access and save the generated meme
            
        Raises:
            MemeClipError: If the API returns an error
        """
        payload = {
            "text": text,
            "format": format,
        }
        
        # Add optional parameters
        if style:
            payload["style"] = style
        if format == "video" and duration:
            payload["duration"] = duration
        if tags:
            payload["tags"] = tags
        if width:
            payload["width"] = width
        if height:
            payload["height"] = height
            
        try:
            response = self.session.post(
                f"{self.base_url}/v1/memes",
                json=payload
            )
            response.raise_for_status()
            return Meme(response.json())
        except requests.exceptions.RequestException as e:
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    raise MemeClipError(
                        f"API error: {error_data.get('message', str(e))}",
                        status_code=e.response.status_code,
                        error_type=error_data.get("type"),
                        error_code=error_data.get("code"),
                    )
                except (ValueError, KeyError):
                    pass
            raise MemeClipError(f"Request failed: {str(e)}")
    
    def list_memes(self, limit: int = 20, offset: int = 0) -> List[Meme]:
        """
        List memes created by the authenticated user.
        
        Args:
            limit (int, optional): Number of memes to return. Default 20, max 100.
            offset (int, optional): Pagination offset. Default 0.
            
        Returns:
            List[Meme]: List of Meme objects
        """
        try:
            response = self.session.get(
                f"{self.base_url}/v1/memes",
                params={"limit": limit, "offset": offset}
            )
            response.raise_for_status()
            data = response.json()
            return [Meme(item) for item in data.get("data", [])]
        except requests.exceptions.RequestException as e:
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    raise MemeClipError(
                        f"API error: {error_data.get('message', str(e))}",
                        status_code=e.response.status_code,
                        error_type=error_data.get("type"),
                        error_code=error_data.get("code"),
                    )
                except (ValueError, KeyError):
                    pass
            raise MemeClipError(f"Request failed: {str(e)}")
    
    def get_meme(self, meme_id: str) -> Meme:
        """
        Get a specific meme by ID.
        
        Args:
            meme_id (str): The ID of the meme to retrieve
            
        Returns:
            Meme: A Meme object
            
        Raises:
            MemeClipError: If the meme cannot be found or other API error
        """
        try:
            response = self.session.get(f"{self.base_url}/v1/memes/{meme_id}")
            response.raise_for_status()
            return Meme(response.json())
        except requests.exceptions.RequestException as e:
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    raise MemeClipError(
                        f"API error: {error_data.get('message', str(e))}",
                        status_code=e.response.status_code,
                        error_type=error_data.get("type"),
                        error_code=error_data.get("code"),
                    )
                except (ValueError, KeyError):
                    pass
            raise MemeClipError(f"Request failed: {str(e)}")
    
    def delete_meme(self, meme_id: str) -> bool:
        """
        Delete a meme by ID.
        
        Args:
            meme_id (str): The ID of the meme to delete
            
        Returns:
            bool: True if deletion was successful
            
        Raises:
            MemeClipError: If the meme cannot be deleted or other API error
        """
        try:
            response = self.session.delete(f"{self.base_url}/v1/memes/{meme_id}")
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            if e.response is not None:
                try:
                    error_data = e.response.json()
                    raise MemeClipError(
                        f"API error: {error_data.get('message', str(e))}",
                        status_code=e.response.status_code,
                        error_type=error_data.get("type"),
                        error_code=error_data.get("code"),
                    )
                except (ValueError, KeyError):
                    pass
            raise MemeClipError(f"Request failed: {str(e)}") 
