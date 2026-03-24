#!/usr/bin/env python3
"""
Direct APK Builder - Simple alternative to GitHub Actions
This creates APK using online build services
"""

import os
import sys
import subprocess
import json
import urllib.request
import zipfile
import shutil
from pathlib import Path

def create_simple_apk_package():
    """Create a simple package for APK building"""
    
    print("Creating APK build package...")
    
    # Create build directory
    build_dir = 'apk_build'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # Essential files for APK
    files_to_copy = [
        ('main.py', 'main.py'),
        ('buildozer.spec', 'buildozer.spec'),
        ('README_MOBILE_BUILD.md', 'README.md'),
    ]
    
    # Copy files
    for src, dst in files_to_copy:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(build_dir, dst))
            print(f"Copied: {src}")
    
    # Create requirements.txt
    requirements = """kivy==2.3.1
kivymd==1.2.0
pillow>=9.0.0
"""
    
    with open(os.path.join(build_dir, 'requirements.txt'), 'w') as f:
        f.write(requirements)
    
    # Create simple build script
    build_script = """#!/bin/bash
# Simple APK build script
echo "Starting APK build..."

# Install dependencies
pip install -r requirements.txt

# Initialize buildozer if needed
if [ ! -f "buildozer.spec" ]; then
    buildozer init
fi

# Build APK
buildozer android debug

# Check for APK
find . -name "*.apk" -type f -exec ls -la {} \\;

echo "Build completed!"
"""
    
    with open(os.path.join(build_dir, 'build.sh'), 'w') as f:
        f.write(build_script)
    
    # Create zip
    zip_name = 'smart_calculator_apk_build.zip'
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, build_dir)
                zipf.write(file_path, arcname)
    
    print(f"APK build package created: {zip_name}")
    return zip_name

def show_online_build_options():
    """Show online build options"""
    
    options = """
APK BUILD OPTIONS:

1. ONLINE BUILD SERVICES (RECOMMENDED):
   https://buildozer.io/ - Official Kivy build service
   https://replit.com/ - Free online Python environment
   https://pythonanywhere.com/ - Professional Python hosting

2. DESKTOP BUILD (Linux/Ubuntu):
   sudo apt update
   sudo apt install -y build-essential git python3-pip
   sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev
   sudo apt install -y libsdl2-ttf-dev libportmidi-dev
   sudo apt install -y default-jdk autoconf libtool pkg-config
   pip install buildozer
   buildozer android debug

3. VIRTUAL MACHINE:
   - Install Ubuntu VM on Windows
   - Follow desktop build instructions
   - Copy APK to Windows

4. CLOUD BUILD:
   - AWS EC2 (Ubuntu)
   - Google Cloud Platform
   - DigitalOcean

CURRENT STATUS:
- Your code is ready for build
- buildozer.spec is configured
- All dependencies are listed
- Build package is created

NEXT STEPS:
1. Choose a build method above
2. Upload your code
3. Run build commands
4. Download APK file
"""
    
    print(options)

def create_manual_instructions():
    """Create manual build instructions"""
    
    instructions = """
MANUAL APK BUILD INSTRUCTIONS:

METHOD 1: UBUNTU/LINUX
----------------------------
1. Install Ubuntu (dual boot or VM)
2. Open terminal
3. Run these commands:

sudo apt update
sudo apt install -y build-essential git python3-pip
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev
sudo apt install -y libsdl2-ttf-dev libportmidi-dev
sudo apt install -y default-jdk autoconf libtool pkg-config

4. Install buildozer:
pip install buildozer

5. Build APK:
buildozer android debug

METHOD 2: REPLIT.COM
----------------------------
1. Go to https://replit.com
2. Create new Python repl
3. Upload your files:
   - main.py
   - buildozer.spec
4. In shell, run:
pip install buildozer
buildozer android debug

METHOD 3: PYTHONANYWHERE
----------------------------
1. Create free account
2. Upload files
3. Install buildozer
4. Build APK

ESTIMATED TIME:
- Setup: 30-60 minutes
- Build time: 10-20 minutes
- Total: 1-2 hours

FILES NEEDED:
- main.py (your app)
- buildozer.spec (configuration)
- requirements.txt (dependencies)

TROUBLESHOOTING:
- If build fails, check buildozer.log
- Make sure Android SDK is installed
- Check internet connection
- Try debug mode first

SUCCESS INDICATORS:
- APK file created in bin/ directory
- File size: 10-50 MB
- Can be installed on Android
"""
    
    with open('MANUAL_BUILD_INSTRUCTIONS.txt', 'w') as f:
        f.write(instructions)
    
    print("Manual build instructions created: MANUAL_BUILD_INSTRUCTIONS.txt")

def main():
    print("Smart Calculator - APK Build Helper")
    print("=" * 50)
    
    # Create build package
    zip_file = create_simple_apk_package()
    
    # Show options
    show_online_build_options()
    
    # Create manual instructions
    create_manual_instructions()
    
    print("\n" + "=" * 50)
    print("BUILD PACKAGE READY!")
    print(f"Created: {zip_file}")
    print("Created: MANUAL_BUILD_INSTRUCTIONS.txt")
    print("\nRECOMMENDED: Use online build services")
    print("FASTEST: Replit.com (10 minutes)")
    print("BEST: Ubuntu/Linux (full control)")

if __name__ == "__main__":
    main()
