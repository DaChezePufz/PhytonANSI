colors = {
    30: "Black",
    31: "Red",
    32: "Green",
    33: "Yellow",
    34: "Blue",
    35: "Magenta",
    36: "Cyan",
    37: "White",
    40: "Black",
    41: "Red",
    42: "Green",
    43: "Yellow",
    44: "Blue",
    45: "Magenta",
    46: "Cyan",
    47: "White",
    90: "Bright Black (Gray)",
    91: "Bright Red",
    92: "Bright Green",
    93: "Bright Yellow",
    94: "Bright Blue",
    95: "Bright Magenta",
    96: "Bright Cyan",
    97: "Bright White",
    100: "Bright Black (Gray)",
    101: "Bright Red",
    102: "Bright Green",
    103: "Bright Yellow",
    104: "Bright Blue",
    105: "Bright Magenta",
    106: "Bright Cyan",
    107: "Bright White",
}

for bg in range(40, 55):
    if bg > 47:
        bg = bg + 53
    for fg in range(30, 45):
        if fg > 37:
            fg = fg + 53

        print(f"\x1B[{fg};{bg}m This is a test. BG: {colors[bg]}, FG: {colors[fg]} \x1B[0m")


print("\x1B[0m END")