# The Line of Battle
The Line of Battle is a game based on the game Battleship by Hasbro.  In this version, the player faces off against a computer.  Both computer and player have 10 ships placed randomly on a 6 X 6 grid.  Each ship covers one space.  Player and computer alternate guessing which space has
Live demo[_here_](https://the-line-of-battle.herokuapp.com/)

## Table of Contents
* [UX](#ux)
  * [Site Owner Goals](#site-owner-goals)      
  * [Structure](#structure)
  * [Wireframes](#wireframes)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
  * [Issues](#issues)
* [Deployment](#deployment)
* [Credits](#credits)
* [Contact](#contact)



## UX
### Site Owner Goals
- 
### Site User Goals
#### First Time User

### Structure



## Features
### Existing Features
 - The game opens with a 

### Features to Implement



## Technologies Used
- Python for structure and function
- GitHub for software hosting
- GitPod for development hosting
- Git for version control


## Testing
- The code was run through the PEP8 code validator and returned no errors.
- Throughout development testing of the code was done in both the Heroku environment and the gitpod terminal.  Several issues were identified and fixed.
  - The name input function did not return an error if no name was input.
     - This was fixed by creating a separate name_check function.
  - The boards were not printing when called and displayed an error stating list index out of range.
    - The range was not properly zero-indexed.
  - Target selection was not returning a warning that selected coordinates were already used if that previous shot was a hit.
    - Resorted if/elif/else statement to check for previously called shots before checking to see if the shot was a hit.
  - Inputs for single letter answers (start function, column input) were not recognising lowercase letters.
    - Added .upper() to inputs with single letter requirements.
  - When selecting a column or row to fire at, if 2 consecutive letters or numbers, i.e. BC or 23 were selected, the input would cause an error.
    - Instead of checking the input against a string ("123456") or ("ABCDEFG") the input was changed to check against a list of valid options.
  - The game was initially set to take input in a column, row order.  This resulted in the coordinates being interpreted backwards.  For example, A2 should be in the first column and second row, but would appear in the second column and first row.
    - All inputs and functions were changed to take row then column.  This resulted in input and output matching.


  


## Deployment
- The site was deployed to Heroku as follows:
  - I logged in to Heroku and selected create new app
  - The Line of Battle was set as the name and the region was set to Europe, and then Create app was selected
  - In settings, Config Vars was chosen and the key Port was input with a value of 8000
  - Also in settings, Python and Node.js buildpacks were added in that order.
  - On the deploy tab, Github was selected for the deployment method, and then connect.
  - The automatic deploy option was chosen.
  - Deploy branch was selected.


## Credits
- Python time module explanation was found on [_Career Karma_](https://careerkarma.com/blog/python-time/)
- Printing in colour in terminal was found on [_stackabuse_](https://stackabuse.com/how-to-print-colored-text-in-python/)
- Several instances of the print_board function were found, including the Youtube channel Knowledge Mavens and Github user Faris-07



## Contact
Created by Andrew Stanek (notandystanek@gmail.com)