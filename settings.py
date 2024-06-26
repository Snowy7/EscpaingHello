WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
ICON=None
GAME_TITLE = 'Escaping Hello'
GHOST_VOLUME = 0.5
VFX_VOLUME = 0.5

WORLD_MAP = [
    ['tl', 'wa', 'iw', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'tr', 'ar', 'ar', 'ar', 'ar', 'ar', 'tl', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa','wa', 'wa', 'wa', 'wa', 'tr'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', 't3', '  ', '  ', '  ', '  ', '  ','  ','  ','  ', 't3', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ','  ','  ','  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 't4', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ','  ','  ','  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ','  ','  ','  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', 't3', 'dl', 'lh-e', 'lh-a','dl','t3','  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'BLC', 'tw', 'tw', 'tw', 'tw', 'tw', 'BRC', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'lv', 'lv', '  ', '  ', '2p', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 't4', '  ', '  ', 'lv', 'lv', '  ', '  ', '2p', '  ', '  ', '  ', '  ', ' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', ' ', '  ', '  ', '  ', '  ', '  ', '  ', 'TLC', 'bw', 'bw', 'bw', 'bw', 'bw', 'TRC', '  ', '  ', '  ', 'la', 'le', 'ly', 'le', 'lo', 'lu', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['bl', 'wa', 'wa', 'wa', 'wa', 'wa', 'TR', '  ', 'TL', 'wa', 'wa', 'br', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', 't3', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 't3', 'rw'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'bl', 'wa', 'wa', 'wa', 'wa', 'TR', 'dr3', 'TL','wa', 'wa','wa','br',],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar', 'ar', ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '1p', 'LW', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '3p', 'LW', 'ar', 'ar', 'ar'],
    ['tl', 'wa', 'wa', 'wa', 'wa', 'wa', 'BR', 'dr1', 'BL', 'wa', 'wa', 'wa', 'wa', 'tr', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ','  ', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 't4','  ', '  ', 'sk', 'rw', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'RW', '  ', 'LW', 'ar', 'ar', 'ar'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ','  ', '  ', 'rw', 'ar', 'ar', 'ar', 'tl', 'wa', 'wa', 'wa', 'wa', 'BR', '  ', 'BL','wa', 'wa', 'wa', 'wa','tr'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['lw', '  ', '  ', '  ', 'pl', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',  '  ', 'rw'],
    ['lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',  '  ', 'rw'],
    ['lw', '  ', 't4', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', 't3', '  ', '  ', '  ', 't3', '  ', '  ','  ', 'BLC', 'tw', 'tw', 'tw',],
    ['lw', 'swa', 'swa', 'swa', 'TR', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ','  ', '  ', '4p', '  ', '  '],
    ['lw', '  ', '  ', '  ', 'RW', '  ', '  ', '  ', '  ', '  ', '  ', 'pp', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', 'gc', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '4p', '  '],
    ['lw', '  ', 'bx', '  ', 'RW', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'TLC', 'bw', 'bw', 'bw'],
    ['lw', '  ', '  ', '  ', 'RW', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'rw', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', 't3', '  ', '  ', '  ', 't3', '  ', '  ', '  ', 'rw'],
    ['bl', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'br', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '   ', '  ', '  ', '  ', '  ', '  ', 'rw'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',  'rw'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'lw', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ',  'rw'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'bl', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'wa', 'br'],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],
    ['ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar', 'ar' ],

]