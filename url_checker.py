from urllib.parse import urlparse
import re


def analyze_url(url):

    score = 0
    warnings = []

    try:

        parsed = urlparse(url)

        if parsed.scheme != "https":
            score += 2
            warnings.append(
                "Website does not use HTTPS"
            )

        if len(url) > 75:
            score += 1
            warnings.append(
                "URL is unusually long"
            )

        if re.match(r"https?://\d+\.\d+\.\d+\.\d+", url):
            score += 3
            warnings.append(
                "URL uses an IP address instead of a domain"
            )


        suspicious_words = [
            "login",
            "verify",
            "update",
            "claim",
            "free",
            "gift",
            "reward",
            "bank",
            "password",
            "wallet"
        ]


        for word in suspicious_words:

            if word in url.lower():

                score += 1

                warnings.append(
                    f"Suspicious keyword detected: {word}"
                )


        if len(parsed.netloc.split(".")) > 3:

            score += 2

            warnings.append(
                "Multiple subdomains detected"
            )


        if score >= 5:

            verdict = "High Risk"

        elif score >= 3:

            verdict = "Medium Risk"

        else:

            verdict = "Low Risk"


        confidence = min(
            95,
            50 + score * 10
        )


        return {

            "verdict": verdict,

            "confidence": f"{confidence}%",

            "reason": (
                "\n".join(warnings)
                if warnings
                else
                "No major suspicious patterns detected."
            ),

            "advice":
            "Avoid entering passwords, OTPs, or banking details on unknown websites."

        }


    except Exception:

        return {

            "verdict": "Unknown",

            "confidence": "0%",

            "reason":
            "Invalid URL format.",

            "advice":
            "Verify the URL before opening it."

        }