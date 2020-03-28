# Micro:bit Quiz Runner

This contains the code for the micro:but + PC Quiz Runner Application.

## Hardware required

You will need a PC, Raspberry Pi or laptop that can run Python3 and a micro:bit for the host running thw quiz.
You will also need a micro:bit for each quiz team.

You'll need a USB data cable to connect the PC and the runner micro:bit and a power source (battery or USB power cable) for each team's micro:bit.

## Software installation

Clone this repository into the directory of your choice by running `git clone xxx` in that dictory.

I use the mu editor to install software on the micro:bits, but you can use another technique if you prefer.

All the software is in the `src` directory of the repository.

Install `mb_runner.py` on the runner's micro:bit and `mb.player.py` on each team's micro:bit.

Run `pip3 install guizero pyserial microfs` to install the required software packages on your pc or laptop.

Now you're ready to run a quiz.

## Running a quiz

You can read details of how to run a quiz [here](overview.md).


