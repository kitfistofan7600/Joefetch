Joefetch is a minimal neofetch-type script that I created and its goes like this as an example:

![image](https://github.com/user-attachments/assets/b87f266f-a675-4c6d-b494-fe70ed5ee231)


I have written this in Python it took me a couple of programming languages before I settled on Python

For now this script only works on Unix-Like systems (I do not know if I will port it to other platforms.) (I have yet to test it on BSD and macOS)

To run it:

`python3 joefetch.py`




To create an executable:

Install pyinstaller:

`pip install pyinstaller`

Create the executable:

`pyinstaller --onefile joefetch.py`

This will create the folders `build` and `dist`. In which the `dist` directory contains the executable




To install:

In the working directory run:

`sudo/doas mv dist/joefetch /usr/bin/joefetch`

To test if it works run this in the bash prompt:

`joefetch`


It is currently not perfect









