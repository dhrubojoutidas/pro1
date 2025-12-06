# 📘 CMPE3002 – Computer Technology Project 1 (CTP1)
### Curtin University | Semester 2, 2025



---

# 🚗 IoT-Based Accident Detection & Emergency Alert System

**Arduino MKR WiFi 1010 • Firebase • Twilio SMS • Google Maps API**

## 🚀 **Project Overview**


This project is a real-time **IoT Accident Detection & Emergency Alert System** that uses multiple sensors to detect crashes and automatically notify family members or emergency services. It integrates **embedded hardware, cloud automation, and web visualization**, making it a complete end-to-end IoT solution.

---




## 🔥 **Key Features**
- ✅ **Accident Detection (Real-Time):** Detects sudden impacts using MPU6050 accelerometer & SW-420 vibration sensor.
- ✅ **Automatic Emergency Alerts:** Sends SMS via Twilio API with:
  - GPS coordinates
  - Severity level
  - Timestamp
  - Temperature & gas levels
- ✅ **GPS-Based Location Tracking:** Accurate latitude/longitude using NEO-6M GPS.
- ✅ **Cloud Integration (Firebase):**
  - Stores sensor data
  - Triggers Cloud Functions
  - Maintains accident history logs.
  - Ensures secure HTTPS communication
- ✅ **Web Dashboard:**
  - Live sensor readings
  - Built with HTML, CSS, JavaScript, Chart.js
  - Displays live sensor readings
  - Map visualization
  - Accident event logs and status updates
- ✅ **False-Alarm Prevention:** 10-second cancel button.
- ✅ **Scalable Architecture:**  Easily extendable to ambulance notification, hospital routing, or insurance reporting..


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

---



##  🛠 Tools, Technologies & Methods

- **Firmware:** Arduino C/C++   
- **Cloud:** Firebase Firestore /  Cloud Functions  
- **APIs:** Twilio SMS /  Google Maps / Geocoding  
- **Frontend:** HTML /  CSS /  JavaScript /  Chart.js  
- **Communication:**  HTTP /HTTPS / JSON  
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

## 🎯 **Project Outcomes**

- ✅ Reduced emergency response time  
- ✅ Accurate detection using sensor fusion  
- ✅ Secure cloud communication  
- ✅ Real-time monitoring & historical data visualization  


---

---
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

## 📅 **Timeline**

- Week 5 – Progress Video 1  
- Week 10 – Progress Video 2  
- Week 13 – Final Video + Report  

---








---










