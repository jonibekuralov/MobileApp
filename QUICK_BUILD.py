#!/usr/bin/env python3
"""
Quick APK Builder - Online Build Script
This script helps build APK using online services
"""

import os
import sys
import subprocess
import json
import urllib.request
import zipfile
import shutil

def create_build_package():
    """Create a zip package for online build"""
    
    # Files to include
    files_to_include = [
        'main.py',
        'buildozer.spec',
        'README_MOBILE_BUILD.md',
        'DEPLOYMENT_GUIDE.md'
    ]
    
    # Create build directory
    build_dir = 'build_package'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # Copy files
    for file in files_to_include:
        if os.path.exists(file):
            shutil.copy2(file, build_dir)
            print(f"Copied: {file}")
    
    # Create zip
    zip_name = 'smart_calculator_build.zip'
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, dirs, files in os.walk(build_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, build_dir)
                zipf.write(file_path, arcname)
    
    print(f"Build package created: {zip_name}")
    return zip_name

def show_build_instructions():
    """Show instructions for different build methods"""
    
    instructions = """
SMART CALCULATOR - BUILD INSTRUCTIONS

ANDROID APK BUILD METHODS:

1. GITHUB ACTIONS (RECOMMENDED):
   - Upload to GitHub
   - Actions will build automatically
   - Download APK from Releases

2. ONLINE BUILD SERVICES:
   - https://buildozer.io/
   - https://replit.com/
   - https://pythonanywhere.com/

3. LOCAL BUILD (Linux/Ubuntu):
   sudo apt install buildozer
   buildozer android debug

iOS BUILD METHODS:

1. MACOS + XCODE:
   - Install Xcode
   - Use kivy-ios toolchain

2. ONLINE BUILD:
   - GitHub Actions (macOS runner)
   - Cloud build services

3. APP STORE:
   - Use Apple Developer account
   - Submit through App Store Connect

FILES READY:
- main.py - Main application
- buildozer.spec - Build configuration
- GitHub Actions - Automated builds
- Documentation - Complete guides

NEXT STEPS:
1. Upload to GitHub
2. Wait for automatic build
3. Download APK/IPA files
4. Install on devices

SUPPORT:
- GitHub Issues
- Documentation files
- Community forums
"""
    
    print(instructions)

def create_demo_apk_info():
    """Create demo APK information file"""
    
    apk_info = {
        "app_name": "Smart Calculator",
        "package_name": "org.uzbekdev.smartcalculator",
        "version": "1.0",
        "platforms": ["Android", "iOS"],
        "build_status": "Ready for build",
        "features": [
            "Material Design UI",
            "Full calculator functions",
            "Mobile-optimized interface",
            "Uzbek language support"
        ],
        "requirements": {
            "android": "5.0+",
            "ios": "12.0+",
            "python": "3.7+"
        },
        "build_methods": [
            "GitHub Actions",
            "Buildozer",
            "Online build services"
        ]
    }
    
    with open('apk_info.json', 'w') as f:
        json.dump(apk_info, f, indent=2)
    
    print("APK info created: apk_info.json")

def main():
    print("Smart Calculator - Quick Build Tool")
    print("=" * 50)
    
    # Create build package
    zip_file = create_build_package()
    
    # Show instructions
    show_build_instructions()
    
    # Create demo info
    create_demo_apk_info()
    
    print("\nBuild package ready!")
    print("Upload to GitHub for automatic APK build")
    print("Or use online build services")

if __name__ == "__main__":
    main()
