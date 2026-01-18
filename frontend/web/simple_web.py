"""
Simple Web Interface for AI Fitness Trainer
"""
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

def main():
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
        h1 { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: clamp(1.5rem, 4vw, 3rem);
            font-weight: 700;
            text-align: center;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }
        
        .subtitle { 
            text-align: center; 
            color: #666; 
            margin-bottom: 1.5rem;
            font-size: clamp(0.9rem, 2vw, 1.1rem);
            padding: 0 1rem;
        }
        
        /* Buttons */
        .stButton>button { 
            width: 100%; 
            border-radius: 8px; 
            font-weight: 600;
            padding: 0.6rem 1rem;
            font-size: clamp(0.85rem, 2vw, 1rem);
            transition: all 0.3s ease;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] { 
            background-color: #f8f9fa;
            padding: 1rem;
        }
        
        /* Video/Image Container */
        .stImage { border-radius: 12px; overflow: hidden; }
        
        /* Metrics */
        [data-testid="stMetricValue"] { font-size: clamp(1.2rem, 3vw, 1.8rem) !important; }
        [data-testid="stMetricLabel"] { font-size: clamp(0.8rem, 2vw, 1rem) !important; }
        
        /* Info boxes */
        .stInfo, .stSuccess, .stWarning, .stError {
            padding: 0.8rem;
            border-radius: 8px;
            font-size: clamp(0.85rem, 2vw, 0.95rem);
        }
        
        /* Mobile Responsive (< 768px) */
        @media (max-width: 768px) {
            .main { padding: 1rem 0.5rem; }
            .block-container { padding: 1rem 0.5rem; max-width: 100%; }
            h1 { font-size: 1.8rem; margin-bottom: 0.5rem; }
            .subtitle { font-size: 0.9rem; margin-bottom: 1rem; }
            section[data-testid="stSidebar"] { padding: 1rem 0.5rem; }
            .stButton>button { padding: 0.5rem 0.8rem; font-size: 0.9rem; }
            h3, h4 { font-size: 1.1rem !important; }
            [data-testid="column"] { padding: 0.25rem !important; }
        }
        
        /* Tablet Responsive (768px - 1024px) */
        @media (min-width: 768px) and (max-width: 1024px) {
            .main { padding: 1.5rem 1rem; }
            .block-container { padding: 1.5rem 1rem; max-width: 100%; }
            h1 { font-size: 2.5rem; }
            .subtitle { font-size: 1rem; }
        }
        
        /* Desktop Responsive (> 1024px) */
        @media (min-width: 1024px) {
            .block-container { max-width: 1400px; }
        }
        
        /* Touch-friendly spacing for mobile devices */
        @media (hover: none) and (pointer: coarse) {
            .stButton>button { padding: 0.8rem 1rem; min-height: 44px; }
            .stSelectbox, .stSlider { margin: 1rem 0; }
            select, input[type="range"] { min-height: 44px; }
        }
        
        /* Landscape mobile orientation */
        @media (max-width: 768px) and (orientation: landscape) {
            .main { padding: 0.5rem; }
            h1 { font-size: 1.5rem; }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🏋️ AI Fitness Trainer")
    st.markdown('<p class="subtitle">Real-time exercise form analysis using computer vision</p>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'camera_on' not in st.session_state:
        st.session_state.camera_on = False
    if 'rep_count' not in st.session_state:
        st.session_state.rep_count = 0
    
    # Sidebar with improved layout
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        st.markdown("")
        
        exercise = st.selectbox(
            "Choose Exercise",
            ["Bicep Curls", "Squats", "Push-ups", "Shoulder Press"],
            help="Select your workout exercise"
        )
        
        st.slider("Target Reps", 5, 20, 10, key="target_reps", help="Set your rep goal")
        
        st.markdown("---")
        st.markdown("### 🎬 Controls")
        st.markdown("")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Start" if not st.session_state.camera_on else "⏹️ Stop", use_container_width=True):
                st.session_state.camera_on = not st.session_state.camera_on
        with col2:
            if st.button("🔄 Reset", use_container_width=True):
                st.session_state.rep_count = 0
        
        st.markdown("---")
        st.markdown("### 📊 Stats")
        st.markdown("")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Completed", st.session_state.rep_count)
        with col_b:
            st.metric("Target", st.session_state.target_reps)
        
        # Progress bar with label
        progress = min(st.session_state.rep_count / st.session_state.target_reps, 1.0)
        st.progress(progress)
        st.caption(f"Progress: {progress*100:.0f}%")
    
    # Main area with responsive layout
    # Use single column on mobile, two columns on larger screens
    if st.session_state.get('mobile_view', False) or 'mobile' in st.get_option('browser.gatherUsageStats').lower() if hasattr(st, 'get_option') else False:
        # Mobile: Stack vertically
        st.markdown("### 📹 Live Feed")
        st.markdown("")
        
        if st.session_state.camera_on:
            # Camera code here (keeping existing logic)
            camera_placeholder = st.empty()
            cap = cv2.VideoCapture(0)
            
            if not cap.isOpened():
                st.error("❌ Could not access camera. Please check if it's being used by another application.")
            else:
                st.success("✅ Camera connected successfully!")
                
                while st.session_state.camera_on and cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to capture frame")
                        break
                    
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2.putText(frame_rgb, f"Exercise: {exercise}", (50, 50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(frame_rgb, f"Reps: {st.session_state.rep_count}", (50, 100), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame_rgb, "Placeholder - Desktop version has full AI", (50, 150), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    
                    camera_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
                    time.sleep(0.1)
                
                cap.release()
        else:
            st.info("👆 Click 'Start' to begin your workout")
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 100px 20px; border-radius: 12px; text-align: center; color: white;">
                <h2 style="margin: 0; color: white;">🎥 Camera Feed</h2>
                <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9);">Will appear here</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Form guide below camera on mobile
        st.markdown("")
        st.markdown("### 💡 Form Guide")
        st.markdown("")
        
        if exercise == "Bicep Curls":
            st.info("""
            **Bicep Curl Form:**
            
            ✓ Keep elbows close to body  
            ✓ Fully extend at bottom  
            ✓ Control the movement  
            ✓ Don't swing torso
            """)
            
            st.markdown("")
            st.markdown("#### 🔍 Form Check")
            col_a, col_b = st.columns(2)
            with col_a:
                st.success("✅ Elbow")
                st.warning("⚠️ Extension")
            with col_b:
                st.success("✅ Wrist")
                st.error("❌ Sway")
                
        elif exercise == "Squats":
            st.info("""
            **Squat Form:**
            
            ✓ Feet shoulder-width apart  
            ✓ Knees aligned with toes  
            ✓ Back straight  
            ✓ Go to parallel
            """)
        
        elif exercise == "Push-ups":
            st.info("""
            **Push-up Form:**
            
            ✓ Keep body straight  
            ✓ Elbows at 45°  
            ✓ Full range of motion  
            ✓ Engage core
            """)
            
        st.markdown("")
        st.markdown("#### 🎯 Quick Tips")
        st.markdown("""
        • Warm up before starting  
        • Maintain proper form  
        • Breathe consistently  
        • Stay hydrated
        """)
    else:
        # Desktop/Tablet: Two columns
        col1, col2 = st.columns([2.5, 1.5], gap="large")
    
    with col1:
        st.markdown("### 📹 Live Feed")
        st.markdown("")
        
        if st.session_state.camera_on:
            camera_placeholder = st.empty()
            cap = cv2.VideoCapture(0)
            
            if not cap.isOpened():
                st.error("❌ Could not access camera. Please check if it's being used by another application.")
            else:
                st.success("✅ Camera connected successfully!")
                
                while st.session_state.camera_on and cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to capture frame")
                        break
                    
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    cv2.putText(frame_rgb, f"Exercise: {exercise}", (50, 50), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.putText(frame_rgb, f"Reps: {st.session_state.rep_count}", (50, 100), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame_rgb, "Placeholder - Desktop version has full AI", (50, 150), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
                    
                    camera_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)
                    time.sleep(0.1)
                
                cap.release()
        else:
            st.info("👆 Click 'Start' to begin your workout")
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 150px 20px; border-radius: 12px; text-align: center; color: white;">
                <h2 style="margin: 0; color: white;">🎥 Camera Feed</h2>
                <p style="margin: 10px 0 0 0; color: rgba(255,255,255,0.9);">Will appear here</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💡 Form Guide")
        st.markdown("")
        
        if exercise == "Bicep Curls":
            st.info("""
            **Bicep Curl Form:**
            
            ✓ Keep elbows close to body  
            ✓ Fully extend at bottom  
            ✓ Control the movement  
            ✓ Don't swing torso
            """)
            
            st.markdown("")
            st.markdown("#### 🔍 Form Check")
            col_a, col_b = st.columns(2)
            with col_a:
                st.success("✅ Elbow")
                st.warning("⚠️ Extension")
            with col_b:
                st.success("✅ Wrist")
                st.error("❌ Sway")
                
        elif exercise == "Squats":
            st.info("""
            **Squat Form:**
            
            ✓ Feet shoulder-width apart  
            ✓ Knees aligned with toes  
            ✓ Back straight  
            ✓ Go to parallel
            """)
        
        elif exercise == "Push-ups":
            st.info("""
            **Push-up Form:**
            
            ✓ Keep body straight  
            ✓ Elbows at 45°  
            ✓ Full range of motion  
            ✓ Engage core
            """)
            
        st.markdown("")
        st.markdown("#### 🎯 Quick Tips")
        st.markdown("""
        • Warm up before starting  
        • Maintain proper form  
        • Breathe consistently  
        • Stay hydrated
        """)

if __name__ == "__main__":
    main()