_registry={}

def register_encoder(name:str):
    """
    Decorator Factory to register a encoder

    Usage:
        @register_encoder('encoder_kind')
        def encode_kind(data):
    """
    def decorator(fn):
        if name in _registry:
            raise KeyError(f"Entry {name} already exists")
        _registry[name] = fn
        return fn
    return decorator

def get_encoder(name:str):
    """
    Fetches a registered encoder
    Raises error if no registered encoder exists

    """
    if name in _registry:
        return _registry[name]
    raise ValueError(f"Entry {name} does not exist")

def list_encoders()-> list[str]:
    """
    Returns a list of registered encoders
    """
    return list(_registry.keys())

def clear_registry():
    """
    Clears the registry
    """
    _registry.clear()