# -*- coding: utf-8 -*-

import re

st = "忙完这阵子，就可以接着忙下阵子了"
new_st = re.sub(r'忙', '过', st)
print(new_st)
