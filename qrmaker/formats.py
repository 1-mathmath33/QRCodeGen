from qrmaker.registry import register_encoder


@register_encoder("url")
def encode_url(data: dict):
    """
    Input: dictionary with "url" key
    expects a url key and value pair
    raise ValueError if key is not url or the value is empty
    missing scheme would use https:// prefix
    """
    value=data.get("url", "").strip()
    if not value:
        raise ValueError("Missing url key or value")
    if "://" not in value:
        value = "https://" + value

    return value