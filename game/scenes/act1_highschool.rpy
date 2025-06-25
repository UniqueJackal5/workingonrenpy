label classroom_intro:
    scene bg classroom day
    show anusha neutral at center
    
    anusha "Welcome to Calculus! This seat's been empty all semester..."
    samir "Mind if I...?"
    
    menu:
        "Take the seat next to Anusha":
            $ change_affinity("anusha", +2)
            jump library_study_scene
        "Sit near the window alone":
            $ change_affinity("rites", +1)
            jump cafeteria_intro

label act1_highschool_start:
label exam_prep_scene:
    scene bg classroom day
    show anusha neutral at center
    
    anusha "Let's review the calculus problems together. I brought extra notes!"
    
    menu:
        "Study diligently with Anusha":
            $ change_affinity("anusha", +2)
            jump library_study_scene
        "Pretend to understand and chat instead":
            $ change_affinity("rites", +1)
            jump courtyard_scene

label rooftop_scene:
    scene bg rooftop sunset
    show nina thoughtful at right
    
    nina "Sometimes I come here to sketch the clouds. They're... transient, aren't they?"
    
    menu:
        "Comment on the sunset beauty":
            $ change_affinity("nina", +2)
            jump art_club_scene
        "Make a joke about the height":
            $ change_affinity("rites", +1)
            jump sports_club_scene

label festival_committee:
    scene bg auditorium
    show anusha enthusiastic at left
    show ritesh smirk at right
    
    anusha "We need proper planning for the cultural exhibition!"
    ritesh "Relax, Asha. We've got the best team in school!"
    
    menu:
        "Support Anusha's detailed approach":
            $ change_affinity("anusha", +3)
            jump festival_preparation
        "Side with Ritesh's casual strategy":
            $ change_affinity("rites", +3)
            jump courtyard_scene
        "Stay neutral about Nina's artistic flair":
            $ change_affinity("nina", +1)
            jump courtyard_scene

label cafeteria_intro:
    scene bg cafeteria
    show ritesh happy at left

    ritesh "Hey, new face! Grab a seat. The food's terrible, but the company's great."

    menu:
        "Join Ritesh and his friends":
            $ change_affinity("rites", +2)
            jump sports_club_scene
        "Find a quiet corner to eat alone":
            $ change_affinity("nina", +1)
            jump rooftop_scene

label library_study_scene:
    scene bg library
    show anusha smiling at center

    anusha "I knew you'd make the right choice. Focus is key to success."

    menu:
        "Ask Anusha for help with a difficult problem":
            $ change_affinity("anusha", +2)
            jump exam_prep_scene
        "Get distracted by a book on poetry":
            $ change_affinity("nina", +1)
            jump art_club_scene

label courtyard_scene:
    scene bg courtyard
    show ritesh smirk at left
    show nina thoughtful at right

    ritesh "See? Told you things would work out. Spontaneity beats stuffy plans any day."
    nina "Or perhaps, a balance of both is ideal..."

    menu:
        "Agree with Ritesh's carefree attitude":
            $ change_affinity("rites", +2)
            jump sports_club_scene
        "Contemplate Nina's point about balance":
            $ change_affinity("nina", +2)
            jump art_club_scene

label sports_club_scene:
    scene bg gym
    show ritesh determined at center

    ritesh "Alright, time for some real action! Let's see what you've got."

    menu:
        "Show off your athletic skills":
            $ change_affinity("rites", +3)
            jump festival_committee
        "Struggle but show good sportsmanship":
            $ change_affinity("anusha", +1)
            jump festival_committee

label art_club_scene:
    scene bg art_room
    show nina smiling at center

    nina "You have an eye for beauty. It's not just about what you see, but how you see it."

    menu:
        "Ask Nina to teach you some techniques":
            $ change_affinity("nina", +3)
            jump festival_committee
        "Praise her work sincerely":
            $ change_affinity("anusha", +1)
            jump festival_committee