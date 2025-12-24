#!/usr/bin/env python3
"""
Quick test to show sign capture is working with real webcam.
"""

import cv2
import numpy as np
from bi_directional_demo import SignToTextModule

print("=" * 60)
print("OmniSign - Sign-to-Text Capture Test")
print("=" * 60)
print()

# Initialize module
module = SignToTextModule()
print("[*] SignToTextModule initialized")
print(f"[*] Available signs: {module.actions}")
print()

# Test capture with target languages
print("[*] Testing capture with English and Spanish...")
print("    Press 'q' in camera window to stop capturing")
print()

result = module.capture_and_recognize(target_languages=["en", "es"])

print()
print("=" * 60)
print("CAPTURE RESULTS:")
print("=" * 60)
print(f"Status: {result['status']}")
print(f"Frames captured: {len(result['frames'])}")
print(f"Predicted sign: {result['predicted_sign']}")
print(f"Confidence: {result['confidence']:.2%}")
print()
print("Translations:")
for lang, text in result['translations'].items():
    print(f"  {lang.upper()}: {text}")
print()
print("=" * 60)

if result['status'] == 'completed':
    print("✅ CAPTURE SUCCESSFUL - Webcam is working!")
elif result['status'] == 'demo':
    print("⚠️  DEMO MODE - Webcam not available, using mock data")
else:
    print(f"❌ CAPTURE FAILED - Status: {result['status']}")
