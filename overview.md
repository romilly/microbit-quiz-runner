
People involved in the game:

1. Quiz Host
1. Two or more Teams, each with a Team Captain

The Quiz Host has a micro:bit attached to a laptop, workstation or Raspberry Pi.

Each team has a battery-powered micro:bit

The [README file](README.md) tells you how to install the software.

Apply power to the micro:bits.

On the quiz host's PC,

1. Open a terminal/command window.
1. Change to the directory in which you cloned the repository.
1. Type `python3 src/quizrunner/pc_runner.py'

# Running A Game

1. Before tgame starts the Host gives each Team Captain a micro:bit and tells them their team number.
1. At the start of the game,
    1. The System show a status of 'Waiting to Start Check-in'. 
    1. The Host starts the app.
    1. The Host specifies the number of teams.
    1. The host starts the check-in phase.
    1. The System show a status of 'Teams checking-in'.
    
1. For each Team,
    1. The Host asks the Team to check in.
    1. The Team Captain checks in by pressing button A on their micro:bit.
    1. The System adds the Team to the list of teams.
    
1. When each Team has checked in, a new round starts.
    1. The System displays a status of 'Playing Round xx' where xx is the round number.
    1. The System shows each team's scores. *These will be zero to start with, but will go up as play progresses.*
    1. The Host asks the question and invites teams to buzz.
    1. If a Team thinks they knows the answer, the Team Captain *buzzes* by pressing button A on their micro:bit.
    1. If the answer is right,
        1. The Host says 'Correct'.
        1. The Host clicks the 'Tick button'.
        1. the System shows the updated scores.
        1. The System Returns to step 4.
    1. If the answer is wrong,
        1. The Host says 'Incorrect'.
        1. The Host clicks the 'Cross' button.
    1. If all the teams have tried to answer
        1. The System displays a status of round ended for 5 seconds.
        1. The system returns to step 4.
    1.  If no team wants to answer, the Host can end the round. 
        
            


