import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

vial = Vial(
    vial_id=[0xAA, 0xBB, 0xCC, 0xDD, 0x11, 0x22, 0x33, 0x44],
    vial_keyboard_uid=[0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC],
)
keyboard.modules.append(vial)

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS=[board.D1, board.D2, board.D3, board.D4, board.D5, board.D6, board.D7, board.D8, board.D10]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False,
)

keyboard.keymap = [
    [
        KC.UP,
        KC.DOWN,
        KC.LEFT,
        KC.RIGHT,

        KC.AUDIO_VOL_UP,
        KC.AUDIO_VOL_DOWN,

        KC.UNDO,
        KC.REDO,
        KC.AUDI_PLAY_PAUSE,



    ]

]

if __name__ == '__main__':
    keyboard.go()
