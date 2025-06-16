# The script of the game goes in this file.






# The game starts here.

# Define the player character and their name variable
define player = Character("Samir") # Default name, will be updated
default player_name = "Samir"

label start:
    # Define the player character's name.
    $ player_name = renpy.call_screen("name_input") # Call the screen and get the returned value
    $ player.name = player_name
    jump act1_highschool_start

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

