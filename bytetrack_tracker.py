from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def track_people(frame):
    results = model.track(
        frame,
        persist=True,
        classes=[0],   # person class only
        tracker="bytetrack.yaml"
    )

    people_count = 0

    if results[0].boxes is not None:
        people_count = len(results[0].boxes)

        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

    return frame, people_count
