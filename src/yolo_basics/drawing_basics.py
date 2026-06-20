import cv2 

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("camera is not accessible")
        return 
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("failed to grab frame")
            break

        #drawing on the live video 

        #line
        cv2.line(frame, (50, 50), (400, 50), (0, 255, 0), 2)
        #draw rectangle
        cv2.rectangle(frame, (100, 100), (300, 300), (255, 0, 0), 3)
        #put text on the frame
        cv2.putText(
            frame, "Smart Occupancy System",
            (50, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2   
        )
        cv2.imshow("live Drawing", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
