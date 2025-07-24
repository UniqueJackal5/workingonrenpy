# act2_college.rpy

label act2_college:
    scene bg college_campus with dissolve
    "Years have passed since high school. You're now navigating the bustling campus of Northwood University."
    "College life is a whirlwind of lectures, late-night study sessions, and new friendships."

    # Placeholder for college-specific interactions and choices
    "You encounter familiar faces and new challenges."

    # Example: A choice related to college life
    menu:
        "Focus on academics":
            "You spend most of your time in the library, excelling in your studies."
            $ change_affinity("anusha", +1) # Example: Anusha might appreciate this
        "Join a campus club":
            "You decide to join the debate club, meeting new people and honing your public speaking skills."
            $ change_affinity("ritesh", +1) # Example: Ritesh might be in a tech club
        "Explore the city":
            "You take advantage of your newfound freedom to explore the vibrant city life."
            $ change_affinity("nina", +1) # Example: Nina might enjoy exploring

    "College is a time of immense growth and self-discovery."

    jump act2_transition