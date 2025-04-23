"""
Exception classes for MemeClip API.
"""

from typing import Optional


class MemeClipError(Exception):
    """
    Exception raised for errors in the MemeClip API.
    
    Attributes:
        message (str): Error message
        status_code (int, optional): HTTP status code if applicable
        error_type (str, optional): Type of error from API
        error_code (str, optional): Error code from API
    """
    
    def __init__(
        self, 
        message: str,
        status_code: Optional[int] = None,
        error_type: Optional[str] = None,
        error_code: Optional[str] = None,
    ):
        """
        Initialize MemeClipError.
        
        Args:
            message (str): Error message
            status_code (int, optional): HTTP status code if applicable
            error_type (str, optional): Type of error from API
            error_code (str, optional): Error code from API
        """
        self.message = message
        self.status_code = status_code
        self.error_type = error_type
        self.error_code = error_code
        super().__init__(self.message)
    
    def __str__(self) -> str:
        """String representation of the error."""
        parts = [self.message]
        if self.status_code:
            parts.append(f"Status code: {self.status_code}")
        if self.error_type:
            parts.append(f"Error type: {self.error_type}")
        if self.error_code:
            parts.append(f"Error code: {self.error_code}")
        
        return " - ".join(parts) 
