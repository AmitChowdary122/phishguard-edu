# PhishGuard EDU

AI-Powered Explainable Phishing Detection for Students

## Problem
Students are frequent targets of phishing attacks including fake internship offers, scholarship scams, and impersonated university login portals. Traditional tools block threats but do not educate users.

## Solution
PhishGuard EDU analyzes URLs in real-time, assigns a risk score, and provides plain-language explanations to help students understand why a link may be dangerous.

## Features
- Real-time phishing detection
- Multi-level risk classification
- Explainable AI output
- Visual risk meter
- Privacy-first local analysis
- Educational cyber safety tips

## Tech Stack
Frontend: HTML, CSS, JavaScript  
Backend: FastAPI (Python)  
Security Logic: Feature-based phishing detection  
Architecture: Local inference, REST API communication

## How to Run

### Backend
cd backend  
uvicorn main:app --reload  

### Frontend
cd frontend  
python -m http.server 5500  

Open http://127.0.0.1:5500

## Impact
- Reduces phishing victimization among students  
- Builds digital hygiene awareness  
- Strengthens institutional cybersecurity posture  
- Preserves user privacy through local analysis  
