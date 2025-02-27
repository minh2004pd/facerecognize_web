import torch
from pathlib import Path
import cv2
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Load YOLOv5 model (e.g., YOLOv5 trained for face detection)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', source='github')  # or a custom face-detection model

# Set model to evaluation mode
model.eval()

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # Perform inference
    results = model(frame)

    # Parse results (e.g., display the face bounding boxes)
    results.render()  # renders the bounding boxes on the frame

    # Display the frame with bounding boxes
    cv2.imshow('YOLO Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
