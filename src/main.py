# Import OpenCV for drawing text, rectangles, and displaying video
import cv2

# Import our camera management system
from src.vision.camera_manager import CameraManager

# Import our YOLO person detector
from src.vision.detector import Detector

# Import our ByteTrack-based tracker
from src.vision.tracker import Tracker


def main():
    """
    Main application function.

    This function connects all components of the
    Smart Occupancy System.

    Pipeline:

    Camera
       ↓
    Detector
       ↓
    Tracker
       ↓
    Display
    """

    # Initialize the camera system
    camera = CameraManager(source=0)

    # Initialize the YOLO detector
    detector = Detector()

    # Initialize the person tracker
    tracker = Tracker()

    # Main application loop
    while True:

        # Get the latest frame from the camera
        frame = camera.get_frame()

        # If the camera fails to provide a frame,
        # stop the application safely
        if frame is None:
            print("Camera frame could not be captured.")
            break

        # Send the frame to YOLO for person detection
        detections = detector.detect(frame)

        # Send the detections to ByteTrack
        # which will assign persistent IDs
        tracked_people = tracker.update(detections)

        # Loop through every tracked person
        for person in tracked_people:

            # Extract the person's unique ID
            track_id = person["track_id"]

            # Extract the person's bounding box
            x1, y1, x2, y2 = person["bbox"]

            # Extract the confidence score
            confidence = person["confidence"]

            # Draw a green rectangle around the person
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Create the label text
            label = f"ID: {track_id} | {confidence:.2f}"

            # Draw the ID and confidence above the person
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Display the current number of tracked people
        people_count = len(tracked_people)

        cv2.putText(
            frame,
            f"People Count: {people_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        # Show the final processed video frame
        cv2.imshow(
            "Smart Occupancy System",
            frame
        )

        # Press Q to close the application
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the camera resource
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# This ensures the program starts only when this file
# is executed directly
if __name__ == "__main__":
    main()