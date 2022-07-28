s = input()
f = []
d = {}
first,last = 0,0
new_str = ""
for i in range(len(s)):
    if s[i].isalnum() or s[i] == "'":
        last += 1        
    else:
        if first < last:
            if d.get(s[first:last].lower()) == None:
                d[s[first:last].lower()] = 1
            else:
                d[s[first:last].lower()]+=1
            f.append(s[first:last])
            f.append(s[i])
        else:
            f.append(s[i])
        first,last = i+1,i+1
for i in range(len(f)):
    if d.get(f[i].lower()) != None :
        if d[f[i].lower()] > 1:
            f[i]+="zzz"
for j in f:
    new_str+=j
print(new_str)
print(d)
