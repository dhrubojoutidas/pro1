

**🚗 IoT-Based Accident Detection & Emergency Alert System**

_Arduino MKR WiFi 1010 • Firebase • Twilio SMS • Google Maps API_

This project is a real-time IoT accident detection and alert system that uses multiple sensors to detect emergencies and automatically notify family members or medical services. It integrates embedded hardware, cloud automation, and web visualization—making it a complete end-to-end IoT solution.


**🔥 Key Features**

 - **Accident Detection (Real-Time):**
Uses MPU6050 accelerometer + SW-420 vibration sensor to detect sudden impacts or crashes.

  * Automatic Emergency Alerts:
Sends SMS alerts instantly using Twilio API, including:

GPS coordinates of location

Accident severity

Timestamp

Temperature & gas levels (if fire risk is detected)

GPS-Based Location Tracking:
NEO-6M GPS module provides accurate latitude/longitude for rescue teams.

Cloud Integration with Firebase:

Stores real-time sensor data

Triggers Cloud Functions

Maintains accident history logs

Ensures secure HTTPS communication

Web Dashboard (Live Monitoring):
Built with HTML, CSS, JavaScript, Chart.js, showing:

Live sensor readings

Map visualization

Accident event logs

Status updates

False-Alarm Prevention:
Includes a 10-second cancel button to stop alerts if the user is safe.

Scalable Architecture:
Can be extended to ambulance notification, hospital routing, or insurance reporting.

🧩 Hardware Components

Arduino MKR WiFi 1010

MPU6050 accelerometer

SW-420 vibration sensor

MQ-2 gas sensor

MQ-3 alcohol sensor

DHT11 temperature & humidity

GPS NEO-6M module

Buzzer + OLED Display

Twilio + Firebase Cloud Services

🧠 Software/Tech Stack

Firmware: Arduino C/C++

Cloud: Firebase Firestore, Cloud Functions

APIs: Twilio SMS, Google Maps/Geocoding

Frontend: HTML, CSS, JavaScript, Chart.js

Communication: HTTP/HTTPS, JSON

📸 System Workflow

Sensors continuously monitor acceleration, vibration, alcohol level, temperature, and gas.

If an accident is detected:

System starts a 10-second safety countdown.

If not cancelled, data is pushed to Firebase.

Firebase Cloud Function triggers a Twilio SMS alert.

Dashboard displays accident location + sensor data history.

🎯 Project Outcomes

Reduced emergency response time

Accurate and reliable detection using sensor fusion

Secure cloud communication

Real-time monitoring and historic data visualization
