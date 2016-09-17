#!/usr/bin/env python
import getpass
import os
import sys

# Tanaka would have gotten it right.
def run():
        user = getpass.getuser()
        if len(sys.argv) > 1:
                user = sys.argv[1]
        directory = get_directory(user)
        rename_all_screenshots(directory)

def get_directory(user):
        target_directory = 'C:\\Users\\{u}\\Documents\\My Games\\' \
                           'FINAL FANTASY XIV - A Realm Reborn\\' \
                           'screenshots\\'.format(u = user)
        return target_directory

def rename_all_screenshots(directory):
        screenshot_list = os.listdir(directory)
        for s in screenshot_list:
                rename_screenshot_if_necessary(s, directory)
        return

def rename_screenshot_if_necessary(screenshot, directory):
        if screenshot.startswith("ffxiv_"):
                do_rename_screenshot(screenshot, directory)
        return

def do_rename_screenshot(screenshot, directory):
        new_name = get_new_name(screenshot)
        new_file = directory + new_name
        old_file = directory + screenshot
        print("Renaming {o}  >>  {n}".format(o = screenshot, n = new_name))
        os.rename(old_file, new_file)
        return

def get_new_name(old_name):
        date_part = old_name[6:14]
        rest = old_name[14:]
        proper_date = reformat_date(date_part)
        new_name = "ffxivarr_{d}{r}".format(d = proper_date, r = rest)
        return new_name

def reformat_date(bad_date):
        year = bad_date[-4:]
        month = bad_date[2:4]
        day = bad_date[0:2]
        proper_date = "{y}{m}{d}".format(y = year, m = month, d = day)
        return proper_date

run()
