import numpy as np

def predict_phishing(feature_values):
    score = 0

    url_length, has_https, num_dots, num_hyphens, num_at, num_subdirs, has_ip, suspicious_keyword = feature_values

    if url_length > 75:
        score += 15
    if has_https == 0:
        score += 20
    if num_dots > 3:
        score += 10
    if num_hyphens > 2:
        score += 10
    if num_at > 0:
        score += 15
    if has_ip == 1:
        score += 20
    if suspicious_keyword == 1:
        score += 10

    risk_score = min(score, 100)

    if risk_score >= 60:
        label = "High Risk - Likely Phishing"
    elif risk_score >= 35:
        label = "Suspicious - Proceed with Caution"
    else:
        label = "Safe"

    return label, risk_score