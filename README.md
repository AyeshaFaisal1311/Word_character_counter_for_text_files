# Word Character Counter

A simple Python command-line tool that analyzes text — typed directly or read from a `.txt` file.

## Features
- Accepts typed text or a `.txt` file as input
- Counts characters (with and without spaces)
- Counts total words
- Shows character frequency
- Shows top 5 most frequent words (stopwords excluded, punctuation/case handled)
- Handles missing files and empty input without crashing
- Saves results to a report file

## How to Run
```bash
python code.py
```

## Example
**Input:** `hdhidi`
**Output:**
```
Character (with spaces): 6
Characters without spaces: 6
Words Count: 1
Characters occurrence: {'h': 2, 'd': 2, 'i': 2}
Frequent words: [('hdhidi', 1)]
```

## Concepts Used
- Functions, dictionaries, `dict.get()`
- String methods, `in` operator
- `sorted()` with lambda, list slicing
- File handling (`open`, `with`)
- `try`/`except`, input validation
- Docstrings