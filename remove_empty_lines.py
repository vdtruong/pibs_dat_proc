# This file removes the blank lines.
# Code is from 8bitavenue.com.

# Open new data file for writing.
# Read existing file into a string.
# Replace white space with new line characters

import re
open('f:/pibs_2u_venv/data/new_dat.txt', 'w').write(
        re.sub('\n\s*\n', '\n',
            open('f:/pibs_2u_venv/data/record_temp.txt').read()))
