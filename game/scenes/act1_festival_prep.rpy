label festival_preparation:
    scene bg_highschool_exterior with dissolve
    play music "audio/festival_theme.ogg" fadein 1.0

    show anusha uniform neutral at left
    show ritesh uniform smile at right

    samir "The cultural festival committee needs help setting up decorations. Who should I partner with?"

    menu:
        "Help Anusha with traditional artwork":
            $ anusha_points += 2
            show anusha uniform blush
            anusha "I could use your eye for color..."
            jump cultural_art_scene

        "Assist Ritesh with sound system setup":
            $ ritesh_points += 2
            ritesh "Perfect! Let's make this sound system boom!"
            jump tech_setup_scene

        "Coordinate with Nina on food stalls":
            $ nina_points += 1
            nina "Great! Let's ensure authentic flavors!"
            jump food_prep_scene

label cultural_art_scene:
    scene bg_classroom_art with fade
    show anusha uniform apron

    anusha "This mandala design represents eternal love..."
    samir "It's beautiful. How can I help?"

    menu:
        "Focus on precise patterns":
            $ anusha_points += 1
            anusha "Your attention to detail is impressive."

        "Suggest vibrant color combinations":
            $ anusha_points += 2
            anusha "These hues capture our festival spirit!"

    jump festival_continuation

label tech_setup_scene:
    # Additional scene content would go here
    jump festival_continuation

label food_prep_scene:
    # Additional scene content would go here
    jump festival_continuation

label festival_continuation:
    scene bg_festival_night with dissolve
    "As the festival lights illuminate the night..."