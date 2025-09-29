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

@register_encoder("email")
def encode_email(data: dict):
    """
    Input: dictionary with "email" key
    expects an email key and value pair
    raise ValueError if key is not email or the value is empty
    A valid input is to be given
    """
    value=data.get("email", "").strip()
    if not value:
        raise ValueError("Missing email key or value")
    value ="mailto:" + str(value) # can this be improved??
    return value