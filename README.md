# Solitaire-Sim

This repository is dedicated to the development of a python program designed to simulation thousands if not millions of solitaire games as quickly as possible. The idea is to learn about the game by simply making the computer play the game a lot using different strategies and keeping track of different statistics.

Some questions I hope to answer with this project are:

	What percent of solitaire games are winnable using a given strategy?
	
	What is the best strategy to use to win the most games?
	
	What percent of starting deck combinations are actually winnable?
	
		Is it possible for a given starting configuration to be literally unwinnable regardless of strategy?

## What the code does

Please check the lesser known terminology and rules headers below in order to fully understand this section.



# Lesser Known Terminology
Here is some of the lesser known solitaire terminology that is used in this project
	
	Tableau - the area where the game is played with seven piles of cards
	
	Stock - the deck from which new cards are introduced into the tableau by the player
	
	Foundation - the area where cards are collected by suit. The game is won when all cards are in their proper place in the foundation
	
	Source, and some more terms:
	https://www.semicolon.com/Solitaire/Rules/Glossary.html#Skill
	
# Rules
	
Depending on who you ask or what version of the game you are playing the rules of solitaire can change a little bit. Because of this I will breifly go over some of the small rules that can change and what rule I used when building the simulation

#### Moving cards from the foundation

In some games you are allowed to take back cards you already put in the foundation and move them back into the tableau. I found that in most versions of the game you are allowed to do this, even if human players don't take advantage of it often. In any case it is possible for a game to only be winnable due to this type of move. In this simulation this is allowed.

#### Moving cards from the hand

In the version of solitaire played by the program, the cards in the hand can be utlized and dealt out even if there are other valid moves. This means that a move in the tableau or foundation can be ignored in favor of using cards from the hand. This feature drastically increases the amount of the games that are winnable, although human players almost never intentionally would ignore moves in favor of using the cards in their hand. 

Depending on the difficulty of the game, cards can be dealt out from the hand differently. For a more easy game cards are dealt from the face down pile into the face up pile one at a time. For a more difficult game they are usually dealt two at a time. The code allows for this value to be easily changed, but for all my testing and analysis cards were dealt from the hand three at a time.

# An Imperfect Simulation

My original intention with this project was to deal out a game of solitaire, and then make the computer play along every possible path that game could take. This means that every time a player would have the choice between two moves, the program would create a branch and play through both possibilities. Unfortunately, as it turns out, most solitaire games end up branching out so much that there are hundreds of thousands of different states the game could take. The program is unable to process these all and search for solutions in a reasonable amount of time.
