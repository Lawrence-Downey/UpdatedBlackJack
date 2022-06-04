'''import csv
import sys

FILENAME = "playerMoney.csv"

def readMoney(playerMoney):
    try:
        with open (FILENAME, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                playerMoney.append(row)
            return playerMoney
    except FileNotFoundError as e:
        error = "Unable to locate file: {file}.\nAs a result, the program is terminated.\nPlease locate file and try" \
                " again.\nGoodbye.".format(file=FILENAME)
        print(error)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()

def withdrawMoney(playerMoney):
    while True:
        try:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(playerMoney)
                return playerMoney
        except Exception as e:
            error = "Uh-oh! Looks like something went wrong.\nUnable to provide money. Sorry! " \
                    "\nUnfortunately, we have to terminate the program. Goodbye."
            print(error)
            print(type(e), e)
            sys.exit()
'''
