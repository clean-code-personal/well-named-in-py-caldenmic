from cable_functions import MAJOR_COLORS, MINOR_COLORS

REFERENCE_MANUAL = dict()

def print_reference_manual():
    REFERENCE_MANUAL_LIST = []
    for major_color_index in range(len(MAJOR_COLORS)):
        for minor_color_index in range(len(MINOR_COLORS)):
            REFERENCE_MANUAL_LIST.append(MAJOR_COLORS[major_color_index] + " " + MINOR_COLORS[minor_color_index])
    REFERENCE_MANUAL = dict(list(enumerate(REFERENCE_MANUAL_LIST)))
    print(REFERENCE_MANUAL)
