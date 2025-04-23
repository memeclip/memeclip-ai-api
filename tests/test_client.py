"""
Tests for the MemeClip client.
"""

import os
import unittest
from unittest.mock import patch, Mock

from memeclip import MemeClip
from memeclip.models import Meme, MemeClipError


class TestMemeClipClient(unittest.TestCase):
    """Test cases for the MemeClip client."""
    
    def setUp(self):
        """Set up test environment."""
        # Use a test API key
        self.api_key = "test_api_key"
        self.client = MemeClip(api_key=self.api_key)
    
    def test_init_with_api_key(self):
        """Test client initialization with API key."""
        client = MemeClip(api_key="test_key")
        self.assertEqual(client.api_key, "test_key")
        self.assertEqual(client.base_url, "https://memeclip.ai")
    
    @patch.dict(os.environ, {"MEMECLIP_API_KEY": "env_test_key"})
    def test_init_with_env_var(self):
        """Test client initialization with environment variable."""
        client = MemeClip()
        self.assertEqual(client.api_key, "env_test_key")
    
    def test_init_missing_api_key(self):
        """Test client initialization with missing API key."""
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                MemeClip()
    
    @patch("requests.Session.post")
    def test_create_meme(self, mock_post):
        """Test creating a meme."""
        # Mock the API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "meme_123",
            "url": "https://memeclip.ai/m/123.jpg",
            "text": "Test meme",
            "format": "image",
            "style": "tech",
            "width": 800,
            "height": 600,
            "created_at": "2023-07-01T12:00:00Z"
        }
        mock_post.return_value = mock_response
        
        # Call the client
        meme = self.client.create_meme(text="Test meme", style="tech")
        
        # Verify the result
        self.assertIsInstance(meme, Meme)
        self.assertEqual(meme.id, "meme_123")
        self.assertEqual(meme.text, "Test meme")
        self.assertEqual(meme.style, "tech")
        
        # Verify the request
        mock_post.assert_called_once()
        args, kwargs = mock_post.call_args
        self.assertEqual(kwargs["json"]["text"], "Test meme")
        self.assertEqual(kwargs["json"]["style"], "tech")
    
    @patch("requests.Session.post")
    def test_create_meme_error(self, mock_post):
        """Test handling API errors when creating a meme."""
        # Mock an error response
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {
            "message": "Invalid request",
            "type": "invalid_request_error",
            "code": "parameter_invalid"
        }
        mock_post.side_effect = Exception("API error")
        mock_post.return_value = mock_response
        
        # Call the client and expect an error
        with self.assertRaises(MemeClipError):
            self.client.create_meme(text="Test meme")


if __name__ == "__main__":
    unittest.main() 
