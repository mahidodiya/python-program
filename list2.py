#list oprations
friends=['rajvi','dhruvi','gaytri','aayushi','palak']
print(friends)
f=friends
#at begining
f.insert(0,'nandni')
f.insert(1,'divyanshi')
print(f)
#at last
f.append('krisha')
f.append('khushi')
print(f)
#another list 
relative=['mama','mami','masi','dadi','dada']
r=relative
print(r)
#mearge both list
f.extend(r)
print(f)
#remove 1st item
f.pop(0)
print(f)
#remove name'aayushi'
f.remove('aayushi')
print(f)
#clear all
f.clear()
print(f)

