import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Load the video file
video_path = r"C:\Users\LongboyLog\DataAnalyticsCaptstone\IMG_9108.mp4"  # Ensure the correct file extension (.mp4, .avi, etc.)
cap = cv2.VideoCapture(video_path)

# Performance tracking
prev_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Convert frame to RGB (MediaPipe requires RGB format)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    # Draw landmarks
    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Display FPS on the frame
    cv2.putText(frame, f"FPS: {int(fps)}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the output
    cv2.imshow("MediaPipe Pose Test - Video File", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
