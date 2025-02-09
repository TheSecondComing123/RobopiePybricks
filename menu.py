from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

menu_options = ("1", "2", "3", "4")

hub = PrimeHub()

while True:
    hub.system.set_stop_button(None)  # Disable the stop button for the menu
    menu_index = 0

    # Menu loop
    while True:
        hub.display.char(menu_options[menu_index])

        # Wait for a button to be pressed
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)
        
        # Wait for the button to be released
        while hub.buttons.pressed():
            wait(10)

        # Check which button was pressed
        if Button.CENTER in pressed:
            # Center button pressed, break out of menu loop
            break
        elif Button.LEFT in pressed:
            # Left button pressed, increment menu index
            menu_index = (menu_index + 1) % len(menu_options)
        elif Button.RIGHT in pressed:
            # Right button pressed, decrement menu index
            menu_index = (menu_index - 1) % len(menu_options)

    # Restore the stop button functionality
    hub.system.set_stop_button(Button.CENTER)

    # Based on the selection, choose a program and run it
    selected = str(menu_options[menu_index])
    
    if selected == "1":
        import run1
    elif selected == "2":
        import run4
    elif selected == "3":
        import krakens
    elif selected == "4":
        import stick

    wait(1000)  # Short delay before the menu shows again
