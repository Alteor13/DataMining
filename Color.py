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
    distance = math.sqrt((color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)

    # Calcul de la distance en pourcentage
    distance_pourcentage = (distance / math.sqrt((255**2) * 3)) * 100

    # Check if the distance is within the tolerance
    return distance_pourcentage <= tolerance


def hex_to_rgb(color: str) -> list:
    """
    Convert a color from HEX to RGB.
    :param color: HEX color string, e.g. '#FF0000'
    :return: [r, g, b] -- RGB components, each ranging from 0 to 255.
    """
    color = color.lstrip('#')
    return [int(color[i:i+2], 16) for i in (0, 2, 4)]


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
