# The script of the game goes in this file.





# The game starts here.
label start:
    # Show a background.
    scene bg highschool_exterior

    # This ensures that the affinity system is initialized at the start of the game.
    python:
        init_affinity_system()

    # Call the name input screen to allow the player to enter their name.
    call screen name_input

    # Display a dialogue.
    player "Hello, world!"

    # This is a placeholder jump to the high school scene.
    jump act1_highschool_start
    


    
label act1_festival_transition:
    # After last high school scene
    show bg school_exterior with dissolve
    mc "The festival preparations gave me new insights..."
    jump festival_preparation

label act1_festival:
    call festival_preparation
    if anusha_points >= 3:
        jump cultural_bonding
    elif ritesh_points >= 3:
        jump tech_collaboration
    else:
        jump festival_wrapup

label act1_transition:
    scene black with fade
    play music "audio/ambient_piano.ogg" fadeout 1.0
    show text "Years Later..." with dissolve
    pause 2.0
    
    if anusha_points > 5:
        show bg city_skyline with dissolve
        mc "Anusha and I kept in touch through letters, her words becoming my anchor..."
    elif rites_points > 5:
        show bg football_field with dissolve
        mc "Ritesh's relentless energy somehow carried me through those final exams..."
    else:
        show bg library with dissolve
        mc "The quiet moments between classes became my sanctuary..."
    
    jump act2_college

label act2_transition:
    scene black with fade
    show text "Graduation Day" with dissolve
    pause 1.5
    
    show bg graduation with dissolve
    mc "As I tossed my cap, I realized these connections had shaped who I'd become..."
    
    if persistent.ending_unlocked:
        jump endings
    else:
        jump act3_adulthood
    
    # This ends the game.
    return

screen name_input():
    modal True
    zorder 100

    default screen_player_name = player_name # Initialize with current player_name

    frame:
        xalign 0.5
        yalign 0.5
        background "gui/frame.png"
        padding (50, 50)

        vbox:
            label "Enter your name:"

            input default screen_player_name length 20

            textbutton "Confirm" action Return(screen_player_name)

