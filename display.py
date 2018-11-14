_DISPLAY = True
_DISPLAY_LEN = 20
_DISPLAY_FACTOR = 3
_DISPLAY_CHAR = "="
_count = _DISPLAY_FACTOR
_display_line = _DISPLAY_CHAR

def display(text = ""):
    """
    For nice progress display
    """
    if _DISPLAY:
        global _display_line, _count
        _count -= 1
        if not _count:
            _count = _DISPLAY_FACTOR
            _display_line += _DISPLAY_CHAR
            print('\r', end='')
            print("[{}{}]".format(_display_line, "-" * (_DISPLAY_LEN - len(_display_line))), end='')
            
            if _display_line == _DISPLAY_CHAR * _DISPLAY_LEN:
                _display_line = ""