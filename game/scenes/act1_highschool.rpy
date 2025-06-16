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