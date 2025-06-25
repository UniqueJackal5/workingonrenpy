label festival_preparation:
    scene bg_highschool_exterior with dissolve
    play music "audio/festival_theme.ogg" fadein 1.0

    show anusha uniform neutral at left
    show ritesh uniform smile at right

    samir "The cultural festival committee needs help setting up decorations. Who should I partner with?"

    menu:
        "Help Anusha with traditional artwork":
            $ change_affinity("anusha", +2)
            show anusha uniform blush
            anusha "I could use your eye for color..."
            jump cultural_art_scene

        "Assist Ritesh with sound system setup":
            $ change_affinity("ritesh", +2)
            ritesh "Perfect! Let's make this sound system boom!"
            jump tech_setup_scene

        "Coordinate with Nina on food stalls":
            $ change_affinity("nina", +1)
            nina "Great! Let's ensure authentic flavors!"
            jump food_prep_scene

label cultural_art_scene:
    scene bg_classroom_art with fade
    show anusha uniform apron

    anusha "This mandala design represents eternal love..."
    samir "It's beautiful. How can I help?"

    menu:
        "Focus on precise patterns":
            $ change_affinity("anusha", +1)
            anusha "Your attention to detail is impressive."

        "Suggest vibrant color combinations":
            $ change_affinity("anusha", +2)
            anusha "These hues capture our festival spirit!"

    jump festival_continuation

label tech_setup_scene:
    scene bg stage_backstage
    show ritesh determined at center

    ritesh "This wiring is a mess. We need to get this sorted before the show starts."

    menu:
        "Help organize the cables neatly":
            $ change_affinity("anusha", +1) # Shows organizational skills
            ritesh "Thanks, that's a huge help."
        "Offer to test the microphones":
            $ change_affinity("ritesh", +2)
            ritesh "Good idea. Let's check the levels."

    jump festival_continuation

label food_prep_scene:
    scene bg kitchen
    show nina focused at center

    nina "The spices need to be perfectly balanced for the samosas."

    menu:
        "Help with the chopping and prep work":
            $ change_affinity("anusha", +1) # Shows diligence
            nina "Your help is appreciated."
        "Taste-test and give feedback":
            $ change_affinity("nina", +2)
            nina "An excellent suggestion. That really enhances the flavor!"

    jump festival_continuation

label festival_continuation:
    scene bg_festival_night with dissolve
    "As the festival lights illuminate the night..."