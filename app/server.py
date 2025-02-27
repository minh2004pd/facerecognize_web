import torch
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from starlette.responses import StreamingResponse
from starlette.background import BackgroundTask
import cv2
import numpy as np
from io import BytesIO
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load YOLOv5 model (pre-trained on faces or custom trained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', source='github')
model.eval()

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    html_content = """
    <html>
        <head>
            <title>Webcam Face Detection</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f4f4f9;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                .container {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                video {
                    border: 4px solid #333;
                    border-radius: 8px;
                    width: 640px;
                    height: 480px;
                    margin-top: 20px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                }
                .footer {
                    margin-top: 20px;
                    color: #666;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Real-Time Webcam Face Detection</h1>
                <video id="video" autoplay></video>
                <div class="footer">Allow camera access to start face detection.</div>
            </div>
            <script>
                const video = document.getElementById('video');
                navigator.mediaDevices.getUserMedia({ video: true })
                    .then(stream => video.srcObject = stream)
                    .catch(err => console.error('Error accessing webcam:', err));
            </script>
        </body>
    </html>
    """
    return html_content

def generate_frames():
    """Capture frames from the webcam and run face detection with YOLOv5."""
    cap = cv2.VideoCapture(0)  # Open webcam (default camera)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame from BGR to RGB (since YOLOv5 expects RGB images)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform face detection using YOLOv5
        results = model(frame_rgb)  # Detect faces
        img = results.render()[0]  # Render bounding boxes on the image

        # Convert back to BGR for OpenCV to display the result (OpenCV works with BGR)
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Encode the frame to JPEG
        _, buffer = cv2.imencode('.jpg', img_bgr)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')

    cap.release()

@app.get("/video_feed")
async def video_feed():
    """Stream video feed with detected faces."""
    background_task = BackgroundTask(stop_webcam)
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame", background=background_task)

def stop_webcam():
    """Function to stop the webcam when the client disconnects."""
    cv2.VideoCapture(0).release()  # Release the webcam
