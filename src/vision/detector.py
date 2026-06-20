#Detector
#|
#├── YOLO model
#|
#├── Model settings
#|       |
#|       ├── Model path
#|       ├── Confidence threshold
#|       └── Detection classes
#|
#└── Functions
#       |
#       └── detect(frame)


from ultralytics import YOLO

from typing import List, Dict, Any

class Detector:
    def __init__(
            self,
            model_path="models/yolov8n.pt",
            confidence_threshold: float = 0.5,
            classes: list = [0]
    ):
        self.confidence_threshold = confidence_threshold
        self.classes = classes
        self.model = YOLO(model_path)
        pass
    def detect(self, frame) -> List[Dict[str, Any]]:
        results = self.model(frame)
        result = results[0]
        detections = []
        for box in result.boxes:
            class_id = int(box.cls.item())
            confidence = float(box.conf.item())
            if confidence < self.confidence_threshold:
                continue
            if class_id not in self.classes:
                continue
            x1, y1, x2, y2 = map(
                int, 
                box.xyxy[0]
            )
            detections.append(
                {
                    "class_id": class_id,
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                }
            )
        return detections
    