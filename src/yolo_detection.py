# System Design
'''
            1. Import libraries

            2. Load YOLO model

            3. Start camera

            4. Read each frame

            5. Send frame to YOLO

            6. Get detections

            7. Keep only people

            8. Draw rectangles

            9. Display person count

            10. Exit safely
'''


# Import OpenCV library
# It is used for:
# - accessing the webcam
# - handeling images (frames)
# - drawing rectangles and text
# - displaying the video window
import cv2


#import the YOLO class from the Ultralytics library
from ultralytics import  YOLO
#this line loads the AI model into memory.
model = YOLO("yolov8n.pt")

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("camera could not be opened")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        result = model(frame)
        result = result[0]
        boxes = result.boxes
        person_count = 0

        for box in boxes:
            class_id = int(box.cls.item())
            confidence = box.conf.item()
            coordinates = box.xyxy[0].tolist()
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            x2 = int(coordinates[2])
            y2 = int(coordinates[3])

            #check whether the detected object is a person.  HEHEHE!!!😝
            if class_id == 0:
                #increase the person counter by 1
                person_count += 1
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                label = f"Person {confidence:.2f}"
                #draw the label above the rectangle.
                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )
        cv2.putText(
            frame,
            f"Occupancy: {person_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )
        cv2.imshow(
            "Smart Occupancy System",
            frame
        )
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
