# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:20:11 2021

@author: tyler
"""

"""
player starts the game and a word is generated for to guess for
the length of the word is shown through --------
the player is given 7 guesses to guess the word
the player can guess either a letter or a word
each counts as one guess and this subtracts from the total amound of guesses left
input of the word should be case insensitive 
if the player guesses the word correctly they win
if the player guesses the word incorrectly after the guesses goes to 0 they lose
a new game should start after win or lose
"""

#imports random module for random functions
import random

#converts string into a list
def split(x):
    return [y for y in x]

#converts list into a string
def list_string(s): 
    y = "" 
    for i in s:
        y += i
    return y

#opens txt file containing words and ASII images

word_file = open("words.txt")

phase1_file = open("phase1.txt")
phase2_file = open("phase2.txt")
phase3_file = open("phase3.txt")
phase4_file = open("phase4.txt")

phase1_lines = phase1_file.read()
phase2_lines = phase2_file.read()
phase3_lines = phase3_file.read()
phase4_lines = phase4_file.read()


word_lines = word_file.read().splitlines()
for i in range(0,len(word_lines)):
    word_lines[i] = word_lines[i].lower()
word_file.close()
phase1_file.close()
phase2_file.close()
phase3_file.close()
phase4_file.close()

#sets counts for wins, losses, total games

game_count = 0;
win_count = 0;
lose_count = 0;

#list of constants and vowels

constant = ['a', 'e', 'i', 'o', 'u']
vowels = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#wheel of fortune values
fortune_wheel1 = [800, 350, 450, 700,300,600,500,600,500,300,500,800,550,400,300,900,500,300,900,"bankrupt",600,400,300,"lose turn"]

#sets money amount for contestants
contestant1 = 0

#continues to play game until game_count reaches 1000, this allows looping gameplay

while game_count < 1000:
#word to be guessed is found here

    word = random.choice(word_lines)
    word_lines.remove(word)
    print(word)
    word_list = split(word)
    
    guess_list = []

#converts length of the word into a set of dashes so the player knows the lenght of the word
    blank_word = '-'*len(word)

    blank_word_set = split(blank_word)

#count of guesses
    guess_count = 7
#will count so that an image will show depending on value to show progress per game
    progress_count = 0 
    percent_value = 0

#stores values guessed for the given game so that repeats cannot be made
    values_guessed = []
#keeps playing game while count is above 0
    while guess_count > 0:
#returns ascii image based on how well player is doing        
        if percent_value < .33:
            print(phase1_lines)
        elif percent_value < .66 and percent_value >= .33:
            print(phase2_lines)
        elif percent_value < 1 and percent_value >= .66:
            print(phase3_lines)
#shows placeholder dashes that show how many letters are in whord and how many attempts are left
        print('Guess this word:', blank_word,', you have',guess_count,'attempt(s)')
        guess = input().lower().strip()
        guess_count = guess_count - 1
#if then statement for checking if the value is a single character or not
        if len(guess) == 1:
#if value is already used it repeats and adds back one attempt
            if guess in values_guessed:
                print('You already tried this letter, guess again')
                guess_count = guess_count + 1
#attempt is added to list
            else:
                values_guessed.append(guess)
#changes the dashed/place holder word list and add corretly guessed letters to the list
                if guess in word:
                    for i in range(0,len(word)):
                        if word_list[i] == guess:
                            blank_word_set[i] = guess
                            progress_count = progress_count + 1
                blank_word = list_string(blank_word_set)
#if value is greater than on and matches the length of the guess               
        elif len(guess) > 1 and len(guess) == len(word):
             guess_list = split(guess)
             previous_val = progress_count
#if the value was already guessed, it repeats and adds one attempt back
             if guess in values_guessed:
                 print('you already tried this word, try again')
                 guess_count = guess_count +1
#if guess is new, guess is checked against the actual word through a for loop
             else:
                 values_guessed.append(guess)
                 for i in range(0,len(word_list)):
                     if word_list[i] == guess_list[i]:
                         blank_word_set[i] = guess_list[i]
                         progress_count = progress_count + 1
                 blank_word = list_string(blank_word_set)
                 progress_count = progress_count-previous_val
#if the length of the guess is not equal to the length of the word, it returns invalid  
        elif len(guess) > 1 and len(guess) != len(word):
            print('Invalid attempt, try again')
            guess_count = guess_count + 1
#sets conditions for winning, if the blank word is equal to the actual word
#increases win counter
        if blank_word == word:
            response_count = 0
            win_count = win_count + 1
            print(phase4_lines)
            print('You have ',win_count,'wins and ',lose_count,'losses, would you like to play again?')
#while loop that keeps going if you input incorrect response
#yes or no response whether user wants to play again
            while response_count < 2000   :
                response1 = input('type yes or no: ',).strip().lower()
                if response1 =="yes":
                    guess_count = 0
                    response_count = 10001
                elif response1 =="no":
                    guess_count = 0
                    game_count = 10001
                    response_count = 10001
                else:
                    print("incorrect response, try again")
#conditions for losing are set and lose counter increases by one
        elif blank_word != word and guess_count == 0:
            response_count2 = 0
            lose_count = lose_count + 1
            print('you lose')
            print(phase1_lines)
            print('You have ',win_count,'wins and ',lose_count,'losses, would you like to play again?')
#while loop that keeps going if you input incorrect response
#yes or no response whether user wants to play again

            while response_count2 < 2000   :
                response2 = input('type yes or no: ',).strip().lower()
                if response2 =="yes":
                    guess_count = 0
                    response_count2 = 10001
                elif response2 =="no":
                    guess_count = 0
                    game_count = 10001
                    response_count2 = 10001
                else:
                    print("incorrect response, try again")
#percent value is calculated that is tied to the printing of images
        percent_value = (progress_count/len(word))










