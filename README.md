# BookBot

BookBot is a [Boot.dev](https://www.boot.dev) project, simple Python command-line tool for analyzing text files (books). It provides word and character counts, and displays a sorted list of character frequencies.

## Features

- Counts total words in a book.
- Counts occurrences of each character.
- Displays character frequencies sorted by count.

## Requirements

- Python 3.x

## Usage

1. Place your book (text file) in a known location.
2. Run BookBot from the command line:

   ```bash
   python3 main.py <path_to_book>
   ```

   Example:

   ```bash
   python3 main.py books/frankenstein.txt
   ```

3. The output will show word count and character frequencies.

## File Structure

- `main.py`: Main entry point for the application.
- `stats.py`: Contains functions for word and character counting, and sorting.

## Example Output

```
=======+==== BOOKBOT ===+========
Analyzing book found at: books/frankenstein.txt...
----------- Word Count ----------
Found 73520 total words
-------- Character Count --------
a: 44210
b: 8123
...
============ END ==============
```

## License

MIT License