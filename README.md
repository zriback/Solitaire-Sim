# Solitaire-Sim

This repository is dedicated to the development of a python program designed to simulation thousands if not millions of solitaire games as quickly as possible. The idea is to learn about the game by simply making the computer play the game a lot using different strategies and keeping track of different statistics.

Some questions I hope to answer with this project are:

	What percent of solitaire games are winnable using a given strategy?
	
	What is the best strategy to use to win the most games?
	
	What percent of starting deck combinations are actually winnable?
	
		Is it possible for a given starting configuration to be literally unwinnable regardless of strategy?

The code uses a breadth first search algorithm to search through all possible states and paths the game could take from the start depending on what moves a player could choose. That is to say that every time there is more than one move, the simulation branches out and plays both moves. It repeats this branching process for each time there is more than one move to choose from. It does this until it finds a path to a winning solution, or until it it exhausts all paths thereby finding that there is no solution.

## Breadth First Search Implementation

The starting state of the game is the first configuration that is looked at. Its successors are generated from all the possible single moves that could be done. Moving one card in the tableau is a single move, moving one stack of cards in the tableau is one move, moving one card from the hand is one move, dealing out more cards from the hand is one move, etc.

For every successor that is generated, it is first checked against the keys of a dictionary. If the successor is already in this dictionary, then it means that configuration has already been looked at so we do not need to move further with it. If the configuration is not in this dictionary, it means it is the first time we are seeing it. It would then be first added to the dictionary, where the key is the config itself and the value is the parent that it came from. The config is then added to the end of a queue of configurations to be looked at. When a configuration is picked from the queue, it is treated as the parent and it has its successors generated and the process repeats.

After a game is solved, and if a solution is found, then the dictionary can be used to construct a path of moves to do in order to reach a solution.

See the "An Imperfect Simulation" section below for details on how this algorithm had to be modified for the sake of time.

## Lesser Known Terminology
Here is some of the lesser known solitaire terminology that is used in this project
	
	Tableau - the area where the game is played with seven piles of cards
	
	Stock - the deck from which new cards are introduced into the tableau by the player
	
	Foundation - the area where cards are collected by suit. The game is won when all cards are in their proper place in the foundation
	
	Source, and some more terms:
	https://www.semicolon.com/Solitaire/Rules/Glossary.html#Skill
	
## Rules
	
Depending on who you ask or what version of the game you are playing the rules of solitaire can change a little bit. Because of this I will briefly go over some of the small rules that can change and what rule I used when building the simulation

#### Moving cards from the foundation

In some games you are allowed to take back cards you already put in the foundation and move them back into the tableau. I found that in most versions of the game you are allowed to do this, even if human players don't take advantage of it often. In any case it is possible for a game to only be winnable due to this type of move. In this simulation this is allowed.

#### Moving cards from the hand

In the version of solitaire played by the program, the cards in the hand can be utilized and dealt out even if there are other valid moves. This means that a move in the tableau or foundation can be ignored in favor of using cards from the hand. This feature drastically increases the amount of the games that are winnable, although human players almost never intentionally would ignore moves in the tableau or foundation in favor of using the cards in their hand. 

Depending on the difficulty of the game, cards can be dealt out from the hand differently. For a more easy game cards are dealt from the face down pile into the face up pile one at a time. For a more difficult game they are usually dealt two at a time. The code allows for this value to be easily changed, but for all my testing and analysis cards were dealt from the hand three at a time.

# An Imperfect Simulation

My original intention with this project was to deal out a game of solitaire, and then make the computer play along every possible path that game could take. This means that every time a player would have the choice between two moves, the program would create a branch and play through both possibilities. Unfortunately, as it turns out, most solitaire games end up branching out so much that there are millions of different states the game could take. The program is unable to process these all and search for solutions in a reasonable amount of time.

Due to this fact, the simulation has to make some concessions for the sake of time. The program implements a sort of pruning process because of this in order to limit the amount of games that it needs to check. It keeps track of the maximum amount of cards that the game has thus far been able to get into the foundation. Periodically, the program will run through the entire queue of games that still need to be looked at and remove all the games that have too many cards less than the max. The amount of cards in the foundation that games have to be within of the maximum is the the pruning threshold. In order to maximize the amount of games that are solvable in a reasonable amount of time I found that the optimal value for this is 1 card. This means that if the maximum amount of cards any configuration the game has looked at has had in the foundation is twenty cards, then when it is time for pruning all games with 18 or fewer cards will be removed from the queue, meaning they will never be looked at by the solver. As for how often the pruning happens, (or the pruning interval), I settled on a value of 500, meaning that every 500 games added to the queue the pruning will take place. 

In addition to pruning, not every single successor for a configuration is always generated. In general, if a single card can be moved to multiple places in the tableau, only one of those moves will be generated. Additionally, if a card can be moved to the tableau but can also be moved to the foundation then only the foundation move will be generated.

Finally, there is one last catch to make the program running reasonably fast. If any game is taking over 500 seconds to evaluate, the program will just kill the solver, and the game will be marked as unwinnable. Unfortunately, for reasons I cannot yet discern some games will run for a very long time. Perhaps there are just too many move options very early on in these games and so the amount of configurations in the queue balloons too quickly for pruning or for the program's evaluation to keep up. In any case, in my limited experience, many of the game that take this long or longer are losers anyway, and so killing them for the sake of time is not too big a loss.

# Results

### Percent of all games that are winnable

Since there are 52! different combinations of starting decks, it is impossible to test them all. In fact, if you shuffle a deck of cards well and then deal them out, it is almost guaranteed that game of solitaire has never been played before. However, we can still get a good idea of the proportions of games that are winnable by testing enough randomly generated games using the breadth first search algorithm outlined in this document.

This program is able to find a solution for about 60% of randomly generated solitaire games. A quick google search gives a figure of 80% for the percent of games that are winnable, but due to the concessions the program had to make on account of not having access to infinite computing power, this appears to be the highest this program will be able to achieve. One thing the program can do that the google search cannot is actually provide a solution to solving the given game of solitaire; it is able to give all the steps that one would need to take in order to win the game. This shows us that most solitaire games can be solved in around 80 to 120 moves.

Additionally, as a consequence of these figures, yes, there are plenty of games that are unwinnable regardless of what a player does. It would be interesting if you were able to tell the chances of a game being winnable just based on the seven face up cards displayed at the very beginning of the game. If someone could do this, they would be able to not even bother playing a game if they think they had no chance of winning it!

### Human players

Human players do not have luxury of being able to try out several different moves each time they have multiple options; they have to choose one move and if it was the wrong one then it could sentence them to losing the game. When simulating how a human plays the game, I assumed a couple of things:

	Human players move cards to the foundation before anything else.
	
	Human players move cards in the tableau before going to the cards in their hand.
	
	Human players only deal out more cards from their hand if they have no other options.
	
Assuming these things about the average or casual solitaire player, it is very easy to simulate thousands of games using these strategies.

	Using these rules, about 20% of games will be winnable by a human.
	
	The easiest strategy to implement that boosts your chances a little is to take cards away from the largest piles in the tableau. Doing this takes you chances from around 	  14% to 16% to around 20% of games winnable. This makes sense as moving cards from that area increases your chances of eventually uncovering a vital card that is need to 	   win.
	
	
