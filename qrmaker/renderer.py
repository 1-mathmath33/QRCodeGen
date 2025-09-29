import io
import qrcode
from qrcode import constants

_error_map={}
_error_map["L"]=constants.ERROR_CORRECT_L
_error_map["M"]=constants.ERROR_CORRECT_M
_error_map["Q"]=constants.ERROR_CORRECT_Q
_error_map["H"]=constants.ERROR_CORRECT_H
def default_renderer(payload: str, *, size: int = 300, error: str = "M",
                     border: int = 4, image_format: str = "PNG") -> bytes:
    """
    Render the given payload string into image bytes.

    Args:
        payload: the canonical string to encode (e.g. "https://example.com").
        size: approximate desired image width/height in pixels (square).
        error: error-correction level ("L","M","Q","H") — default "M".
        border: quiet-zone border in modules (default 4).
        image_format: output image format, e.g. "PNG".

    Returns:
        Raw image bytes in the requested format.

    Behavior/implementation notes:
    - Build a QR with the requested error correction level.
    - Choose a box/module size so the final pixel dimensions are about `size x size`,
      using the formula:
          box_size = max(1, size // (modules_count + 2 * border))
      where `modules_count` is the number of modules (modules per side) in the QR.
    - Create a Pillow Image (or let the library produce one), save into an in-memory
      bytes buffer (BytesIO) and return the buffer contents.
    - Do not write files or print. Raise exceptions if rendering fails.
    """

    if error not in _error_map:
        raise ValueError("Unknown error code")
    level=_error_map[error]

    # step 1: build a temporary QR to figure out modules_count
    tmp = qrcode.QRCode(error_correction=level, border=border)
    tmp.add_data(payload)
    tmp.make(fit=True)
    modules_count = tmp.modules_count  # modules per side

    # compute box_size so final image is roughly size x size pixels
    box_size = max(1, size // (modules_count + 2 * border))

    # step 2: build the real QR with computed box_size and render to an image
    qr = qrcode.QRCode(error_correction=level, box_size=box_size, border=border)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # save image to bytes and return
    buf = io.BytesIO()
    img.save(buf, format=image_format)
    return buf.getvalue()


