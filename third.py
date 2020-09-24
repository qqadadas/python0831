import re


# .
# ret = re.match('.','sjkshfkshahsfkh')
# print(ret)  # <re.Match object; span=(0, 1), match='s'>
# print(ret.group()) # s

# ret = re.match('.','\nsjkshfkshahsfkh')
# print(ret)  # None
# print(ret.group()) # 报错

# ret = re.search('.','\nsjkshfkshahsfkh')
# print(ret)  # <re.Match object; span=(1, 2), match='s'>
# print(ret.group()) # s

# ret = re.findall('.','\nsjkshfkshahsfkh')
# print(ret) # ['s', 'j', 'k', 's', 'h', 'f', 'k', 's', 'h', 'a', 'h', 's', 'f', 'k', 'h']

# []
# ret = re.findall('[1a6b]',"dfj16a3")
# print(ret) # ['a',]

# 匹配所有的大写字母
# ret = re.findall('[A-Z]','ERUQOIUFASDHKWEHTKQTQ4aswerqwe')
# print(ret)
# 匹配所有的大写和小写字母
# ret = re.findall('[A-Za-z]','ERUQOIswerKWEHTKQTQ4aqwe')
# print(ret)

# \d
# ret = re.findall("\d","2341235hsdfy68")
# ret = re.match("\d","2341235hsdfy68")
# print(ret)


# \s
# ret = re.findall(r"\s","   \t \n 2341fasdf  \t")  # [' ', ' ', ' ', '\t', ' ', '\n', ' ', ' ', ' ', '\t']
ret = re.findall(r"\S","   \t \n 2341fasdf  \t")
print(ret)

# 匹配标识符
# ret = re.findall("[a-zA-Z0-9_]",'weruqu23^Z868)&(^*62142')
# ret = re.findall("\w",'weruqu23^Z868)&(^*62142')
# print(ret)


# \b
print(re.findall(r'\bam\b', 'I am hamha'))  # ['am']
print(re.findall(r'am{5}', 'I am hamha'))  # ['am', 'am']


# \B
# print(re.split(r'he', 'I heshe he me'))  #
print(re.split(r'he\B', 'I heshe he me'))  # ['I ', 'she he me']














