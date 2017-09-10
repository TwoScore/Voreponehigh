# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("vorepone")
image vp n = "vpn.png"
image vp m = "vpm.png"
image bg school = "school.png"
image bg black = "black.png"

transform center:
    xalign .5
    yalign .5
    xpos .5
    ypos .5
    zoom .5

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg school

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "9am at Horse Mouth High"

    show vp n at center
        
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

    hide vp
    
    "..."
    
    return

label goodend:
    
    v "Great!  just stand still and I'll give you the view of your life!"

    show vp m at center
    
    v "Aaaaaaah~"
    
    v "gulp!"

    hide vp
    scene bg black
    
    "YOU HAVE DIED"

    # This ends the game.

    return
