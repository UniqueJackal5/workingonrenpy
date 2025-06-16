# Seasons of Us - Visual Novel

## Project Overview

**Title:** Seasons of Us
**Genre:** Romantic coming-of-age visual novel
**Theme:** Love, growth, and the passage of time
**Perspective:** Player takes the role of Samir (male) or Samira (female), name customizable.
**Structure:** The story progresses across 3 acts — High School, College, and Adulthood — with branching routes and multiple romance outcomes.

## Narrative Flow

### ACT 1: High School
**Setting:** Urban Nepali high school (Grade 11/12), final year
**Main Themes:** First love, friendships, identity, social anxiety, self-expression

**Key Scenes:**
1.  **Morning Classroom Introduction:** Player introduction, first interactions with key characters, early choices impact affinity values.
2.  **Group Project Event:** Forced collaboration (choose who to work with), emotional bonding and secrets revealed.
3.  **Farewell Party / Exam Results:** Major emotional moment, optional confession scene (if high affinity), ends with everyone going their own way.

### ACT 2: College / Reunions
**Setting:** University campus or city life (new but familiar)
**Main Themes:** Maturity, career goals, drifting relationships, temptation, rediscovery

**Key Scenes:**
1.  **Random Reunion:** Bump into one of the Act 1 characters (who depends on Act 1 choices), build new tension or deepen bond.
2.  **College Festival or Cultural Show:** Romantic opportunity or conflict, player starts realizing values have changed.
3.  **Big Choice: Relationship or Growth:** Determine future endings available based on choice to stay close to a person or focus on career/self.

### ACT 3: Adulthood
**Setting:** Small apartment, cafe, office space, or village return
**Main Themes:** Closure, rekindling love, acceptance, life beyond romance

**Key Scenes:**
1.  **Final Meeting:** One character reaches out (based on prior choices), long emotional dialogue, discuss past, missed chances, or next step.
2.  **Life Choice Ending:** Settle down with a character, stay friends, or leave alone choosing personal freedom.

## Characters and Romance Paths

*   **Anusha (The Dreamer):** Artistic, poetic, sensitive. Best path: patient support, creative bonding.
*   **Ritesh (The Logical One):** Focused, perfectionist, emotionally distant. Best path: confront him honestly, open him up.
*   **Nina (The Bright Spark):** Outgoing, funny, avoids serious topics. Best path: show her it’s okay to be vulnerable.

## Gameplay Notes

**Love Points System:** Each dialogue or action adds or removes points per character (e.g., `anusha_points`, `ritesh_points`, `nina_points`).

**Affection Thresholds:**
*   `>5`: potential romantic confession
*   `>8`: unlock extra flashback scene
*   `10+`: unlock true ending

**Endings:**
*   Romantic Ending
*   Bittersweet Separation
*   Self-Growth / Independence
*   Secret “True Ending” (deep connection and wise choices across all 3 acts)

## Assets Suggestions

*   **Backgrounds:** Classroom, park bench, festival stage, apartment.
*   **Sprites:** Casual outfits, 3 expressions per character (neutral, happy, sad).
*   **Music:** Lo-fi chill beats for high school; mellow piano or ambient pads for adult scenes.

## Implementation Order Suggestion

1.  Fully write Act 1 (3 scenes, 3 key choices).
2.  Implement love points system.
3.  Write dynamic Act 2 based on Act 1 choices.
4.  Finalize Act 3 endings.
5.  Add music and polish.