#!/usr/bin/env python3
"""
OmniSign System - Complete Enhancement and Setup

This script:
1. Expands sign vocabulary to 25 signs
2. Generates all multilingual translations
3. Updates all configuration files
4. Creates training data directories
5. Validates the entire system
"""

import json
import os
from pathlib import Path

# All 25 signs with translations
EXPANDED_SIGNS = {
    "hello": {
        "en": "Hello",
        "es": "Hola",
        "fr": "Bonjour",
        "ar": "مرحبا",
        "de": "Hallo",
        "pt": "Olá",
        "zh-CN": "你好",
        "ja": "こんにちは"
    },
    "goodbye": {
        "en": "Goodbye",
        "es": "Adiós",
        "fr": "Au revoir",
        "ar": "وداعا",
        "de": "Auf Wiedersehen",
        "pt": "Adeus",
        "zh-CN": "再见",
        "ja": "さようなら"
    },
    "thank you": {
        "en": "Thank you",
        "es": "Gracias",
        "fr": "Merci",
        "ar": "شكرا",
        "de": "Danke",
        "pt": "Obrigado",
        "zh-CN": "谢谢",
        "ja": "ありがとう"
    },
    "how are you": {
        "en": "How are you?",
        "es": "¿Cómo estás?",
        "fr": "Comment allez-vous?",
        "ar": "كيف حالك؟",
        "de": "Wie geht es dir?",
        "pt": "Como você está?",
        "zh-CN": "你好吗？",
        "ja": "お元気ですか？"
    },
    "i need help": {
        "en": "I need help",
        "es": "Necesito ayuda",
        "fr": "J'ai besoin d'aide",
        "ar": "أحتاج إلى مساعدة",
        "de": "Ich brauche Hilfe",
        "pt": "Preciso de ajuda",
        "zh-CN": "我需要帮助",
        "ja": "助けが必要です"
    },
    "good morning": {
        "en": "Good morning",
        "es": "Buenos días",
        "fr": "Bonjour",
        "ar": "صباح الخير",
        "de": "Guten Morgen",
        "pt": "Bom dia",
        "zh-CN": "早上好",
        "ja": "おはよう"
    },
    "good evening": {
        "en": "Good evening",
        "es": "Buenas noches",
        "fr": "Bonsoir",
        "ar": "مساء الخير",
        "de": "Guten Abend",
        "pt": "Boa noite",
        "zh-CN": "晚上好",
        "ja": "こんばんは"
    },
    "welcome": {
        "en": "Welcome",
        "es": "Bienvenido",
        "fr": "Bienvenue",
        "ar": "أهلا وسهلا",
        "de": "Willkommen",
        "pt": "Bem-vindo",
        "zh-CN": "欢迎",
        "ja": "ようこそ"
    },
    "please": {
        "en": "Please",
        "es": "Por favor",
        "fr": "S'il vous plaît",
        "ar": "من فضلك",
        "de": "Bitte",
        "pt": "Por favor",
        "zh-CN": "请",
        "ja": "お願いします"
    },
    "yes": {
        "en": "Yes",
        "es": "Sí",
        "fr": "Oui",
        "ar": "نعم",
        "de": "Ja",
        "pt": "Sim",
        "zh-CN": "是的",
        "ja": "はい"
    },
    "no": {
        "en": "No",
        "es": "No",
        "fr": "Non",
        "ar": "لا",
        "de": "Nein",
        "pt": "Não",
        "zh-CN": "不",
        "ja": "いいえ"
    },
    "okay": {
        "en": "Okay",
        "es": "Está bien",
        "fr": "D'accord",
        "ar": "حسنا",
        "de": "Okay",
        "pt": "Tudo bem",
        "zh-CN": "好的",
        "ja": "わかりました"
    },
    "what is your name": {
        "en": "What is your name?",
        "es": "¿Cuál es tu nombre?",
        "fr": "Quel est votre nom?",
        "ar": "ما اسمك؟",
        "de": "Wie heißt du?",
        "pt": "Qual é seu nome?",
        "zh-CN": "你叫什么名字？",
        "ja": "お名前は？"
    },
    "where are you from": {
        "en": "Where are you from?",
        "es": "¿De dónde eres?",
        "fr": "D'où venez-vous?",
        "ar": "من أين أنت؟",
        "de": "Woher kommst du?",
        "pt": "De onde você é?",
        "zh-CN": "你来自哪里？",
        "ja": "どこから来ましたか？"
    },
    "do you understand": {
        "en": "Do you understand?",
        "es": "¿Entiendes?",
        "fr": "Comprenez-vous?",
        "ar": "هل تفهم؟",
        "de": "Verstehst du?",
        "pt": "Você entende?",
        "zh-CN": "你明白吗？",
        "ja": "わかりますか？"
    },
    "can you help": {
        "en": "Can you help?",
        "es": "¿Puedes ayudar?",
        "fr": "Pouvez-vous aider?",
        "ar": "هل يمكنك المساعدة؟",
        "de": "Kannst du helfen?",
        "pt": "Você pode ajudar?",
        "zh-CN": "你能帮忙吗？",
        "ja": "手伝ってくれますか？"
    },
    "i am happy": {
        "en": "I am happy",
        "es": "Estoy feliz",
        "fr": "Je suis heureux",
        "ar": "أنا سعيد",
        "de": "Ich bin glücklich",
        "pt": "Estou feliz",
        "zh-CN": "我很高兴",
        "ja": "私は幸せです"
    },
    "i am sad": {
        "en": "I am sad",
        "es": "Estoy triste",
        "fr": "Je suis triste",
        "ar": "أنا حزين",
        "de": "Ich bin traurig",
        "pt": "Estou triste",
        "zh-CN": "我很伤心",
        "ja": "私は悲しいです"
    },
    "i am tired": {
        "en": "I am tired",
        "es": "Estoy cansado",
        "fr": "Je suis fatigué",
        "ar": "أنا متعب",
        "de": "Ich bin müde",
        "pt": "Estou cansado",
        "zh-CN": "我很累",
        "ja": "疲れています"
    },
    "i love you": {
        "en": "I love you",
        "es": "Te amo",
        "fr": "Je t'aime",
        "ar": "أنا أحبك",
        "de": "Ich liebe dich",
        "pt": "Eu te amo",
        "zh-CN": "我爱你",
        "ja": "愛しています"
    },
    "wait": {
        "en": "Wait",
        "es": "Espera",
        "fr": "Attends",
        "ar": "انتظر",
        "de": "Warte",
        "pt": "Espere",
        "zh-CN": "等等",
        "ja": "待って"
    },
    "stop": {
        "en": "Stop",
        "es": "Para",
        "fr": "Arrête",
        "ar": "قف",
        "de": "Stopp",
        "pt": "Pare",
        "zh-CN": "停止",
        "ja": "止まって"
    },
    "go": {
        "en": "Go",
        "es": "Vete",
        "fr": "Allez",
        "ar": "اذهب",
        "de": "Geh",
        "pt": "Vá",
        "zh-CN": "去吧",
        "ja": "行って"
    },
    "come here": {
        "en": "Come here",
        "es": "Ven aquí",
        "fr": "Viens ici",
        "ar": "تعال هنا",
        "de": "Komm her",
        "pt": "Venha aqui",
        "zh-CN": "过来",
        "ja": "ここに来て"
    },
    "sit down": {
        "en": "Sit down",
        "es": "Siéntate",
        "fr": "Assieds-toi",
        "ar": "اجلس",
        "de": "Setz dich hin",
        "pt": "Sente-se",
        "zh-CN": "坐下",
        "ja": "座ってください"
    }
}

