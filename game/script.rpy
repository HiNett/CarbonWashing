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
    scene darty
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
    "You completed the 1st chapter! You just obtained the dishwasher's trust. Congratulations!"
    "Your objective for this 2nd chapter is to make the dishwasher fall in love with you."
    "Nevertheless, you'll have to be more careful in the decisions you make."
    "It won't be an easy task, but it already seems like they like you, keep going!"

    jump Q4

label Q4:
    d "Since we are in the same place now, we need to agree on some things. So, first of all..."
    d "Where do you want to go to buy washing detergent?"

    menu:
        "I think we just need to go to the little shop near the subway station. It's not too far.":
            d "... Okay why not, I'll let you go there then."
            jump Q5
        "Well, actually you're already perfect. We don't need detergent.":
            d "*laugh* Okay okay, you got me there, idiot. We need to agree on that though."
            jump Q5
        "Maybe if I make it on my own...":
            d "*slap* Do not finish your sentence, you pipsqueak."
            jump end

label Q5:
    d "So.. What is the type of detergent you want to use?"

    menu:
        "detergent tablet.":
            d "I think liquid detergent could be nice. It's cheap and comes in handy."
        "Finish quantum gel.":
            d "In my opinion, the powder detergent is THE BEST. I LOVE that you thought about that."
        "Only flush the dishwasher":
            d "I don't have any preferences as well. You can just go to the shop and bring whatever you want."
    jump Q6

label Q6:
    d "Okayy, you just came back with the detergent. Nice, thank you!"
    d "Well... Which program do you want to launch?"

    menu:
        "Be soft, launch at 30°C":
            c "Let's go with a long program. You'll need some time to wash all those dirty plates, I've been stacking them for days now..."
            d "Do not worry, I'm used to big amounts of dishes."
        "Launch at 60°C":
            c "Let's go with a small program, it is going to be less exhaustive for you. You just restarted to work, we're not going too fast for now."
            d "Aww you're cute. You don't need to be so kind with me."
    jump Q7

label Q7:
    d "I'm done with the current program, may I go for another one?"

    menu:
        "Yes":
            d "As you wish. Here we go again. *blush*"
            jump Q6
        "No":
            d "Oke, I'll stop here. I'll do some more later. Well hum... I need to confess that I like the time spent with you. I'd... like to go further."
            jump narration_ending_2

label narration_ending_2:
    "You completed the 2nd chapter! Their now in love with you. Congratulations!"
    "Your objective for this 3rd chapter is to marry the dishwasher."
    "You'll have to be straightforward with them, but be careful with the other people, you may encounter."

    jump Q8

label Q8:
    d "Well, since we're planning on getting married, we need some more stuff to do it."
    d "What do you want to purchase for your wedding?"

    menu:
        "Ring.":
            d "OH my God, do you want to waste your money like that? Just for me?"
            "You both go to the nearest jewelry to find Clem69 an engagement ring. You arrive at the jewelry store and choose the prettiest ring in the entire."
            jump Q9
        "Dress.":
            d "Do you think I'll fit in the dress..? Hmm.. I'll trust you then."
            "You both go to the nearest wedding shop to find an appropriate dress for Clem69. It was hard... but you successfully found a dress."
            jump Q9
        "Painting":
            d "P-Painting-? Wh-Why?" 
            "It was quite disappointing for Clem69. She decided to... put some distance with Carbon."
            jump end

label Q9:
    d "Hum... We got a difficult situation you know, you're a man and I'm.. a dishwasher. So we need to go to a lawyer."

    menu:
        "Be honest":
            c "I directly fell in love with them. I can't take it anymore, I need to marry her."
            d "Awww that's so sweet of you, honey."
            "The lawyer understood that love is stronger, and no matter what, you'll be together. He told you that the wedding will take place."
            jump Q10
        "Use humor":
            c "You know, this is not the kind of women we're used to meet. Although, I'd be glad to marry this dishwasher."
            "The appointment went quite bad. The lawyer looked at you awfuly, and took a call. Then, a S.W.A.T. team came in and grabbed the dishwasher. They threw them in the dump."
            jump end
        "Say the first thing that goes to your mind":
            c "I love dishwashers, even more when they can't go away from me..."
            "The appointment went quite bad. The lawyer looked at you grimly and took a call. Then, a S.W.A.T. team came in and grabbed Carbon. He went in court and he got a life sentence."
            jump end

label Q10:
    d "Okay, so we got some stuff. Now, we just need to plan what we're going to do. Let's get married!"
    "What do you want to do during the wedding?"

    menu:
        "Kiss the bride.":
            c "Well, I wanna do something that I already want to do... I want to kiss you."
            d "Let's kiss. *smouch* Thank you Carbon for everything, you're the love of my life. *blush*"
            jump narration_good_ending
        "Get scared.":
            c "Well hum, I think it went a bit far... You were faithful, but I'm not. Farewell, Dishwasher."
            d "How dare you do this to me Carbon... you were the one that I was trusting, the one that I was loving... You're such a disgusting person.."
            jump narration_sad_ending
        "Travel.":
            c "Would you mind if... we go to a Honeymoon?- I'd be grateful to do it with you by my side."
            d "A Honeymoon, are you for real? Yes, I'd love to go especially with you, I love you so much! *happy*"
            jump narration_best_ending

label narration_good_ending:
    nvl_narrator ""
    jump end

label narration_good_ending:
    nvl_narrator ""
    jump end

label narration_good_ending:
    nvl_narrator ""
    jump end

label end:
    return # Main menu