def big_text():
    space = [
        " ",
        "    ",
        "    ",
        "    ",
        "    ",
        "    ",
        "    "
    ]
    a = [
        "A",
        "   xx   ",
        " xx  xx ",
        " xx  xx ",
        "xxxxxxxx",
        "xx    xx",
        "xx    xx"
    ]
    b = [
        "B",
        "xxxxxx  ",
        "xx    xx",
        "xxxxxx  ",
        "xx    xx",
        "xx    xx",
        "xxxxxxx "
    ]
    c = [
        "C",
        " xxxxxx ",
        "xx    xx",
        "xx      ",
        "xx      ",
        "xx    xx",
        " xxxxxx "
    ]
    d = [
        "D",
        "xxxxxx  ",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xxxxxx  "
    ]
    e = [
        "E",
        "xxxxxxxx",
        "xx      ",
        "xxxxxx  ",
        "xx      ",
        "xx      ",
        "xxxxxxxx"
    ]
    f = [
        "F",
        "xxxxxxxx",
        "xx      ",
        "xxxxxx  ",
        "xx      ",
        "xx      ",
        "xx      "
    ]
    g = [
        "G",
        " xxxxxx ",
        "xx    xx",
        "xx      ",
        "xx  xxxx",
        "xx    xx",
        " xxxxxx "
    ]
    h = [
        "H",
        "xx    xx",
        "xx    xx",
        "xxxxxxxx",
        "xx    xx",
        "xx    xx",
        "xx    xx"
    ]
    i = [
        "I",
        " xxxxxx ",
        "   xx   ",
        "   xx   ",
        "   xx   ",
        "   xx   ",
        " xxxxxx "
    ]
    j = [
        "J",
        "      xx",
        "      xx",
        "      xx",
        "xx    xx",
        "xx    xx",
        " xxxxxx "
    ]
    k = [
        "K",
        "xx    xx",
        "xx  xx  ",
        "xxxxx   ",
        "xx   xx ",
        "xx    xx",
        "xx    xx"
    ]
    l = [
        "L",
        "xx      ",
        "xx      ",
        "xx      ",
        "xx      ",
        "xx      ",
        "xxxxxxxx"
    ]
    m = [
        "M",
        "xx    xx",
        "xxx  xxx",
        "xx xx xx",
        "xx    xx",
        "xx    xx",
        "xx    xx"
    ]
    n = [
        "N",
        "xx    xx",
        "xxx   xx",
        "xxxx  xx",
        "xx  xxxx",
        "xx   xxx",
        "xx    xx"
    ]
    o = [
        "O",
        " xxxxxx ",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        " xxxxxx "
    ]
    p = [
        "P",
        "xxxxxxx ",
        "xx    xx",
        "xxxxxxx ",
        "xx      ",
        "xx      ",
        "xx      "
    ]
    q = [
        "Q",
        " xxxxxx ",
        "xx    xx",
        "xx    xx",
        "xx  x xx",
        "xx   xxx",
        " xxxxx x"
    ]
    r = [
        "R",
        "xxxxxxx ",
        "xx    xx",
        "xxxxxxx ",
        "xx   xx ",
        "xx    xx",
        "xx    xx"
    ]
    s = [
        "S",
        " xxxxxx ",
        "xx    xx",
        " xxxx   ",
        "   xxxx ",
        "xx    xx",
        " xxxxxx "
    ]
    t = [
        "T",
        "xxxxxxxx",
        "   xx   ",
        "   xx   ",
        "   xx   ",
        "   xx   ",
        "   xx   "
    ]
    u = [
        "U",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        " xxxxxx "
    ]
    v = [
        "V",
        "xx    xx",
        "xx    xx",
        " xx  xx ",
        " xx  xx ",
        "  xxxx  ",
        "   xx   "
    ]
    w = [
        "W",
        "xx    xx",
        "xx    xx",
        "xx    xx",
        "xx xx xx",
        "xxx  xxx",
        "xx    xx"
    ]
    x = [
        "X",
        "xx    xx",
        " xx  xx ",
        "   xx   ",
        "   xx   ",
        " xx  xx ",
        "xx    xx"
    ]
    y = [
        "Y",
        "xx    xx",
        " xx  xx ",
        "  xxxx  ",
        "   xx   ",
        "   xx   ",
        "   xx   "
    ]
    z = [
        "Z",
        "xxxxxxxx",
        "     xx ",
        "    xx  ",
        "   xx   ",
        " xx     ",
        "xxxxxxxx"
    ]

    big_letters = [space, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
    msg = input("Msg: ").upper()
    base_lines = (1, 2, 3, 4, 5, 6)
    letter_section = ""

    # Going through the message
    # Going through every line

    for num in base_lines:
        letter_line = ""
        for letter in msg:
            for bigLetter in big_letters:
                # Finding which letter
                if letter == bigLetter[0]:
                    letter_section = bigLetter[num]
            letter_line += letter_section + "  "
            letter_section = ""
        print(letter_line)