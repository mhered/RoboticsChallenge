import cv2
import os
import sys

def resize_with_aspect_ratio(image, max_size=640):
    """Resizes the image while maintaining aspect ratio, ensuring the largest dimension is max_size."""
    height, width = image.shape[:2]
    
    # Determine scale factor
    if width > height:
        scale = max_size / width
    else:
        scale = max_size / height

    new_width = int(width * scale)
    new_height = int(height * scale)
    
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

def create_video_thumbnail(video_path, output_path, max_size=640):
    """Creates a thumbnail from the middle frame of a video, resizing it while maintaining aspect ratio."""
    if not os.path.exists(video_path):
        print(f"Error: Video file '{video_path}' not found.")
        return
    
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open {video_path}")
        return
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames // 2)  # Seek to the middle
    ret, frame = cap.read()

    if not ret:
        print(f"Error: Could not read frame from {video_path}")
        cap.release()
        return

    # Resize while maintaining aspect ratio
    thumbnail = resize_with_aspect_ratio(frame, max_size)

    # Save the thumbnail
    cv2.imwrite(output_path, thumbnail)
    cap.release()

    print(f"Thumbnail saved: {output_path}")


if __name__ == "__main__":
    # Ensure a day number is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python generate_thumbnail.py <day_number>")
        print("Example: python generate_thumbnail.py 05 (for Day05)")
        sys.exit(1)

    # Get the day number from command line arguments
    day_number = sys.argv[1].zfill(2)  # Ensure it's zero-padded (e.g., "5" -> "05")
    day_str = f"Day{day_number}"

    video_path = os.path.join(".",day_str,"assets", f"{day_str}.mp4")
    thumbnail_path = os.path.join(".",day_str,"assets", "thumbnail.jpg")

    print(f"Processing {video_path}...")
    if os.path.exists(video_path):
        create_video_thumbnail(video_path, thumbnail_path)
    else:
        print(f"No video found for {day_str}, skipping...")

    print("Processing complete.")


