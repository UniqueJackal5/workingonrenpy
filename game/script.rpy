# The script of the game goes in this file.






# The game starts here.

# Define the player character and their name variable
define player = Character("Samir") # Default name, will be updated
default player_name = "Samir"

label start:
    # Initial setup
    scene bg_highschool_exterior
    "Freshman year begins..."
    jump act1_highschool_intro

label act1_highschool_intro:
    call screen name_input
    jump classroom_intro

label act1_festival:
    call festival_preparation
    if anusha_points >= 3:
        jump cultural_bonding
    elif ritesh_points >= 3:
        jump tech_collaboration
    else:
        jump festival_wrapup

label act1_transition:
    # Shared post-festival scene
    scene bg_school_gate
    "As the semester ends..."
    jump act2_college_intro

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

