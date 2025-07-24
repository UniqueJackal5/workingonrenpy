# act3_adulthood.rpy

label act3_adulthood:
    scene bg city_apartment with dissolve
    "Years have flown by. You've settled into adulthood, building a career and a life."
    "The choices you made in high school and college have shaped who you are today."

    # Placeholder for adulthood-specific interactions and choices
    "Life presents new challenges and opportunities."

    # Example: A choice related to career or personal life
    menu:
        "Focus on career advancement":
            "You dedicate yourself to your profession, striving for success and recognition."
            $ change_affinity("anusha", +1) # Example: Anusha might be career-focused
        "Prioritize personal relationships":
            "You invest deeply in your connections with friends and loved ones, finding fulfillment in shared experiences."
            $ change_affinity("ritesh", +1) # Example: Ritesh might value strong bonds
        "Pursue a long-held dream":
            "You decide to finally chase that passion project you've always dreamed of."
            $ change_affinity("nina", +1) # Example: Nina might encourage creative pursuits

    "This is your life, and you are the author of its next chapter."

    jump endings