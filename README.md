# CSE420 Compiler Design Labs

Python labs from **CSE420 Compiler Design** at BRAC University (2020), covering the front end of a compiler.

| Lab | File | What it does |
|---|---|---|
| 1 | `LAB_01.py` | **Lexical analysis.** Reads C-like source from `test.txt` and groups the tokens into keywords, identifiers, math operators, logical operators, numbers and other symbols |
| 3 | `CSE 420 Lab 3.py` | **Regular expressions.** Reads a set of patterns and a set of strings, and reports which pattern (if any) matches each string |

The lab briefs are included as PDFs.

## Run

```bash
python LAB_01.py
```

```text
Keywords: int, float, if, else
Identifiers: a, b, c, d, e
Math Operators: -, *, +, =
Logical Operators: >, ||, <
Numerical Values: 2.5, 1
Others: , ; ( ) { }
```

```bash
printf '2\n^[a-z]+$\n[0-9]+\n3\nhello\nabc123\nHELLO\n' | python "CSE 420 Lab 3.py"
# YES, 1
# YES, 2
# NO, 0
```

## Maintenance notes (2026)

- Added the sample `test.txt` that Lab 1 reads; it wasn't in the repository
- Fixed logical-OR detection: the lexer compared against `'||*'`, so `||` was never recognised
