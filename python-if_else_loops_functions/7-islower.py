#!/usr/bin/python3
def islower(c):
    """Retorna True se c for letra minúscula, caso contrário False."""
    if not isinstance(c, str) or len(c) != 1:
        return False
    return ord('a') <= ord(c) <= ord('z')

