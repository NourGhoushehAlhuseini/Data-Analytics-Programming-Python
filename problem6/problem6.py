problem = "problem6"
student_name = "nour"
student_number = "t0326796"
import pandas as pd
import re
import networkx as nx
import random
import os

# part a
def text_analyser(user_text):
    try:
        # open and read file content
        with open(user_text, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        # let user know the user if the file is not found
        print(f"File {user_text} not found.")
        return

    # remove punctuation 
    text = re.sub(r"[^\w\s']", '', text.lower())
    words = text.split()

    # builds graph
    edges = [(words[i], words[i+1]) for i in range(len(words)-1)]
    G = nx.DiGraph() 
    G.add_edges_from(edges) # adds word connections to the graph

    # counts word frequency using pandas
    word_series = pd.Series(words)
    word_counts = word_series.value_counts().reset_index()
    word_counts.columns = ['Word', 'Frequency']

    # how many times word pairs appear/ frequency
    edge_df = pd.DataFrame(edges, columns=['From', 'To'])
    edge_counts = edge_df.value_counts().reset_index(name='Count')

    # user interaction menu to choose from the list
    while True:
        print("\nChoose an analysis option:")
        print("1. Count of distinct words in the text")
        print("2. Most frequent word with its frequency")
        print("3. Word with the largest number of unique neighbours")
        print("4. Word with the smallest number of unique neighbours")
        print("5. Show edge DataFrame and descriptive statistics")
        print("6. Find shortest path between two words (BFS)")
        print("7. Generate random sentence (DFS-based)")
        print("8. Show graph structure (adjacency list)")
        print("9. Return a list of all words that appear only once in the text")
        print("10. Return the longest word in the text")
        print("11. Return the number of unique edges in the word graph")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ").strip()

        # option 1 count of distinct words
        if choice == '1':
            print(f"Total distinct words: {word_counts.shape[0]}")
        # option 2 most frequesnt word
        elif choice == '2':
            top_word = word_counts.iloc[0]
            print(f"Most frequent word: '{top_word['Word']}' (Frequency: {top_word['Frequency']})")
            # option 3 
        elif choice == '3':
            out_degrees = G.out_degree()
            max_deg_word = max(out_degrees, key=lambda x: x[1])
            print(f"Word with most unique neighbours: '{max_deg_word[0]}' ({max_deg_word[1]} neighbours)")
            # option 4
        elif choice == '4':
            out_degrees = G.out_degree()
            filtered = [node for node in out_degrees if node[1] > 0]
            if filtered:
                min_deg_word = min(filtered, key=lambda x: x[1])
                print(f"Word with fewest unique neighbours: '{min_deg_word[0]}' ({min_deg_word[1]} neighbour(s))")
            else:
                print("No word has outgoing neighbours.")
        # option 5
        elif choice == '5':
            print("\nTop 5 Word Frequencies:")
            print(word_counts.head())
            print("\nTop 5 Most Common Edges:")
            print(edge_counts.head())
            print("\nDescriptive Stats (word frequencies):")
            print(word_counts['Frequency'].describe())
        # part b

        elif choice == '6': # option 6
            word1 = input("Enter the starting word: ").strip().lower()
            word2 = input("Enter the ending word: ").strip().lower()
            if word1 not in G.nodes:
                print(f"'{word1}' is not in the text.")
            elif word2 not in G.nodes:
                print(f"'{word2}' is not in the text.")
            else:
                try:
                    path = nx.shortest_path(G, source=word1, target=word2)
                    print(f"Shortest path from '{word1}' to '{word2}':")
                    print(" → ".join(path))
                except nx.NetworkXNoPath:
                    print(f"No path exists from '{word1}' to '{word2}'.")
        # part c
        elif choice == '7': # option 7
            choice = input("Would you like to enter a start word? (yes/no): ").strip().lower()
            if choice == 'yes':
                start_word = input("Enter the starting word: ").strip().lower()
                if start_word not in G.nodes:
                    print(f"'{start_word}' is not in the text.")
                    continue
            else:
                start_word = random.choice(list(G.nodes))

            # DFS sentence sentence generator 
            sentence = [start_word]
            current = start_word
            visited = set()
            while len(sentence) < 20:
                neighbors = list(G.successors(current))
                unvisited = [n for n in neighbors if n not in visited]
                if not unvisited:
                    break
                next_word = random.choice(unvisited)
                sentence.append(next_word)
                visited.add(current)
                current = next_word

            print("Generated sentence:")
            print(" ".join(sentence) + ".")

        elif choice == '8': # option 8 
            print("\nWord Graph Adjacency List:")
            for node in G.nodes:
                neighbors = list(G.successors(node))
                if neighbors:
                    print(f"{node} → {', '.join(neighbors)}")

        elif choice == '9': # option 9
            single_occurrences = word_counts[word_counts['Frequency'] == 1]['Word'].tolist()
            print("Words that appear only once:")
            print(single_occurrences)

        elif choice == '10': #option 10
            max_length = max(len(word) for word in words)
            longest_words = [w for w in words if len(w) == max_length]
            print(f"Longest word(s) ({max_length} characters): {set(longest_words)}")

        elif choice == '11': # option 11
            unique_edges = len(set(edges))
            print(f"Number of unique edges in the word graph: {unique_edges}")

        elif choice == '12': # option 12 exit the program 
            print("Exiting analysis.")
            break

        else:
            print("Invalid choice. Please Try again.")

if __name__ == "__main__":
    print("Available text files in the folder:")
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    for file in txt_files:
        print(" -", file)
        # asks users to choose a file 
    filename = input("\nEnter the filename of the text you want to analyze: ").strip()
    text_analyser(filename)
