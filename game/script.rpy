# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character(_("Carbon"), color = "#666464")
define d = Character(_("Dishwasher"), color = "#cc9dcf")

image bg narty = "img/bg/narty.png"
image bg appartementCarbon = "img/bg/appartementCarbon.png"
image bg bedroomDay = "img/bg/bedroomDay.jpg"
image bg bedroomNight = "img/bg/bedroomNight.jpg"
image bg dump = "img/bg/dump.png"
image bg garden = "img/bg/garden.png"
image bg Honeymoon = "img/bg/honeyMoon.png"
image bg jewelryStore = "img/bg/jewelryStore.jpg"
image bg lawyerOffice = "img/bg/lawyerOffice.jpg"
image bg paintStore = "img/bg/paintStore.png"
image bg prison = "img/bg/prison.jpg"
image bg roseOnBed = "img/bg/roseOnBed.jpg"
image bg runAway = "img/bg/runAway.jpg"
image bg streetNight = "img/bg/streetNight.jpg"
image bg wedding = "img/bg/wedding.jpg"
image bg weddingStore = "img/bg/weddingStore.jpg"

image carbon smiling = "img/visual-novel-carbon/carbonSmiling.png"
image carbon crying = "img/visual-novel-carbon/cryingCarbon.png"
image carbon happy = "img/visual-novel-carbon/happyCarbon.png"
image carbon happyCrying = "img/visual-novel-carbon/happyCryingCarbon.png"
image carbon lovely = "img/visual-novel-carbon/lovelyCarbon.png"
image carbon neutral = "img/visual-novel-carbon/neutralCarbon.png"
image carbon sad = "img/visual-novel-carbon/sadCarbon.png"


image dishwasher neutral = "img/visual-novel-dishwasher/basicDishwasher.png"
image dishwasher happy = "img/visual-novel-dishwasher/happyDishwasher.png"
image dishwasher angry = "img/visual-novel-dishwasher/angryDishwasher.png"
image dishwasher sad = "img/visual-novel-dishwasher/cryingDishwasher.png"
image dishwasher blushing = "img/visual-novel-dishwasher/blushingDishwasher.png"

define audio.menu = "musics/menu.mp3"
define audio.dump = "musics/chillHollowKnightMusic.mp3"
define audio.intense = "musics/intense.MP3"
define audio.slap = "musics/slap.mp3"
define audio.wedding = "musics/wedding.mp3"
define audio.bg = "musics/bgSoundtrack.mp3"
define audio.death = "musics/death.mp3"
define audio.victory = "musics/victory.mp3"
define audio.romantic = "musics/romanticMusic.mp3"

# The game starts here.

label start:
    jump synopsis

    # /!\ ALL CHARACTERS DEPICTED IN THIS GAME ARE OVER 18 YEARS OLD /!\


    # ***** CARBON *****

    # Carbon is a trainee at dishwasher's cemetery NARTY. He got long hair, but he cut them due to his job.
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
    # They got abandoned by its owners in the terrible dishwasher's cemetery named NARTY to be recycled.
    # Clementine 
    # They are a bit shy, but they are always there for Carbon. They are always happy to help him, and they are always happy to see him.
    
    # // CLEMENTINE IMAGE USE //
    # The images we should use when he has a particular behavior / feeling




    # " Once Carbon brought them to his house, like a month ago, the apartment-sharing seems quite awkward. Something might happen... "
    

label synopsis:
    scene bg narty
    play music audio.dump
    nvl_narrator "A dishwasher has been abandoned by its owners in the terrible dishwasher's cemetery named NARTY to be recycled."
    nvl_narrator "However, the logistic services of NARTY forgot about it and the dishwasher is becoming really sad."
    nvl_narrator "One day, an intern was verifying the stocks as he had nothing to do and tripped over the dishwasher."
    nvl_narrator "After a few seconds, he realized what he had stumbled upon."
    nvl_narrator "A magnificent dishwasher, with full options, in a perfect working state, which had slept here over 1 hour! What a shame."
    nvl_narrator "He instantly took a pallet truck and took the dishwasher in his car. It was love at first sight."    
    nvl_narrator "All the rest of the day, he was amazed by this electronic device waiting in the trunk of his car."
    nvl_narrator "He had one idea for his future: Marry the dishwasher."
    stop music

    jump Q1

