# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("vorepone")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "9am at Horse Mouth High"

    v "Hey there!"

    v "There's nothing really here, so there's nothing to see yet"
    
    v "unless you want to see the inside of my mouth"
    
    menu:
        "No thanks I'm good":
            jump badend
        
        "Sure why not?":
            jump goodend
        
label badend:
    
    v "*sigh* alright get out of here ya twerp"
    
    "..."
    
    return

label goodend:
    
    v "Great!  just stand still and I'll give you the view of your life!"
    
    v "Aaaaaaah~"
    
    v "gulp!"
    
    "YOU HAVE DIED"

    # This ends the game.

    return
