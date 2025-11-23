

**🚗 IoT-Based Accident Detection & Emergency Alert System**

_Arduino MKR WiFi 1010 • Firebase • Twilio SMS • Google Maps API_

This project is a real-time IoT accident detection and alert system that uses multiple sensors to detect emergencies and automatically notify family members or medical services. It integrates embedded hardware, cloud automation, and web visualization—making it a complete end-to-end IoT solution.


**🔥 Key Features**

 **- Accident**
** -  Detection (Real-Time):**
 -  Uses MPU6050 accelerometer + SW-420 vibration sensor to detect sudden impacts or crashes.

**Automatic Emergency Alerts:**
 Sends SMS alerts instantly using Twilio API, including:

GPS coordinates of location.
Accident severity.
Timestamp.
Temperature & gas levels (if fire risk is detected).
GPS-Based Location Tracking: NEO-6M GPS module provides accurate latitude/longitude for rescue teams.

**Cloud Integration with Firebase:**

1. Stores real-time sensor data.
2. Triggers Cloud Functions.
3. Maintains accident history logs.
4. Ensures secure HTTPS communication.

**Web Dashboard (Live Monitoring):**
Built with HTML, CSS, JavaScript, Chart.js, showing:

1. Live sensor readings.
2. Map visualization.
3. Accident event logs.
4. Status updates.

**False-Alarm Prevention:**

Includes a 10-second cancel button to stop alerts if the user is safe.

**Scalable Architecture:** 

Can be extended to ambulance notification, hospital routing, or insurance reporting.

**🧩 Hardware Components**

1. Arduino MKR WiFi 1010.
2. MPU6050 accelerometer.
3. SW-420 vibration sensor.
4. MQ-2 gas sensor.
5. MQ-3 alcohol sensor.
6. DHT11 temperature & humidity.
7. GPS NEO-6M module.
8. Buzzer + OLED Display.
9. Twilio + Firebase Cloud Services.

**🧠 Software/Tech Stack**

1. Firmware: Arduino C/C++.
2. Cloud: Firebase Firestore, Cloud Functions.
3. APIs: Twilio SMS, Google Maps/Geocoding.
4. Frontend: HTML, CSS, JavaScript, Chart.js.
5. Communication: HTTP/HTTPS, JSON

**📸 System Workflow**

1. Sensors continuously monitor acceleration, vibration, alcohol level, temperature, and gas.
2. If an accident is detected:

 - System starts a 10-second safety countdown.
 - If not cancelled, data is pushed to Firebase.

3. Firebase Cloud Function triggers a Twilio SMS alert.
4. Dashboard displays accident location + sensor data history.

**🎯 Project Outcomes**

1. Reduced emergency response time.
2. Accurate and reliable detection using sensor fusion.
3. Secure cloud communication.
4. Real-time monitoring and historic data visualization
