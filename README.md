# Video Quality Evaluation App

This README provides instructions for the `Video Quality Evaluation` app, which uses OpenCV, NumPy, and Streamlit to assess the visual quality of two uploaded videos. The app evaluates video quality based on **resolution**, **blur**, and **motion**.

## Features

1. **Resolution Detection**: The app determines the resolution (width x height) of the uploaded videos.
2. **Blur Calculation**: The app uses the Laplacian variance method to evaluate the amount of blur in each video frame.
3. **Motion Calculation**: The app uses optical flow to calculate average motion between frames in the video.

## Setup Instructions

### Prerequisites
You need to have the following libraries installed in your Python environment:

- `opencv-python`
- `numpy`
- `streamlit`

You can install them using pip:

```bash
pip install opencv-python numpy streamlit
```

### Running the App

1. Save the provided Python script (`app.py`).
2. Open a terminal and navigate to the directory where the script is saved.
3. Run the app using Streamlit:

```bash
streamlit run app.py
```

4. Your default web browser should automatically open the app interface. If it doesn’t, visit `http://localhost:8501` in your browser.

### How the App Works

1. **Uploading Videos**: The app allows users to upload two videos side by side for evaluation. Supported video formats include `.mp4`, `.avi`, and `.mov`.
   
2. **Blur Calculation**: For each video, the app computes the blur using the inverse of Laplacian variance. Higher values indicate more blur in the video.

3. **Motion Calculation**: The app calculates the average motion in the video by computing the optical flow between consecutive frames.

4. **Results**: For each video, the app displays:
   - Resolution
   - Average blur (Laplacian variance)
   - Average motion magnitude

### Code Explanation

1. **`calculate_blur(image)`**: This function calculates the inverse of the Laplacian variance to assess how blurry a frame is. The higher the value, the blurrier the frame.

2. **`calculate_motion(video_path)`**: This function uses optical flow (Farneback method) to measure the amount of motion between frames in the video.

3. **`evaluate_video_quality(video_file, video_label)`**: This function processes the uploaded video and computes its resolution, blur, and motion. It displays the results on the Streamlit UI.

4. **Streamlit UI**: The app uses Streamlit to provide an easy-to-use interface for video upload and quality evaluation.

### Example UI

Once the app is running, you will see the following layout:

- **Video 1** (on the left): Upload and evaluate the first video.
- **Video 2** (on the right): Upload and evaluate the second video.
- For each video, the app will display:
  - Video resolution (e.g., 1920x1080)
  - Average blur (e.g., 10.45)
  - Average motion magnitude (e.g., 5.32)

### Troubleshooting

- If you encounter any issues while opening videos, ensure the video format is supported (`mp4`, `avi`, `mov`).
- Check for any errors in the terminal for debugging.

### License

This project is licensed under the MIT License.
