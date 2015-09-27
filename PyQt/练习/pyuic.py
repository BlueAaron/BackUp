# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.ui'):
            print file
            os.system('pyuic4 -o %s.py %s' % (file.rsplit('.', 1)[0], file))
        elif file.endswith('.qrc'):
            print file
            os.system('pyrcc4 -o %s_rc.py %s' % (file.rsplit('.', 1)[0], file))