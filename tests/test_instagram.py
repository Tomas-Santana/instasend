import unittest
from unittest.mock import patch, MagicMock
from instasend.Instagram import Instagram
from instasend.custom_types.payload import InstagramPayload

class TestInstagram(unittest.TestCase):
    def setUp(self):
        self.access_token = "test_access_token"
        self.instagram = Instagram(self.access_token)

    @patch("instasend.Instagram.requests.post")
    def test_send_text_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_post.return_value = mock_response

        response = self.instagram.send_text("Hello", "12345")
        self.assertEqual(response, {"success": True})
        mock_post.assert_called_once()

    @patch("instasend.Instagram.requests.post")
    def test_send_text_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response

        with self.assertRaises(Exception) as context:
            self.instagram.send_text("Hello", "12345")
        self.assertIn("Error sending message", str(context.exception))
        mock_post.assert_called_once()

    def test_process_payload_success(self):
        payload = {
            "object": "page",
            "entry": [
                {
                    "id": "123",
                    "time": 1234567890,
                    "messaging": [
                        {
                            "sender": {"id": "user1"},
                            "recipient": {"id": "page1"},
                            "timestamp": 1234567890,
                            "message": {"mid": "mid1", "text": "Hello"}
                        }
                    ]
                }
            ]
        }
        result = self.instagram.process_payload(payload)
        self.assertIsInstance(result, InstagramPayload)
        self.assertEqual(result.object, "page")

    def test_process_payload_invalid(self):
        payload = {"invalid": "data"}
        with self.assertRaises(ValueError) as context:
            self.instagram.process_payload(payload)
        self.assertIn("Invalid payload", str(context.exception))

if __name__ == "__main__":
    unittest.main()
