def rep_char(c, n):
    print(c*n)

def draw_line_string(msg_1, msg_2):
    nstr = len(msg_1) if (len(msg_1) > len(msg_2)) else len(msg_2)
    rep_char('-', nstr)
    print(msg_1); print(msg_2)
    rep_char('-', nstr)


name = input('Input his/her name: ')
msg1 = f' Hello {name}, '
msg2 = ' Welcome to Seoul. '
draw_line_string(msg1, msg2)
