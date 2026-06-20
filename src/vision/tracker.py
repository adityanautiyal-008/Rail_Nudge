# Import NumPy because ByteTrack works with numerical arrays
import numpy as np

# Import the Supervision library which provides the ByteTrack implementation
import supervision as sv


class Tracker:
    """
    This class handles multi-object tracking.

    It receives detections from our Detector class,
    sends them to ByteTrack, and returns people
    with stable tracking IDs.
    """

    def __init__(self):
        """
        Create the ByteTrack tracker.

        The tracker stores information about objects
        between video frames and predicts their movement.
        """

        # Create a ByteTrack instance
        self.tracker = sv.ByteTrack()

    def update(self, detections):
        """
        Update the tracker using new detections.

        Parameters:
            detections:
                List of dictionaries received from detector.py.

        Returns:
            A list containing tracked people with IDs.
        """

        # If no people are detected, return an empty list
        if len(detections) == 0:
            return []

        # Create a list to store bounding boxes
        boxes = []

        # Create a list to store confidence scores
        confidences = []

        # Convert our detector output into arrays
        # that the Supervision ByteTrack expects
        for detection in detections:

            # Get the bounding box coordinates
            boxes.append(detection["bbox"])

            # Get the confidence score
            confidences.append(detection["confidence"])

        # Convert Python lists into NumPy arrays
        boxes = np.array(boxes)
        confidences = np.array(confidences)

        # Create class IDs array.
        # We only track persons, so every class ID is zero.
        class_ids = np.zeros(len(boxes), dtype=int)

        # Convert detections into Supervision format
        sv_detections = sv.Detections(
            xyxy=boxes,
            confidence=confidences,
            class_id=class_ids
        )

        # Send detections to ByteTrack.
        # ByteTrack will match them with previous frames
        # and assign unique IDs.
        tracked = self.tracker.update_with_detections(
            sv_detections
        )

        # This list will contain our clean tracking output
        tracked_people = []

        # Loop through every tracked person
        for i in range(len(tracked)):

            # Get the tracker ID assigned by ByteTrack
            track_id = tracked.tracker_id[i]

            # Get the updated bounding box
            bbox = tracked.xyxy[i].astype(int).tolist()

            # Get the confidence score
            confidence = float(tracked.confidence[i])

            # Store everything in our own format
            tracked_people.append(
                {
                    "track_id": int(track_id),
                    "bbox": bbox,
                    "confidence": confidence
                }
            )

        # Return the final tracked people
        return tracked_people