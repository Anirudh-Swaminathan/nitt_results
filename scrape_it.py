#!/usr/bin/env python3

from scraper import ResultScraper as RS
from argparse import ArgumentParser

def main():
    """main method"""
    parser = ArgumentParser(
            description='Fetch Student Results using Delta\'s server'
            )
    parser.add_argument(
            "-r",
            "--roll_number",
            dest="uname",
            help="NITT Rollnumber",
            type=str,
            required=True
            )
    parser.add_argument(
            "-p",
            "--password",
            dest="pwd",
            help="Webmail or Octa Password",
            type=str,
            required=True
            )
    args = parser.parse_args()
    if None in [args.uname, args.pwd]:
        print("Please enter both roll number and password")
    else:
        data = dict()
        data['uname'] = args.uname
        data['pwd'] = args.pwd
        rCls = RS(data)
        rCls.print_results()

if __name__ == "__main__":
    main()
