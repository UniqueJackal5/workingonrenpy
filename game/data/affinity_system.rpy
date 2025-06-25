# Affinity ranges from -10 (dislike) to +10 (admiration)
default persistent.anusha_affinity = 0
default persistent.ritesh_affinity = 0
default persistent.nina_affinity = 0
default persistent.total_choices = 0

default persistent.anusha_route_unlocked = False
default persistent.ritesh_route_unlocked = False
default persistent.nina_route_unlocked = False

init python:
    def init_affinities():
        # This function resets the values for a new game.
        persistent.anusha_affinity = 0
        persistent.ritesh_affinity = 0
        persistent.nina_affinity = 0
        persistent.total_choices = 0
        
        persistent.anusha_route_unlocked = False
        persistent.ritesh_route_unlocked = False
        persistent.nina_route_unlocked = False

    def change_affinity(character, amount):
        # Cap affinity between -10 and +10
        current = getattr(persistent, f'{character}_affinity', 0)
        new_value = max(-10, min(10, current + amount))
        setattr(persistent, f'{character}_affinity', new_value)
        
        renpy.notify(f"{character.capitalize()}'s affinity changed by {amount} (Now: {new_value})")