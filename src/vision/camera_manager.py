# Import OpenCV to communicate with cameras
import cv2


class CameraManager:
    """
    Handles camera connections and frame capture.

    This class hides all OpenCV camera operations from
    the rest of the Smart Occupancy System.
    """

    def __init__(self, source=0):
        """
        Initialize the camera manager.

        Parameters:
            source:
                The camera source.

                0 = default webcam
                video file path = recorded video
                RTSP URL = CCTV stream
        """

        # Save the source for future reference
        self.source = source

        # Create the OpenCV camera object
        self.camera = cv2.VideoCapture(self.source)

        # Verify the camera opened successfully
        if not self.camera.isOpened():
            raise Exception(
                f"Could not open camera source: {self.source}"
            )

    def get_frame(self):
        """
        Capture one frame from the camera.

        Returns:
            frame:
                The latest image from the camera.

            None:
                If the frame could not be captured.
        """

        # Ask the camera for the next frame
        success, frame = self.camera.read()

        # If reading fails, return nothing
        if not success:
            return None

        # Return the captured image
        return frame

    def release(self):
        """
        Safely close the camera connection.
        """

        # Release the OpenCV camera resource
        self.camera.release()