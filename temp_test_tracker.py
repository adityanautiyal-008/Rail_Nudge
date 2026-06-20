# Import OpenCV for webcam access, drawing boxes, and showing video
import cv2

# Import our custom Detector class
from src.vision.detector import Detector

# Import our custom Tracker class
from src.vision.tracker import Tracker


def main():
    """
    Test the complete detection and tracking pipeline.

    Flow:
    Camera
      ↓
    Detector
      ↓
    Tracker
      ↓
    Display tracked people with IDs
    """

    # Create a Detector object.
    # This loads YOLO into memory.
    detector = Detector()

    # Create a Tracker object.
    # This initializes ByteTrack.
    tracker = Tracker()

    # Open the default webcam (0 means primary camera)
    camera = cv2.VideoCapture(0)

    # Check whether the camera opened successfully
    if not camera.isOpened():
        print("Could not open camera.")
        return

    # Keep running until the user quits
    while True:

        # Read a single frame from the camera
        success, frame = camera.read()

        # If frame was not captured, exit
        if not success:
            print("Failed to capture frame.")
            break

        # Send the frame to YOLO detector
        detections = detector.detect(frame)

        # Send detections to ByteTrack
        tracked_people = tracker.update(detections)

        # Loop through every tracked person
        for person in tracked_people:

            # Get the unique tracking ID
            track_id = person["track_id"]

            # Get the person's bounding box
            x1, y1, x2, y2 = person["bbox"]

            # Get detection confidence
            confidence = person["confidence"]

            # Draw a green rectangle around the person
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Create text showing ID and confidence
            label = f"ID: {track_id} | {confidence:.2f}"

            # Draw the label above the box
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Show total number of currently tracked people
        count_text = f"People: {len(tracked_people)}"

        cv2.putText(
            frame,
            count_text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        # Display the final video frame
        cv2.imshow(
            "Smart Occupancy System - Tracker Test",
            frame
        )

        # Press Q key to quit the test
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam resource
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# This makes sure the file only runs when executed directly
if __name__ == "__main__":
    main()