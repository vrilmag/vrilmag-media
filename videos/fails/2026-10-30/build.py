# Daily Bucket | Oct 30, 2026 — template derived from 2026-10-29/build.py
import subprocess,textwrap,os,json
TB='fonts/TinosBold.ttf'; IN='fonts/Inter.ttf'
S='src/'
DATE='Oct 30, 2026'
# (file, in, out, name, office, dateline, source, quote)
SEG=[
 ('cut_wmur_ice.mp4',13.90,26.35,'Stefany Shaheen','Democratic nominee, U.S. House (N.H.-1)','Oct 29, 2026 · WMUR Granite State Debate','Source: WMUR-TV',
  '"My opponent is making things up from the very first examples of the violence that was unleashed by ICE agents. I called for reform of the Department of Homeland Security. I stand by that position."'),
 ('cut_wmur_ice.mp4',81.80,88.85,'Stefany Shaheen','Democratic nominee, U.S. House (N.H.-1)','Oct 29, 2026 · WMUR Granite State Debate','Source: WMUR-TV',
  '"Well, again, I\'ve said it just like I said earlier, a few seconds ago, I stand by my position to dismantle ICE."'),
 ('wmur_trans.mp4',37.10,49.75,'Stefany Shaheen','Democratic nominee, U.S. House (N.H.-1)','Oct 29, 2026 · WMUR Granite State Debate','Source: WMUR-TV',
  '"I also believe that these decisions need to be made on a case-by-case basis with the coaches, the superintendents and teams that are impacted by trans athletes. I don\'t believe we need a federal law here."'),
 ('x_2116179019100045312.mp4',4.90,26.10,'Suzan DelBene','U.S. Rep. (D-Wash.), DCCC Chair','Oct 30, 2026 · CNN News Central','Source: CNN (clip via RNC Research)',
  'Q: Does it bother you when you see what looks like shenanigans happening...?\nDELBENE: "...look at what Republicans have been doing across the country since the very beginning--"\nQ: If it\'s bad for them, is it bad for Democrats, too?\nDELBENE: "No, this-- the Peltola campaign has denied that that happened. And-- but we can\'t deny what we have seen happen from Republicans on the ground every day this cycle."'),
 ('x_2115983219258527744.mp4',22.45,34.50,'Nancy Pelosi','Speaker Emerita, U.S. Rep. (D-Calif.)','Oct 29, 2026 · "On Brand with Donny Deutsch"','Source: On Brand (clip via Greg Price)',
  '"No, it\'s more than concerning. It\'s wrong. It\'s wrong, and it isn\'t a reflection of the Democrats in the Congress of the United States. This new person in Michigan, we\'ll see if he gets elected to the Congress."'),
 ('x_2116297804502986752.mp4',105.95,125.30,'Thom Tillis','U.S. Senator (R-N.C.)','Oct 30, 2026 · PBS News Hour interview','Source: PBS News Hour',
  'Q: Does Secretary Hegseth, in your view, deserve to be impeached?\nTILLIS: "You know, I hope the president will simply fire him or get him to move on. And after the election, I think that we\'re clearly going to take some losses. I still hold out the hope that we can have a slim majority in the Senate. I believe that the House is lost."'),
]
os.makedirs('build',exist_ok=True); open('build/hdr.txt','w').write('DAILY BUCKET · OCT 30')
def tf(name,txt):
    p=f'build/{name}.txt'; open(p,'w').write(txt); return p
def wrap(t,w): return '\n'.join('\n'.join(textwrap.wrap(l,w)) for l in t.split('\n'))
NAVY='0x0C111E'; BR='0xBF9B5B'
ENC=['-c:v','libx264','-pix_fmt','yuv420p','-preset','medium','-crf','21','-r','30','-c:a','aac','-b:a','160k','-ar','48000','-ac','2']
def card(out,dur,lines):
    vf=f"drawbox=x=96:y=820:w=888:h=4:c={BR}:t=fill"
    for (font,txt,col,size,y) in lines:
        vf+=f",drawtext=fontfile={font}:textfile={tf(out+'_'+str(y),txt)}:fontcolor={col}:fontsize={size}:x=(w-tw)/2:y={y}"
    subprocess.run(['ffmpeg','-y','-v','error','-f','lavfi','-i',f'color=c={NAVY}:s=1080x1920:r=30:d={dur}','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-t',str(dur),
      '-vf',vf]+ENC+[f'build/{out}.mp4'],check=True)
card('s0',2,[(TB,'Daily Bucket | Oct 30, 2026','0xF5F2EC',68,880),(IN,'Shaheen · DelBene · Pelosi · Tillis','0xA0A5AF',32,990),(TB,'@vrilmag','0xF5F2EC',44,1700)])
for i,(f,a,b,name,role,dl,src,q) in enumerate(SEG,1):
    for fs,ww in [(50,36),(44,36),(40,40),(36,44),(32,50),(30,56)]:
        w=wrap(q,ww); n=len(w.split('\n'))
        if n*(fs*1.25+10)<=455: break
    print(i,name,n,'lines',fs)
    qf=tf(f"q{i}",w); nf=tf(f'n{i}',name); rf=tf(f'r{i}',role); df=tf(f'd{i}',dl); sf=tf(f's{i}',src)
    vf=(f"scale=1080:-2,pad=1080:1920:0:660:color={NAVY},"
        f"drawbox=x=96:y=84:w=888:h=4:c={BR}:t=fill,drawtext=fontfile={IN}:textfile=build/hdr.txt:fontcolor={BR}:fontsize=30:x=96:y=110,"
        f"drawtext=fontfile={TB}:textfile={qf}:fontcolor=0xF5F2EC:fontsize={fs}:line_spacing=10:x=96:y=180,"
        f"drawbox=x=96:y=1310:w=10:h=200:c={BR}:t=fill,drawtext=fontfile={TB}:textfile={nf}:fontcolor=0xF5F2EC:fontsize=56:x=126:y=1306,"
        f"drawtext=fontfile={IN}:textfile={rf}:fontcolor=0xD8D4CC:fontsize=34:x=126:y=1378,"
        f"drawtext=fontfile={IN}:textfile={df}:fontcolor=0xA0A5AF:fontsize=30:x=126:y=1426,"
        f"drawtext=fontfile={IN}:textfile={sf}:fontcolor={BR}:fontsize=30:x=126:y=1470,"
        f"drawtext=fontfile={TB}:text=@vrilmag:fontcolor=0xF5F2EC:fontsize=40:x=96:y=1780,fps=30")
    subprocess.run(['ffmpeg','-y','-v','error','-ss',str(a),'-to',str(b),'-i',S+f,'-vf',vf,'-af','aresample=48000,afade=t=in:d=0.08,afade=t=out:st=%.2f:d=0.12'%(b-a-0.12)]+ENC+[f'build/s{i}.mp4'],check=True)
card(f's{len(SEG)+1}',2,[(TB,'@vrilmag','0xF5F2EC',110,870),(IN,'Daily Bucket | Oct 30, 2026','0xA0A5AF',40,1020)])
open('build/list.txt','w').write(''.join(f"file 's{i}.mp4'\n" for i in range(len(SEG)+2)))
subprocess.run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i','build/list.txt','-c','copy','-movflags','+faststart','montage.mp4'],check=True)
print('ok')
