# Arm Alarm

A computer vision system that monitors sleep positions in real time and alerts when the arm is in a nerve-compressing pose — targeting the prolonged compression that causes repetitive nerve injuries.

An IR camera on a Raspberry Pi captures video during sleep. A custom-trained object detection model runs on-device and triggers a phone alert when a risky position is detected.

## How It Works

```
IR Camera → Frame Capture → TFLite Inference → Classifier → Phone Alert
```

1. **Capture** — Pi IR camera records continuously at night
2. **Inference** — Lightweight YOLOv8 model (converted to TFLite) detects arm position on-device
3. **Classify** — Heuristics determine if the pose poses a compression risk
4. **Alert** — Notification sent to phone to wake the sleeper

## Hardware

| Component | Details |
|-----------|---------|
| Raspberry Pi 5 | 8 GB RAM |
| IR Camera | 120° wide-angle, Pi-compatible |

## Project Structure

```
src/
  main.py          # Entry point — orchestrates capture/inference loop
  capture.py       # Pi camera interface
  inference.py     # TFLite model runner
  classifier.py    # Pose risk classification logic
  alert.py         # Phone notification trigger
training/          # Model training pipeline
config.yaml        # Runtime configuration
```

## Setup

### On the Raspberry Pi

```bash
pip install -r requirements-pi.txt
python src/main.py
```

### Training (development machine)

```bash
pip install -r requirements-training.txt
```

The training pipeline uses [Label Studio](https://labelstud.io/) for annotation and [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) for training. The trained model is exported to TFLite for deployment on the Pi.

## Model Pipeline

1. Collect frames of sleep positions with the IR camera
2. Annotate in Label Studio
3. Train YOLOv8 on the labeled dataset
4. Export to TFLite (`float16` quantized for Pi performance)
5. Drop the `.tflite` file into the config path and run
