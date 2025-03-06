# utils.py
def clean_text(text):
    """Remove extra whitespace and unwanted characters."""
    return " ".join(text.split()).strip()