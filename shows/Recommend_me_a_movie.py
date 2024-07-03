# imports
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

# main function
def main ():
    conn = sqlite3.connect("shows.db")
    cur = conn.cursor()
    cur.execute('SELECT shows.episodes, ratings.rating FROM shows JOIN ratings ON shows.id = ratings.show_id')
    results = cur.fetchall()

    # print the max number of episodes
    print(max(results, key=lambda x: float('-inf') if x[0] is None else x[0])[0])

    cur.close()
    conn.close()
    
    make_plot(results)

# make plot
def make_plot (results):
    x = []
    y = []
    for i in results:
        x.append(i[1])
        y.append(i[0])
    plt.scatter(x, y)
    plt.xlabel("Score")
    plt.ylabel("Number of episodes")
    plt.show()

if __name__ == "__main__":
    main()