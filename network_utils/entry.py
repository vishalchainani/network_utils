#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import argparse, argcomplete
from .password_generator import generate_password

def cli_entry_point():
    parser = argparse.ArgumentParser(description="Network Utilities CLI")
    parser.add_argument('-v','--version', dest='command', action='store_const', const='version', help='Show version and exit')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    passwd_generator_parser = subparsers.add_parser('passwd-generator', help='Generate a random password')
    passwd_generator_parser.add_argument('-l','--length', type=int, default=8, help='Length of the password')
    # print("This is the entry point for the network-utils CLI.")
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    if args.command == 'passwd-generator':
        length = args.length
        print(f"Generating a password of length {length}")
        print("Here is your password:", generate_password(length))
    elif args.command == 'version':
        get_version()
    else:
        parser.print_help()

def get_version():
    import pkg_resources
    version = pkg_resources.get_distribution("network-utils").version
    print(f"Version: {version}")
    exit(0)
