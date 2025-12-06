


# 📘 CMPE3002 – Computer Technology Project 1 (CTP1)
### Curtin University | Semester 2, 2025


---


# 🚀 Project Title
---

# 🚗 IoT-Based Accident Detection & Emergency Alert System

**Arduino MKR WiFi 1010 • Firebase • Twilio SMS • Google Maps API**

This project is a real-time IoT accident detection and alert system that uses multiple sensors to detect emergencies and automatically notify family members or medical services. It integrates embedded hardware, cloud automation, and web visualization—making it a complete end-to-end IoT solution.



---





## 🔥 Key Features

- **Accident Detection (Real-Time):**  
  Detects sudden impacts or crashes using MPU6050 accelerometer and SW-420 vibration sensor.

- **Automatic Emergency Alerts:**  
  Sends SMS alerts instantly via Twilio API, including:
  - GPS coordinates of the accident
  - Severity level
  - Timestamp
  - Temperature & gas levels (if fire risk is detected)

- **GPS-Based Location Tracking:**  
  Uses NEO-6M GPS module for accurate latitude/longitude to assist rescue teams.

- **Cloud Integration with Firebase:**
  - Stores real-time sensor data
  - Triggers Cloud Functions
  - Maintains accident history logs
  - Ensures secure HTTPS communication

- **Web Dashboard (Live Monitoring):**
  - Built with HTML, CSS, JavaScript, Chart.js
  - Displays live sensor readings
  - Map visualization
  - Accident event logs and status updates

- **False-Alarm Prevention:**  
  Includes a 10-second cancel button to stop alerts if the user is safe.

- **Scalable Architecture:**  
  Easily extendable to ambulance notification, hospital routing, or insurance reporting.

---


## 🧩 Hardware Components

- Arduino MKR WiFi 1010  
- MPU6050 accelerometer  
- SW-420 vibration sensor  
- MQ-2 gas sensor  
- MQ-3 alcohol sensor  
- DHT11 temperature & humidity sensor  
- GPS NEO-6M module  
- Buzzer + OLED Display  
- Twilio + Firebase Cloud Services  

---

## 🧠 Software / Tech Stack

- **Firmware:** Arduino C/C++  
- **Cloud:** Firebase Firestore, Cloud Functions  
- **APIs:** Twilio SMS, Google Maps/Geocoding  
- **Frontend:** HTML, CSS, JavaScript, Chart.js  
- **Communication:** HTTP/HTTPS, JSON  

---


---

# 🛠 Tools, Technologies & Methods

- Arduino / ESP32 / Microcontroller  
- Python / C / Embedded C  
- Firestore / MQTT / LoRaWAN  
- Circuit diagrams  
- Project management documentation  
- IEEE-style referencing  

---
## 📸 System Workflow

1. Sensors continuously monitor acceleration, vibration, alcohol level, temperature, and gas.
2. If an accident is detected:
   - A 10-second safety countdown begins.
   - If not cancelled, data is pushed to Firebase.
   - Firebase Cloud Function triggers a Twilio SMS alert.
   - Dashboard displays accident location and sensor data history.

---

## 🎯 Project Outcomes

- Reduced emergency response time  
- Accurate and reliable detection using sensor fusion  
- Secure cloud communication  
- Real-time monitoring and historical data visualization  

---





# 📝 Deliverables Included

### **📄 1. Progress Report**
- `/report/progress_report.pdf`

### **📊 2. Presentation Slides**
- Presentation 1 (Proposal) – *[Click to open]*  
- Presentation 2 (Design & Progress) – *[Click]*  
- Presentation 3 (Final Results) – *[Click]*  

### **🎥 3. Progress Video Links (Hosted Externally)**
- Video 1 – *[Google Drive / YouTube link]*  
- Video 2 – *[Link]*  
- Video 3 – *[Link]*  

---




# 📅 Timeline

- Week 5 – Progress  Video 1  
- Week 10 –  Progress Video 2  
- Week 13 –  Progress Video 3 + Progress Report  

---



