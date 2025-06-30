# This file will contain the scenes and choices for the festival continuation.

label act1_festival_continuation_start:
    "The festival continues... The air is filled with laughter and the aroma of street food."

    player "This festival is amazing!"

    menu:
        "Look for Anusha":
            jump festival_anusha_encounter
        "Look for Ritesh":
            jump festival_ritesh_encounter
        "Look for Nina":
            jump festival_nina_encounter

label festival_anusha_encounter:
    show anusha neutral at center
    anusha "Oh, hey, [player_name]! Enjoying the festival?"
    player "Definitely! What are you up to?"
    anusha "Just admiring the lanterns. They're so intricate."
    jump festival_post_encounter

label festival_ritesh_encounter:
    show ritesh neutral at center
    ritesh "[player_name]! Glad you made it. The sound system is holding up!"
    player "Sounds great! You did a good job."
    ritesh "Thanks! Want to grab some food?"
    jump festival_post_encounter

label festival_nina_encounter:
    show nina neutral at center
    nina "[player_name]! Have you tried the takoyaki? It's authentic!"
    player "Not yet, but I will! How are the food stalls doing?"
    nina "Busy, but everything's running smoothly. It's a success!"
    jump festival_post_encounter

label festival_post_encounter:
    "You spend some more time enjoying the festival."
    jump act1_festival_continuation_end

label act1_festival_continuation_end:
    "The festival concludes."
    return