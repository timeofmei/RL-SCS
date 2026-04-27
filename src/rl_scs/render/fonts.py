import pygame

def _pick_font(candidates: list[str]) -> str:
    pygame.font.init()
    for name in candidates:
        if pygame.font.match_font(name):
            return name
    return ""

FONT_SANS = _pick_font(["arial", "liberationsans", "freesans", "dejavusans", "ubuntu"])
FONT_MONO = _pick_font(["consolas", "couriernew", "liberationmono", "dejavusansmono", "ubuntumono"])
