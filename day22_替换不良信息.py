import re
sentence = '你是傻逼吗？不好好做个正常人偏要去做脑残粉……'

sentence_new = re.sub(r'[SB, 傻逼, 艹, 脑残]', '*', sentence)

print(sentence_new)
