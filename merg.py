d1={'color':'red','fruit':'grapes','climate':'cold'}
print(d1)
d2={'price':"20",'age':'18'}
print(d2)
d=d1.copy()
d.update(d2)
print("merged dictionary",d)