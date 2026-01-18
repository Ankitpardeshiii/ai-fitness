#!/usr/bin/env python3
"""
AI Fitness Trainer - Main Entry Point
Updated with proper file paths after restructuring
"""
import argparse
import sys
import os
import subprocess

def run_simple_trainer():
    """Run simple trainer (bicep curls only)"""
    print("Starting Simple AI Fitness Trainer (Bicep Curls Only)...")
    subprocess.run([sys.executable, "core/fixed_main.py"])

def run_enhanced_trainer():
    """Run enhanced trainer (6 exercises + analytics)"""
    print("Starting Enhanced AI Fitness Trainer...")
    subprocess.run([sys.executable, "core/main.py"])

def run_web_interface():
    """Run web interface"""
    print("Starting Web Interface...")
    subprocess.run([sys.executable, "../frontend/web/web_interface.py"])

def main():
    parser = argparse.ArgumentParser(description='AI Fitness Trainer')
    parser.add_argument('--mode', choices=['simple', 'enhanced', 'web'], 
                       default='enhanced', help='Run mode (default: enhanced)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🏋️ AI FITNESS TRAINER - Choose Your Interface")
    print("=" * 60)
    
    # Default to enhanced mode
    if args.mode == 'simple':
        run_simple_trainer()
    elif args.mode == 'enhanced':
        run_enhanced_trainer()
    elif args.mode == 'web':
        run_web_interface()
    else:
        # Interactive mode selection
        print("Available Interfaces:")
        print("1. 💪 Enhanced Trainer - 6 Exercises + Analytics (RECOMMENDED)")
        print("2. 🔧 Simple Trainer - Bicep Curls Only (Testing)")
        print("3. 🌐 Web Interface - Browser-based UI")
        
        choice = input("\nEnter your choice (1-3, default=1): ").strip() or "1"
        
        if choice == "1":
            run_enhanced_trainer()
        elif choice == "2":
            run_simple_trainer()
        elif choice == "3":
            run_web_interface()
        else:
            print("Invalid choice. Running enhanced trainer...")
            run_enhanced_trainer()

if __name__ == "__main__":
    main()