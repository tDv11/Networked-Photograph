# CR: I'd give this file a better name. Maybe `log.py` or something similar?
import sys
from datetime import datetime


def rw_file(faces, facetime, file):  # CR: don't name your variable `file` as this overrides the builtin type `file`
    now = datetime.now()
    # Timestamp in txt
    file.write(now.strftime('%Y-%m-%d %H:%M ->\n'))
    # current num of faces in txt
    file.write('Faces Detected={0}\n'.format(len(faces)))
    # coordinates in txt
    for x, y, w, h in faces:
        file.write('x={0} y={1}\n'.format(x, y))
    # num of faces so far in txt
    file.write('Face Time={0}seconds\n'.format(facetime))
    file.write('¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n')
