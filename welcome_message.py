"""High level text editor and generator for PSM string handling.
Supposedly, the following should work in PSM
    
    STRING Hello$, "Hello, World!"
    LOAD&RETURN s5, Hello$

But we couln't get it to work, so we have to do it the hard way...
"""


welcome_string = f"  _       __     __                        !@"\
                 f" | |     / /__  / /________  ____ ___  ___ !@"\
                 f" | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \!@"\
                 f" | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/!@"\
                 f" |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/ !@"\
                 f"!@"                                                              \
                 f"    Authors: John Garzon-Ferrer, Sergio Flores Rodriguez, Ameena Mohammed       !@"



# expected output= f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "                                                               
#                  f"                                                                                "                                           
#                  f"                    _       __     __                                           "
#                  f"                   | |     / /__  / /________  ____ ___  ___                    "
#                  f"                   | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \                   "
#                  f"                   | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/                   "
#                  f"                   |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/                    "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"    Authors: John Garzon-Ferrer, Sergio Flores Rodriguez, Ameena Mohammed       "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "
#                  f"                                                                                "







main_menu_string = f"Menu options:!@"\
                   f"1. Play recording!@"\
                   f"2. New Recording!@"\
                   f"3. Delete Recording!@"\
                   f"4. Delete All Recordings!@"\
                   f"5. Volume Control!@"\


mydict = {
    "A": "ascii_A",
    "B": "ascii_B",
    "C": "ascii_C",
    "D": "ascii_D",
    "E": "ascii_E",
    "F": "ascii_F",
    "G": "ascii_G",
    "H": "ascii_H",
    "I": "ascii_I",
    "J": "ascii_J",
    "K": "ascii_K",
    "L": "ascii_L",
    "M": "ascii_M",
    "N": "ascii_N",
    "O": "ascii_O",
    "P": "ascii_P",
    "Q": "ascii_Q",
    "R": "ascii_R",
    "S": "ascii_S",
    "T": "ascii_T",
    "U": "ascii_U",
    "V": "ascii_V",
    "W": "ascii_W",
    "X": "ascii_X",
    "Y": "ascii_Y",
    "Z": "ascii_Z",
    "a": "ascii_a",
    "b": "ascii_b",
    "c": "ascii_c",
    "d": "ascii_d",
    "e": "ascii_e",
    "f": "ascii_f",
    "g": "ascii_g",
    "h": "ascii_h",
    "i": "ascii_i",
    "j": "ascii_j",
    "k": "ascii_k",
    "l": "ascii_l",
    "m": "ascii_m",
    "n": "ascii_n",
    "o": "ascii_o",
    "p": "ascii_p",
    "q": "ascii_q",
    "r": "ascii_r",
    "s": "ascii_s",
    "t": "ascii_t",
    "u": "ascii_u",
    "v": "ascii_v",
    "w": "ascii_w",
    "x": "ascii_x",
    "y": "ascii_y",
    "z": "ascii_z",
    "`": "ascii_TICK",
    "!": "ascii_LF",
    "@": "ascii_CR",
    "_": "ascii_UNDER",
    " ": "ascii_SPACE",
    "|": "ascii_VBAR",
    "\\": "ascii_BKSLASH",
    "/": "ascii_FWDSLASH",
    ",": "ascii_COMMA",
    ":": "ascii_COLON",
    "-": "ascii_MINUS",
}
# minus and underline might be mixed up
buffer_in = buffer_out = ""
repeat_output = "OUTPUT s0, uart_data_tx\n"

with open("welcome_message.txt", "w") as f:

    for i in welcome_string:
        buffer_in =f"LOAD s0, {mydict.get(i, i)}\n" \
                   f"OUTPUT s0, uart_data_tx\n" \
                   f"call wait\n"
        
        if buffer_out != buffer_in:
            f.write(buffer_in)
            buffer_out = buffer_in
        else:
            f.write(repeat_output)
