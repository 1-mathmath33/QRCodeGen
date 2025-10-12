from typing import Callable, Any, Dict

from qrmaker.registry import Registry
from qrmaker.renderer import default_renderer

Renderer = Callable[[str, int, str, int, str], bytes]  # approximate type for clarity
registry = Registry()
def generate_qr(kind: str, data: Dict[str, Any], *,
                renderer: Renderer = default_renderer,
                size: int = 300,
                error: str = "M",
                border: int = 4,
                image_format: str = "PNG") -> bytes:
    """
    Generate a QR image bytes for the given kind and input data.

    Args:
        kind: registered encoder name (e.g. "url", "wifi").
        data: dictionary of inputs for the encoder (e.g. {"url": "example.com"}).
        renderer: function that renders a payload string into image bytes.
                  It must accept signature compatible with default_renderer.
        size: approximate desired pixel size (square) for the generated image.
        error: error-correction level ("L","M","Q","H"), case-insensitive.
        border: quiet-zone border in modules.
        image_format: output image format passed to Pillow (e.g. "PNG").

    Returns:
        Bytes of the rendered image (PNG bytes by default).

    Raises:
        ValueError: when `kind` is unknown (no encoder registered) or when renderer/encoder raise validation errors.
        Any exceptions raised by the renderer will propagate (caller may catch them).
    """

    encoder=registry.get_encoder(kind)
    payload=encoder(data)
    result = renderer(payload, size=size, error=error, border=border, image_format=image_format)
    return result