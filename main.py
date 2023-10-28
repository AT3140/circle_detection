import sys
from detect import detect

def main():
    file_str = sys.argv[1]
    linear_error = 1.0
    if(len(sys.argv) == 3):
        linear_error = float(sys.argv[2])
    file = open(file_str,'r')
    vcords = []
    for line in file.readlines():
        line = line.strip('\n')
        cords = line.split(' ')
        if(len(cords) == 2):
            x = float(cords[0])
            y = float(cords[1])
            vcords.append((x,y))
    circles = detect(vcords,linear_error)
    print(f'Detected Circles  : {len(circles)}')
    print('===')
    print('CRP')
    print('===')
    for circle in circles:
        print(f'{circle[0]}')
        print(f'{circle[1]}')
        print(circle[2])
        print('===')

main()
