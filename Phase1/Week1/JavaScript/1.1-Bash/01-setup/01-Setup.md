# Python Foundations
## Week 1, Day 1 - Environment Setup

### Part 1 - System Update

- Mac users, update your system and make sure you have the latest version of OS X (High Sierra)  Apple's instructions are [https://support.apple.com/en-us/HT201541]

- Windows users, you need Windows 10 installed. Unfortunately, this is not free if you have 7 or 8. Run Windows update.

- Windows users will also need an account with Microsoft's app store, but the app you will need to install (Ubuntu 18.04) is free.

- On both Windows and Mac, you need to be using an account with administrator privileges.

- If you are using a Linux distribution, you should be on its latest stable release. (18.04 for Ubuntu). If that release's python3 package is of a version prior to 3.6, you should look up how to manually upgrade.

### Part 2 - VSCode

* Download and install VSCode from [https://code.visualstudio.com/].

* Now open VSCode.

* First go to View -> Extensions in the menu.

* Search for and install the following extensions. If you have used VSCode in the past, you should disable all other extensions.

* * Python (by Microsoft)
* * Code Runner (by Jun Han)
* * Markdown Preview Enhanced (by Yiyi Wang)
* * JetJet-theme (byJohny Georges)

* Now close the extensions tab. There is a small x that appears when you
hover your mouse over the name of the tab (above the editor). Click it.

* Now go to File -> Preferences -> Settings

* On the right hand side of this view, click 'User Settings.' It should now say 'Place your settings here to override the default settings'

* Delete any settings that are there and copy the following code into the
editor.


```json
{
    /* Projector-friendly colors */
    "workbench.colorTheme": "JetJet-Light",
 
    /* No hints! (comment out after phase 1 if you like) */
    "editor.quickSuggestions": false,
    "editor.suggestOnTriggerCharacters": false,
    "editor.wordBasedSuggestions": false,
    "editor.quickSuggestionsDelay": 1000000,
    "editor.tabCompletion": false,
    "editor.parameterHints": false,
    "python.linting.enabled": false,
    
    /* use system terminal and python environment */
    "code-runner.runInTerminal": true,

    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\bash.exe",
 }
```

* Hit Ctrl-s or Command-s (for mac) to save your changes. You can also use
File -> Save in the menu.

* If your editor had a dark background, it should now be light!

* Now close the settings tab. Keep VSCode open for the next part.

* Now you will need to configure some things to get python working.

### Part 3 - python and the shell

#### Mac instructions:

* In VSCode open the **terminal** by holding Command and the key to the left
of the numbers with ~ and \` on it. These are called tilde and backtick.

* Click in the new window that opens.

* Now copy and paste the following command into that window:

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* If it didn't start running after you pasted, press 'Enter.' It will take a minute or two to install.

* Now type the following command and hit enter:

```sh
brew install python
```

* You should be all ready! Close the terminal window.

* In the future, you can issue command-line commands either from VSCode's terminal you access with Command + ~ or in the OS X "terminal" app. There is a Mac app called iTerm2 that some people prefer to the built-in terminal.

#### Windows:

* Unfortunately Windows is a little bit more complicated.

* Windows 10 and a Microsoft Store account are requirements.

* Type 'Powershell' into the search bar at the bottom of the screen. Right click the program that it finds and select 'Run as administrator.'

* In the window that opens up, there will be a prompt ending in '\>' copy the following command
and hit enter.

```cmd.exe
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

* After that command finishes running, you can close Powershell.

* Open the Microsoft store. Search for 'Ubuntu 18.04', install it. Fortunately this
is free!

* If Ubuntu doesn't begin running after install, search for the application and run it.

* You will be asked to create a username and password. It's ok if your password is simple and easy to remember, this won't be available online.

* Once you have, you can exit.

* Open VSCode and then hold down the Control key and press the key to the left of the numbers
labeled '~ \`'

* Click in the window that opens at the bottom of the screen. It should show you a prompt
that ends in a $. If it ends in a \>, make sure your VSCode user settings are as described above.

* Continue following the instructions after the next heading.

##### Windows users, keep going. Linux users, you can start here.

* Type the following commands and hit enter after each one. Some of them might take a little while
to complete. When you execute a command with sudo (which is like 'Run as Administor' on Linux) you will need to type the username and password you set when you installed Linux.

```sh
sudo apt update
sudo apt upgraded
sudo apt install python3 python3-pip
echo "alias python=python3" >> ~.bashrc
```

* * If you are using Linux and not on a Debian-based system (Debian, Ubuntu, Mint, etc.) use your distribution's package manager to install python (and pip if it is in a separate package). Make sure you have python 3.6 or greater. You will need to alias python to python3.

* Now you can close the terminal window in VSCode. Ok! You should be good! Thanks for your patience!

### Part3 - Your folder for work

* Create a folder on your system called 'foundation' or 'byte'
  (if you are on Windows, ask for help creating a location that
  is accessible to both Windows and the Linux Subsystem.)

* * What you want to do in Windows is find a folder in your Linux directories' home folder and create a Windows shortcut to it on your Desktop or in your Documents folder or somewhere like that. Information on how to find you Linux directories is here [https://askubuntu.com/questions/759880/where-is-the-ubuntu-file-system-root-directory-in-windows-subsystem-for-linux-an] and then your home folder in Linux is home/yourusername

* Create a folder in that folder called 'week1' inside of 'foundation.'

* Now download day1.zip (that I will give you) move it to the week1 folder
you made. Unzip it. This will create a folder called day1.

### Part 4 - Open your work folder and do an assignment.

* Now in VSCode go to File -> Open Folder. Find the 'byte' or 'foundation' folder you created. Open week1.

* Play around with the Explorer on the left hand side of the screen. Click on the arrows next to sub-folders to see what is inside them. Click on a file to open it in an editor window. Click the close 'x' on that file's tab to make it go away.

* Note: you may sometimes hear the word 'directory.' It just means folder.

* Files that end in .md are instructions. They are written in 'markdown.' You'll learn more about that later. To see a markdown file with the right formatting, right-click (Windows, some Mac setups) or hold Ctrl and click (on Mac) on the .md file and select 'Open Preview'

* Once you're feeling a little bit comfortable, open the the 'day1' folder, then the '02-HelloWorld' folder and then look at the preview for '02-HelloWorld.md' These are the instructions for your first coding exercise.

* In the Explorer, hover your mouse over the 02-HelloWorld folder name. You should see an icon appear that looks like a piece of paper with a + on it. Click it. This will open a text box where you can type the name of a new file. Call your file something like 'solution.py' The name should have no spaces and it must end in .py

* Try to solve the assignment. To test your solution, save your file by hitting Ctrl-s (Command-s on Mac) then right-click or Ctrl-click (Mac) on the contents of the editor tab where you are editing your code. Click 'Run code' you should see the output in the terminal window.

### Part 5 to Infinity: Ask your cohort-mates, the TAs, or the instructors for help!

* This is a school! If you already knew how to do this stuff, you wouldn't be here. When you get stuck, ask for help.