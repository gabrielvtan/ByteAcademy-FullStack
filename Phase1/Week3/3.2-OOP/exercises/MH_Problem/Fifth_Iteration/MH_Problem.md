
## The Monty Hall Problem

Loosely based on the 1960s game show "Let's Make a Deal", the Monty Hall problem is a paradox in probability.

A player is presented with three doors from which to choose. Behind one of the doors is a brand new car. Behind the other two are goats. The winning door is completely random.

Obviously the player wants to win the new car, and must pick a door to open, hoping to reveal it.

Before it is revealed however, the host will open one of the doors for the player to reveal one of the goats. The player can choose to stick with their original choice, or change their choice and pick the one other possible door.

## First Iteration

Using the Model-View-Controller pattern, let's first build out a terminal application for users to play the game.

#### The View

Let's keep all messages and user prompts inside the views file. If you would like you can create a class to hold the views, or you can just use the file as a module.

Just don't hold any state in the views. Every variable, likely just user choices, should be passed back to the controller.

#### The Models

We'll be using the models for two things:

1. To handle any "business logic" the program needs. An example would be generating what's behind each door.

2. To commit to the database. Let's save user names, whether they chose to switch their choice or not when prompted, and whether they won the car.

A model in general should not communicate with other models, and should definitely not communicate directly with views. All communication should be handled through the controller.

#### The Controller

No spaghetti code! All user choices should be passed from the views back to the controller. Any business logic should be passed from the models to the controller. Any data that needs persistence should be sent from the controller to the model that writes to the db.

Before you move on, make sure you can play your game without error, that it tells you whether you won or not, and that it commits the correct data to the db.

## Second Iteration

Now for the fun part.

Copy your code into a different folder because we're going to hack it up. You shouldn't even need your views anymore.

Change your code so that it runs automated - the computer is the one choosing the door, and choosing whether or not to change their choice after the host's reveal. This should all be at random to ensure an equitable range of choices.

You should write the same data to the db as previously.

Run your program 100,000 times.

Write another program to query the database and return to you the percentage of times the choice was changed after the reveal and the car was won, and the percentage of times the choice was not changed after the reveal and the car was won.

Write your findings in this file. Read through the [wikipedia](http://en.wikipedia.org/wiki/Monty_Hall_problem)
