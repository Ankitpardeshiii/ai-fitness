#!/usr/bin/env python3
"""
AI Fitness Trainer - Main Entry Point
Supports Desktop, Enhanced Desktop, Web UI, and Interactive Mode
"""

import argparse
import sys
import os
import subprocess


# -----------------------------
# Helper function to safely run scripts
# -----------------------------
def run_script(script_path: str):
    if not os.path.exists(script_path):
        print(f"❌ Error: '{script_path}' not found.")
        sys.exit(1)

    subprocess.run([sys.executable, script_path], check=True)


# -----------------------------
# Run Modes
# -----------------------------
def run_desktop_mode():
    """Run in desktop mode with OpenCV window"""
    print("🖥️  Starting AI Fitness Trainer in Desktop Mode...")
    run_script("run_fitness_trainer.py")


def run_enhanced_desktop():
    """Run enhanced desktop version"""
    print("💪 Starting Enhanced AI Fitness Trainer...")
    run_script("enhanced_trainer.py")


def run_web_mode():
    """Run web interface launcher"""
    print("🌐 Starting AI Fitness Trainer Web Interface...")
    run_script(os.path.join("web", "run_website.py"))


def run_dashboard():
    """Run progress dashboard"""
    print("📊 Opening Progress Dashboard...")
    run_script("progress_dashboard.py")


# -----------------------------
# Interactive Menu
# -----------------------------
def interactive_menu():
    print("\nAvailable Interfaces:")
    print("1. 🖥️  Desktop App (OpenCV) - Full AI Features")
    print("2. 💪 Enhanced Desktop - Advanced Analytics")
    print("3. 🌐 Web Interface - Professional Website")
    print("4. 📊 Progress Dashboard - View Your Data")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
        run_desktop_mode()
    elif choice == "2":
        run_enhanced_desktop()
    elif choice == "3":
        run_web_mode()
    elif choice == "4":
        run_dashboard()
    else:
        print("❌ Invalid choice. Exiting.")
        sys.exit(1)


# -----------------------------
# Main Entry Point
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="AI Fitness Trainer")

    parser.add_argument(
        "--mode",
        choices=["desktop", "enhanced", "web", "ui"],
        help="Run a specific interface directly"
    )

    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Launch interactive interface selection menu"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("🏋️ AI FITNESS TRAINER - Launcher")
    print("=" * 60)

    # Interactive menu has highest priority
    if args.interactive:
        interactive_menu()
        return

    # Direct mode selection
    if args.mode is None or args.mode == "desktop":
        run_desktop_mode()
    elif args.mode == "enhanced":
        run_enhanced_desktop()
    elif args.mode in ("web", "ui"):
        run_web_mode()
    else:
        print("❌ Invalid mode selected.")
        sys.exit(1)


if __name__ == "__main__":
    main()
