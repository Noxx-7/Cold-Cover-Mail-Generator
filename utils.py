import re

def clean_text(text, keep_links=False):
    """
    Clean text from job descriptions or resumes.

    Args:
        text (str): Input text.
        keep_links (bool): If True, keep URLs (for resumes).
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)

    if not keep_links:
        # Remove URLs if we don't want them
        text = re.sub(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            '',
            text
        )

    # Remove special characters (but keep spaces and alphanumeric)
    text = re.sub(r'[^a-zA-Z0-9:/.\- ]', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)

    # Trim leading/trailing whitespace
    return text.strip()
