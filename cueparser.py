import os, sys

SAVE_FILE_NAME = "SearchResults.txt"

class CueSheet:
    def __init__(self, filepath):
        self.found = False
        self.file = filepath
        self.count = 0
        with open(self.file, 'r', encoding="utf-8") as cueFile:
            self.cueFileContents = cueFile.read().splitlines()

    def findItem(self, searchKey):
        for item in self.cueFileContents:
            if searchKey in item:
                self.found = True

        if self.found == True:
            self.itemFound()
        else:
            self.itemNotFound()
        
        return self.found
            
    def itemNotFound(self):
        self.count += 1
            
    def itemFound(self):
        print("Item found! Saving to SearchResults.txt...")
        with open(SAVE_FILE_NAME, 'a', encoding="utf-8") as outputFile:
            outputFile.write(self.file + '\n')
        print("Displaying the directory where the item was found...")
        print(self.file)
        self.count += 1
        
def main():
    rootdir = os.path.dirname(os.path.abspath(__file__))
    searchKey = ''
    foundCount = 0
    count = 0
    
    try:
        searchKey = sys.argv[1]
    except IndexError:
        print("No search key provided. Terminating...")
    
    if searchKey != '':
        with open(SAVE_FILE_NAME, 'a', encoding="utf-8") as outputFile:
            outputFile.write("RESULTS FOR: " + searchKey + '\n')
        
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file
                if filepath.endswith(".cue"):
                    currentCue = CueSheet(filepath)
                    if currentCue.findItem(searchKey):
                        foundCount += 1
                        
            count += 1
        print("The total number of CUE files processed is: ", count)
        print("The total number of matches is: ", foundCount)
    
    with open(SAVE_FILE_NAME, 'a', encoding="utf-8") as outputFile:
        outputFile.write('\n')

main() 
        
