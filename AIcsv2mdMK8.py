TAGS = "#daily, #daylio, #journal"
HOW_ACTIVITIES_ARE_DELIMITED_IN_DAYLIO_EXPORT_CSV = " | "
NOTE_TITLE_PREFIX = "Daylio "
NOTE_TITLE_SUFFIX = ""
HEADER_LEVEL_FOR_INDIVIDUAL_ENTRIES = "##"
DO_YOU_WANT_YOUR_ACTIVITIES_AS_TAGS_IN_OBSIDIAN = False

days = {}

class Entry(object):
    def __init__(self, parsedLine, propInsideDelimiter = HOW_ACTIVITIES_ARE_DELIMITED_IN_DAYLIO_EXPORT_CSV):
        self.time = parsedLine[3]
        self.mood = parsedLine[4]
        self.activities = self.sliceQm(parsedLine[5]).split(propInsideDelimiter)
        self.title = self.sliceQm(parsedLine[6])
        self.note = self.sliceQm(parsedLine[7])

    @staticmethod
    def sliceQm(str):
        if len(str) > 2: return str.strip("\"")
        else: return ""

import csv
import os
import glob

# Get the path of the directory containing the CSV files
directory_path = os.path.dirname(os.path.abspath(__file__))

# Use glob to search for files with the pattern "*.csv" in the directory
csv_files = glob.glob(os.path.join(directory_path, "*.csv"))

# Sort the files by modification time, so the newest file is at the end of the list
csv_files.sort(key=lambda x: os.path.getmtime(x))

# Get the path of the newest file
newest_file = csv_files[-1]

with open(newest_file, newline='', encoding='UTF-8') as daylioRawImport:
    daylioImport = csv.reader(daylioRawImport, delimiter=',', quotechar='"')
    days = {}
    next(daylioImport)
    for row in daylioImport:
        currentEntry = Entry(row)

        if (days.get(row[0]) == None):
            entryList = list()
            entryList.append(currentEntry)
            days[row[0]] = entryList
        else:
            its_a_string_trust_me = row[0]
            days[its_a_string_trust_me].append(currentEntry)


from datetime import datetime

...

for date, entries in days.items():
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date_str = date_obj.strftime("%A the %dth of %B %Y")
    with open(NOTE_TITLE_PREFIX + date + NOTE_TITLE_SUFFIX + '.md', 'w', encoding='UTF-8') as obsidianFile:
        obsidianFile.write("tags: #dates/" + date + ", " + TAGS + "\n\n")
        obsidianFile.write("Date:" + date_str + "\n\n")
        for entry in entries:
            obsidianFile.write(HEADER_LEVEL_FOR_INDIVIDUAL_ENTRIES + " " + entry.time + " | " + entry.mood + "\n")
            obsidianFile.write("I felt #" + entry.mood + " with the following activities: '" + " '".join(entry.activities) + "\n")
            obsidianFile.write(entry.note + "\n\n")
