#DNA & RNA transcriber
from colorama import init
from colorama import Fore, Style
import sys

init()

version = "1.0"

def welcome():
    print(Style.BRIGHT + "DNA/RNA Transcriber [v." + version + "]")
    print("Platform[" + sys.platform + "]")
    print("c. Andrew Eckerman 2017" + Style.RESET_ALL)
    print()

def program_loop():
    return 0


def transcribe(origin, strand):
    s = strand
    o = origin.lower()
    if o == 'dna':
        transcribeDNA(s)
    elif o == 'rna':
        transcribeRNA(s)

if __name__ == '__main__':
    welcome()
