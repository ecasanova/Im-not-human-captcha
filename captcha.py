"""
CAPTCHA system that only automated agents can solve.
Provides two types of challenges:
1. Base64 encoded text that must be decoded
2. Geometric sequence patterns that require calculation
"""

import base64
import random
import string


def generate_captcha():
    """
    Generates a CAPTCHA challenge.
    
    Returns:
        dict: A dictionary containing:
            - 'type': Type of challenge ('base64' or 'sequence')
            - 'challenge': The challenge text/question
            - 'answer': The correct answer (for validation)
    """
    challenge_type = random.choice(['base64', 'sequence'])
    
    if challenge_type == 'base64':
        return _generate_base64_challenge()
    else:
        return _generate_sequence_challenge()


def _generate_base64_challenge():
    """
    Generates a base64 encoded text challenge.
    
    Returns:
        dict: Challenge with base64 encoded text
    """
    # Generate random text or use predefined texts
    texts = [
        'SoloParaAgentes',
        'AutomatedOnly',
        'NoHumansAllowed',
        'BotsWelcome',
        'MachineReadable'
    ]
    
    text = random.choice(texts)
    encoded = base64.b64encode(text.encode()).decode()
    
    return {
        'type': 'base64',
        'challenge': f'Decode this base64 text: {encoded}',
        'answer': text
    }


def _generate_sequence_challenge():
    """
    Generates a geometric sequence challenge.
    
    Returns:
        dict: Challenge with geometric sequence
    """
    # Generate geometric sequence (e.g., 3, 9, 27, ?)
    first_term = random.choice([2, 3, 4, 5])
    ratio = random.choice([2, 3, 4])
    length = random.randint(3, 5)
    
    sequence = [first_term * (ratio ** i) for i in range(length)]
    next_value = first_term * (ratio ** length)
    
    sequence_str = ', '.join(map(str, sequence))
    
    return {
        'type': 'sequence',
        'challenge': f'What is the next number in this sequence: {sequence_str}, ?',
        'answer': str(next_value)
    }


def validate_captcha(challenge, response):
    """
    Validates a CAPTCHA response.
    
    Args:
        challenge (dict): The challenge dictionary returned by generate_captcha()
        response (str): The user's response
        
    Returns:
        bool: True if the response is correct, False otherwise
    """
    if not isinstance(challenge, dict) or 'answer' not in challenge:
        return False
    
    return str(response).strip() == str(challenge['answer']).strip()