label Q1:
    stop music
    play music audio.bg
    scene bg appartementCarbon
    "At the end of the day, Carbon finally comes back at home and goes directly to his trunk, to see his marvelous dishwasher."
    "He opens it and finally sees it after this long day, he is so happy!"
    show carbon happy at left 
    "However, it isn't a shared feeling. As soon as the dishwasher is free, they tell him:"
    show dishwasher angry at right
    d "Why should I trust you? You kidnapped me!"
    
    menu:
        "I fell in love with you at the first sight":
            show dishwasher neutral at right
            d "I don't believe in love at first sight... But I trust you."
            jump Q2
        "I didn't kidnap you, I saved your life":
            show dishwasher blushing at right
            d "Awwww, that is so sweet of you, I'm really thanksful for what you did. I will never leave you or disagree with you ever again!"            
            jump Q3
        "Yes I did, so what":
            show dishwasher angry at right
            d "Go f*** yourself!"
            "You just started but you already disappointed your crush. Make an effort!"
            jump endBad

label Q2:
    show dishwasher blushing at right
    d "Could I, at least, ask why did you fall in love with me?"
    d "I mean... I'm only an ordinary dishwasher which was abandonned in a poor NARTY cemetery... So..."

    menu:
        "I find you very magnificent":
            d "Awwww~, thank you so much mister! I'm really flattered by what you just said!"
            jump narration_ending_1
        "I just needed something to wash my dishes":
            show dishwasher neutral at right
            d "Seriously?! I guess you are honest at least..."
            jump Q3
        "I was bored":
            show dishwasher angry at right
            d "Go f*** yourself!!!!"
            "Are you serious? Do you really want to loose?"
            jump endBad

label Q3:
    show dishwasher happy at right
    d "Okay then.. Actually, I was in a big trouble where I was, the fact that you saved me was meant to be."
    d "Humm, so.. May I ask you.."
    show dishwasher blushing at right
    d "What do you prefer about me?"

    menu:
        "Your options":
            d "I guess it could have been worse. *shrug* Thank you!"
            show dishwasher neutral at right
            jump narration_ending_1
        "Your shape":
            show dishwasher blushing at right
            d "Oh... Well, I wasn't expecting this. It pleases me more than I thought it would..."
            jump narration_ending_1
        "Your cave":
            d "You jerk! I was sure I couldn't trust you!"
            show dishwasher angry at right
            d "Why does it always end like this..."
            show dishwasher sad at right
            "Well, you made a mistake, it happens."
            jump endBad
        "your capacity (6.9 L)":
            d "I mean... That IS true. I have a great capacity, but you would never fill it! I hate you!"
            show dishwasher angry at right
            "Hum, I guess you just.. like different things from other people. Pull yourself together!"
            jump endBad

label narration_ending_1:
    scene bg streetNight
    "You completed the 1st chapter! You just obtained the dishwasher's trust. Congratulations!"
    "Your objective for this 2nd chapter is to make the dishwasher fall in love with you."
    "Nevertheless, you'll have to be more careful in the decisions you make."
    "It won't be an easy task, but it already seems like they like you, keep going!"

    jump Q4

