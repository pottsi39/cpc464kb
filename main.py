print ("starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

#                   2           3          4         5           6          7            8          9          10
keyboard.col_pins =(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
#                       1           11           12         13         14           15          16         17             18      19                 
keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [
    [KC.DELETE,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO
     ,KC.NO,KC.N1,KC.N2,KC.ESCAPE,KC.Q,KC.TAB,KC.A,KC.CAPSLOCK,KC.Z
     ,KC.NO,KC.N4,KC.N3,KC.E,KC.W,KC.S,KC.D,KC.C,KC.X
     ,KC.NO,KC.N6,KC.N5,KC.R,KC.T,KC.G,KC.F,KC.B,KC.V
     ,KC.NO,KC.N8,KC.N7,KC.U,KC.Y,KC.H,KC.J,KC.N,KC.SPACE
     ,KC.NO,KC.N0,KC.N9,KC.O,KC.I,KC.L,KC.K,KC.M,KC.COMMA
     ,KC.NO,KC.UP,KC.MINUS,KC.AT,KC.P,KC.SCOLON,KC.COLON,KC.SLASH,KC.DOT
     ,KC.NO,KC.BSPACE,KC.LBRACKET,KC.ENTER,KC.RBRACKET,KC.KP_4,KC.LSHIFT,KC.BSLASH,KC.RCTRL
     ,KC.NO,KC.LEFT,KC.LCTRL(KC.C),KC.KP_7,KC.KP_8,KC.KP_5,KC.KP_1,KC.KP_2,KC.KP_0
     ,KC.NO,KC.UP,KC.RIGHT,KC.DOWN,KC.KP_9,KC.KP_6,KC.KP_3,KC.KP_ENTER,KC.PDOT
     ]
    ]


if __name__ == '__main__':
    keyboard.go()