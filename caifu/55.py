#zyx
import pickle
pf=open('kk.txt','rb')
list=pickle.load(pf)
pf.close()
for line in list:
    print(line)