label Q4:
    scene bg appartementCarbon
    show dishwasher neutral at right
    show carbon smiling at left
    d "Since we are in the same place now, we need to agree on some things. So, first of all..."
    d "Where do you want to go to buy washing detergent?"

    menu:
        "I think we just need to go to the little shop near the subway station. It's not too far.":
            show dishwasher happy at right
            d "... Okay why not, I'll let you go there then."
            jump Q5
        "Well, actually you're already perfect. We don't need detergent.":
            show dishwasher happy at right
            d "*laugh* Okay okay, you got me there, idiot. We need to agree on that though."
            jump Q5
        "Maybe if I make it on my own...":
            show dishwasher angry at right
            stop music
            play sound audio.slap
            d "*slap* Do not finish your sentence, you pipsqueak."
            "Huh? Are you alright mate? Why did you choose that?"
            jump endBad

label Q5:
    play music audio.bg
    show dishwasher blushing at right
    d "So.. What is the type of detergent you want to use?"

    menu:
        "Detergent tablet.":
            show dishwasher happy at right
            d "I think liquid detergent could be nice. It's cheap and comes in handy."
        "Finish quantum gel.":
            show dishwasher neutral at right
            d "In my opinion, the powder detergent is THE BEST. I LOVE that you thought about that."
        "Only flush the dishwasher":
            show dishwasher neutral at right
            d "I don't have any preferences as well. You can just go to the shop and bring whatever you want."
    jump Q6

label Q6:
    stop music 
    play music audio.romantic
    scene bg roseOnBed
    show dishwasher happy at right
    d "Okayy, you just came back with the detergent. Nice, thank you!"
    d "Well... Which program do you want to launch?"

    menu:
        "Be soft, launch at 30°C":
            show carbon lovely at left
            c "Let's go with a long program. You'll need some time to wash all those dirty plates, I've been stacking them for days now..."
            show dishwasher blushing at right
            d "Do not worry, I'm used to big amounts of dishes."
        "Launch at 60°C":
            show carbon lovely at left 
            c "Let's go with a small program, it is going to be less exhaustive for you. You just restarted to work, we're not going too fast for now."
            show dishwasher blushing at right 
            d "Aww you're cute. You don't need to be so kind with me."
    jump Q7

label Q7:
    stop music 
    play music audio.bg
    scene bg bedroomNight
    show dishwasher blushing at right 
    d "I'm done with the current program, may I go for another one?"

    menu:
        "Yes":
            show dishwasher blushing at right
            d "As you wish. Here we go again."
            jump Q6
        "No":
            show dishwasher sad at right 
            d "Oke, I'll stop here. I'll do some more later. Well hum... I need to confess that I like the time spent with you. I'd... like to go further."
            jump narration_ending_2

label narration_ending_2:
    scene bg streetNight
    "You completed the 2nd chapter! Their now in love with you. Congratulations!"
    "Your objective for this 3rd chapter is to marry the dishwasher."
    "You'll have to be straightforward with them, but be careful with the other people, you may encounter."

    jump Q8

label Q8:
    scene bg bedroomDay
    show dishwasher happy at right 
    d "Well, since we're planning on getting married, we need some more stuff to do it."
    d "What do you want to purchase for your wedding?"

    menu:
        "Ring.":
            show dishwasher blushing at right
            d "OH my God, do you want to waste your money like that? Just for me?"
            scene bg jewelryStore
            "You both go to the nearest jewelry to find Clem69 an engagement ring. You arrive at the jewelry store and choose the prettiest ring in the entire."
            jump Q9
        "Dress.":
            show dishwasher neutral at right 
            d "Do you think I'll fit in the dress..? Hmm.. I'll trust you then."
            scene bg weddingStore
            "You both go to the nearest wedding shop to find an appropriate dress for Clem69. It was hard... but you successfully found a dress."
            jump Q9
        "Painting":
            show dishwasher angry
            d "P-Painting-? Wh-Why?"
            scene bg paintStore 
            "It was quite disappointing for Clem69. She decided to... put some distance with Carbon."
            "Between all the possibilities you got, you chose the worst one. "
            jump endBad

