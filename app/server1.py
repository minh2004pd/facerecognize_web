from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
import cv2
from fastapi.templating import Jinja2Templates
import numpy as np
import base64
from io import BytesIO
import torch
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Load YOLOv5 model (pre-trained on faces or custom trained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', source='github', trust_repo=True)
model.eval()

app = FastAPI()

templates = Jinja2Templates(directory="./app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_frame")
async def process_frame(request: Request):
    """Process the Base64 image frame sent from the frontend."""
    data = await request.json()
    base64_image = data.get("image")

    if not base64_image:
        return {"error": "No image provided"}

    # Decode Base64 image to raw bytes
    image_data = base64.b64decode(base64_image)
    np_image = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

    # Process the frame using YOLOv5
    results = model(frame)
    processed_frame = results.render()[0]  # Render detections on the frame

    # Encode the processed frame as JPEG
    _, buffer = cv2.imencode('.jpg', processed_frame)
    return StreamingResponse(BytesIO(buffer.tobytes()), media_type="image/jpeg")
