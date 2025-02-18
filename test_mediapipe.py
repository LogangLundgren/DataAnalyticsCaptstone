import cv2
import mediapipe as mp
import os

# Define video paths
input_video_path = r"C:\Users\LongboyLog\Downloads\DataAnalyticsCaptstone-main\DataAnalyticsCaptstone-main\barbell biceps curl_1.mp4"
output_video_path = "C:/Users/LongboyLog/DataAnalyticsCaptstone/processedvideos/processed_video.mp4"

# Ensure output directory exists
output_dir = os.path.dirname(output_video_path)
os.makedirs(output_dir, exist_ok=True)

# Initialize Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Open video
cap = cv2.VideoCapture(input_video_path)

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define Video Writer with proper codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' if mp4v doesn't work
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Start Mediapipe Pose detection
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video processing complete.")
            break

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process with Mediapipe
        results = pose.process(rgb_frame)

        # Draw landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Write frame to output video
        out.write(frame)

        # Show frame
        cv2.imshow("Processed Video", frame)

        # Keyboard controls
        key = cv2.waitKey(20) & 0xFF
        if key == ord('q'):  # Quit
            break
        elif key == ord('r'):  # Restart video
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {output_video_path}")
