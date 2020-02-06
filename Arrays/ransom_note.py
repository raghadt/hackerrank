from collections import Counter

mag= "apgo clm w lxkvg mwz elo bg elo lxkvg elo apgo apgo w elo bg"
note = "elo lxkvg bg mwz clm w"
mag = mag.split()
note = note.split()

mag_dict = Counter(mag)
note_dict = {i:0 for i in note}

count = 0
for i in note:
    if i in mag_dict.keys() and mag_dict[i]!=0:
        count+=1
        mag_dict[i]-=1
            
if count==len(note):
    print('Yes')
else:
    print('No')