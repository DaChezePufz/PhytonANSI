# PhytonANSI
A sollection of Python demos that make use of ANSI Escape Codes

All of these programs work by calling the ANSI Escape in Python during a print statment, then providing the information, like colors to the terminal
For Python, start by `\x1B[` then the color/ formatting code (which can be seperated with semi-colons `;` then `m` to end the statment.
Example:
`print("\x1B[103;34mHelo World!\x1B[0m")`
would display: `Hello World!` in Blue text, with a Bright Yellow background. The closing escape with `0` as the code resets the formatting back to default.

[Wikipedia page on ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)

## ansiColorsDemo
This is a program that displays all 256 colour combinations.
**DOES NOT DISPLAY IN IDLE, USE CMD/TERMINAL**

![Grid Layout](https://github.com/DaChezePufz/PhytonANSI/tree/main/.images/gridLayout.png)
![Grid Layout](https://github.com/DaChezePufz/PhytonANSI/tree/main/.images/listLayout.png)
