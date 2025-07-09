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
    anusha "Just admiring the lanterns. They're so intricate. Each one tells a story, don't you think?"
    player "They really do. It's like a canvas of light."

    menu:
        "Ask about her favorite lantern design":
            $ change_affinity("anusha", +1)
            anusha "Oh, that's a tough one! I love the ones with the floral patterns, they remind me of traditional embroidery."
        "Comment on the peaceful atmosphere":
            $ change_affinity("anusha", +2)
            anusha "Exactly! It's moments like these that make all the hard work worth it. So calming."

    anusha "Well, I'm off to check out the pottery stall. Maybe I'll find some inspiration."
    player "Sounds good! Maybe I'll see you around."
    jump festival_post_encounter

label festival_ritesh_encounter:
    show ritesh neutral at center
    ritesh "[player_name]! Glad you made it. The sound system is holding up!"
    player "Sounds great! You did a good job."
    ritesh "Thanks! All that setup made me hungry. Want to grab some food? There's a great takoyaki stand over there."
    player "Takoyaki sounds good! Lead the way."

    menu:
        "Suggest trying something new together":
            $ change_affinity("ritesh", +1)
            player "How about we try that spicy ramen stall instead? I heard it's a local favorite."
            ritesh "Ramen? You're on! Always up for a challenge."
        "Agree to the takoyaki":
            $ change_affinity("ritesh", +2)
            player "Takoyaki it is! Can't go wrong with a classic."
            ritesh "My man! You've got good taste."

    ritesh "Alright, I'm going to go check on the stage lighting one last time. Catch you later!"
    player "See ya, Ritesh!"
    jump festival_post_encounter

label festival_nina_encounter:
    show nina neutral at center
    nina "[player_name]! Have you tried the takoyaki? It's authentic!"
    player "Not yet, but I will! How are the food stalls doing?"
    nina "Busy, but everything's running smoothly. It's a success! The community really came together for this."
    player "It's inspiring to see. Everyone's having such a good time."

    menu:
        "Discuss the cultural significance of the festival":
            $ change_affinity("nina", +2)
            nina "Absolutely. It's more than just fun; it's about preserving our heritage and sharing it with others. It's a beautiful thing."
        "Offer to help clean up later":
            $ change_affinity("nina", +1)
            nina "That's very thoughtful of you, [player_name]. We'll definitely need all hands on deck later."

    nina "I need to go check on the dessert section. Make sure they're not running out of mochi!"
    player "Good luck, Nina!"
    jump festival_post_encounter

label festival_post_encounter:
    "You spend some more time enjoying the festival."
    jump act1_festival_continuation_end

label act1_festival_continuation_end:
    "The festival concludes."
    jump act1_transition