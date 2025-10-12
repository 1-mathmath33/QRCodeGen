from collections import defaultdict


class Registry:
    _instance = None
    _registry = defaultdict()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance= super().__new__(cls)
        return cls._instance

    def register_encoder(self,name:str):
        """
        Decorator Factory to register a encoder

        Usage:
            @register_encoder('encoder_kind')
            def encode_kind(data):
        """
        def decorator(fn):
            if name in self._registry:
                raise KeyError(f"Entry {name} already exists")
            self._registry[name] = fn
            return fn
        return decorator

    def get_encoder(self,name:str):
        """
        Fetches a registered encoder
        Raises error if no registered encoder exists

        """
        if name in self._registry:
            return self._registry[name]
        raise ValueError(f"Entry {name} does not exist")

    def list_encoders(self)-> list[str]:
        """
        Returns a list of registered encoders
        """
        return list(self._registry.keys())

    def clear_registry(self):
        """
        Clears the registry
        """
        self._registry.clear()