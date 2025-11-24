import os
import webbrowser
import pyautogui
import random

commands_file = 'commands.txt'

# Open new tab and navigate to URL
webbrowser.open_new_tab("https://chat.openai.com/chat")

# Wait for Chrome to open a new tab
pyautogui.sleep(3)

# Loop through the commands file and send each request
with open(os.path.join(os.path.dirname(__file__), commands_file), 'r') as f:
    commands = f.readlines()
    for command in commands:
        command = command.strip() # Remove newline characters
        pyautogui.write(command)
        pyautogui.press('enter')
        # Wait for a range of seconds for response to complete before the next prompt. This also helps on timeouts from too many prompts in a given time period.
        pyautogui.sleep(random.uniform(180, 240))
