"""
Unit tests for the I'm not human CAPTCHA system.
"""

import unittest
import base64
from captcha import generate_captcha, validate_captcha


class TestCaptcha(unittest.TestCase):
    """Test cases for CAPTCHA generation and validation."""
    
    def test_generate_captcha_returns_dict(self):
        """Test that generate_captcha returns a dictionary."""
        challenge = generate_captcha()
        self.assertIsInstance(challenge, dict)
    
    def test_generate_captcha_has_required_keys(self):
        """Test that generated challenge has required keys."""
        challenge = generate_captcha()
        self.assertIn('type', challenge)
        self.assertIn('challenge', challenge)
        self.assertIn('answer', challenge)
    
    def test_generate_captcha_type_is_valid(self):
        """Test that challenge type is either base64 or sequence."""
        for _ in range(10):
            challenge = generate_captcha()
            self.assertIn(challenge['type'], ['base64', 'sequence'])
    
    def test_base64_challenge_encoding(self):
        """Test that base64 challenges are properly encoded."""
        # Generate multiple challenges to eventually get a base64 one
        base64_challenge = None
        for _ in range(50):
            challenge = generate_captcha()
            if challenge['type'] == 'base64':
                base64_challenge = challenge
                break
        
        # If we didn't get a base64 challenge, skip this test
        if base64_challenge is None:
            self.skipTest("Did not generate base64 challenge")
        
        # Verify the challenge can be decoded
        try:
            decoded = base64.b64decode(base64_challenge['challenge']).decode()
            self.assertEqual(decoded, base64_challenge['answer'])
        except Exception as e:
            self.fail(f"Failed to decode base64 challenge: {e}")
    
    def test_sequence_challenge_format(self):
        """Test that sequence challenges are properly formatted."""
        # Generate multiple challenges to eventually get a sequence one
        sequence_challenge = None
        for _ in range(50):
            challenge = generate_captcha()
            if challenge['type'] == 'sequence':
                sequence_challenge = challenge
                break
        
        # If we didn't get a sequence challenge, skip this test
        if sequence_challenge is None:
            self.skipTest("Did not generate sequence challenge")
        
        # Verify format: "n1, n2, n3, ..."
        challenge_str = sequence_challenge['challenge']
        self.assertIn(',', challenge_str)
        self.assertTrue(challenge_str.endswith(', ?'))
    
    def test_validate_captcha_correct_response(self):
        """Test validation with correct response."""
        challenge = generate_captcha()
        result = validate_captcha(challenge, challenge['answer'])
        self.assertTrue(result)
    
    def test_validate_captcha_incorrect_response(self):
        """Test validation with incorrect response."""
        challenge = generate_captcha()
        result = validate_captcha(challenge, 'wrong_answer')
        self.assertFalse(result)
    
    def test_validate_captcha_with_whitespace(self):
        """Test validation handles whitespace in response."""
        challenge = generate_captcha()
        result = validate_captcha(challenge, '  ' + challenge['answer'] + '  ')
        self.assertTrue(result)
    
    def test_validate_captcha_empty_response(self):
        """Test validation with empty response."""
        challenge = generate_captcha()
        result = validate_captcha(challenge, '')
        self.assertFalse(result)
    
    def test_validate_captcha_invalid_challenge(self):
        """Test validation with invalid challenge."""
        result = validate_captcha({}, 'answer')
        self.assertFalse(result)
        
        result = validate_captcha(None, 'answer')
        self.assertFalse(result)
    
    def test_sequence_challenge_pattern(self):
        """Test that sequence challenges follow geometric pattern."""
        # Generate multiple sequence challenges
        for _ in range(10):
            challenge = generate_captcha()
            if challenge['type'] == 'sequence':
                # Extract numbers from challenge
                challenge_str = challenge['challenge'].replace(', ?', '')
                numbers = [int(n.strip()) for n in challenge_str.split(',')]
                
                # Verify it's a geometric sequence (ratio between consecutive terms is constant)
                if len(numbers) >= 2:
                    ratio = numbers[1] / numbers[0]
                    for i in range(1, len(numbers) - 1):
                        self.assertAlmostEqual(numbers[i + 1] / numbers[i], ratio, places=5)
                
                # Verify answer continues the pattern
                answer = int(challenge['answer'])
                expected_ratio = numbers[1] / numbers[0]
                self.assertAlmostEqual(answer / numbers[-1], expected_ratio, places=5)


class TestBase64Challenge(unittest.TestCase):
    """Specific tests for base64 challenge type."""
    
    def test_base64_challenge_specific_example(self):
        """Test the specific example from requirements."""
        original = "SoloParaAgentes"
        encoded = base64.b64encode(original.encode()).decode()
        
        # The encoded version should be "U29sb1BhcmFBZ2VudGVz"
        self.assertEqual(encoded, "U29sb1BhcmFBZ2VudGVz")
        
        # Decoding should return the original
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(decoded, original)


class TestSequenceChallenge(unittest.TestCase):
    """Specific tests for sequence challenge type."""
    
    def test_sequence_challenge_specific_example(self):
        """Test the specific example from requirements: 3, 9, 27, ?"""
        # This is a geometric sequence with base=3, ratio=3
        sequence = [3, 9, 27]
        next_value = 81
        
        # Verify the pattern
        ratio = sequence[1] / sequence[0]
        self.assertEqual(ratio, 3)
        self.assertEqual(sequence[2], sequence[1] * ratio)
        self.assertEqual(next_value, sequence[2] * ratio)


if __name__ == '__main__':
    unittest.main()
