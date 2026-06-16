# AI-Powered Driver Safety Monitoring System

An AI-driven computer vision system developed to enhance driver safety during long-distance travel. Driver fatigue and drowsiness are major leading causes of road accidents, with subtle signs often going unnoticed until it becomes critical. To address this challenge, this system monitors driver alertness through visual cues in real-time and triggers an automated audio warning when signs of prolonged eye closure are detected.

## Key Value Propositions
*   **Real-Time Detection:** Continuously monitors eye states frame-by-frame to ensure immediate driver alertness tracking.
*   **Instant Audio Alert:** An audio warning is triggered instantly when drowsiness (prolonged eye closure) is detected to wake up or alert the driver.
*   **Safety First Approach:** Specifically designed to actively reduce road accidents caused by driver fatigue.
*   **Practical Visual Analytics:** Transforms simple visual camera data into practical, life-saving safety solutions.

## Methodology & Workflow

The system processing loop follows a structured 5-step pipeline as shown below:

- Camera Input (Captures real-time live video feed from the vehicle webcam)
- Face & Eye Detection (Leverages Haar Cascades to locate the face and isolate the eye region)
- Eye Monitoring (Analyzes the isolated eye state (Open vs. Closed) via OpenCV processing)
- Drowsiness Detection (Evaluates alertness levels based on prolonged eye closure conditions)
- Alarm Warning (Triggers an automated audio alert immediately to warn the driver)

## Core System Components

This lightweight and efficient architecture relies on the following core technologies:
*   **Python:** The core programming language utilized for state logic and system orchestration.
*   **OpenCV:** Powers the real-time video stream capture, frame manipulation, and UI overlays.
*   **Haar Cascades:** Chosen for fast, low-latency face and eye localization, making it ideal for real-time edge deployment.
*   **Audio Alert System:** Integrates localized sound playback mechanisms to produce instantaneous warnings.


### System States Breakdown:
1.  **EYES OPEN - NORMAL:** 
    *   *Visual indicator:* Green bounding boxes around the detected eye regions.
    *   *System Status:* **SAFE** (Eyes detected normally).
2.  **EYES CLOSED - WARNING:** 
    *   *Visual indicator:* Red bounding boxes around the face with a bold "WARNING!" text overlay.
    *   *System Status:* **WARNING - Alert Activated** (Prolonged eye closure detected).

## Environment Prerequisites

To set up and run this driver safety project on your local machine, ensure you have the required Python libraries installed:

```bash
pip install opencv-python
```
