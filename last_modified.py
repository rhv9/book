import json
import sys
import logging
import os
import time
import subprocess
import datetime

class FileLogger:
    def __init__(self, log_file: str, log_level: int = logging.INFO):
        self.log_file = log_file

        # Create the logger
        self.logger = logging.getLogger('FileLogger')
        self.logger.setLevel(log_level)

        # Ensure we don't add multiple handlers if this is called multiple times
        if not self.logger.handlers:
            if os.path.exists(log_file):
                os.remove(log_file)

            # Create the file handler
            file_handler = logging.FileHandler(self.log_file)
            file_handler.setLevel(log_level)

            # Create a formatter and set it for the handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Add the handler to the logger
            self.logger.addHandler(file_handler)

    def print(self, message: str):
        self.logger.info(message)

def recursiveEdit(items):
    for section in items:
        if section == "Separator" or section == None:
            continue
        
        chapterName = section['Chapter']['name']
        chapterPath = section['Chapter']['source_path']

        if chapterPath != None:
            file_path = "./pages/" + chapterPath
            process = subprocess.run(["git", "log", "-1", "--format=%cd", file_path], capture_output=True)
            # mtime = os.path.getmtime(file_path)
            # mTimeString = time.ctime(mtime)
            # readableElapsedTime = getReadableTimeAgo(time.time(), mtime)
            mTimeString = str(process.stdout)[2:-2]
            
            readableElapsedTime = ""
            logger.print("Last modified time:" + mTimeString)

            section['Chapter']['content'] = "*last modified: "+readableElapsedTime+" ("+mTimeString+")*\n\n" + section['Chapter']['content']

        chapterSubItems = section['Chapter']['sub_items']

        logger.print(chapterName + ", path: " + str(chapterPath))

        if len(chapterSubItems) != 0:
            recursiveEdit(chapterSubItems)


def getReadableTimeAgo(tbig, tsmall):
    week = 60 * 60 * 24 * 7
    seconds = tbig - tsmall

    # within minute, give seconds
    if seconds < 60:
        return str(seconds) + " seconds ago"
    
    # within hour, give minutes
    minutes = seconds / 60.0
    if minutes < 60.0:
        return str(round(minutes)) + " minutes ago"

    # within day, give hours
    hours = minutes / 60.0
    if hours < 24:
        return str(round(hours)) + " hours ago"
    
    # within week, give days
    days = hours / 24.0
    if days < 7:
        return str(round(days)) + " days ago"
    
    # within within a month, give weeks
    weeks = days / 7.0
    if weeks < 4:
        return round(weeks) + " weeks ago"
    
    # within a year, give months
    

    # give years

    return tbig - tsmall


            
if __name__ == '__main__':
    if len(sys.argv) > 1: # we check if we received any argument
        if sys.argv[1] == "supports": 
            # then we are good to return an exit status code of 0, since the other argument will just be the renderer's name
            sys.exit(0)

    # load both the context and the book representations from stdin
    context, book = json.load(sys.stdin)
    # and now, we can just modify the content of the first chapter
    book['sections'][0]['Chapter']['content'] = '# Hello'
    
    # Dump json
    # f = open("jsonDump.json", "w")
    # f.write(json.dumps(book))
    
    # Debugging printer
    logger = FileLogger("preprocessor.log")

    i = 0

    recursiveEdit(book['sections'])


    # we are done with the book's modification, we can just print it to stdout, 
    print(json.dumps(book)) 