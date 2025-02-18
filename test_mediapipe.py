import cv2
import mediapipe as mp

# Path to a test video from your dataset
VIDEO_PATH = r"C:\Users\LongboyLog\DataAnalyticsCaptstone\barbell biceps curl\barbell biceps curl_1.mp4"

# Initialize MediaPipe Pose Detection
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# OpenCV video capture
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Video finished or failed to load. Press 'R' to replay or 'Q' to quit.")
            break

        # Convert frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process with MediaPipe
        results = pose.process(rgb_frame)

        # Draw keypoints if detected
        if results.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

        # Show the video
        cv2.imshow("Workout Video", frame)

        # Key press events: 'R' to replay, 'Q' to quit
        key = cv2.waitKey(10) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video

    cap.release()
    cv2.destroyAllWindows()

# Run the function
play_video(VIDEO_PATH)
