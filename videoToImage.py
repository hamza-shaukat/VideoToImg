


#2 frames per second.

import cv2
import os

def extract_frames(video_path, output_folder, frames_per_second=2):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video
    video_capture = cv2.VideoCapture(video_path)
    
    if not video_capture.isOpened():
        print("Error: Couldn't open the video file.")
        return

    # Get the frames per second (fps) of the video
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print("Error: Couldn't get the FPS of the video.")
        return

    # Calculate the interval to capture 2 frames per second
    interval = int(fps / frames_per_second)

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Save 2 frames every second
        if frame_count % interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.png")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1

        frame_count += 1

    video_capture.release()
    print(f"Extracted {saved_frame_count} frames at a rate of {frames_per_second} frames per second.")

# Example usage
video_path = 'input/1.ts'  # Ensure proper path formatting
output_folder = 'vid1'
extract_frames(video_path, output_folder, frames_per_second=2)




#pip install opencv-python
#numpy