label Q9:
    stop music
    play music audio.bg
    scene bg appartementCarbon
    show dishwasher neutral at right
    d "Hum... We got a difficult situation you know, you're a man and I'm.. a dishwasher. So we need to go to a lawyer."
    scene bg lawyerOffice
    stop music
    play sound audio.intense

    menu:
        "Be honest":
            show carbon lovely at left
            c "I directly fell in love with them. I can't take it anymore, I need to marry her."
            show dishwasher blushing at right
            d "Awww that's so sweet of you, honey."
            "The lawyer understood that love is stronger, and no matter what, you'll be together. He told you that the wedding will take place."
            jump Q10
        "Use humor":
            show carbon lovely at left
            c "You know, this is not the kind of women we're used to meet. Although, I'd be glad to marry this dishwasher."
            stop sound
            play sound audio.dump
            scene bg dump
            "The appointment went quite bad. The lawyer looked at you awfuly, and took a call. Then, a S.W.A.T. team came in and grabbed the dishwasher. They threw them in the dump."
            "Well, it's not what we're supposed to say in that situation..."
            stop sound
            jump endBad
        "Say the first thing that goes to your mind":
            show carbon lovely at left
            c "I love dishwashers, even more when they can't go away from me..."
            scene bg prison
            stop sound
            "The appointment went quite bad. The lawyer looked at you grimly and took a call. Then, a S.W.A.T. team came in and grabbed Carbon. He went in court and he got a life sentence."
            "Bruv, what have you done..."
            jump endBad

label Q10:
    stop sound
    stop music
    play music audio.bg
    scene bg appartementCarbon
    show dishwasher blushing at right 
    d "Okay, so we got some stuff. Now, we just need to plan what we're going to do. Let's get married!"
    stop music
    play music audio.wedding
    scene bg wedding
    "What do you want to do during the wedding?"

    menu:
        "Kiss the bride.":
            show carbon happyCrying at left
            c "Well, I wanna do something that I already want to do... I want to kiss you."
            show dishwasher blushing at right 
            d "Let's kiss. *smouch* Thank you Carbon for everything, you're the love of my life."
            jump narration_good_ending
        "Get scared.":
            show carbon crying at left
            c "Well hum, I think it went a bit far... You were faithful, but I'm not. Farewell, Dishwasher."
            show dishwasher sad at right 
            d "How dare you do this to me Carbon... you were the one that I was trusting, the one that I was loving... You're such a disgusting person.."
            jump narration_sad_ending
        "Travel.":
            show carbon happy at left 
            c "Would you mind if... we go to a Honeymoon?- I'd be grateful to do it with you by my side."
            show dishwasher happy at right 
            d "A Honeymoon, are you for real? Yes, I'd love to go especially with you, I love you so much! *happy*"
            jump narration_best_ending

label narration_good_ending:
    stop music
    stop sound
    play music audio.bg
    scene bg garden
    "You kissed the bride and are now spending a happy life with Clem69."
    "You're living together happily in a huge house, sharing dishes between each other."
    jump end

label narration_best_ending:
    stop music
    play music audio.victory
    scene bg Honeymoon
    "You didn't only kiss the bride, you also went straight for a Honeymoon. "
    "You are the most loved person on the planet and are happy living with Clem69. "
    "You had a lot of miniature and portable dishwashers that can speak, and were buried together after more than 80 years spent together. "
    jump end

label narration_sad_ending:
    stop music
    stop sound
    play music audio.dump
    scene bg runAway
    "You were not a man and decided to run away. "
    show bg dump
    show dishwasher sad at right
    "You also put Clem69 into the dump. They passed away from obsolescence about 10 years later. "
    "You are now banned from society. What a shame!"
    jump end

label end:
    stop music 
    stop sound
    play music audio.death
    return

label endBad:   
    stop music 
    stop audio
    play music audio.death
    "You just lost the game. "
    "Try to improve your reactions and how you behave to make them in love with you!"
    return # Main menu