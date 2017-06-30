
import sys
from datetime import datetime

def log(faces, face_time, my_file): 
    now = datetime.now()
    # Timestamp in txt
    my_file.write(now.strftime('%Y-%m-%d %H:%M ->\n'))
    # current num of faces in txt
    my_file.write('Faces Detected={0}\n'.format(faces))
    # num of faces so far in txt
    my_file.write('Face Time={0}seconds\n'.format(face_time))
    my_file.write('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
    return now.strftime('%H:%M')
