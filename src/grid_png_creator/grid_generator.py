from __future__ import annotations

import struct
import zlib
from pathlib import Path


WIDTH = 1600
HEIGHT = 900
LINE_COLOR = (0, 0, 0, 255)
TRANSPARENT = (0, 0, 0, 0)


def render_grid_png(rows: int, columns: int, output_path: str | Path) -> Path:
    """Render a transparent PNG grid with black walls, ceilings, and floors."""
    if rows <= 0 or columns <= 0:
        raise ValueError("rows and columns must both be positive integers")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    pixels = bytearray(WIDTH * HEIGHT * 4)
    transparent_pixel = bytes(TRANSPARENT)
    line_pixel = bytes(LINE_COLOR)

    for index in range(WIDTH * HEIGHT):
        offset = index * 4
        pixels[offset : offset + 4] = transparent_pixel

    x_lines = {round(i * (WIDTH - 1) / columns) for i in range(columns + 1)}
    y_lines = {round(i * (HEIGHT - 1) / rows) for i in range(rows + 1)}

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x in x_lines or y in y_lines:
                offset = (y * WIDTH + x) * 4
                pixels[offset : offset + 4] = line_pixel

    raw_scanlines = bytearray()
    row_length = WIDTH * 4
    for y in range(HEIGHT):
        raw_scanlines.append(0)
        start = y * row_length
        raw_scanlines.extend(pixels[start : start + row_length])

    png = b"".join(
        [
            b"\x89PNG\r\n\x1a\n",
            _chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 6, 0, 0, 0)),
            _chunk(b"IDAT", zlib.compress(bytes(raw_scanlines), level=9)),
            _chunk(b"IEND", b""),
        ]
    )
    output_path.write_bytes(png)
    return output_path


def _chunk(chunk_type: bytes, data: bytes) -> bytes:
    checksum = zlib.crc32(chunk_type + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + chunk_type + data + struct.pack(">I", checksum)


if __name__ == "__main__":
    render_grid_png(21, 36, Path(__file__).with_name("grid_21x36.png"))
