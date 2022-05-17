import sys
from behave.__main__ import main as behave_main

tags = ['wallabot_launch_and_save_in_file_all_items']

if __name__ == '__main__':
    sys.exit(behave_main(['-t @'+ str(tags[0])]))