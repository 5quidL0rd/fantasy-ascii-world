import time
import curses 


def add_castle(stdscr):
    castle_image = r"""
                  [\                                    ____
              |\)                                  __(_   )__
              |                                 _(          )
              Y\          ___                 (     )-----`
             T  \       __)  )--.              `---'
            J    \   ,-(         )_                   __
           Y/T`-._\ (     (       _)                 __)
           /[|   ]|  `-(__  ___)-`  |\            ,-(  __)
           | |    |      (__)       J'           (     )
   _       | |  ] |    _           /;\            `-  '
  (,,)     [| |    |    L'         /;  \               __
         /||.| /\ |   /\         /.,-._\            ,-(  __)
        /_|||| || |  /  \        | |{  |           (     )
 L/\    | \| | '` |_ _ {|          | | U |   /\       `-  '
/v^v\/\ `|  Y | [  '-' '--''-''-"-'`'   | ,`^v\ /\,`\
/ ,'./  \.` |[   |       [     __   L    ] |      /^v\  \
,'     `    |    |           ,`##Y.   ]    |___Y Y____,_,,_,,_
--   -----.-(] [ |   ]     o/####U|o      ]|| /`-, Y   _   Y  Y
 Y Y  --;`~T   |      }   \####U|[\ _,.-(^) ,-'  _  (^)__  _
  Y  YY   ;'~~l  |   L     [|\###U'E'\  \ \Y-` _  (^) _Y  _
 Y  Y Y   ;\~~/\{| [      _,'-\`= = '.\_ ,`   (^)(^) (^) (^)
     --   ;\~~~/\|  _,.-'`_  `.\_..-'"  _ . ,_ Y_ Y_ _Y  _Y__
    _    _; \~~( Y``   Y (^) / `,      (^)      _   (^) (^)
   (^)  (^)`._~ /  L \  _.Y'`  _  ` --  Y - - -(^) - Y - Y -
    Y    Y    `'--..,-'`      (^)   _  -    _   Y ____ 
      --           _    _ --   Y   (^)   _ (^)  ===   ----
          __   -  (^)  (^)      --- Y   (^) Y
    """

    max_y, max_x = stdscr.getmaxyx()
    castle_lines = castle_image.strip("\n").splitlines()
    castle_height = len(castle_lines)
    castle_width = max(len(line) for line in castle_lines)
    
    # Position castle vertically centered and flush to the right (with a 2-column margin)
    start_y = max_y // 2 - castle_height // 2
    start_x = max_x - castle_width - 2

    # Display castle
    for i, line in enumerate(castle_lines):
        y = start_y + i
        if 0 <= y < max_y and start_x >= 0:
            try:
                stdscr.addstr(y, start_x, line, curses.color_pair(2))
            except curses.error:
                pass

    return start_y, castle_height, start_x

def add_mountains(stdscr):
    mountains_image = r"""
                  /#\
                 /###\     /\
                /  ###\   /##\  /\
               /      #\ /####\/##\
              /  /      /   # /  ##\             _       /\
            // //  /\  /    _/  /  #\ _         /#\    _/##\    /\
           // /   /  \     /   /    #\ \      _/###\_ /   ##\__/ _\
          /  \   / .. \   / /   _   { \ \   _/       / //    /    \\ 
 /\     /    /\  ...  \_/   / / \   } \ | /  /\  \ /  _    /  /    \ /\
/  \  /// / .\  ..%:.  /... /\ . \ {:  \\   /. \     / \  /   ___   /  \
/.\ .\.\// \/... \.::::..... _/..\ ..\:|:. .  / .. \\  /..%. \  /./:..\__   \
/...\.../..:.\. ..:::::::..:..... . ...\{:... / %... \\/..%. \  /./:..\__   \
 .:..\:..:::....:::;;;;;;::::::::.:::::.\}.....::%.:. \ .:::. \/.%:::.:..\
::::...:::;;:::::;;;;;;;;;;;;;;:::::;;::{:::::::;;;:..  .:;:... ::;;::::.. 
;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;];;;;;;;;;;::::::;;;;:.::;;;;;;;;:..
;;;;;;;;;;;;;;ii;;;;;;;;;;;;;;;;;;;;;;;;[;;;;;;;;;;;;;;;;;;;;;;:;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;iiiiiiii;;;;;;;;;;;;;;};;ii;;iiii;;;;i;;;;;;;;;;;;;;;ii;;;
iiii;;;iiiiiiiiiiIIIIIIIIIIIiiiiiIiiiiii{iiIIiiiiiiiiiiiiiiii;;;;;iiiilliiiii
IIIiiIIllllllIIlllIIIIlllIIIlIiiIIIIIIIIIIIIlIIIIIllIIIIIIIIiiiiiiiillIIIllII
IIIiiilIIIIIIIllTIIIIllIIlIlIIITTTTlIlIlIIIlIITTTTTTTIIIIlIIllIlIlllIIIIIIITT
IIIIilIIIIITTTTTTTIIIIIIIIIIIIITTTTTIIIIIIIIITTTTTTTTTTTTTTIIIIIIIIIlIIIIIIIITTTT
IIIIIIIIITTTTTTTTTTTTTIIIIIIIITTTTTTTTIIIIIITTTTTTTTTTTTTTIIIIIIIIIIIIIITTTTT
    """
    
    max_y, max_x = stdscr.getmaxyx()
    mountains_lines = mountains_image.strip("\n").splitlines()
    mountains_height = len(mountains_lines)
    mountains_width = max(len(line) for line in mountains_lines)

    # Position mountains on the far left and at the same height as the castle
    start_mountains_x = 0
    start_mountains_y = 0
    # Display mountains
    for i, line in enumerate(mountains_lines):
        y = start_mountains_y + i
        if 0 <= y < max_y and start_mountains_x >= 0:
            try:
                stdscr.addstr(y, start_mountains_x, line, curses.color_pair(3))
            except curses.error:
                pass

    return start_mountains_y, mountains_height, start_mountains_x

