
# string = input()
# count = 1
# for i in range(len()string)-1): 
#     if string [i] == string[i + 1]:
#         count += 1
#     else:
#         a = string[i]
#         count = 1
#     print(count, string[i])


s = '21a45d'
count = ''
for i in range(len(s) - 1):
    if s[i].isdigit():
        count += s[i]
    else:
        count = ''
    if s[i].isdigit() and not s[i + 1].isdigit():
        print(int(count) * s[i + 1], end='')




