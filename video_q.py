import cv2
import numpy as np
import streamlit as st
import tempfile

def calculate_blur(image):
    """ Calculate the inverse of the Laplacian variance to assess blur (larger values mean more blur). """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Avoid division by zero
    if laplacian_var == 0:
        return float('inf')  # Very high blur if variance is zero
    
    # Invert the Laplacian variance
    blur_score = 1000 / laplacian_var
    return blur_score


def calculate_motion(video_path):
    """ Calculate average motion in the video based on optical flow. """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        st.error("Error opening video file")
        return None

    ret, prev_frame = cap.read()
    if not ret:
        st.error("Failed to read the first frame")
        return None

    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    motion_values = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        curr_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, curr_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        magnitude, _ = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        avg_magnitude = np.mean(magnitude)
        motion_values.append(avg_magnitude)

        prev_gray = curr_gray

    cap.release()
    overall_motion = np.mean(motion_values)
    return overall_motion

def evaluate_video_quality(video_file, video_label):
    """ Evaluate the visual quality of the video based on resolution, blur, and motion. """
    # Write the uploaded video to a temporary file for OpenCV processing
    with tempfile.NamedTemporaryFile(delete=False) as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        st.error(f"Error opening {video_label} file")
        return None

    # Get video resolution
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    st.write(f"{video_label} Resolution: {width}x{height}")

    blur_values = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        blur = calculate_blur(frame)
        blur_values.append(blur)

    cap.release()
    overall_blur = np.mean(blur_values)
    overall_motion = calculate_motion(video_path)

    st.write(f"{video_label} Average Blur (Laplacian Variance): {overall_blur:.2f}")
    st.write(f"{video_label} Average Motion Magnitude: {overall_motion:.2f}")

# Streamlit UI
st.title("Video Quality Evaluation for Two Videos")

col1, col2 = st.columns(2)

# Video 1 Upload and Evaluation
with col1:
    st.header("Video 1")
    uploaded_file1 = st.file_uploader("Upload Video 1", type=["mp4", "avi", "mov"], key="video1")
    if uploaded_file1 is not None:
        st.video(uploaded_file1)
        evaluate_video_quality(uploaded_file1, "Video 1")

# Video 2 Upload and Evaluation
with col2:
    st.header("Video 2")
    uploaded_file2 = st.file_uploader("Upload Video 2", type=["mp4", "avi", "mov"], key="video2")
    if uploaded_file2 is not None:
        st.video(uploaded_file2)
        evaluate_video_quality(uploaded_file2, "Video 2")
