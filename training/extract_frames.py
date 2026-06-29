import cv2 as cv
import os

video_dir = 'training/data/raw'
output_dir = 'training/data/frames'
sample_rate = 20 

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(video_dir):
    if not filename.endswith('.mp4'):
        continue
    video_path = os.path.join(video_dir, filename)
    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open file")
        exit()

    total_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    print(f"Total Frames:{total_frames}")

    for frame_number in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break 
        if frame_number % sample_rate == 0:
            frame_filename = os.path.join(output_dir, f"frame_{frame_number:04d}.jpg")
            cv.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")

    cap.release()
    print(f"Finished extracting {total_frames} frames")

print("Success") 