def add_trees(stdscr, ground_y):
    tree_art = r"""
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
 \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
    """
    lines = tree_art.strip("\n").splitlines()
    tree_width = max(len(line) for line in lines)
    max_y, max_x = stdscr.getmaxyx()
    gap = 2  # horizontal gap between trees
    # Tile trees across the screen starting at ground_y
    for x in range(0, max_x, tree_width + gap):
        for i, line in enumerate(lines):
            y = ground_y + i
            if 0 <= y < max_y:
                try:
                    stdscr.addstr(y, x, line, curses.color_pair(3))
                except curses.error:
                    pass

def add_dragon(stdscr, x, y, dragon_lines):
    for i, line in enumerate(dragon_lines):
        try:
            stdscr.addstr(y + i, x, line, curses.color_pair(1))
        except curses.error:
            # The dragon might be partially off-screen.
            pass

def animate_wizard(stdscr, max_y, max_x):
    """Animate the wizard: appear in a puff of '@', remain briefly, then vanish in a puff of '#'."""
    wizard_art = r"""
     __/\__
. _  \\''//
-( )-/_||_\
 .'. \_()_/
  |   | . \
  || .  \
 .'. ,\_____'
    """
    wizard_lines = wizard_art.strip("\n").splitlines()
    wizard_height = len(wizard_lines)
    wizard_width = max(len(line) for line in wizard_lines)
    # Position the wizard in the lower right (if possible)
    start_y = max_y - wizard_height
    start_x = max_x - wizard_width
    if start_y < 0 or start_x < 0:
        return

    # Puff of "@" before the wizard appears.
    for i in range(wizard_height):
        try:
            stdscr.addstr(start_y + i, start_x, "@" * wizard_width, curses.color_pair(4))
        except curses.error:
            pass
    stdscr.refresh()
    time.sleep(0.5)

    # Display the wizard.
    for i, line in enumerate(wizard_lines):
        try:
            stdscr.addstr(start_y + i, start_x, line, curses.color_pair(4))
        except curses.error:
            pass
    stdscr.refresh()
    time.sleep(2)  # Wizard remains visible for 2 seconds.

    # Vanish in a puff of "#".
    for i in range(wizard_height):
        try:
            stdscr.addstr(start_y + i, start_x, "#" * wizard_width, curses.color_pair(4))
        except curses.error:
            pass
    stdscr.refresh()
    time.sleep(0.5)

def animate_goblin_loop(stdscr, max_y, max_x):
    """
    In an endless loop the wizard's vanished wall remains (a block of '#' in the wizard area)
    and occasionally a goblin's head (in magenta) peeks out before disappearing again.
    """
    wizard_art = r"""
     __/\__
. _  \\''//
-( )-/_||_\
 .'. \_()_/
  |   | . \
  || .  \
 .'. ,\_____'
    """
    wizard_lines = wizard_art.strip("\n").splitlines()
    wizard_height = len(wizard_lines)
    wizard_width = max(len(line) for line in wizard_lines)
    start_y = max_y - wizard_height
    start_x = max_x - wizard_width

    goblin_art = r"""
  .---.
 ( o.o )
  '---'
"""
    goblin_lines = goblin_art.strip("\n").splitlines()
    goblin_height = len(goblin_lines)
    goblin_width = max(len(line) for line in goblin_lines)
    # Position the goblin so its head appears inside the wizard area.
    goblin_y = start_y + (wizard_height - goblin_height) // 2
    goblin_x = start_x + 1

    while True:
        stdscr.erase()
        # Redraw static elements (castle and trees) so the lower-right area is visible.
        add_mountains(stdscr)
        castle_y, castle_height, _ = add_castle(stdscr)
        ground_y = castle_y + castle_height
        add_trees(stdscr, ground_y)
        # Draw the wizard wall (a block of '#' characters).
        for i in range(wizard_height):
            try:
                stdscr.addstr(start_y + i, start_x, "#" * wizard_width, curses.color_pair(4))
            except curses.error:
                pass
        stdscr.refresh()
        time.sleep(2)

        # The goblin peeks out.
        for i, line in enumerate(goblin_lines):
            try:
                stdscr.addstr(goblin_y + i, goblin_x, line, curses.color_pair(5))
            except curses.error:
                pass
        stdscr.refresh()
        time.sleep(0.7)

        # Remove the goblin by redrawing the wall.
        for i in range(wizard_height):
            try:
                stdscr.addstr(start_y + i, start_x, "#" * wizard_width, curses.color_pair(4))
            except curses.error:
                pass
        stdscr.refresh()
        time.sleep(1)

        # Check for quit.
        try:
            key = stdscr.getch()
            if key != -1 and chr(key).lower() == 'q':
                break
        except Exception:
            break

