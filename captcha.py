"""
I'm not human CAPTCHA system.
A CAPTCHA system designed to be solved by automated agents but difficult for humans.
"""

import base64
import random
from typing import Dict, Tuple


def generate_captcha() -> Dict[str, str]:
    """
    Generate a CAPTCHA challenge that can be either:
    1. Base64 encoded text that needs to be decoded
    2. Geometric sequence where the next number needs to be calculated
    
    Returns:
        Dict with 'type', 'challenge', and 'answer' keys
    """
    challenge_type = random.choice(['base64', 'sequence'])
    
    if challenge_type == 'base64':
        return _generate_base64_challenge()
    else:
        return _generate_sequence_challenge()


def _generate_base64_challenge() -> Dict[str, str]:
    """
    Generate a base64 encoded text challenge.
    
    Returns:
        Dict with type='base64', challenge=encoded text, answer=original text
    """
    texts = [
        'SoloParaAgentes',
        'AutomationOnly',
        'NoHumansAllowed',
        'BotAccess',
        'MachineReadable'
    ]
    
    original_text = random.choice(texts)
    encoded = base64.b64encode(original_text.encode()).decode()
    
    return {
        'type': 'base64',
        'challenge': encoded,
        'answer': original_text
    }


def _generate_sequence_challenge() -> Dict[str, str]:
    """
    Generate a geometric sequence challenge.
    The sequence follows the pattern: a, a*r, a*r^2, ...
    
    Returns:
        Dict with type='sequence', challenge=sequence string, answer=next number
    """
    # Generate geometric sequence parameters
    base = random.randint(2, 5)
    ratio = random.randint(2, 4)
    length = random.randint(3, 5)
    
    # Generate sequence
    sequence = [base * (ratio ** i) for i in range(length)]
    next_value = base * (ratio ** length)
    
    # Format as string
    challenge_str = ', '.join(str(n) for n in sequence) + ', ?'
    
    return {
        'type': 'sequence',
        'challenge': challenge_str,
        'answer': str(next_value)
    }


def validate_captcha(challenge: Dict[str, str], response: str) -> bool:
    """
    Validate the response to a CAPTCHA challenge.
    
    Args:
        challenge: The challenge dict returned by generate_captcha()
        response: The user's response as a string
    
    Returns:
        True if response is correct, False otherwise
    """
    if not challenge or not isinstance(challenge, dict):
        return False
    
    if 'answer' not in challenge:
        return False
    
    return str(response).strip() == str(challenge['answer']).strip()
