#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse, argcomplete
from .password_generator import generate_password

def cli_entry_point():
    parser = argparse.ArgumentParser(description="Network Utilities CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    passwd_generator_parser = subparsers.add_parser('passwd-generator', help='Generate a random password')
    passwd_generator_parser.add_argument('--length', type=int, default=8, help='Length of the password')
    # print("This is the entry point for the network-utils CLI.")
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    if args.command == 'passwd-generator':
        length = args.length
        print(f"Generating a password of length {length}")
        print("Here is your password:", generate_password(length))
    else:
        parser.print_help()

