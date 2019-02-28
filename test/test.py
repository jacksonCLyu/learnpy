# _ *  coding: utf-8 _ * _
__author__ = "young"

import re

line = "yooooooyoouyng123"
regex_str = ".*?(y.*?y).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
else:
    print("no")

# ^: 以后面的字符(可以是字符串)开始
# .: 可以匹配所有字符(范围很大)
# *: 前面的字符可以出现任意次数
# ?: 切换成非贪婪模式(匹配的是后一个字符,顺序由左到右)
