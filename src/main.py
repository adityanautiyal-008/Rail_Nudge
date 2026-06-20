# Import OpenCV for drawing and displaying video
import cv2

# Import our camera manager
from src.vision.camera_manager import CameraManager

# Import our YOLO person detector
from src.vision.detector import Detector

# Import our ByteTrack tracker
from src.vision.tracker import Tracker

# Import zone and occupancy logic
from src.occupancy.zones import Zone
from src.occupancy.counter import OccupancyCounter


def main():
    """
    Main Smart Occupancy System.

    Complete pipeline:

    Camera
       ↓
    Detector
       ↓
    Tracker
       ↓
    Zone Analysis
       ↓
    Occupancy Counter
       ↓
    Live Dashboard Display
    """

    # Initialize camera
    camera = CameraManager(source=0)

    # Initialize YOLO detector
    detector = Detector()

    # Initialize ByteTrack tracker
    tracker = Tracker()


    platform_zone = Zone(
        name="Platform",
        x1=200,
        y1=150,
        x2=900,
        y2=700
    )

    # Create occupancy counter for this zone
    counter = OccupancyCounter(platform_zone)

    # Start the main application loop
    while True:

        # Capture latest frame
        frame = camera.get_frame()

        # Stop if the camera fails
        if frame is None:
            print("Camera frame capture failed.")
            break

        
        # Detect all people in the frame using YOLO
        

        detections = detector.detect(frame)

        
        # Assign a persistent ID to each person
        # using ByteTrack
        

        tracked_people = tracker.update(detections)

        
        # Update occupancy information
       

        counter.update(tracked_people)

        
        # Draw the monitoring zone
        

        cv2.rectangle(
            frame,
            (platform_zone.x1, platform_zone.y1),
            (platform_zone.x2, platform_zone.y2),
            (255, 0, 0),
            2
        )

        # Write zone name
        cv2.putText(
            frame,
            platform_zone.name,
            (platform_zone.x1, platform_zone.y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

        
        # Draw every tracked person
        

        for person in tracked_people:

            track_id = person["track_id"]
            x1, y1, x2, y2 = person["bbox"]

            # Draw green box around person
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Display tracking ID
            cv2.putText(
                frame,
                f"ID: {track_id}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Display actual occupancy count

        cv2.putText(
            frame,
            f"Occupancy: {counter.get_count()}",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        # Show final processed frame
        cv2.imshow(
            "Smart Occupancy System",
            frame
        )

        # Exit when Q is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources properly
    camera.release()
    cv2.destroyAllWindows()


# Run only when this file is executed directly
if __name__ == "__main__":
    main()