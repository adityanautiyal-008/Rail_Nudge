import cv2

from bytetrack_tracker import track_people
from mqtt_publisher import publish_occupancy
from occupancy_counter import calculate_occupancy

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame, people = track_people(frame)

    occupancy = calculate_occupancy(people)

    publish_occupancy(
        "B2",
        occupancy
    )

    cv2.putText(
        frame,
        f"Occupancy: {occupancy}%",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow(
        "Rail Nudge",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
