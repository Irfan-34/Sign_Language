#!/usr/bin/env python3
"""
Test script to verify text-to-sign display functionality.
This demonstrates how the sign visualization works.
"""

import sys
from bi_directional_demo import TextToSignModule

def test_display():
    """Test the display_sign functionality."""
    print("[*] Testing Text-to-Sign Display Module")
    print("-" * 50)
    
    # Initialize module
    module = TextToSignModule()
    
    print(f"[OK] Module initialized")
    print(f"[OK] Available signs: {list(module.available_signs.keys())}")
    print()
    
    # Test cases
    test_cases = ["Hello", "Goodbye", "Thank you"]
    
    for text_input in test_cases:
        print(f"\nTest: Display sign for '{text_input}'")
        print("-" * 30)
        
        # Lookup
        sign = module.lookup_sign(text_input)
        print(f"Lookup result: {sign}")
        
        if sign:
            print(f"Displaying sign: {sign}")
            print("(A window should appear with an animated skeleton)")
            print("(Press 'q' in the window to close it)")
            result = module.display_sign(sign, display_frames=30)
            print(f"Display result: {result['status']}")
        else:
            print(f"[ERROR] Sign not found for '{text_input}'")
    
    print("\n[OK] All tests completed!")

if __name__ == "__main__":
    test_display()
