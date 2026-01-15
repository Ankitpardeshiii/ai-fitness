"""
Web Interface for AI Fitness Trainer
"""
import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from datetime import datetime
import time

st.set_page_config(
    page_title="AI Fitness Trainer",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Responsive CSS
st.markdown("""
<style>
    /* Global Styles */
    * { box-sizing: border-box; }
    .main { padding: 2rem 1rem; }
    .block-container { padding-top: 2rem; max-width: 1400px; margin: 0 auto; }
    
    /* Typography */
    .main-header {
        font-size: clamp(1.5rem, 4vw, 3.5rem);
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 0 0 1rem 0;
        padding: 0.5rem 0;
        line-height: 1.2;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: clamp(0.9rem, 2vw, 1.1rem);
        margin-bottom: 1.5rem;
        padding: 0 1rem;
    }
    
    /* Cards & Containers */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    .info-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    /* Feedback Styles */
    .feedback-positive { color: #00D26A; font-weight: 600; }
    .feedback-warning { color: #FFB02E; font-weight: 600; }
    .feedback-error { color: #FF4B4B; font-weight: 600; }
    
    /* Sidebar */
    .css-1d391kg { padding: 1.5rem 1rem; }
    section[data-testid="stSidebar"] { background-color: #f8f9fa; }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        font-size: clamp(0.85rem, 2vw, 1rem);
    }
    
    /* Video Container */
    .stImage { border-radius: 12px; overflow: hidden; }
    
    /* Metrics */
    [data-testid="stMetricValue"] { font-size: clamp(1.2rem, 3vw, 1.8rem) !important; }
    [data-testid="stMetricLabel"] { font-size: clamp(0.8rem, 2vw, 1rem) !important; }
    
    /* Mobile Responsive (< 768px) */
    @media (max-width: 768px) {
        .main { padding: 1rem 0.5rem; }
        .block-container { padding: 1rem 0.5rem; max-width: 100%; }
        .main-header { font-size: 1.8rem; margin-bottom: 0.5rem; }
        .subtitle { font-size: 0.9rem; margin-bottom: 1rem; }
        .metric-card, .info-card { padding: 0.8rem; margin: 0.5rem 0; }
        section[data-testid="stSidebar"] { padding: 1rem 0.5rem; }
        .stButton>button { padding: 0.5rem 0.8rem; font-size: 0.9rem; }
        h3 { font-size: 1.2rem !important; }
    }
    
    /* Tablet Responsive (768px - 1024px) */
    @media (min-width: 768px) and (max-width: 1024px) {
        .main { padding: 1.5rem 1rem; }
        .block-container { padding: 1.5rem 1rem; max-width: 100%; }
        .main-header { font-size: 2.5rem; }
        .subtitle { font-size: 1rem; }
        .metric-card, .info-card { padding: 1.2rem; }
    }
    
    /* Desktop Responsive (> 1024px) */
    @media (min-width: 1024px) {
        .block-container { max-width: 1400px; }
    }
    
    /* Touch-friendly spacing */
    @media (hover: none) and (pointer: coarse) {
        .stButton>button { padding: 0.8rem 1rem; min-height: 44px; }
        .stSelectbox, .stSlider { margin: 1rem 0; }
    }
</style>
""", unsafe_allow_html=True)

class SimpleTrainer:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.rep_count = 0
        self.current_stage = "start"
        
    def calculate_angle(self, a, b, c):
        a, b, c = np.array(a), np.array(b), np.array(c)
        ba, bc = a - b, c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        cosine_angle = np.clip(cosine_angle, -1, 1)
        return np.degrees(np.arccos(cosine_angle))
    
    def analyze_bicep_curl(self, landmarks):
        if not landmarks: return {'rep_count': self.rep_count, 'errors': ['No pose detected']}
        
        # Get key points
        key_points = {}
        indices = {11: 'shoulder', 13: 'elbow', 15: 'wrist'}
        for idx, name in indices.items():
            if idx < len(landmarks):
                landmark = landmarks[idx]
                key_points[name] = (landmark.x, landmark.y)
        
        if len(key_points) != 3:
            return {'rep_count': self.rep_count, 'errors': ['Not all points visible']}
            
        shoulder = key_points['shoulder']
        elbow = key_points['elbow']
        wrist = key_points['wrist']
        
        angle = self.calculate_angle(shoulder, elbow, wrist)
        
        # Rep counting
        if self.current_stage == "start" and angle < 80:
            self.current_stage = "up"
        elif self.current_stage == "up" and angle > 160:
            self.current_stage = "down"
            self.rep_count += 1
        elif self.current_stage == "down" and angle < 80:
            self.current_stage = "up"
            
        errors = []
        if abs(elbow[0] - shoulder[0]) > 0.15:
            errors.append("Keep elbow close to body")
            
        return {
            'rep_count': self.rep_count,
            'angle': angle,
            'stage': self.current_stage,
            'errors': errors
        }

def main():
    st.markdown('<h1 class="main-header">🏋️ AI Fitness Trainer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Real-time exercise form analysis with AI-powered feedback</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### ⚙️ Workout Settings")
        st.markdown("")
        exercise = st.selectbox("Select Exercise", ["Bicep Curls", "Squats", "Push-ups"], help="Choose your exercise")
        target_reps = st.slider("Target Reps", 5, 20, 10, help="Set your rep goal")
        
        st.markdown("---")
        st.markdown("### 📹 Camera Controls")
        st.markdown("")
        col_a, col_b = st.columns(2)
        with col_a:
            start_camera = st.button("▶️ Start", use_container_width=True)
        with col_b:
            stop_camera = st.button("⏹️ Stop", use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📊 Session Stats")
        st.markdown("")
        if 'rep_count' not in st.session_state:
            st.session_state.rep_count = 0
        if 'session_start' not in st.session_state:
            st.session_state.session_start = datetime.now()
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current", st.session_state.rep_count, delta=None)
        with col2:
            st.metric("Target", target_reps, delta=None)
        
    # Main area with responsive layout
    # Streamlit automatically handles column stacking on mobile
    col1, col2 = st.columns([2.5, 1.5], gap="medium")
    
    with col1:
        st.markdown("### 📹 Live Camera Feed")
        st.markdown("")
        
        if start_camera:
            # Initialize camera
            cap = cv2.VideoCapture(0)
            trainer = SimpleTrainer()
            
            # Create placeholder for video
            video_placeholder = st.empty()
            feedback_placeholder = st.empty()
            
            while cap.isOpened() and not stop_camera:
                ret, frame = cap.read()
                if not ret:
                    break
                    
                # Process frame
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = trainer.pose.process(image_rgb)
                
                if results.pose_landmarks:
                    # Draw landmarks
                    mp.solutions.drawing_utils.draw_landmarks(
                        frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
                    
                    # Analyze exercise
                    analysis = trainer.analyze_bicep_curl(results.pose_landmarks.landmark)
                    st.session_state.rep_count = analysis['rep_count']
                    
                    # Add overlay
                    cv2.putText(frame, f"Reps: {analysis['rep_count']}", (50, 50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f"Stage: {analysis['stage']}", (50, 80), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    cv2.putText(frame, f"Angle: {analysis.get('angle', 0):.1f}°", (50, 110), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                
                # Display frame
                video_placeholder.image(frame, channels="BGR", use_column_width=True)
                
                # Display feedback
                with feedback_placeholder.container():
                    if analysis.get('errors'):
                        for error in analysis['errors']:
                            st.error(f"⚠️ {error}")
                    if analysis['rep_count'] > 0:
                        st.success(f"🎉 {analysis['rep_count']} reps completed!")
                        
                time.sleep(0.1)
                
            cap.release()
            
    with col2:
        st.markdown("### 📈 Workout Analytics")
        st.markdown("")
        
        # Progress with better styling
        progress = min(st.session_state.rep_count / target_reps, 1.0)
        st.progress(progress)
        st.metric("Completion", f"{progress*100:.1f}%", delta=f"{st.session_state.rep_count}/{target_reps} reps")
        
        st.markdown("")
        
        # Form tips with better formatting
        st.markdown("### 💡 Form Guide")
        if exercise == "Bicep Curls":
            st.info("""
            **Bicep Curl Tips:**
            
            ✓ Keep elbows close to body  
            ✓ Fully extend arms at bottom  
            ✓ Control the movement  
            ✓ Avoid swinging torso
            """)
        elif exercise == "Squats":
            st.info("""
            **Squat Tips:**
            
            ✓ Knees aligned with feet  
            ✓ Maintain straight back  
            ✓ Go parallel to floor  
            ✓ Push through heels
            """)
        elif exercise == "Push-ups":
            st.info("""
            **Push-up Tips:**
            
            ✓ Keep body straight  
            ✓ Elbows at 45° angle  
            ✓ Full range of motion  
            ✓ Engage core muscles
            """)
        
        st.markdown("")
        
        # Session summary with better layout
        st.markdown("### ⏱️ Session Summary")
        duration = datetime.now() - st.session_state.session_start
        col_x, col_y = st.columns(2)
        with col_x:
            st.metric("Duration", f"{duration.seconds // 60}m {duration.seconds % 60}s")
        with col_y:
            st.metric("Reps/Min", f"{st.session_state.rep_count / max(duration.seconds / 60, 1):.1f}")

if __name__ == "__main__":
    main()