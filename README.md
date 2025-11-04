Data Analytics Techniques and Programming 

This repository contains Python solutions for the coursework at Nottingham Trent University. 
The work covers object oriented programming, algorithm analysis, dynamic programming, simulation and text analysis.

Overview of problems

Problem 1 – Iterative and bisection search  
Implements iterative and bisection search routines to approximate numerical solutions. Demonstrates convergence through test examples.

Problem 2 – Fraction class and Python data model  
Implements a Fraction class to represent rational numbers in simplified form.  
Supports initialisation with automatic reduction using gcd,  
conversion to string and float,  
arithmetic and comparison operators,  
and reciprocal and reduction methods.

Problem 3 – Runtime comparison of sorting algorithms  
Compares Bubble Sort, Selection Sort and Merge Sort on random and pre-sorted data.  
Count comparisons and execution time to demonstrate O(n²) vs O(n log n) behaviour.

Problem 4 – Dynamic programming: coin change and word segmentation  
Solves the coin-change problem using tables for minimum coins and optimal sets.  
Implements a word-segmentation algorithm using a dictionary and recursion with memoisation.

Problem 5 – Knight’s Tour simulation and visualisation  
Simulates the Knight’s Tour problem on an 8×8 chessboard using brute-force random and Warnsdorff heuristic approaches.  
Generates success statistics and heatmaps to compare strategies.

Problem 6 – Text analysis using graph algorithms  
Builds a directed word graph from Project Gutenberg texts with NetworkX and pandas.  
Calculates frequencies, degrees, shortest paths and random walks to generate sentences.

Technologies and libraries  
Python 3, NumPy, pandas, matplotlib, seaborn, NetworkX, random, time, re and os.

How to run  
Install required libraries:  
pip install numpy pandas matplotlib seaborn networkx  
Run individual problems, for example:  
python problem2/Problem2.py  
python problem5/problem5.py
