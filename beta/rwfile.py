import sys
from datetime import datetime


def rw_file( faces, facetime, file ):
    now = datetime.now()
    # Timestamp in txt
    file.write(now.strftime('%Y-%m-%d %H:%M ->\n'))
    # current num of faces in txt
    file.write('Faces Detected=' + format(len(faces)) + '\n')
    # coordinates in txt
    for (x, y, w, h) in faces:
        file.write('x=' + str(x) + ' y=' + str(y) + '\n')
    #num of faces so far in txt
    file.write('Face Time=' + str(facetime) + 'seconds')
    file.write('\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')

