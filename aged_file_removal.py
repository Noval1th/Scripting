#!/usr/bin/env python3

import os
from pathlib import Path
import datetime
import argparse


def checkdate(modifytime, purgedate):
    if datetime.date.fromtimestamp(modifytime) < purgedate:
        return True


def purgescript(root, purgedays):
    purgedate = datetime.date.today() - datetime.timedelta(days=purgedays)
    rootdir = Path(root)
    for subdir, dirs, files in os.walk(rootdir):
        curpath = Path(rootdir) / subdir
        print(f'\nchecking path: {curpath}')
        for file in files:
            curfile = Path(rootdir) / subdir / file
            if checkdate(os.path.getmtime(curfile), purgedate):
                print(f'Modify Date outside of Save range of {purgedays} days, deleting file {curfile}')
                Path.unlink(curfile)
            else:
                print(f'Modify Date inside of Save range of {purgedays} days, saving file {curfile}')


parser = argparse.ArgumentParser(prog='Cleanup')
parser.add_argument('--path', help='The Directory to cleanup', required=True)
parser.add_argument('--days', type=int, help='Number of days to save', required=True)
args = parser.parse_args()

path = args.path
days = args.days

if __name__ == "main":
    purgescript(path, days)
