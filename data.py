#Data loader(highscore)

import csv

def read(filename):
    scores = []
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line = 0
            for row in csv_reader: #HEADER will be the first row
                if row != []:
                    scores.append(row)
                line += 1
        return scores
    except IOError:
        with open(filename, "w") as csv_file:
            print("Created " + filename)
        write(filename, [["Number", "Scores"]])
        return scores

def write(filename, scores):
    with open(filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in scores:
            csv_writer.writerow(row)

def update(new_score):
    scores_list = [new_score]
    scores_board = read("scores.txt")
    for scores in scores_board[1:]: #start from second row(skip header)
        scores_list.append(int(scores[1]))
    scores_list.sort(reverse=True)
    scores_board = [scores_board[0]]
    for i, score in enumerate(scores_list):
        scores_board.append([f'#{i+1}', score])

    #write into file
    write("scores.txt", scores_board)
    print("Scoreboard has been updated!")

def reset():
    #reset the scores board
    scores_board = read("scores.txt")
    write("scores.txt", [scores_board[0]])
    print("Scoreboard has been reset!")
