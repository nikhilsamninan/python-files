a="Betty Bought a butter the butter was bitter so betty bought a better butter which was not bitter"
v=[a[-1] for a in a.split() if(len(a)%2==0)]
print(v)