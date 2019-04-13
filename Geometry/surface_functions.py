import pygame


def collides_surface(surface, pos):
    rect = surface.get_rect()
    offset = surface.get_abs_offset()
    return rect.collidepoint(pos[0] - offset[0], pos[1] - offset[1])
