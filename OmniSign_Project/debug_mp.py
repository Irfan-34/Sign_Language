
import mediapipe as mp
import sys
import os

print(f"Python executable: {sys.executable}")
print(f"MediaPipe location: {mp.__file__}")
print(f"Dir(mp): {dir(mp)}")

try:
    print(f"mp.solutions: {mp.solutions}")
except AttributeError as e:
    print(f"Error accessing mp.solutions: {e}")

try:
    import mediapipe.python.solutions as solutions
    print("Successfully imported mediapipe.python.solutions directly")
except ImportError as e:
    print(f"Error importing mediapipe.python.solutions: {e}")
