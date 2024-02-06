# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character(_("Carbon"), color = "#666464")
define d = Character(_("Dishwasher"), color = "#cc9dcf")







# The game starts here.

label start:

    # "Carbon is portuguese, and lives in France for 15 years, near Switzerland. He always wears glasses, some grayish clothes and a headgear. "
    # "He likes sports, programming, and alcohol (he isn't alcoholic, he often goes to the bar though.) "
    # "He's always good-looking, joyful and lovely. Everyone gets along well with Carbon, talking with him is always a pleasure. "
    # "He's a trainee at Darty, and once upon a time, he stumbled into an open dishwasher forgotten at the back of the warehouse. "

    # "Clementine is the later dishwasher from the Curel® company. 'Its' pronouns are they/them. They have been taken by Carbon one day. "
    # "Once Carbon brought them to his house, like a month ago, the apartment-sharing seems quite awkward. Something might happen..."

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
