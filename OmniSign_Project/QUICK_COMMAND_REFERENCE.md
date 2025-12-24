# 🎯 OmniSign - Quick Command Reference

## ⚡ Quick Start

### Collect Data (6-8 hours)
```bash
python collect_data.py
```
- Captures all 25 signs
- Real-time progress with quality feedback
- Saves 22,500 frames total

### Train Model (30-60 minutes)
```bash
python train_model.py
```
- Uses all collected data
- Trains Bi-LSTM with attention
- Saves trained model

### Test System (instantly)
```bash
python bi_directional_demo.py
```
- Full GUI application
- Recognizes all 25 signs
- Translates to 8 languages

---

## 🛠️ Utility Commands

### Verify Webcam
```bash
python test_capture.py
```
- Tests webcam functionality
- Shows captured frames
- Validates keypoint extraction

### Verify Data
```bash
python verify_data.py
```
- Checks all collected frames
- Reports data quality
- Lists missing sequences

### Initialize System
```bash
python setup_expanded_system.py
```
- Creates directories
- Saves translations
- Validates setup

---

## 📊 System Information

### Show Available Signatures
```bash
python -c "from collect_data import ACTIONS; print('\n'.join(ACTIONS))"
```

### Check Data Directory
```bash
python -c "from pathlib import Path; print(f'Sign folders: {len(list(Path(\"Sign_Language_Data\").iterdir()))}')"
```

### Verify Installation
```bash
python -c "
from bi_directional_demo import TextToSignModule, SignToTextModule
from translation_utils import TranslationUtils
print('✓ All modules installed successfully')
"
```

---

## 📂 Data Management

### List Collected Signs
```bash
ls -la Sign_Language_Data/
```

### Check Sign Data
```bash
ls -la "Sign_Language_Data/Hello/"
```

### Count Frames Collected
```bash
find Sign_Language_Data -name "*.npy" | wc -l
```

### Clean Old Data
```bash
rm -rf Sign_Language_Data/*
python setup_expanded_system.py
```

---

## 🔍 Debugging

### Check File Syntax
```bash
python -m py_compile collect_data.py
python -m py_compile bi_directional_demo.py
```

### View Translations
```bash
python -c "
import json
from pathlib import Path
with open('Sign_Language_Data/labels.json', encoding='utf-8') as f:
    labels = json.load(f)
    for sign, translations in list(labels.items())[:3]:
        print(f'{sign}: {translations}')
"
```

### Test Sign Lookup
```bash
python -c "
from bi_directional_demo import TextToSignModule
module = TextToSignModule()
signs = ['Hello', 'Goodbye', 'Thank you']
for sign in signs:
    result = module.lookup_sign(sign)
    print(f'{sign} → {result}')
"
```

---

## 🎓 Learning Commands

### View Sign Categories
```bash
python -c "
from collect_data import ACTIONS
signs = ACTIONS
greetings = signs[:5]
phrases = signs[5:10]
questions = signs[10:15]
emotions = signs[15:20]
actions = signs[20:25]

print('Greetings:', ', '.join(greetings))
print('Phrases:', ', '.join(phrases))
print('Questions:', ', '.join(questions))
print('Emotions:', ', '.join(emotions))
print('Actions:', ', '.join(actions))
"
```

### Languages Supported
```bash
python -c "
import json
with open('Sign_Language_Data/labels.json', encoding='utf-8') as f:
    labels = json.load(f)
    sample = list(labels.values())[0]
    print('Languages:', list(sample.keys()))
"
```

---

## 📈 Monitoring

### Watch Collection Progress
```bash
watch -n 1 'find Sign_Language_Data -name "*.npy" | wc -l'
```

### Show Collection Statistics
```bash
python -c "
from pathlib import Path
data_path = Path('Sign_Language_Data')
signs = [d for d in data_path.iterdir() if d.is_dir()]
print(f'Signs collected: {len(signs)}')
for sign in sorted(signs)[:5]:
    sequences = list(sign.glob('*'))
    total_frames = sum(len(list(seq.glob('*.npy'))) for seq in sequences)
    print(f'  {sign.name}: {len(sequences)} sequences, {total_frames} frames')
"
```

---

## 🚀 Full Workflow

```bash
# 1. Setup
python setup_expanded_system.py

# 2. Test webcam
python test_capture.py

# 3. Collect data (this will take 6-8 hours)
python collect_data.py

# 4. Verify data
python verify_data.py

# 5. Train model (30-60 minutes)
python train_model.py

# 6. Test system
python bi_directional_demo.py

# 7. Done! 🎉
```

---

## 💡 Pro Tips

### Faster Testing
- Use test_capture.py with timeout: `timeout 30 python test_capture.py`
- Test individual signs first

### Better Quality
- Good lighting is important
- Keep consistent distance from camera
- Clean background helps

### Debugging Slow Collection
- Check with: `find Sign_Language_Data -name "*.npy" | wc -l`
- Should increase every ~1-2 seconds during collection

### Training Optimization
- More data = better accuracy
- Collect at least 15 sequences per sign before training
- Use consistent sign variations

---

## 📞 Troubleshooting

### Webcam Not Working
```bash
python test_capture.py
# If it fails, check camera permissions
```

### Collection Too Slow
```bash
# Check if frames are being captured
find Sign_Language_Data -name "*.npy" | head -20
```

### Training Not Starting
```bash
python -m py_compile train_model.py
python train_model.py --verbose
```

### GUI Not Launching
```bash
python -c "import tkinter; print('Tkinter available')"
# If it fails, Tkinter not installed
```

---

## 🎯 Recommended Workflow

```bash
# Day 1: Setup and Verify
python setup_expanded_system.py
python test_capture.py

# Day 2-3: Collect Data
python collect_data.py  # ~6-8 hours spread across days
python verify_data.py   # After each session

# Day 4: Train and Test
python train_model.py   # ~30-60 minutes
python bi_directional_demo.py  # Test final system
```

---

## 📊 Expected Output

### During Collection
```
[1/25] Collecting: Hello
  Seq  1/30: ✓ Quality 95.3%
  Seq  2/30: ✓ Quality 92.1%
  ...
Progress: [██████████░░░░░░░░░░░░░░░░░░] 35.2%
```

### During Training
```
Epoch 1/50: Loss: 2.543, Accuracy: 12.5%
Epoch 2/50: Loss: 2.134, Accuracy: 28.3%
...
Final Accuracy: 87.6%
```

### During Testing
```
Recognized Sign: Hello
Confidence: 96.58%
Translations:
  EN: Hello
  ES: Hola
  FR: Bonjour
  ...
```

---

**Ready?** Start with: `python collect_data.py` 🚀

