

## REAL-TIME COACH OCCUPANCY & CROWD-SAFETY INTELLIGENCE SYSTEM


> RailSense turns existing door cameras into a real-time occupancy sensor that tells passengers
> which coach to move to, alerts TTEs to ticketless clusters, and does it all with **zero new
> track hardware** and **zero face data**.

---

## 📌 The Problem

Indian Railways has **no real-time, coach-by-coach data** on how full each coach is. The result:

- Coach **B2 jammed at 150%** — people falling from doors — while **B6 on the same train is half empty.** Nobody tells passengers to move.
- **Ticketless travel goes undetected** — a coach overflows but only 60% of seats were sold.
- **Every crowd decision is a guess** — there is no live information to act on.

> If you can't measure how full a coach is, you can't fix overcrowding. RailSense measures it.

---

## ✅ The Solution

Three layers, with a single hero path: **Camera → Count → "Move to Coach B6."**

1. **Smart Occupancy Sensing** — existing door CCTV + edge AI count people IN/OUT per coach.
2. **The Brain** — live occupancy % aggregated into a train/station dashboard.
3. **Actionable Alerts** — redistribute passengers, flag ticketless clusters, inform control rooms.

---

## 🧠 How It Works
Door CCTV → YOLO (detect) + ByteTrack (track) → IN/OUT line-crossing → Occupancy % (with capacity cap + drift correction) → MQTT tiny alert ("B2:150") → Passenger display + TTE app


- **Detection + Tracking:** YOLO + ByteTrack count net occupancy without double-counting.
- **Privacy by design:** bounding boxes only — **no faces, no identity.** Only numbers are transmitted.
- **Built for bad train internet:** MQTT sends tiny text payloads, not video.

---

## ✨ Key Features

| Feature | What it does |
| --- | --- |
| 🎯 Real-time occupancy | Live % per coach from door counting |
| 🚶 Passenger redistribution | "Coach B2 150% → move to Coach B6 (40%)" |
| 🎫 Ticketless detection | Occupancy vs tickets sold → "inspect this coach" |
| 🔒 Privacy-first | No faces, edge-only processing, numbers-only transport |

---

## 🛠️ Tech Stack

| Tool | Role |
| --- | --- |
| Python | Core logic |
| OpenCV + YOLO + ByteTrack | Detection & tracking ("the digital eyes") |
| MQTT | Lightweight real-time alerts over weak networks |
| Flutter | TTE app + passenger display |
| Edge AI (Jetson / Coral) | On-coach, offline, private processing |

---
