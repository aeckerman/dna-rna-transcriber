#DNA & RNA transcriber
from colorama import init
from colorama import Fore, Style
import sys
from time import sleep

init()

version = "1.0"

def welcome():
    print(Style.BRIGHT + "DNA/RNA Transcriber [v." + version + "]")
    print("Platform[" + sys.platform + "]")
    print("c. Andrew Eckerman 2017" + Style.RESET_ALL)
    print()

def drhelp():
    print("help function")

def drquit():
    print(Fore.RED + 'Erasing strands...')
    sleep(.5)
    print('Closing...' + Fore.RESET)

def transcribeDNA(strand):
    print('dna', strand)

def transcribeRNA(strand):
    print('rna', strand)

'''def transcribe(origin, strand):
    s = strand
    o = origin.lower()
    if o == 'dna':
        transcribeDNA(s)
    elif o == 'rna':
        transcribeRNA(s)'''

def program_loop():
     l = True
     while l == True:
        a = input('>>> ')
        a = a.lower()
        if a == "help":
            drhelp()
        if a == 'quit':
            drquit()
            l = False
        if a[0:10] == "transcribe":
            if a[11:14].lower() == "dna":
                transcribeDNA(a[15:])
            elif a[11:14].lower() == "rna":
                transcribeRNA(a[15:])
            else:
                print(Fore.RED + "Uknown format..." + Fore.RESET)



if __name__ == '__main__':
    welcome()
    program_loop()
