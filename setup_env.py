#!/usr/bin/env python3
"""
Setup script to help create .env file for EduChain MCP
"""

import os
import shutil

def setup_env():
    """Create .env file from env.example if it doesn't exist"""
    
    if os.path.exists('.env'):
        print("✅ .env file already exists!")
        return
    
    if not os.path.exists('env.example'):
        print("❌ env.example file not found!")
        return
    
    try:
        shutil.copy('env.example', '.env')
        print("✅ Created .env file from env.example")
        print("📝 Please edit .env file and add your OpenRouter API key")
        print("🔒 Remember: Never commit .env file to version control!")
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

if __name__ == "__main__":
    setup_env() 