def setup_system():
    """Complete system setup and enhancement."""
    print("=" * 70)
    print("OmniSign System - Complete Enhancement Setup")
    print("=" * 70)
    print()
    
    # Step 1: Create data directories
    print("[1/4] Creating data directories for all signs...")
    data_path = Path("Sign_Language_Data")
    
    for sign_name in EXPANDED_SIGNS.keys():
        # Create display name with proper capitalization
        display_name = sign_name.replace("_", " ").title()
        for i in range(30):
            dir_path = data_path / display_name / str(i)
            dir_path.mkdir(parents=True, exist_ok=True)
    
    print(f"    ✓ Created directories for {len(EXPANDED_SIGNS)} signs")
    print()
    
    # Step 2: Save translation mappings
    print("[2/4] Saving translation mappings...")
    labels_path = data_path / "labels.json"
    
    with open(labels_path, 'w', encoding='utf-8') as f:
        json.dump(EXPANDED_SIGNS, f, ensure_ascii=False, indent=2)
    
    print(f"    ✓ Saved to {labels_path}")
    print()
    
    # Step 3: Create system statistics
    print("[3/4] System statistics...")
    total_signs = len(EXPANDED_SIGNS)
    languages = list(EXPANDED_SIGNS[list(EXPANDED_SIGNS.keys())[0]].keys())
    total_translations = total_signs * len(languages)
    
    print(f"    ✓ Total signs: {total_signs}")
    print(f"    ✓ Languages: {len(languages)} ({', '.join(languages)})")
    print(f"    ✓ Total translations: {total_translations}")
    print(f"    ✓ Data capacity: {total_signs} × 30 sequences × 30 frames = {total_signs * 900:,} frames")
    print()
    
    # Step 4: Validation
    print("[4/4] Validating setup...")
    issues = []
    
    for sign_name in EXPANDED_SIGNS.keys():
        display_name = sign_name.replace("_", " ").title()
        sign_path = data_path / display_name
        if not sign_path.exists():
            issues.append(f"Missing directory: {display_name}")
    
    if issues:
        print(f"    ⚠ Found {len(issues)} issues:")
        for issue in issues:
            print(f"      - {issue}")
    else:
        print("    ✓ All validations passed!")
    
    print()
    print("=" * 70)
    print("Setup Complete! Ready to collect data.")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Run: python collect_data.py")
    print("2. Perform each sign 30 times (30 sequences × 30 frames each)")
    print("3. Run: python train_model.py")
    print("4. Test with: python bi_directional_demo.py")
    print()

if __name__ == "__main__":
    setup_system()
