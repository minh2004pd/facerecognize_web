# Webcam Processing with YOLOv5 & FastAPI 📸

This project demonstrates real-time webcam processing using **YOLOv5** for object detection, powered by **FastAPI** for quick deployment. The system captures the webcam feed and processes the frames to detect objects, with the output including bounding boxes and confidence scores around detected objects. It uses **Docker Compose** to simplify the setup and deployment.

## Features 🚀
- Real-time object detection using **YOLOv5** 🧠
- Process webcam frames with **FastAPI** 🖥️
- Display bounding boxes around detected objects 👁️
- Confidence scores for detected objects 📊
- Simplified setup using **Docker Compose** 🐳

## How It Works ⚙️

1. **Webcam Feed**: The webcam captures the live feed of your environment.
2. **Object Detection**: YOLOv5 processes each frame, detecting objects such as persons, animals, or other items.
3. **Processed Frame**: The detected objects are outlined with bounding boxes, and a confidence score is displayed for each detection.

![Webcam Processing](https://github.com/minh2004pd/facerecognize_web/blob/main/pic/image.png)

### Example of processed frame:
- **Original Webcam Feed** (Left) – The raw video feed from the webcam.
- **Processed Frame** (Right) – The processed video feed with detected objects, including confidence levels.

## Getting Started 🛠️

To get started with this project using **Docker Compose**, follow these steps:

### Prerequisites 📝
- **Docker** and **Docker Compose** installed on your machine. If you don't have them, you can download them from the following:
  - [Docker](https://www.docker.com/get-started)
  - [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Project with Docker Compose 🐳

1. Clone the repository:
   ```bash
   git clone https://github.com/minh2004pd/facerecognize_web.git
   cd facerecognize_web
   ```

2. Build and start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Open a browser and go to `http://127.0.0.1:8000` to see the webcam feed with live object detection.

### Stopping the Containers 🚫
To stop the services, run the following command:
```bash
docker-compose down
```

## Technologies Used 🛠️
- **FastAPI**: A modern web framework for building APIs with Python 3.6+.
- **YOLOv5**: A state-of-the-art real-time object detection model.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

## Contributing 🤝
Feel free to fork this project and contribute by opening issues or submitting pull requests!

---

For more details, visit the project on [GitHub](https://github.com/minh2004pd/facerecognize_web).
