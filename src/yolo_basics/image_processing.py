import  cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not accessible")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        #grayscale window
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #blur
        blur = cv2.GaussianBlur(frame, (15, 15), 0)

        #edge detection
        edges = cv2.Canny(frame, 100, 200)

        #resize
        small = cv2.resize(frame, (320, 240))

        #outputs

        cv2.imshow("original", frame)
        cv2.imshow("grey", gray)
        cv2.imshow("small", small)
        cv2.imshow("edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()