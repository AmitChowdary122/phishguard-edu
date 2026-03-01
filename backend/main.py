from fastapi import FastAPI
from pydantic import BaseModel
from utils import extract_url_features
from model import predict_phishing
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PhishGuard EDU")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str

@app.get("/")
def root():
    return {"message": "Welcome to PhishGuard EDU API"}

@app.post("/analyze")
def analyze_url(request: URLRequest):
    features, feature_dict = extract_url_features(request.url)
    label, risk_score = predict_phishing(features)

    explanation = []

    if feature_dict["has_ip"]:
        explanation.append("The URL uses an IP address instead of a domain name.")
    if feature_dict["suspicious_keyword"]:
        explanation.append("The URL contains suspicious keywords like 'login' or 'verify'.")
    if feature_dict["num_dots"] > 3:
        explanation.append("The URL contains multiple subdomains, which can indicate spoofing.")
    if feature_dict["has_https"] == 0:
        explanation.append("The website does not use HTTPS encryption.")

    if not explanation:
        explanation.append("No major phishing indicators detected.")

    return {
        "label": label,
        "risk_score": risk_score,
        "explanation": explanation,
        "cyber_tip": "Always verify the domain name carefully before entering credentials."
    }
