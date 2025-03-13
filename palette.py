import colorsys

def generate_golden_ratio_palette(n=25, s_range=(0.7, 0.9), v_range=(0.7, 0.9)):
    """Generate a diverse palette using the golden ratio, varying saturation and brightness."""
    phi = 0.61803398875  # Golden ratio conjugate
    hue = 0.3  # Starting hue (adjustable)

    palette = []
    for i in range(n):
        h = (hue + i * phi) % 1  # Spread hues using golden ratio
        s = s_range[0] + (s_range[1] - s_range[0]) * ((i % 3) / 2)  # Vary saturation
        v = v_range[0] + (v_range[1] - v_range[0]) * (((i // 3) % 3) / 2)  # Vary brightness
        rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v))
        palette.append(rgb)

    return palette

def generate_interpolated_hsv_palette(n=25, h_range=(0, 1), s_range=(0, 1), v_range=(0, 1)):
    palette = []
    hs = (h_range[1] - h_range[0]) / n
    ss = (s_range[1] - s_range[0]) / n
    vs = (v_range[1] - v_range[0]) / n
    for i in range(n):
        h = h_range[0] + i*hs
        s = s_range[0] + i*ss
        v = v_range[0] + i*vs
        rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(h, s, v))
        palette.append(rgb)

    return palette

def generate_pastel_palette(n=25, s = 0.5, v=0.9):
    """Generate soft pastel colors."""
    return generate_interpolated_hsv_palette(n, (0, 1), (s, s), (v, v))

def generate_neon_palette(n=25, v=0.9):
    """Generate vibrant, neon-like colors."""
    return generate_pastel_palette(n, 1, v)

def generate_single_hue_palette(n=25, hue=0.6):
    """Generate vibrant, neon-like colors."""
    return generate_interpolated_hsv_palette(n, (hue, hue), (1,1), (0, 1))

def generate_warm_palette(n=5, s=1, v=0.9):
    return generate_interpolated_hsv_palette(n, (0, 0.15), (s, s), (v, v))

def generate_cool_palette(n=5, s=1, v=0.9):
    return generate_interpolated_hsv_palette(n, (0.55, 0.8), (s, s), (v, v))