def main(stdscr):
    # Setup curses: hide the cursor and enable non-blocking input.
    curses.curs_set(0)
    stdscr.nodelay(True)
    # Initialize color pairs.
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)      # Dragon (red)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)    # Castle (green)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Trees (yellow)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)     # Wizard wall (cyan)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # Goblin (magenta)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    max_y, max_x = stdscr.getmaxyx()

    # Draw the castle and trees.
    add_mountains(stdscr)
    castle_y, castle_height, _ = add_castle(stdscr)
    ground_y = castle_y + castle_height
    add_trees(stdscr, ground_y)
    castle_y, castle_height, _= add_castle(stdscr)
    stdscr.refresh()

 
    # --- Define Dragon ASCII Art Frames for Wing-Beating ---
    dragon_art_frame1 = r"""
        \****__              ____
         |    *****\_      --/ *\-__
         /_          (_    ./ ,/----'
         \__         (_./  /
         \__           \___----^__
               _/   _                  \
        |    _/  __/ )\"\ _____         *\
        |\__/   /    ^ ^       \____      )
         \___--"                    \_____ )
                                          "
    """
    dragon_art_frame2 = r"""
        \****  __             ____
         |    ****  \_      --/ *\-__
         /_          (_    ./ ,/----'
         \__         (_./  /
         \__           \___----^__
               _/   _                  \
        |    _/  __/ )\"\ _____         *\
        |\__/   /    ^ ^       \____      )
         \___--"                    \_____ )
                                          "
    """
    dragon_frame1 = dragon_art_frame1.strip("\n").splitlines()
    dragon_frame2 = dragon_art_frame2.strip("\n").splitlines()
    # Use frame1's width (assume both frames have similar width).
    dragon_width = max(len(line) for line in dragon_frame1)
    # Set up for continuous wrap-around.
    total_width = max_x + dragon_width
    # We'll let dragon_pos cycle continuously.
    dragon_pos = 0
    # Position the dragon a few lines above the castle.
    dragon_y = castle_y - len(dragon_frame1) - 2
    if dragon_y < 0:
        dragon_y = 0

    # --- Animate Dragon Flying Overhead Continuously for One Minute ---
    start_time = time.time()
    speed = 2    # columns per frame
    delay = 0.1  # seconds per frame
    frame_count = 0

    while time.time() - start_time < 10:
        stdscr.erase()
        add_castle(stdscr)
        add_trees(stdscr, ground_y)
        add_mountains(stdscr)
        # Alternate between frames to simulate wing beating.
        if frame_count % 2 == 0:
            current_dragon = dragon_frame1
        else:
            current_dragon = dragon_frame2

        # Compute effective x so that the dragon never vanishes:
        eff_x = (dragon_pos % total_width) - dragon_width
        # Draw two copies for a continuous wrap-around.
        add_dragon(stdscr, eff_x, dragon_y, current_dragon)
        add_dragon(stdscr, eff_x + total_width, dragon_y, current_dragon)
        stdscr.refresh()
        time.sleep(delay)
        dragon_pos = (dragon_pos + speed) % total_width
        frame_count += 1

        # Allow early quit.
        try:
            key = stdscr.getch()
            if key != -1 and chr(key).lower() == 'q':
                return
        except Exception:
            pass

    # --- After One Minute, Animate Wizard and Then Goblin Loop ---
    stdscr.erase()
    add_castle(stdscr)
    add_trees(stdscr, ground_y)
    add_mountains(stdscr)
    stdscr.refresh()
    animate_wizard(stdscr, max_y, max_x)
    animate_goblin_loop(stdscr, max_y, max_x)

curses.wrapper(main)
