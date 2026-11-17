import os,json,re,subprocess
src="/mnt/user-data/uploads/Downloads/Hand audio files/Podcast"
M={1:["distal-humerus-fractures","elbow-dislocation-instability","radial-head-neck-fractures","olecranon-fractures"],
2:["congenital-hand"],3:["hand-infections"],4:["hand-infections"],5:["hand-wrist-tumours"],6:["dupuytrens-disease"],
7:["small-joint-arthritis","base-of-thumb-arthritis","rheumatoid-hand-wrist","slac-snac"],8:["kienbocks-disease"],
9:["upper-limb-nerve-injury","tendon-transfers","digital-nerve-injury"],10:["upper-limb-nerve-injury"],11:["vascular-hand"],
12:["fingertip-injuries","replantation-mangled-hand"],13:["fingertip-injuries"],14:["druj-ulnar-wrist-pain"],
15:["flexor-tendon-injuries","extensor-tendon-injuries","tendinopathies-hand-wrist"],
16:["acute-scaphoid-fractures","carpal-instability","perilunate-injuries","acute-sl-lt-injury"],
17:["metacarpal-phalangeal-fractures"],18:["distal-radius-fractures"],19:["forearm-wrist-approaches","hand-examination"],
20:["thumb-injuries"],21:["slac-snac"],22:["scaphoid-non-union"],23:["finger-joint-injuries","rheumatoid-hand-wrist","extensor-tendon-injuries"],
24:["slac-snac"],25:["slac-snac","scaphoid-non-union"],26:["fingertip-injuries"],27:["hand-infections"],28:["acute-scaphoid-fractures"],
29:["carpal-instability","acute-sl-lt-injury"],30:["acute-scaphoid-fractures"],31:["flexor-tendon-injuries","hand-amputation"],
32:["perilunate-injuries","distal-radius-fractures"],33:["thumb-injuries"],34:["extensor-tendon-injuries"],35:["druj-ulnar-wrist-pain","tendinopathies-hand-wrist"],
36:["tendinopathies-hand-wrist"],37:["upper-limb-nerve-injury","brachial-plexus"],38:["metacarpal-phalangeal-fractures"],
39:["small-joint-arthritis","rheumatoid-hand-wrist"],40:["flexor-tendon-injuries","hand-amputation"],41:["finger-joint-injuries"],
42:["upper-limb-nerve-injury"],43:["metacarpal-phalangeal-fractures"],44:["flexor-tendon-injuries"],45:["rheumatoid-hand-wrist","hand-examination"],
46:["tendinopathies-hand-wrist"],47:["kienbocks-disease"],48:["extensor-tendon-injuries"],49:["upper-limb-nerve-injury","tendon-transfers"],
50:["finger-joint-injuries","metacarpal-phalangeal-fractures"],51:["carpal-instability","acute-sl-lt-injury"]}
eps=[]
for f in sorted(os.listdir(src)):
    n=int(f[:2]); t=f[3:-4]
    t=re.sub(r'^\d+\.?\s*','',t).replace(' (Millers)','')
    if '(Millers)' in f[3:] or n<=19: t=t+" (Millers)"
    t=t.replace("Tumors","Tumours")
    d=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',os.path.join(src,f)],capture_output=True,text=True).stdout)
    slug="hand-%02d-"%n+re.sub(r'[^a-z0-9]+','-',t.lower().replace("'","")).strip('-')
    eps.append(dict(n=n,title=t,file=slug+".mp3",src=f,dur=round(d),bytes=os.path.getsize(os.path.join(src,f)),notes=M[n]))
json.dump(eps,open('hand.json','w'),indent=0)
for e in eps: print(e['n'],e['title'],e['dur']//60,e['file'])
