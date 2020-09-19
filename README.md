# Hangman-Pygame
It is a simple game named HANGMAN made by python and python library *Pygame*. You have to guess the word before hangman hangs.


Hangman rules:  
A word would be displayed with underscores _ _ _ _ like this. You have to guess it by clicking the buttons of letters below. 
If you choose a letter which was not in the word, Hangman's face will appear. After 6 chances his whole body will appear and you will lost. 

How it chooses a word?
The words are written comma-separted in word_w.txt file. It chooses random word from that file. 
The code to read the text file and make into a list is writtem in words.py

To customize the words, write the words comma seprated in words_w.txt. Without newlines. Unless it automatically does.  
