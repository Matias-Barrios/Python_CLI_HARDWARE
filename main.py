#!/usr/bin/python3

import command_line.command_line as cmd
import sys
import handlers.handlers as hdl

def main(a) :
    if hasattr(a, 'which') :
        print(str(hdl.get_handler(a.which)()))
    else :
        print("Please choose a subcommand!")

main(cmd.get_parameters())

