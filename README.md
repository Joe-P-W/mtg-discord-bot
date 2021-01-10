# Magic the Gathering Discord Bot
A bot to aid the playing of Magic the Gathering over Discord

## Invite MTG Bot to your discord server:
https://discord.com/api/oauth2/authorize?client_id=698834698381819915&permissions=522304&scope=bot

## Searching the Scryfall Database:
To search the database of cards simply put "/s" followed by the card name you want to search.  
Example: `/s jace beleren` will return you the results for the card Jace Beleren

The search uses fuzzy matching so you can slightly misspell the card and still get a match.

## Rolling
- To roll a d6 simply type into the discord chat "/r d6"
- To roll multiple of the same dice "/r 2d8"
- To roll different dice "/r 1d8 + 2d12"
- To roll with an added bonus "/r 1d20 + 7"
- To roll with a multiplicative bonus "/r 2d6*2"

## Flipping coins
- To flip a coin "/flip"  
- To flip multiple coins "/flip 6"
- To flip until a given output "/flip until heads"
- To flip until a given output with Krark's Thumb "/flip until head with thumb"

## Using MTG Bot as a calculator
- You can use the bot as a basic calculator "/c (7 + 5)*6"