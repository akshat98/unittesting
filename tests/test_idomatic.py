from pathlib import Path

from idomatic import get_report

CURRENT_DIR = Path.cwd()
DATA_DIR = CURRENT_DIR.parent / "unittesting/data"

DATA_FILE1 = DATA_DIR / "missing_data1.txt"
DATA_FILE2 = DATA_DIR / "missing_data2.txt"
DATA_FILE3 = DATA_DIR / "empty.txt"


expected1 = """missing values: 2
highest number: 99.0
most common words: john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 99.0, 6.72, 2.0, 2.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'was', 'here', 'this', 'is', 'totally', 'random', 'john']"""

expected2 = """missing values: 3
highest number: 101.0
most common words: doe, john
occurrences of most common: 4
#####
numbers: [1.0, 2.0, 101.0, 6.72, 2.0, 2.0, 67.0, 2.0]
words: ['john', 'doe', 'john', 'john', 'doe', 'was', 'doe', 'here', 'this', 'is', 'totally', 'random', 'john', 'doe']"""

expected3 = """missing values: 0
highest number: None
most common words: 
occurrences of most common: 0
#####
numbers: []
words: []"""

assert get_report(DATA_FILE1) == expected1
print("First one OK!")

assert get_report(DATA_FILE2) == expected2
print("Second one OK!")

assert get_report(DATA_FILE3) == expected3
print("All OK, woop woop!")