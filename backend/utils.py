import re
from urllib.parse import urlparse

def extract_url_features(url: str):
    features = {}

    parsed = urlparse(url)

    features["url_length"] = len(url)
    features["has_https"] = 1 if parsed.scheme == "https" else 0
    features["num_dots"] = url.count(".")
    features["num_hyphens"] = url.count("-")
    features["num_at"] = url.count("@")
    features["num_subdirs"] = url.count("/")
    features["has_ip"] = 1 if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.netloc) else 0

    suspicious_keywords = ["login", "verify", "update", "bank", "secure", "account"]
    features["suspicious_keyword"] = 1 if any(word in url.lower() for word in suspicious_keywords) else 0

    return list(features.values()), features