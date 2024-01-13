# AutoClicker in Python
## Introduction
This repository contains a simple AutoClicker script written in Python using the pynput library. The AutoClicker is designed to simulate mouse clicks or any keyboard key at a specified delay interval. Feel free to customize the script according to your needs.

## Installation
Before using this AutoClicker, make sure to install the required dependencies. You can install them using the following command:

`pip install pynput`
## Usage
Run the script by executing the following command in your terminal:

`py [script path]`

### Start / Stop
**Press the designated start/stop key to toggle the AutoClicker on and off.**

_By default, the start/stop key is set to $._

To change it, change the value of the start_stop_key variable in the script, here it is `$`.

`start_stop_key = KeyCode(char='$')`

### Exit
**Press the exit key to stop the AutoClicker and exit the program.**

_By default, the exit key is set to £._

To change it, change the value of the exit_key variable in the script, here it is `£`.

`exit_key = KeyCode(char='£')`

### Delay between clicks
_By default, the delay is set to 0.001 sec._

To change it, change the value of the delay variable in the script, here it is `0.001`.

`delay = 0.001`

### Button
_By default, the button is set to left mouse button._

To change it, change the value of the button variable in the script, here it is `Button.left`.

`button = Button.left`

## Disclaimer
* This AutoClicker is intended for educational purposes only and should not be used for any form of cheating or unethical activities. Please use this tool responsibly and in compliance with the terms of service of the applications or games you interact with.

* Misuse of this AutoClicker may result in consequences, such as being banned from certain services or games. Be aware of the rules and guidelines of the platforms you use and exercise caution while utilizing this tool.

* Always be mindful of the ethical implications of your actions.
