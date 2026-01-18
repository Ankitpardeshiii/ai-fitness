# 🏋️‍♂️ AI Fitness Trainer with Real-Time Pose Estimation

An intelligent AI-powered fitness trainer that uses **Computer Vision**, **MediaPipe**, and **OpenCV** to analyze human exercises in real time using a webcam. It provides live feedback, repetition counting, form correction, and workout session tracking — making at-home fitness training more accessible, interactive, and accurate.

This project is built with learning, extensibility, and real-world usability in mind, making it suitable for students, beginners, and contributors interested in AI, computer vision, and fitness technology.

---

## ✨ Key Features

- 🎥 **Real-time Pose Detection** using MediaPipe (33 body landmarks)
- 📐 **Exercise Form Analysis** with angle-based posture validation  
- 🔢 **Automatic Repetition Counting** for multiple exercises
- ⏱️ **Time-based Tracking** for static exercises (e.g., plank)
- 🔥 **Calorie Estimation** and performance metrics
- 💾 **Workout Session Storage** (JSON format)
- 🖥️ **Multiple Interfaces** (Desktop OpenCV + Web Streamlit)
- 🚀 **Lightweight & CPU-friendly** (no GPU required)
- 🧩 **Extensible Exercise Modules**

### Supported Exercises

✔️ **Bicep Curls** - Elbow flexion analysis  
✔️ **Squats** - Hip/knee flexion tracking  
✔️ **Push-ups** - Chest depth measurement  
✔️ **Shoulder Press** - Vertical motion analysis  
✔️ **Lunges** - Lower body form validation  
✔️ **Plank** - Time-based core stability  

Each exercise includes dedicated form validation and real-time feedback.

---

## � What This Project Does

1. **Pose Detection** - Captures webcam video and detects human body landmarks
2. **Movement Analysis** - Analyzes exercise movements in real time using joint angles
3. **Form Validation** - Provides instant visual and textual feedback on exercise form
4. **Progress Tracking** - Counts repetitions, tracks duration, and estimates calories burned
5. **Data Persistence** - Saves workout session data for later review and analysis

---

## 👥 Who This Project Is For

- **Beginners** learning computer vision and MediaPipe
- **Students** building AI or fitness-related projects  
- **Contributors** looking for an approachable open-source project
- **Developers** exploring real-time pose-based applications
- **Fitness Enthusiasts** wanting AI-powered workout feedback

---

## 🎥 Demo & Screenshots

### � Applictation Screenshots

#### 🏠 Home Interface
![Home Page](screenshots/home.png)

#### 💪 Bicep Curls Analysis
![Bicep Curls](screenshots/bicep.png)

#### 🏋️ Squats Tracking
![Squats](screenshots/squat.png)

#### 🤸 Push-ups Monitoring
![Push-ups](screenshots/pushup.png)

> **Note:** Screenshots show the desktop interface with real-time pose detection and form analysis.

---

## 🚀 Quick Start

### **Prerequisites**
- **Python:** 3.8+ 
- **Camera:** Any 720p webcam
- **OS:** Windows / Linux / macOS

### **1. Clone the Repository**

```bash
git clone https://github.com/PathakAman66/ai-fitness-trainer.git
cd ai-fitness-trainer
```

### **2. Install Dependencies**

```bash
# Recommended installation
pip install -r Requirements/requirements-simple.txt

# Alternative manual installation
pip install mediapipe opencv-python numpy streamlit matplotlib
```

### **3. Test Your Setup**

```bash
# Quick test to verify camera and imports
python3 Test/simple_test.py
```

---

## 🏃‍♂️ Running the Application

### **Option A: Desktop Trainer (Recommended)**

```bash
# Simple trainer (bicep curls focus)
python3 Core/fixed_main.py

# Enhanced trainer (6 exercises + analytics)
python3 Core/main.py

# Main launcher with options
python3 run.py
```

### **Option B: Web Interface**

```bash
# Streamlit web interface
streamlit run Web/web_interface.py

# Alternative simple web UI
streamlit run Web/simple_web.py
```

**Access at:** `http://localhost:8501`

---

## 📊 Exercise Detection Logic

| Exercise | Detection Method | Key Measurements |
|----------|------------------|------------------|
| **Bicep Curl** | Elbow angle analysis | Shoulder → Elbow → Wrist angle |
| **Squat** | Hip/knee flexion | Hip → Knee → Ankle angle |
| **Push-up** | Chest depth tracking | Shoulder → Elbow angle + body alignment |
| **Shoulder Press** | Vertical motion | Wrist → Elbow → Shoulder movement |
| **Lunge** | Lower body form | Hip and knee angle coordination |
| **Plank** | Body alignment | Shoulder → Hip → Ankle straightness |

---

## � Current Project Structure

```text
ai-fitness-trainer/
│
├── Core/                      # Core AI & fitness logic
│   ├── main.py                 # Advanced trainer (6 exercises)
│   ├── fixed_main.py          # Simple trainer (bicep focus)
│   └── run_fitness_trainer.py # Basic exercise analysis
│
├── Web/                       # Web interfaces
│   ├── web_interface.py       # Main Streamlit app
│   ├── simple_web.py          # Basic web UI
│   ├── launch_web.py          # Web launcher
│   └── progress_dashboard.py  # Analytics dashboard
│
├── Test/                      # Testing files
│   ├── simple_test.py         # Camera & import test
│   └── test_setup.py          # Environment validation
│
├── Requirements/              # Dependencies
│   ├── requirements.txt       # Full dependencies
│   └── requirements-simple.txt # Minimal dependencies
│
├── Scripts/                   # Utility scripts
├── screenshots/               # Demo images
├── reports/                   # Workout data (auto-generated)
├── run.py                     # Main entry point
├── report_manager.py          # Data persistence
└── README.md                  # This file
```

