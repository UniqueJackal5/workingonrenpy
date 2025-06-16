init python:
    # Function to change character affinity points.
    # character_name: The name of the character (e.g., "anusha", "ritesh", "nina").
    # points: The number of points to add or subtract from the character's affinity.
    def change_affinity(character_name, points):
        if character_name == "anusha":
            store.anusha_points += points
        elif character_name == "ritesh":
            store.ritesh_points += points
        elif character_name == "nina":
            store.nina_points += points
        else:
            # Log a warning if an unknown character's affinity is attempted to be changed.
            renpy.log(f"Warning: Attempted to change affinity for unknown character: {character_name}")
            return
        
        # Log the affinity change for debugging purposes.
        renpy.log(f"Affinity for {character_name} changed by {points}. New value: {getattr(store, character_name + '_points')}")