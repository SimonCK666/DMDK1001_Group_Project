import PIL.Image as image
import numpy as np
import pandas as pd
from config import config_parser_eval

parser = config_parser_eval()
args = parser.parse_args()

i1 = image.open(args.list[0]).convert('L') 
i2 = image.open(args.list[1]).convert('L') 
a1 = np.array(i1).reshape((-1,))
a2 = np.array(i2).reshape((-1,))
c1 = np.unique(a1)
c2 = np.unique(a2)

print("img {} {}, cluster {}".format(args.list[0],a1.shape,len(c1)))
print("img {} {}, cluster {}".format(args.list[1],a2.shape,len(c2)))

df = pd.DataFrame(0,index=c1, columns=c2)

for k in range(min(len(a1),len(a2))):
    df.at[a1[k],a2[k]]+=1
print("confusion matrix")
print(df)

pair = []
for i in range(min(len(c1),len(c2))):
    pair.append((c1[i],c2[i]))
out = pd.DataFrame(0,index=pair, columns=['accuracy','error','recall','precision'])
for k in range(min(len(c1),len(c2))):
    tp = df.at[c1[k],c2[k]]
    tn = df.loc[np.delete(c1,k),np.delete(c2,k)].values.sum()
    fp = df.loc[c1[k],np.delete(c2,k)].values.sum()
    fn = df.loc[np.delete(c1,k),c2[k]].values.sum()
    all = df.values.sum()
    # print([tp,tn,fp,fn])
    out.iloc[k,0]=(tp+tn)/all
    out.iloc[k,1]=(fp+fn)/all
    out.iloc[k,2]=tp/(tp+fn)
    out.iloc[k,3]=tp/(tp+fp)
print("evaluation matrix")
print(out)