---

## 🧪 Testing & Validation

### **Quick Environment Test**
```bash
# Test camera access and imports
python3 Test/simple_test.py
```

### **Full Application Test**
```bash
# Test simple trainer
python3 Core/fixed_main.py

# Test enhanced trainer  
python3 Core/main.py
```

### **Web Interface Test**
```bash
# Test Streamlit interface
streamlit run Web/web_interface.py
```

---

## 🔧 How It Works (Technical Overview)

### **Application Flow**
1. **Initialization** - Camera setup and pose detector creation
2. **Frame Capture** - Continuous webcam video capture
3. **Pose Detection** - MediaPipe extracts 33 body landmarks
4. **Exercise Analysis** - Calculate joint angles and movement patterns
5. **Form Validation** - Real-time feedback on exercise form
6. **Progress Tracking** - Count reps, track time, estimate calories
7. **Data Persistence** - Save workout sessions to JSON files

### **Core Components**
- **Pose Detector** - MediaPipe integration for landmark detection
- **Exercise Analyzer** - Exercise-specific logic and form validation
- **Session Manager** - Workout lifecycle and data management
- **UI Overlay** - Real-time visual feedback and metrics display
- **Report Manager** - Workout data persistence and export

---

## 🧩 Extending the System

### **Adding New Exercises**

1. **Create Exercise Logic**
   ```python
   # In Core/main.py
   def analyze_new_exercise(self, key_points):
       # Add your exercise analysis logic
       shoulder = key_points.get('right_shoulder')
       elbow = key_points.get('right_elbow')
       # Calculate angles and validate form
   ```

2. **Register Exercise**
   ```python
   # Add to EXERCISES config
   EXERCISES = {
       "new_exercise": {"name": "New Exercise", "muscle": "Target Muscle"}
   }
   ```

3. **Update UI**
   - Add exercise selection option
   - Include form guidance text
   - Update exercise switching logic

### **Improving Analytics**
- Add weekly/monthly progress aggregation
- Export workout data to CSV/Excel
- Create progress visualization dashboards
- Implement streak tracking and personal records

### **Enhancing Detection**
- Fine-tune angle thresholds for better accuracy
- Add more sophisticated form validation rules
- Implement machine learning for personalized feedback
- Add support for different body types and proportions

---

## 🤝 Contributing

We welcome contributions! Here are ways you can help:

### **Code Contributions**
- 🏋️ **New Exercise Models** - Add support for more exercises
- 🎯 **Pose Detection Improvements** - Enhance accuracy and reliability  
- 🖥️ **UI Enhancements** - Improve user interface and experience
- 📊 **Analytics Features** - Add progress tracking and insights
- 🐛 **Bug Fixes** - Fix issues and improve stability

### **Documentation**
- 📝 **API Documentation** - Document functions and classes
- 🎓 **Tutorials** - Create setup and usage guides
- 🔧 **Technical Guides** - Explain architecture and design decisions

### **Testing**
- ✅ **Unit Tests** - Add test coverage for core functions
- 🧪 **Integration Tests** - Test full workflow scenarios
- 📱 **Platform Testing** - Test on different OS and hardware

### **Getting Started**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-exercise`)
3. Make your changes and test thoroughly
4. Submit a pull request with clear description

Refer to `CONTRIBUTING.md` for detailed contribution guidelines.

---

## 📈 Project Goals & Vision

### **Current Goals**
- ✅ Make AI-powered fitness feedback accessible to everyone
- ✅ Keep codebase modular and easy to understand
- ✅ Encourage experimentation and community contributions
- ✅ Serve as foundation for advanced fitness analytics

### **Future Vision**
- 🎯 **Multi-user Support** - User profiles and personalized tracking
- 🌐 **Cloud Integration** - Online workout data synchronization  
- 📱 **Mobile App** - Smartphone camera integration
- 🤖 **AI Coaching** - Personalized workout recommendations
- 🏆 **Gamification** - Achievements, challenges, and social features

---

## 📄 License & Support

### **License**
This project is open source and available under the [MIT License](LICENSE).

### **Support**
- 📚 **Documentation** - Check this README and code comments
- 🐛 **Issues** - Report bugs via GitHub Issues
- 💬 **Discussions** - Join community discussions
- ⭐ **Star the Project** - Show support and help others discover it

### **Acknowledgments**
- **MediaPipe** - Google's pose estimation framework
- **OpenCV** - Computer vision library
- **Streamlit** - Web interface framework
- **Contributors** - Everyone who helps improve this project

---

## 🎉 Summary

The **AI Fitness Trainer** demonstrates how computer vision and real-time analysis can create practical fitness applications. It's intentionally designed to be:

- **Educational** - Learn computer vision and AI concepts
- **Practical** - Actually useful for fitness training
- **Extensible** - Easy to modify and enhance
- **Accessible** - Works with basic hardware and setup

Whether you're a student learning AI, a developer exploring computer vision, or a fitness enthusiast wanting smart workout feedback, this project provides a solid foundation to build upon.

**Get started today** - clone the repo, test your camera, and start your AI-powered fitness journey! 🚀

---

*If this project helped you, please consider giving it a ⭐ on GitHub to support development and help others discover it!*

