"""
:author: Louis ROBERT
:creation: 2024-03-18

This module contains functions for color manipulation and comparison.
"""
import math


def is_near(color1, color2, tolerance, mode='RGB') -> bool:
    """
    Check if two colors are near each other within a certain tolerance.
    :param color1: first color; can be a string(HEX) or a list(RGB;HSV)
    :param color2: second color; can be a string(HEX) or a list(RGB;HSV)
    :param tolerance: distance between the colors in percentage
    :param mode: can be 'RGB', 'HSV' or 'HEX'
    :return:
    """

    # Convert the colors to RGB lists
    if mode == 'HEX':
        color1 = hex_to_rgb(color1)
        color2 = hex_to_rgb(color2)
    elif mode == 'HSV':
        color1 = hsv_to_rgb(color1)
        color2 = hsv_to_rgb(color2)
    elif mode == 'RGB':
        pass
    else:
        raise ValueError('Invalid mode' + mode)

    # Calculate the distance between the colors
    distance = math.sqrt((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2)

    # Calcul de la distance en pourcentage
    distance_pourcentage = (distance / math.sqrt((255 ** 2) * 3)) * 100

    # Check if the distance is within the tolerance
    return distance_pourcentage <= tolerance


def hex_to_rgb(color: str) -> list:
    """
    Convert a color from HEX to RGB.
    :param color: HEX color string, e.g. '#FF0000'
    :return: [r, g, b] -- RGB components, each ranging from 0 to 255.
    """
    color = color.replace('#', '')
    return [int(color[i:i + 2], 16) for i in (0, 2, 4)]


def hsv_to_rgb(color: list) -> list:
    """
    Convert a color from HSV to RGB.
    :param color: list of three values (h, s, v) where:
                 h is the hue, ranging from 0 to 360 degrees,
                 s is the saturation, ranging from 0 to 1,
                 v is the value, ranging from 0 to 1.
    :return: [r, g, b] -- RGB components, each ranging from 0 to 255.
    """
    h, s, v = color
    h /= 360.0
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - (f * s))
    t = v * (1.0 - ((1.0 - f) * s))

    if i % 6 == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q

    return [int(r * 255), int(g * 255), int(b * 255)]


def rgb_to_hex(rgb: list) -> str:
    """
    Convert a color from RGB to HEX.
    :param rgb: list of three values (r, g, b) where each value ranges from 0 to 255.
    :return: HEX color string, e.g. '#FF0000'
    """
    return '#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2])


def hsv_to_hex(hsv: list) -> str:
    """
    Convert a color from HSV to HEX.
    :param hsv: list of three values (h, s, v) where:
                 h is the hue, ranging from 0 to 360 degrees,
                 s is the saturation, ranging from 0 to 1,
                 v is the value, ranging from 0 to 1.
    :return: HEX color string, e.g. '#FF0000'
    """
    return rgb_to_hex(hsv_to_rgb(hsv))


def hex_to_hsv(color: str) -> list:
    """
    Convert a color from HEX to HSV.
    :param color: HEX color string, e.g. '#FF0000'
    :return: list of three values (h, s, v) where:
                 h is the hue, ranging from 0 to 360 degrees,
                 s is the saturation, ranging from 0 to 1,
                 v is the value, ranging from 0 to 1.
    """
    # Convertir la couleur en RGB (0-1)
    r, g, b = hex_to_rgb(color)
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Trouver la valeur maximale et minimale parmi les composantes RVB
    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    # Calculer la valeur (V)
    v = cmax

    # Calculer la saturation (S)
    if cmax != 0:
        s = delta / cmax
    else:
        s = 0

    # Calculer la teinte (H)
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    # Mettre la teinte dans la plage [0, 360)
    h = round(h % 360, 2)

    return [h, s, v]



def generate_colors(n: int, format: str = "HSV"):
    """
    Generate a list of n distinct colors equally spaced around the color wheel.
    :param format: can be 'RGB', 'HSV' or 'HEX'. Default is 'HSV'.
    :param n: number of colors to generate
    :return: list of n colors in hexadecimal format
    """
    colors = []
    for i in range(n):
        # Calculer la composante de couleur en fonction de l'index
        hue = i * (360 / n)
        # Créer la couleur en fonction du type
        if format == 'RGB':
            colors.append(hsv_to_rgb([hue, 1, 1]))
        elif format == 'HSV':
            colors.append([hue, 1, 1])
        elif format == 'HEX':
            colors.append(hsv_to_hex([hue, 1, 1]))
            raise ValueError('Invalid type' + format)
    return colors


def get_color_name(hsv: list) -> str:
    """
    Get the name of a color based on its HSV components.
    :param hsv: list of three values (h, s, v) where:
                 h is the hue, ranging from 0 to 360 degrees,
                 s is the saturation, ranging from 0 to 1,
                 v is the value, ranging from 0 to 1.
    :return: name of the color, e.g. 'red'
    """
    h, s, v = hsv
    if s < 0.1:
        return 'gray'
    if v < 0.1:
        return 'black'
    if v > 0.9:
        return 'white'
    if h < 30:
        return 'red'
    if h < 60:
        return 'orange'
    if h < 90:
        return 'yellow'
    if h < 150:
        return 'green'
    if h < 210:
        return 'cyan'
    if h < 270:
        return 'blue'
    if h < 330:
        return 'magenta'
    return 'red'


def name_list() -> list:
    """
    Get the list of color names.
    :return: list of color names
    """
    return ['black', 'white', 'gray', 'red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta']