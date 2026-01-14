# AI Fitness Trainer with Pose Estimation 🏋️‍♂️

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10-orange)](https://mediapipe.dev)

An intelligent fitness trainer that uses AI and computer vision to provide real-time exercise form feedback and track your workouts.

## ✨ Features

- **Real-time Pose Detection**: Accurate human pose estimation using MediaPipe
- **Exercise Form Analysis**: AI-powered analysis of exercise technique
- **Audio Feedback**: Real-time voice guidance for form corrections
- **Workout Tracking**: Comprehensive progress monitoring and history
- **Multiple Exercises**: Support for bicep curls, squats, push-ups, and more
- **User-friendly Interface**: Streamlit-based dashboard and OpenCV camera view

## 🚀 Quick Start

### Installation
## 🌐 Web Interfaces
### Professional Website
```bash
ai-fitness-trainer/
│
├── core/                      # Core AI & fitness logic
│   ├── enhanced_trainer.py
│   ├── fixed_main.py
│   └── run_fitness_trainer.py
│
├── web/                       # Web interfaces & dashboards
│   ├── web_interface.py
│   ├── simple_web.py
│   ├── launch_web.py
│   └── progress_dashboard.py
│
├── scripts/                   # Setup & automation scripts
│   ├── clean_setup.py
│   ├── create_structure.py
│   ├── create_web_files.py
│   ├── install_dependencies.py
│   ├── install_web_dependencies.py
│   ├── fix_installation.ps1
│   └── install_and_run.bat
│
├── tests/                     # Test and validation files
│   ├── simple_test.py
│   └── test_setup.py
│
├── requirements/              # Dependency files
│   ├── requirements.txt
│   └── requirements-simple.txt
│
├── run.py                     # Main entry point
├── setup.py                   # Project setup & packaging
├── README.md
├── CODE_OF_CONDUCT.md

# Launch HTML website
python web/run_website.py

# Or directly
python web/web_server.py

1. Clone the repository:
```bash
git clone https://github.com/PathakAman66/ai-fitness-trainer.git

cd ai-fitness-trainer
