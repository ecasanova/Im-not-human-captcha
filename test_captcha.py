"""
Unit tests for the CAPTCHA system.
"""

import unittest
import base64
from captcha import generate_captcha, validate_captcha


class TestCaptcha(unittest.TestCase):
    """Test cases for CAPTCHA generation and validation."""
    
    def test_generate_captcha_returns_dict(self):
        """Test that generate_captcha returns a dictionary."""
        captcha = generate_captcha()
        self.assertIsInstance(captcha, dict)
    
    def test_generate_captcha_has_required_fields(self):
        """Test that generated CAPTCHA has required fields."""
        captcha = generate_captcha()
        self.assertIn('type', captcha)
        self.assertIn('challenge', captcha)
        self.assertIn('answer', captcha)
    
    def test_generate_captcha_type_is_valid(self):
        """Test that CAPTCHA type is either base64 or sequence."""
        for _ in range(10):  # Test multiple generations
            captcha = generate_captcha()
            self.assertIn(captcha['type'], ['base64', 'sequence'])
    
    def test_base64_challenge_decoding(self):
        """Test that base64 challenges can be decoded correctly."""
        # Generate multiple base64 challenges to test
        for _ in range(5):
            captcha = generate_captcha()
            if captcha['type'] == 'base64':
                # Extract the base64 string from the challenge text
                encoded_part = captcha['challenge'].split(': ')[1]
                decoded = base64.b64decode(encoded_part).decode()
                self.assertEqual(decoded, captcha['answer'])
                break
        else:
            # If we didn't get a base64 challenge in 5 tries, create one manually
            self.skipTest("Could not generate a base64 challenge in 5 attempts")
    
    def test_sequence_challenge_is_numeric(self):
        """Test that sequence challenges produce numeric answers."""
        for _ in range(10):
            captcha = generate_captcha()
            if captcha['type'] == 'sequence':
                self.assertTrue(captcha['answer'].isdigit())
                break
    
    def test_validate_captcha_correct_answer(self):
        """Test that validation returns True for correct answers."""
        captcha = generate_captcha()
        result = validate_captcha(captcha, captcha['answer'])
        self.assertTrue(result)
    
    def test_validate_captcha_incorrect_answer(self):
        """Test that validation returns False for incorrect answers."""
        captcha = generate_captcha()
        result = validate_captcha(captcha, 'WrongAnswer123')
        self.assertFalse(result)
    
    def test_validate_captcha_with_whitespace(self):
        """Test that validation handles whitespace correctly."""
        captcha = generate_captcha()
        answer_with_spaces = f"  {captcha['answer']}  "
        result = validate_captcha(captcha, answer_with_spaces)
        self.assertTrue(result)
    
    def test_validate_captcha_invalid_challenge(self):
        """Test that validation returns False for invalid challenge format."""
        result = validate_captcha({}, 'answer')
        self.assertFalse(result)
        
        result = validate_captcha({'type': 'base64'}, 'answer')
        self.assertFalse(result)
    
    def test_specific_base64_example(self):
        """Test the specific example from documentation: SoloParaAgentes."""
        challenge = {
            'type': 'base64',
            'challenge': 'Decode this base64 text: U29sb1BhcmFBZ2VudGVz',
            'answer': 'SoloParaAgentes'
        }
        
        # Test correct answer
        self.assertTrue(validate_captcha(challenge, 'SoloParaAgentes'))
        
        # Test incorrect answer
        self.assertFalse(validate_captcha(challenge, 'WrongAnswer'))
    
    def test_specific_sequence_example(self):
        """Test the specific example from documentation: 3, 9, 27."""
        challenge = {
            'type': 'sequence',
            'challenge': 'What is the next number in this sequence: 3, 9, 27, ?',
            'answer': '81'
        }
        
        # Test correct answer
        self.assertTrue(validate_captcha(challenge, '81'))
        
        # Test incorrect answer
        self.assertFalse(validate_captcha(challenge, '80'))


if __name__ == '__main__':
    unittest.main()
