def cubeVolume(width, length, height):
    if isinstance(width, complex) or isinstance(length, complex) or isinstance(height, complex):
        raise ValueError("Complex input to volume formula")
    if width < 0 or length < 0 or height < 0:
        raise ValueError("Negative input to volume formula")
    return width*length*height
