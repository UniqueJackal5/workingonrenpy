# Act 1: High School

label act1_highschool_start:
    # The game starts here for Act 1.

    "This is the beginning of Act 1: High School."

    call highschool_day_1 from _call_highschool_day_1

    return

label highschool_day_1_anusha_path:
    "I walk over to Anusha's group, and she immediately pulls me into their conversation."
    an "So, [player_name], did you do anything fun this summer?"
    player "Just the usual. Spent a lot of time reading, actually."
    an "Oh, really? What did you read?"
    an "So, [player_name], did you do anything fun this summer?"
    player "Just the usual. Spent a lot of time reading, actually."
    an "Oh, really? What did you read?"

    menu:
        "Mention a classic novel":
            player "I reread 'Pride and Prejudice.' It's surprisingly good."
            an "Oh, I love that one! Elizabeth Bennet is such a strong character."
            $ change_affinity("anusha", 1)
        "Talk about a new fantasy series":
            player "I got really into 'The Aethelgard Chronicles.' It's a new fantasy series."
            an "Ooh, I haven't heard of that! Is it good?"
            $ change_affinity("anusha", 0)

    "The bell rings, signaling the start of the first class."
    "We all head inside, chatting about our schedules."
    jump highschool_day_1_end

label highschool_day_1_ritesh_path:
    "I approach Ritesh, who looks up from his book as I get closer."
    player "Hey, Ritesh. What are you reading?"
    ri "Oh, just a classic. 'Pride and Prejudice.' Have you read it?"
    player "I've heard of it. Is it any good?"
    ri "It's quite insightful, actually. A keen observation of human nature and societal norms."
    player "Hey, Ritesh. What are you reading?"
    ri "Oh, just a classic. 'Pride and Prejudice.' Have you read it?"
    player "I've heard of it. Is it any good?"
    ri "It's quite insightful, actually. A keen observation of human nature and societal norms."

    menu:
        "Agree with his assessment":
            player "I can see that. It's interesting how relevant some of those observations still are."
            ri "Indeed. Human nature, it seems, changes little over time."
            $ change_affinity("ritesh", 1)
        "Express a preference for modern literature":
            player "I prefer more modern stories, personally. Something with a bit more action."
            ri "Ah, I understand. To each their own, I suppose."
            $ change_affinity("ritesh", 0)

    "The bell rings, signaling the start of the first class."
    "We walk to class together, discussing the book."
    jump highschool_day_1_end

label highschool_day_1_end:
    "The first day of high school has officially begun."
    # Transition to next scene or day
    return

label highschool_day_1:
    scene bg highschool_exterior # Placeholder background
    with fade

    "It's the first day of high school. The morning sun casts long shadows across the school grounds."

    # Show player character (placeholder)
    show player_sprite at center # Assuming 'player_sprite' is defined elsewhere

    player "(Another year, another chance to make something of myself. Or at least, survive.)"

    "As I walk towards the main entrance, I spot Anusha by the lockers, already surrounded by a small group of friends."

    # Placeholder for Anusha's sprite
    # show anusha_sprite at left

    an "Hey, [player_name]! Over here!"

    "Anusha waves enthusiastically, her smile as bright as ever. She's always been the most outgoing of our group."

    "A moment later, Ritesh walks up, a book in hand, looking a bit more reserved as usual."

    # Placeholder for Ritesh's sprite
    # show ritesh_sprite at right

    ri "Morning, everyone. [player_name], did you finish the summer reading?"

    "I have a choice to make. Do I join Anusha's lively group, or do I go talk to Ritesh about the book?"

    menu:
        "Go talk to Anusha":
            jump highschool_day_1_anusha_path
        "Go talk to Ritesh":
            jump highschool_day_1_ritesh_path

    return

label classroom_intro:
    scene bg_classroom with dissolve
    show anusha uniform neutral at center

    anusha "First day jitters? This seat's been empty all semester..."
    samir "Mind if I...?"

    menu:
        "Take the seat next to Anusha":
            $ anusha_points += 1
            jump library_study_scene

        "Sit near the window alone":
            $ ritesh_points += 1
            jump cafeteria_intro

label cafeteria_intro:
    scene bg_cafeteria with fade
    show ritesh uniform smile at center

    ritesh "Saving seats is against school rules! Mind if I join you?"
    samir "..."

    menu:
        "Slide over to make space":
            $ ritesh_points += 2
            jump sports_club_scene

        "Pretend to be occupied":
            $ nina_points += 1
            jump courtyard_scene

label sports_club_scene:
    scene bg_gymnasium with fade
    show ritesh sports_uniform smile at center

    ritesh "First years never last through warmups! Bet you can't handle 10 laps?"
    samir "..."

    menu:
        "Accept the challenge":
            $ ritesh_points += 3
            jump festival_committee

        "Politely decline":
            $ nina_points += 1
            jump music_room_scene

label courtyard_scene:
    scene bg_courtyard with dissolve
    show nina uniform thoughtful at center

    nina "That tree's been here since our parents' time... Makes you think, doesn't it?"
    samir "..."

    menu:
        "Share a personal memory":
            $ nina_points += 2
            jump art_club_scene

        "Change the subject":
            $ anusha_points += 1
            jump classroom_study_group

label library_study_scene:
    scene bg_library with fade
    show anusha uniform glasses at center

    anusha "This calculus problem has me stuck... Mind brainstorming together?"
    samir "..."

    menu:
        "Work through it step-by-step":
            $ anusha_points += 2
            jump exam_prep_scene

        "Suggest taking a break":
            $ ritesh_points += 1
            jump rooftop_scene

label art_club_scene:
    scene bg_art_room with dissolve
    show nina apron paintbrush at center

    nina "This mural needs something... Maybe your perspective?"
    samir "..."

    menu:
        "Add abstract elements":
            $ nina_points += 3
            jump gallery_visit

        "Keep traditional style":
            $ anusha_points += 2
            jump cultural_event