# Obsidian-Daylio-CSV-Parser
Takes Daylio CSV exports and converts them into mark down files for use with Obsidian.

Important info:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This script has to be in the same folder as the csv files and that folder will also be where all the mark down entries are generated, I will not be changing this. I advise you make sure you have the right folder before running the script

The script will automatically choose the newest CSV file in the folder, if you need it to pull from an older CSV file just open the desired file and save it so that it counts as modified

Some of the results can be easily adjusted through configs in the code. It is currently adjusted how I like it and some non easy to change code reflects that.

The script will automatically overwrite and files using the same naming structure it does. Do not run in a folder containing existing YYYY-MM-DD titled notes (i.e. your daily notes folder)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
You'll need to do a few things to run this script. I'll explain my process but there are other methods you can easily search.

I use Visual Studio Code so download that

Then in VSC install the python plugin

Open the folder containing the script and your csv file in VSC

Right click the script and click Run Python File In Terminal

If that doesn't work for you sorry I can't explain other methods at this time but do give VSC a try it's a good program.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Lastly I just want to say that this was a project made in collaboration between myself and the openai chatbot ChatGPT meaning that while some of this code is handwritten some of it was also generated automatically and an actual back and forth was had between myself and the AI to determine certain methods of doing things. Very neat stuff!
