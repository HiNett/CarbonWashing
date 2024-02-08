# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character(_("Carbon"), color = "#666464")
define d = Character(_("Dishwasher"), color = "#cc9dcf")







# The game starts here.

label start:
    jump synopsis

    # /!\ ALL CHARACTERS DEPICTED IN THIS GAME ARE OVER 18 YEARS OLD /!\


    # ***** CARBON *****

    # Carbon is a trainee at dishwasher's cemetery DARTY. He got long hair, but he cut them due to his job.
    # Carbon is Portuguese, and has been living in France for 15 years, near Switzerland. He always wears glasses, some grayish clothes and a headgear. "
    # He likes sports, programming, and alcohol (he isn't alcoholic, he often goes to the bar though.) 
    # He's always good-looking, joyful and lovely. Everyone gets along well with Carbon, talking with him is always a pleasure. 
    # When he's in love, he stutters a bit, and it can be difficult 
    
    # // CARBON IMAGE USE //
    # The images we should use when he has a particular behavior / feeling

    # - Carbon Neutral -> /img/visual-novel-carbon/neutralCarbon.png
    # - Carbon Happy -> /img/visual-novel-carbon/happyCarbon.png
    # - Carbon Crying (hapiness) -> /img/visual-novel-carbon/happyCryingCarbon.png
    # - Carbon Sad -> /img/visual-novel-carbon/sadCarbon.png
    # - Carbon Crying (sadness) -> /img/visual-novel-carbon/cryingCarbon.png
    # - Carbon In Love -> /img/visual-novel-carbon/lovelyCarbon.png


    # ***** CLEMENTINE *****
    
    # Clementine is the later dishwasher from the Curel® company. 'Its' pronouns are they/them. 
    # They got abandoned by its owners in the terrible dishwasher's cemetery named DARTY to be recycled.
    # Clementine 
    # They are a bit shy, but they are always there for Carbon. They are always happy to help him, and they are always happy to see him.
    
    # // CLEMENTINE IMAGE USE //
    # The images we should use when he has a particular behavior / feeling




    # " Once Carbon brought them to his house, like a month ago, the apartment-sharing seems quite awkward. Something might happen... "
    

label synopsis:
    nvl_narrator "A dishwasher has been abandoned by its owners in the terrible dishwasher's cemetery named DARTY to be recycled."
    nvl_narrator "However, the logistic services of DARTY forgot about it and the dishwasher is becoming really sad."
    nvl_narrator "One day, an intern was verifying the stocks as he had nothing to do and tripped over the dishwasher."
    nvl_narrator "After a few seconds, he realized what he had stumbled upon."
    nvl_narrator "A magnificent dishwasher, with full options, in a perfect working state, which had slept here over 1 hour! What a shame."
    nvl_narrator "He instantly took a pallet truck and took the dishwasher in his car. It was love at first sight."
    nvl_narrator "All the rest of the day, he was amazed by this electronic device waiting in the trunk of his car."
    nvl_narrator "He had one idea for his future: Marry the dishwasher."

    jump Q1

label Q1:
    "At the end of the day, Carbon finally comes back at home and goes directly to his trunk, to see his marvelous dishwasher."
    "He opens it and finally sees it after this long day, he is so happy!"
    "However, it isn't a shared feeling. As soon as the dishwasher is free, they tell him:"
    d "Why should I trust you? You kidnapped me!"

    menu:
        "I fell in love with you at the first sight":
            d "Awwww, that is so sweet of you, I'm really thanksful for what you did. I will never leave you or disagree with you ever again!"
            jump Q2
        "I didn't kidnap you, I saved your life":
            d "I don't believe in the love at first sight... But I trust you."
            jump Q3
        "Yes I did, so what":
            d "Go f*** yourself!"
            jump end

label Q2:
    d "Could I, at least, ask why did you fall in love with me?"
    d "I mean... I'm only an ordinary dishwasher which was abandonned in a poor DARTY cemetery... So..."

    menu:
        "I find you very magnificent":
            d "Awwww~, thank you so much mister! I'm really flattered by what you just said!"
            jump narration_ending_1
        "I just needed something to wash my dishes":
            d "Seriously?! I guess you are honest at least..."
            jump Q3
        "I was bored":
            d "Go f*** yourself!!!!"
            jump end

label Q3:
    d "Okay then.. Actually, I was in a big trouble where I was, the fact that you saved me was meant to be."
    d "Humm, so.. May I ask you.."
    d "What do you prefer about me?"

    menu:
        "Your options":
            d "I guess it could have been worse. *shrug* Thank you!"
            jump narration_ending_1
        "Your shape":
            d "Oh... Well, I wasn't expecting this. It pleases me more than I thought it would... *shy/tsundere*"
            jump narration_ending_1
        "Your cave":
            d "You jerk! I was sure I couldn't trust you! Why does it always end like this... *Auto-destruction*"
            jump end
        "your capacity (6.9 L)":
            d "I mean... That IS true. I have a great capacity, but you would never fill it! I hate you!"
            jump end

label narration_ending_1:
    nvl_narrator "You completed the 1st chapter! You just obtained the dishwasher's trust. Congratulations!"

    jump narration_begin_2

label narration_begin_2:
    nvl_narrator "Your objective for this 2nd chapter is to make the dishwasher fall in love with you."
    nvl_narrator "Nevertheless, you'll have to be more careful in the decisions you make."
    nvl_narrator "It won't be an easy task, but it already seems like they like you, keep going!"

    jump Q4

label Q4:
    "*TODO: end*"
    return # Main menu

label end:
    "*TODO: end*"
    return # Main menu