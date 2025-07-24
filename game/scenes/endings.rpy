# endings.rpy

label endings:
    scene black with fade
    "The journey concludes. Your choices have led you to this moment."

    # Placeholder for different endings based on affinity points or other variables
    if anusha_points > ritesh_points and anusha_points > nina_points:
        jump ending_anusha_path
    elif ritesh_points > anusha_points and ritesh_points > nina_points:
        jump ending_ritesh_path
    elif nina_points > anusha_points and nina_points > ritesh_points:
        jump ending_nina_path
    else:
        jump ending_neutral

label ending_anusha_path:
    scene bg city_park with dissolve
    "You found a deep and lasting connection with Anusha, building a life filled with shared passions and intellectual growth."
    "Together, you explored the world, always learning, always growing."
    "This is the story of your shared journey."
    return

label ending_ritesh_path:
    scene bg tech_office with dissolve
    "Your bond with Ritesh blossomed into a partnership of innovation and adventure. You built a life full of excitement and new discoveries."
    "He pushed you to be your best, and together, you achieved great things."
    "This is the story of your dynamic duo."
    return

label ending_nina_path:
    scene bg art_gallery with dissolve
    "With Nina, you discovered a world of creativity and emotional depth. Your life became a canvas, painted with vibrant experiences and heartfelt moments."
    "She taught you to see the beauty in every day, and to live authentically."
    "This is the story of your artistic journey."
    return

label ending_neutral:
    scene bg quiet_cafe with dissolve
    "Your path was one of self-discovery, forging your own way through life's challenges and triumphs."
    "While romantic connections may have shifted, you found strength and contentment within yourself."
    "This is the story of your personal growth."
    return