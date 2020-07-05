'''
    out - Simple logging with a few fun features.
    © 2018-19, Mike Miller - Released under the LGPL, version 3+.
'''
import os
import env

from console.detection import is_a_tty, choose_palette, get_available_palettes
from console.style import ForegroundPalette, BackgroundPalette, EffectsPalette


def _find_palettes(stream):
    ''' Need to configure palettes manually, since we are checking stderr. '''
    chosen = choose_palette(stream=stream)
    palettes = get_available_palettes(chosen)
    fg = ForegroundPalette(palettes=palettes)
    bg = BackgroundPalette(palettes=palettes)
    fx = EffectsPalette(palettes=palettes)
    return fg, bg, fx, chosen, is_a_tty(stream)

is_fbterm = (env.TERM == 'fbterm')
os_name = os.name
