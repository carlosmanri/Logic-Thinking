M1 = [["4", "7", "1", "3", "5"], ["2", "0", "6", "9", "7"], ["3", "1", "2", "6", "4"],]

M2 = [["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""], ["", "", ""],]

for i in range(3):
    for p in range(5):
        M2[p][i] = M1[i][p]

print("Partimos de esto:", "\n", M1, "\n", "\n", "Para llegar a esto:", M2)
