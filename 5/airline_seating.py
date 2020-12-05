INPUT_FILE = 'my_input.txt'

class Seat:
    def __init__(self, description):
        self.description = description

    def get_row_column(self):
        row = self.description[:7]
        row = int(row.replace('F', '0').replace('B', '1'), 2)
        col = self.description[7:]
        col = int(col.replace('L', '0').replace('R', '1'), 2)
        #print(row, col, 8 * row + col)
        return row, col, 8 * row + col

seats = []
with open(INPUT_FILE, 'r') as fp:
    for line in fp:
        seats.append(Seat(line.strip()))

seats.sort(key=lambda x: x.get_row_column()[2])
prev_seat = seats[0].get_row_column()[2]
for seat in seats[1:]:
    if seat.get_row_column()[2] != prev_seat + 1:
        print(seat.get_row_column())
        prev_seat = seat.get_row_column()[2] - 1
    prev_seat += 1


#part 1:
#cur_max = [0, 0, 0]
#for seat in seats:
#    info = seat.get_row_column()
#    if info[2] > cur_max[2]:
#        cur_max = info
#    if info[2] == 895:
#        print(seat.description)

#print(cur_max)
