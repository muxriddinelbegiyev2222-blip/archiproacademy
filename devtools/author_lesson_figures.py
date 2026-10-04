"""Rebuild explicit course illustrations from existing authored worked examples.

No runtime generation or keyword assignment. MODULE_RECIPES assigns every
remaining module; per-stage focus is fixed in the authored recipe. Geometry is
educational, never a normative minimum or a structural design.
Run from repository root: python devtools/author_lesson_figures.py
"""
import json, sys, textwrap
from pathlib import Path
from html import escape
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'app'))
from courses.workbook_data import WORKBOOKS
from courses.teaching.guides import GUIDES
from courses.content_registry import get_all_lesson_content
D=ROOT/'app/courses/visual_assets'
INK='#203B36'; T='#0E5558'; C='#A65D35'; P='#FFFDF7'; G='#DBE9E2'; BLUE='#D5E7ED'; RED='#A43D32'

def text(x,y,s,size=23,color=INK):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{escape(str(s))}</text>'
def lines(x,y,s,width=68,size=21,color=INK):
 return ''.join(text(x,y+k*(size+9),v,size,color) for k,v in enumerate(textwrap.wrap(s,width=width)))
def line(a,b,c,d,color=INK,w=3,dash=False):
 return f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="{color}" stroke-width="{w}"'+(' stroke-dasharray="9 7"' if dash else '')+'/>'
def rect(x,y,w,h,fill=G,stroke=INK,sw=3):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def poly(points,fill=G,color=INK,w=3):
 return f'<polygon points="{points}" fill="{fill}" stroke="{color}" stroke-width="{w}"/>'
def circle(x,y,r,fill=P,color=INK):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{color}" stroke-width="3"/>'
def arrow(x,y,a,b,color=C):
 return line(x,y,a,b,color,4)+f'<path d="M{a}, {b} l-12,-5 l0,10 Z" fill="{color}" transform="rotate({__import__("math").degrees(__import__("math").atan2(b-y,a-x))} {a} {b})"/>'
def dim(x1,y,x2,s):
 return line(x1,y,x2,y,T,2)+line(x1,y-8,x1,y+8,T,2)+line(x2,y-8,x2,y+8,T,2)+text((x1+x2)/2-42,y-12,s,21,T)
def badge(x,y,n,label=''):
 return circle(x,y,18,T,T)+text(x-7,y+8,n,22,P)+(text(x+27,y+8,label,21,T) if label else '')
def highlight(x,y,w,h):return rect(x,y,w,h,'none',C,5)
def door(x,y,r=65,side=1):
 return line(x,y,x,y-r,T,3)+f'<path d="M{x+side*r},{y} A{r},{r} 0 0,{0 if side==1 else 1} {x},{y-r}" fill="none" stroke="{T}" stroke-width="2"/>'
def table(x,y,headers,rows,widths=None,focus=-1):
 widths=widths or [220]*len(headers);out=''
 for j,row in enumerate([headers]+rows):
  xx=x
  for k,v in enumerate(row):
   out+=rect(xx,y+j*57,widths[k],57,T if j==0 else ('#F1DFC6' if j-1==focus else P),T,1)
   out+=text(xx+10,y+j*57+36,v,19,P if j==0 else INK);xx+=widths[k]
 return out

def facade(kind,i):
 two=kind=='two-facade';y=235 if two else (320 if kind=='proportion' else 310);h=260 if two else (200 if kind=='proportion' else 210)
 out=rect(140,y,800,h,'#E9E1D3')+line(110,520,990,520,T,5)
 if kind in ('style','premium'):out+=rect(170,y+25,80,h-25,'#C9AD84')+rect(850,y+25,50,h-25,'#C9AD84')
 centers=[310,475,695,860]
 if kind=='rhythm':centers=[260,470,680]
 if kind=='symmetry':centers=[340,740];out+=line(540,170,540,550,C,3,True)+text(570,195,'O‘Q: x = 6 m',22,C)
 if kind=='symmetry' and i>=2:out+=rect(220,385,60,135,'#C9AD84')+badge(250,685,1,'Kirish chetda')
 else:out+=rect(510 if kind=='symmetry' else 560,385,60,135,'#C9AD84')
 for j,x in enumerate(centers):
  yy=y+45;ww=80 if kind=='proportion' else 68
  if kind=='rhythm' and i==4 and j==2:x-=28
  if kind=='proportion' and i==4 and j==1:ww=115
  out+=rect(x-ww/2,yy,ww,95,BLUE,T)+line(x,yy,x,yy+95,T,2)
  if two:out+=rect(x-ww/2,y+150,ww,65,BLUE,T)
 if kind=='composition':
  hx=[(545,370,90,150),(530,290,120,230),(150,310,360,210),(545,370,90,150),(800,300,145,220)][i]
  out+=highlight(*hx)+badge(hx[0]+20,hx[1]-25,i+1)
 if kind=='proportion':
  out+=dim(140,565,940,'12 m')+text(50,420,'3 m',21,T)
  if i==0:out+=text(350,625,'12 ÷ 3 = 4:1',30,C)
  elif i==1:
   out+=circle(650,398,12,T,T)+line(650,410,650,465,T,5)+line(650,465,625,513,T,5)+line(650,465,675,513,T,5)+text(690,600,'Inson: tanish o‘lchov',23,T)
  elif i==2:out+=text(320,625,'Deraza: 1,2 ÷ 1,5 = 0,8',27,C)
  else:
   for x in [140,406,673,940]:out+=line(x,235,x,540,C,2,True)
 if kind=='rhythm':
  out+=dim(260,575,470,'3 m')+dim(470,575,680 if i<4 else 652,'3 m' if i<4 else '2,6 m')
  out+=text(240,625,'x = 2 m             x = 5 m             x = 8 m' if i<4 else 'Oxirgi markaz x = 7,6 m: sababini tekshiring',23,C)
  if i==2:
   for x in centers:out+=rect(x-7,245,14,275,'#C9AD84',T)
 if kind=='symmetry':out+=dim(340,580,540,'3 m')+dim(540,580,740,'3 m')+text(280,630,'6 − 3 = 3          9 − 6 = 3',26,C)
 if kind in ('style','premium','local-facade','two-facade'):
  labels=['Hajm / ochilish','Nisbat / ritm','Kirish / soya','Material / tutashuv','Plan bilan tekshiruv']
  out+=badge([150,310,590,880,695][i],y-35,i+1,labels[i])
  if i in (2,3):out+=rect(535,363,115,14,'#C9AD84')+arrow(725,185,660,330,C)+text(780,190,'Soya',22,C)
 return out

def massing(i):
 out=poly('200,360 600,360 600,540 200,540')+poly('200,360 360,250 760,250 600,360',BLUE)+poly('600,360 760,250 760,430 600,540','#C9AD84')
 out+=text(230,590,'Asosiy hajm: 10 × 8 × 3 m',27,T)
 if i in (2,4):out+=poly('170,450 200,430 360,430 330,450','#C9AD84')+poly('170,450 330,450 330,540 170,540','#EFD8B8')+badge(165,415,1,'Ayvon: 4 × 3 m')
 elif i==3:out+=poly('410,335 495,278 610,278 525,335',P,C)+arrow(460,180,485,315)+text(460,165,'Hovli bo‘shlig‘i',25,C)
 else:out+=dim(200,630,600,'10 m')+text(810,385,'h = 3 m',24,T)+text(805,440,'Plan ≠ hajm',23,T)
 return out

def room(kind,i):
 out=rect(145,190,720,390,P,T,8)
 out+=line(420,580,510,580,P,12)+door(420,575,90)+line(330,190,475,190,BLUE,12)
 if kind in ('bed','ergonomic','objects','plan','mini-model','zone'):
  # Uniform 155 px/m for the worked 4x3 m interior and 2x1.6 m bed.
  out=rect(195,195,620,465,P,T,8)+line(470,660,570,660,P,12)+door(470,655,100)+line(310,195,495,195,BLUE,12)
  out+=rect(280,235,248,310,'#E9E1D3')+rect(293,250,100,42,P,T,2)+rect(410,250,100,42,P,T,2)
  out+=rect(707,220,93,310,'#C9AD84')+text(302,382,'KROVAT',24,T)+text(300,420,'1,6 × 2 m',22,T)
  if kind=='zone':out+=rect(210,210,590,435,'none',C,3)+text(255,590,'Z01 · YOTOQXONA · 12 m²',24,C)
  if i==2:out+=highlight(545,235,140,310)+(badge(565,585,1,'Foydalanish / shkaf') if kind!='zone' else badge(900,595,1))
  elif i==3:out+=arrow(525,625,625,575)+arrow(625,575,665,400)+badge(840,525,1)
  elif i==4:out+=highlight(460,550,160,110)+text(830,605,'Eshik yoyi',21,C)
  else:out+=dim(195,710,815,'4 m')+text(95,420,'3 m',23,T)
  if kind=='objects' and i==2:out+=arrow(210,360,265,300)+text(195,165,'90° burilish: gabaritni qayta tekshiring',23,T)
 elif kind=='living':
  out+=rect(220,245,250,80,'#C9AD84')+rect(550,280,85,95,G)+rect(280,430,85,95,G)+rect(380,360,145,85,P,T)
  out+=text(215,220,'DIVAN',23,T)+text(380,405,'STOL',23,T)+arrow(500,550,735,525)+arrow(735,525,785,255)
  out+=badge([220,360,465,735,420][i],[355,350,445,420,545][i],i+1,['Suhbat','O‘tirish','Mebel guruhi','Hovliga yo‘l','Ochilish'][i])
 elif kind=='kitchen':
  pts=[(190,250,'SOVUTGICH'),(330,250,'YUVISH'),(470,250,'TAYYORLASH'),(610,250,'PISHIRISH')]
  for x,y,n in pts:out+=rect(x,y,135,95,BLUE if 'YUV' in n else G)+text(x+8,y+55,n,16,T)
  out+=rect(615,420,145,85,'#E9E1D3')+text(635,470,'STOL',22,T)
  if i==1:
   out=rect(145,190,720,390,P,T,8)+rect(190,245,150,95,G,T)+rect(425,245,150,95,BLUE,T)+rect(425,455,150,95,G,T)+rect(685,330,140,100,'#E9E1D3',T)
   out+=text(195,230,'SOVUTGICH',20,T)+text(435,230,'YUVISH',20,T)+text(435,435,'PISHIRISH',20,T)+text(702,385,'STOL',23,T)
   out+=arrow(265,350,500,350)+arrow(500,355,500,425)+arrow(475,445,265,365)+text(210,650,'Uch nuqta va ovqatlanish oqimi: bir-birini kesishini tekshiring.',23,T)
  else:out+=arrow(250,370,400,370)+arrow(400,370,540,370)+arrow(540,370,680,370)
  if i==4:out+=circle(375,420,22,P,C)+circle(560,420,22,P,C)+text(345,465,'1',20,C)+text(550,465,'2',20,C)
  out+=badge([235,400,545,765,565][i],[205,600,205,455,510][i],i+1,['Saqlash','Ish yo‘li','Ish yuzasi','Stul zonasi','Ikki odam'][i])
 elif kind=='kids':
  out+=rect(200,240,140,220,'#E9E1D3')+rect(390,220,160,70,BLUE)+circle(605,400,90,'#F1DFC6',T)+rect(775,235,60,250,G)
  out+=text(190,500,'UYQU',22,T)+text(405,205,'O‘QISH',22,T)+text(560,405,'O‘YIN',24,T)+text(695,530,'SAQLASH',22,T)
  out+=highlight(*[(200,240,140,220),(390,220,160,70),(765,225,80,270),(510,300,185,200),(410,480,300,85)][i])
 elif kind in ('wet','bath','accessible'):
  out+=rect(200,245,200,180,BLUE)+text(235,345,'DUSH',25,T)+rect(540,250,130,75,P,T)+text(547,230,'RAKOVINA',19,T)
  out+=rect(725,245,95,130,G)+circle(772,330,30,P,T)+text(715,415,'UNITAZ',22,T)
  out+=rect(545,350,155,125,'none',C,3)+text(530,505,'Foydalanish joyi',23,C)
  if i==2:out+=line(145,445,865,445,C,3,True)+text(215,500,'NAM',25,C)+text(710,545,'QURUQ',25,T)
  if kind=='accessible':out+=circle(485,460,52,P,C)+line(485,400,520,455,C,4)+text(195,640,'Burilish / yaqinlashish — o‘lcham talabi alohida tekshiriladi',22,T)
  else:out+=badge([270,620,395,455,785][i],[205,460,470,545,485][i],i+1)
 elif kind=='entry':
  out+=rect(745,225,105,235,'#C9AD84')+text(640,495,'KIYIM / POYABZAL',22,T)+door(500,320,80,-1)+line(145,320,500,320,T,5)+line(580,320,865,320,T,5)
  out+=arrow(460,545,585,420)+arrow(585,420,585,270)+badge([435,600,750,500,250][i],[520,375,210,345,275][i],i+1)
 else:
  for x,name in [(210,'JAVON'),(420,'KIR YUVISH'),(645,'TEXNIK')]:out+=rect(x,250,160,160,G)+text(x+10,335,name,19,T)
  out+=arrow(510,550,590,460)+arrow(590,460,750,460)+badge([220,280,500,735,570][i],[450,230,230,230,520][i],i+1)
 return out

def bubbles(kind,i):
 nodes=[(210,370,'KIRISH'),(455,235,'MEHMON'),(455,510,'TINCH'),(765,235,'OSHXONA'),(765,510,'HOVLI')]
 out=''
 for a,b in [(0,1),(0,2),(1,3),(3,4)]:out+=line(*nodes[a][:2],*nodes[b][:2],T,5)
 out+=line(455,235,455,510,C,3,True)
 for j,(x,y,s) in enumerate(nodes):out+=circle(x,y,85,'#F1DFC6' if j==i else G,T)+text(x-65,y+8,s,22,T)
 out+=text(75,665,'Uzluksiz chiziq: aloqa. Uzilgan chiziq: ajratishni tekshirish.',22,T)
 if kind=='adjacency' or i==3:out+=text(70,145,'OSHXONA — OVQATLANISH: YAQIN',20,C)+text(70,178,'MEHMON — UYQU: AJRATISH',20,C)
 return out

def site(kind,i):
 if kind=='narrow':
  out=rect(450,195,120,400,G,T,4)+rect(465,235,90,315,'#E9E1D3',T,3)+rect(465,335,90,75,G,T)+line(420,600,600,600,T,2)+rect(380,640,260,35,'#E9E1D3',T,2)
  out+=arrow(395,280,395,200,T)+text(345,175,'SHIMOL',21,T)+dim(450,625,570,'12 m')+text(600,405,'40 m',23,T)+text(660,275,'Umumiy zona',23,T)+line(560,275,645,275,T,2)+text(660,375,'Ichki hovli',23,T)+line(560,375,645,375,T,2)+text(660,490,'Tinch zona',23,T)+line(560,490,645,490,T,2)+arrow(475,585,475,250,C)+badge(700,555,i+1)
  return out+text(285,710,'480 m²: kenglik va yorug‘lik masalasi alohida tekshiriladi.',23,T)
 narrow=kind=='narrow';odd=kind=='odd-site';x=315 if narrow else 160;w=300 if narrow else 670
 out=poly('160,185 735,140 845,410 740,595 160,595',G,T) if odd else rect(x,170,w,425,G,T,4)
 out+=rect(x,610,w,45,'#E9E1D3')+text(x+70,643,'KO‘CHA',23,T)
 out+=arrow(90,280,90,195,T)+text(50,165,'SHIMOL',21,T)
 if kind=='parking':
  for xx in [275,550]:
   out+=rect(xx,240,170,280,P,T)+rect(xx+15,290,140,150,BLUE,T)+line(xx+85,240,xx+85,520,C,2,True)
  out+=arrow(750,595,750,300,T)+text(760,550,'Piyoda',20,T)
  if i in (1,2):out+=door(445,360,80)+highlight(430,265,100,210)
  if i==3:out+=highlight(695,255,100,340)
  out+=text(155,705,'Mashina gabariti, eshik ochilishi va manevrni birga tekshiring.',23,T)
 else:
  bx=x+50;by=230;bw=480 if odd else w-100;bh=175
  if kind=='courtyard':
   out+=rect(bx,by,bw,220,'#E9E1D3')+rect(bx+80,by+55,bw-160,130,G,T)+text(bx+110,by+125,'ICHKI HOVLI',21,T)
  else:out+=rect(bx,by,bw,bh,'#E9E1D3')+text(bx+30,by+95,'UY / ASOSIY HAJM',22,T)
  out+=text(x+w/2+40,495,'HOVLI',24,T)+arrow(x+w/2,600,x+w/2,440)+text(x+w/2+20,575,'Kirish',20,T)
  out+=circle(x+w-50,480,30,'#A9C99A',T)+text(x+w-145,450,'Daraxt',20,T)
  if kind=='sun':
   out+=circle(65,390,30,'#EFD3A1',C)+arrow(100,390,160,390)+text(35,460,'G‘ARB',20,C)+line(bx,by+85,bx,by+135,BLUE,10)+line(bx+bw,by+85,bx+bw,by+135,BLUE,10)+arrow(200,365,790,365,T)+text(260,435,'Havo yo‘li — imkoniyat',21,T)
  elif kind in ('access','genplan','place','site'):
   out+=rect(x+25,460,125,115,P,T)+text(x+35,525,'PARKING',19,T)
   out+=arrow(x+65,610,x+65,560)+arrow(x+180,600,x+180,440,T)
   out+=badge([x,x+180,x+80,x+w-40,x+w/2][i],[185,540,570,335,460][i],i+1)
  elif kind in ('landscape','outdoor-kitchen'):
   out+=rect(x+20,435,160,80,'#F1DFC6')+text(x+25,480,'OVQATLANISH',18,T)+rect(x+240,445,150,90,BLUE)+text(x+255,495,'O‘YIN',23,T)
   out+=arrow(x+90,400,x+90,435)+badge(x+250,700,i+1,'Oqimlar to‘qnashmasin')
  elif narrow:out+=dim(x,700,x+w,'12 m')+text(x+w+30,350,'40 m',23,T)+line(x+w/2,185,x+w/2,570,C,3,True)
  elif odd:out+=line(205,215,695,215,C,3,True)+text(230,705,'Bino o‘qi va yer chegarasi boshqa geometriya.',23,T)
  if kind=='courtyard':out+=arrow(bx+30,by+100,bx+110,by+100)+arrow(bx+bw-30,by+100,bx+bw-110,by+100)
 return out

def slope(i,advanced=False):
 h=1 if advanced else .5
 out=line(140,520,880,320,T,5)+text(105,560,'A: ±0.000',23,T)+text(810,295,f'B: +{h:.3f} m',23,T)
 out+=rect(370,250,270,210,P,T)+line(340,460,675,460,C,5)+text(410,225,'Uy pol sathi',25,T)+dim(140,625,880,'10 m')
 out+=text(240,690,f'{h:g} ÷ 10 × 100 = {h*10:g}% — o‘rtacha nishab',28,C)
 if i==3:out+=poly('375,457 640,385 640,457','#F1DFC6',C)+arrow(720,365,540,410)+text(715,355,'Yer ishlari',22,C)
 elif i==4:out+=arrow(325,485,185,520)+text(140,170,'Suv chiqarish nuqtasini kelishing',25,C)
 else:out+=badge([140,880,400,500,185][i],[495,350,465,420,515][i],i+1)
 return out+text(150,745,'Nishab ko‘rinishi kattalashtirilgan; hisob uchun sath va masofani oling.',20,T)

def section(kind,i):
 out=rect(230,230,45,340,'#E9E1D3')+rect(795,230,45,340,'#E9E1D3')+rect(230,365,610,25,G,T)+rect(230,555,610,25,G,T)
 out+=line(230,220,535,130,T,6)+line(535,130,840,220,T,6)+text(855,378,'+3.000',22,T)+text(855,580,'±0.000',22,T)
 if kind=='foundation':
  out+=rect(120,590,820,75,'#C9AD84')+rect(185,575,135,45,BLUE)+rect(750,575,135,45,BLUE)+arrow(252,425,252,560)+arrow(817,425,817,560)+text(350,645,'GRUNT / SUV / GEOLOGIYA',24,T)
  if i==1:
   out+=text(85,710,'Lenta · alohida tayanch · plita · qoziq: tanlov uchun hisob kerak',23,C)
  else:out+=badge([250,250,870,817,535][i],[545,545,685,545,260][i],i+1)
 elif kind in ('wall','seismic'):
  out+=rect(410,240,250,125,G,T)+arrow(530,255,530,355)+text(350,495,'Pastki katta ochilish',25,C)+highlight(275,390,520,165)
  if kind=='seismic':out+=arrow(115,300,215,300)+arrow(115,470,215,470)+text(80,185,'Gorizontal ta’sir',24,C)
  else:out+=text(370,690,'Yuqori tayanch — pastki ochilish: konstruktor bilan tekshiring.',23,T)
 elif kind=='frame':
  out+=rect(400,390,32,165,BLUE)+rect(660,390,32,165,BLUE)+rect(400,365,292,25,'#C9AD84')+arrow(545,285,545,355)+arrow(416,430,416,535)+arrow(676,430,676,535)+dim(416,650,676,'4 000 mm')+text(440,460,'RIGEL → USTUN',23,T)
 elif kind in ('slab','void'):
  out+=line(410,377,635,377,P,35)+text(435,335,'BO‘SHLIQ',24,C)+arrow(520,505,520,405)
  if kind=='void':out+=line(635,320,795,320,C,5)+text(460,640,'Yuqorida pol yo‘q; chet va himoyani tekshiring.',23,T)
  else:out+=text(360,640,'Teshik va tayanch — plan/kesim koordinatsiyasi.',23,T)
 elif kind in ('thermal','waterproof','balcony'):
  out+=line(280,255,280,555,C,12)+line(285,550,795,550,C,12)+rect(840,365,140,25,G,T)
  if kind=='thermal':out+=arrow(510,450,305,450)+highlight(775,340,120,65)+text(390,680,'Issiqlik oqimi / qobiq uzilishi',28,C)
  elif kind=='waterproof':out+=arrow(400,490,400,540)+line(280,490,280,545,'#2387A8',8)+line(280,545,640,545,'#2387A8',8)+text(350,680,'Suv manbai / uzluksiz himoya / chiqarish',26,T)
  else:out+=line(865,310,980,310,T,4)+line(980,310,980,365,T,4)+arrow(880,345,970,345)+text(355,680,'Eshik · chet himoyasi · suv · tayanch',26,T)
 elif kind=='shaft':
  out+=rect(580,240,110,310,BLUE,T)+line(630,230,630,565,C,6)+arrow(415,330,630,330)+arrow(415,520,630,520)+text(320,300,'Sanuzel 1',24,T)+text(320,490,'Sanuzel 0',24,T)+badge(680,400,i+1,'Shaft / xizmat kirishi')
 elif kind in ('stories','stack','two-storey'):
  out+=text(350,310,'1-QAVAT: TINCH ZONA',25,T)+text(350,500,'0-QAVAT: UMUMIY ZONA',25,T)
  if kind=='stack':out+=rect(670,260,100,95,BLUE)+rect(670,445,100,95,BLUE)+line(720,240,720,555,C,5)+text(470,645,'Nam zonalar va tayanchlar ustma-ust tekshiriladi.',23,T)
  else:out+=arrow(420,530,670,405)+arrow(670,405,750,305)+text(350,640,'Sathlar farqi: 3 000 mm',27,C)
  out+=badge([250,850,480,660,600][i],[600,400,355,420,230][i],i+1)
 return out

def stair(kind,i):
 out=line(160,570,400,570,T,5)+line(704,300,970,300,T,5)
 # 18 risers: schematic side representation, tread count is independent.
 for k in range(18):
  x=380+k*18;y=555-k*15
  out+=line(x,y+15,x,y,T,3)+line(x,y,x+18,y,T,3)
 out+=text(120,615,'±0.000',25,T)+text(785,250,'+3.000 m',25,T)+text(150,690,'3 000 ÷ 18 ≈ 166,7 mm / ko‘tarilish',29,C)
 if kind=='railing':
  out+=line(380,475,705,205,C,5)
  for k in range(7):out+=line(385+k*50,535-k*42,385+k*50,470-k*42,C,3)
  out+=text(180,165,'Tayanch / to‘ldirish / tutqich',27,T)
 else:
  out+=line(600,220,930,220,T,5)+arrow(580,355,580,230)+text(600,365,'Bosh usti bo‘shligi',22,C)
  out+=highlight(*[(365,275,345,300),(430,430,90,100),(685,210,240,95),(345,395,180,140),(560,200,160,200)][i])
 return out

def grid(i):
 out=''
 for x,n in [(260,'A'),(780,'B')]:out+=line(x,175,x,620,T,2,True)+circle(x,145,25,P,T)+text(x-8,154,n,25,T)
 for y,n in [(200,'1'),(590,'2')]:out+=line(200,y,840,y,T,2,True)+circle(145,y,25,P,T)+text(137,y+8,n,25,T)
 for x in [260,780]:
  for y in [200,590]:out+=rect(x-18,y-18,36,36,'#C9AD84',T)
 out+=rect(260,200,520,390,'none',T,8)+dim(260,630,780,'4 000 mm')+text(875,425,'3 000 mm',22,T)
 out+=badge([260,500,780,520,780][i],[240,280,540,540,240][i],i+1)
 return out

def layers(kind,i):
 if kind=='composite':
  xs=[180,210,610,810];ws=[30,400,200,30];names=['Pardoz','Yadro','Izolyatsiya','Pardoz'];vals=['15','200','100','15']
  out=''
  for j,(x,w) in enumerate(zip(xs,ws)):
   out+=rect(x,265,w,220,[P,'#C9AD84',BLUE,P][j])+text([90,360,610,890][j],200,names[j],21,T)+line([125,420,685,930][j],210,x+w/2,255,T,2)+text([95,350,630,890][j],555,vals[j]+' mm',21,T)+line(x+w/2,490,[125,400,680,925][j],525,T,2)
  out+=text(230,630,'15 + 200 + 100 + 15 = 330 mm',30,C)+highlight(xs[min(i,3)],265,ws[min(i,3)],220)
  return out
 if kind=='profile':
  out=poly('250,240 650,240 650,375 385,375 385,640 250,640','#C9AD84',T,5)+dim(250,690,650,'300 mm')+text(440,435,'Tokcha: 100 mm',25,T)
  return out+badge([250,650,350,350,650][i],[210,210,590,660,630][i],i+1)
 if kind=='materials':
  return rect(220,250,420,240,'#C9AD84')+rect(640,250,25,240,BLUE)+text(240,230,'Building Material',27,T)+text(675,375,'Surface',26,C)+arrow(845,400,675,400)+text(210,600,'Ichki tarkib ≠ tashqi yuzadagi rang',29,T)+badge(250+80*i,520,i+1)
 return table(150,235,['Layer','PLAN','DOC'],[['AR-WALL','Ko‘rinadi','Ko‘rinadi'],['AR-FURN','Ko‘rinadi','Tanlovga ko‘ra'],['AR-DIMS','Ko‘rinadi','Ko‘rinadi']],[280,260,290],i%3)+text(180,540,'Ko‘rinmas element ≠ o‘chirilgan element',29,C)+badge(180+155*i,650,i+1,['Guruh','Holat','Kombinatsiya','Nomlash','Tekshiruv'][i])

def data(kind,i):
 if kind=='classification':
  return table(80,220,['Model turi','Kelishilgan sinf','Property'],[['Wall','Devor sinfi','Mavjudligini tekshir'],['Door','Eshik sinfi','Mavjudligini tekshir'],['Zone','Xona / makon sinfi','Mavjudligini tekshir']],[260,365,395],i%3)+text(145,545,'Sinfning nomi tanlangan classification tizimiga bog‘liq.',24,T)+text(145,615,'Noto‘g‘ri sinf → noto‘g‘ri maydon yoki jadval mezoni.',25,C)+badge(180+180*i,680,i+1)
 out=rect(110,230,230,240,G,T)+text(130,280,'MODEL',28,T)+text(130,335,'D01: 900 mm',23,T)+text(130,385,'D02: 800 mm',23,T)+text(130,435,'W01: deraza',23,T)
 out+=arrow(355,365,445,365)+table(470,230,['ID','En / kod'],[['D01','900 mm / A'],['D02','800 mm / B']],[175,310],min(i,1))
 labels={'schedule':['Door mezoni','ID + Width','ID tartibi','Turlarni ajratish','2 eshik = 2 satr'],
 'property':['Finish_Code','Maydon turi','A / B qiymat','Jadval maydoni','Bo‘sh qiymatni topish'],
 'classification':['Element turi','Kelishilgan sinf','Property mavjudligi','Jadval mezoni','Manbadan tuzatish'],
 'bim':['Geometriya + data','Element kimligi','Opening bilan moslik','Manba → hujjat','900 → 1 000 mm'],
 'info':['Geometriya / data','D01 / D02 / W01','Finish_Code','Dublikatni qidirish','Eksportda shu ID']}
 out+=badge(490,515,i+1,labels[kind][i])+text(115,615,'W01 eshik mezoniga kirmaydi.',27,C)
 if i==4 and kind in ('bim','schedule'):out+=text(115,685,'Elementni o‘zgartiring → jadvalni qayta tekshiring.',24,T)
 return out

def appearance(kind,i):
 out=''
 for j,(x,n) in enumerate([(180,'MAVJUD'),(470,'BUZILADI'),(760,'YANGI')]):
  color=['#A7B0AA','#D99883','#8DB9A0'][j] if kind=='renovation' else [G,'#F1DFC6',BLUE][j]
  out+=rect(x,240,65,280,color,T)+text(x-45,565,n if kind=='renovation' else ['ODDIY','MEZON','NATIJA'][j],23,T)
 out+=line(110,520,985,520,T,5)+badge([200,495,790,495,790][i],[205,205,205,610,610][i],i+1)
 label={'renovation':'Holat → filtr → hujjat. Element holatini manbadan tekshiring.',
 'overrides':'Grafik qoida rangni o‘zgartiradi; geometriya saqlanadi.',
 'mvo':'Soddalashtirilgan va batafsil ko‘rinish — ayni model.',
 'favorite':'Saqlangan sozlama → yangi element. Global bog‘lanish deb taxmin qilmang.'}[kind]
 return out+lines(120,675,label,75,24,T)

def hotlink(i):
 out=rect(100,250,240,220,G,T)+text(130,290,'MODULE MANBA',23,T)
 for y in [205,445]:
  out+=arrow(350,360,510,y+80)+rect(525,y,300,160,BLUE,T)+text(550,y+90,'HOTLINK NUSXA',24,T)
  out+=rect(545,y+110,80,30,G,T)
 return out+badge([200,200,825,500,825][i],[210,520,190,350,650][i],i+1)+text(100,700,'Manba, joylashuv, ID va yangilanishni alohida tekshiring.',23,T)

def drawing(kind,i):
 if kind=='dimensions':
  out='';xx=[150,550,850,1050]
  for x in xx:out+=line(x,260,x,480,T,4)
  for a,b,s in zip(xx,xx[1:],['4 000','3 000','2 000']):out+=dim(a,350,b,s)
  out+=dim(150,540,1050,'9 000 mm')+text(230,650,'4 000 + 3 000 + 2 000 = 9 000 mm',28,C)
  return out+badge(xx[min(i,3)],225,i+1)
 if kind=='slab-model':
  out=rect(185,230,640,480,G,T)+rect(475,345,160,160,P,C)+text(490,410,'TESHIK',22,C)+text(235,195,'Kontur: 4 × 3 = 12 m²',27,T)
  return out+text(160,690,'12 − 1 = 11 m² geometrik maydon; qoidani alohida belgilang.',23,T)+badge([185,825,475,625,600][i],[200,620,315,430,600][i],i+1)
 if kind=='openings':
  out=rect(200,250,680,290,'#E9E1D3')+rect(295,355,95,185,'#C9AD84')+rect(580,310,130,150,BLUE,T)
  return out+text(205,605,'D01: 900 × 2 100 mm',25,T)+text(555,605,'W01: 1 200 × 1 500 mm',25,T)+text(440,675,'Sill 900 + bo‘y 1 500 = yuqori sath 2 400 mm',24,C)+badge([300,300,710,710,880][i],[220,570,285,490,570][i],i+1)
 if kind=='graphics':
  if i==0:
   return line(165,325,415,325,T,5)+line(615,325,830,325,C,5)+line(830,325,830,500,C,5)+line(830,500,650,500,C,5)+text(180,255,'LINE: BIR SEGMENT',26,T)+text(605,255,'POLYLINE: BOG‘LANGAN',25,C)+text(210,650,'Bitta chiziq va ketma-ket kontur geometriyasini ajrating.',25,T)
  out=rect(200,245,580,320,BLUE,T)+text(270,355,'YOTOQXONA',29,T)+text(270,405,'Text: mustaqil yozuv',23,T)+arrow(965,490,800,490)+text(800,430,'Label',26,C)+text(800,465,'Elementga',21,C)+text(800,510,'bog‘langan',21,C)
  return out+text(220,650,'Fill — 2D belgi. Text va Labelning manbasi farq qiladi.',24,T)+badge(245+125*i,590,i+1)
 raise ValueError(kind)

def roof(i):
 out=poly('170,475 520,273 870,475',G,T,5)+line(170,475,870,475,T,3)+line(520,273,520,475,C,3,True)
 out+=text(250,520,'Yarim oraliq: 2 m',25,T)+text(550,375,'h ≈ 1,155 m',25,C)+text(170,670,'h = 2 × tan(30°) ≈ 1,155 m',29,C)+text(350,210,'Cho‘qqi',24,T)
 return out+badge([170,520,520,870,350][i],[445,180,405,510,580][i],i+1,['Tayanch','Tekisliklar','Qiyalik','Tutashuv','Suv yo‘li'][i])

def roof_plan(i):
 out=poly('180,210 820,210 820,430 560,430 560,600 180,600',G,T,5)+line(370,210,370,600,T,4)+line(370,320,820,320,T,4)+line(370,320,560,430,C,4)
 out+=arrow(290,300,205,300)+arrow(665,350,665,420)+arrow(470,480,555,480)+text(760,510,'Suv yo‘li',24,C)
 return out+badge([180,290,370,560,820][i],[185,380,290,460,465][i],i+1,['Hajm','Qiyalik','Vodiy','Kontur','Variant'][i])+text(180,695,'Murakkab tutashuv: geometriya va suv chiqarishni birga tekshiring.',23,T)

def documents(kind,i):
 out=''
 if kind=='stamp':
  out=rect(120,190,920,460,P,T,4)+rect(150,220,600,260,'none',T,2)+rect(590,530,425,85,P,T,2)
  out+=rect(190,255,270,190,P,T,4)+line(325,255,325,445,T,3)+text(500,315,'A-01 · PLAN',25,T)
  out+=text(610,565,'LOYIHA / VARAQ / SANA',19,T)+text(610,605,'ID: A-01    REVISION: R02',20,C)+highlight(580,520,445,105)
 else:
  for j,x in enumerate([80,615]):
   title=('PLAN_100' if j==0 else 'DETAIL_20') if kind=='view' else ('A-01 · PLAN' if j==0 else 'A-02 · KESIM')
   out+=rect(x,225,455,360,P,T,4)+text(x+25,205,title,26,T)
   if j==0:out+=rect(x+45,270,220,210,P,T,4)+line(x+155,270,x+155,480,T,3)
   else:out+=line(x+55,445,x+385,445,T,5)+line(x+55,445,x+55,335,T,5)+line(x+55,335,x+220,275,T,5)+line(x+220,275,x+385,335,T,5)+line(x+385,335,x+385,445,T,5)
   out+=rect(x+180,520,260,50,P,T,2)+text(x+195,550,('A-01' if j==0 else 'A-02')+' · R02',19,C)
 if kind=='view':out+=text(165,700,'Ayni model: 1:100 umumiy view / 1:20 detal view.',26,C)
 elif kind=='publisher':out+=text(170,700,'Client_PDF → ikki varaq → HOUSE_R02.pdf',26,C)
 else:out+=text(165,700,'View → Drawing → Layout → haqiqiy chiqarilgan fayl',25,T)
 out+=badge([110,600,800,920,990][i],[165,640,640,615,650][i],i+1)
 return out

def exchange(kind,i):
 out=rect(100,245,265,235,G,T)+text(125,295,'MANBA MODEL',26,T)+text(125,355,'D01 / Wall',24,T)+text(125,415,'4 000 mm nazorat',22,T)
 out+=arrow(380,350,480,350)+rect(495,285,200,125,BLUE,T)+text(535,360,kind.upper(),29,T)+arrow(710,350,810,350)+rect(825,245,225,235,P,T)+text(850,300,'QAYTA OCHISH',21,T)+text(850,355,'ID / birlik',23,T)+text(850,410,'geometriya',23,T)
 out+=badge([125,525,525,850,850][i],[215,255,450,215,520][i],i+1)+text(150,625,'Eksport tugashi yetarli emas: natija boshqa muhitda tekshiriladi.',23,C)
 return out

def norm(kind,i):
 if kind in ('escape','fire'):
  out=rect(145,245,320,270,P,T,6)+rect(465,245,460,270,P,T,6)+line(465,400,465,485,P,10)+door(465,480,80)+line(800,515,890,515,P,10)+door(800,510,85)
  out+=text(210,300,'XONA',27,T)+text(545,300,'YO‘LAK',27,T)+arrow(245,410,610,410)+arrow(610,410,845,455)+arrow(845,455,845,600)+text(700,645,'TASHQARIGA',25,T)
  out+=rect(650,380,75,85,'#D99883',RED)+text(575,350,'TO‘SIQ: SHKAF',23,RED)
  return out+highlight(*[(200,350,130,110),(480,355,340,145),(790,440,120,105),(630,365,115,115),(635,365,105,115)][i])+text(135,710,'Yo‘nalish va masofa tegishli obyekt/band bo‘yicha tekshiriladi.',22,T)
 if kind=='light':
  return rect(240,270,320,290,P,T)+rect(760,150,200,410,'#C9AD84',T)+line(550,300,550,420,BLUE,10)+line(760,150,555,300,C,4)+line(760,150,260,540,C,3,True)+text(210,610,'XONA',27,T)+text(770,610,'QO‘SHNI BINO',23,T)+text(185,690,'Joy / sana / orientatsiya / qo‘shni balandligi — hisob shartlari',23,C)+badge([550,760,760,550,300][i],[255,125,560,435,640][i],i+1)
 return table(80,205,['Savol','Manba / dalil','Holat'],[['Obyekt turi','Turar joy / foydalanish','Aniqlash'],['Tahrir / sana','Rasmiy hujjat','Tekshirish'],['Band / talab','Aniq havola','Tekshirish'],['Plan / kesim','Loyiha revisioni','Solishtirish'],['Mas’ul / qayta test','Qaror qaydi','Yopish']],[270,405,310],i)+text(95,655,'Manbasiz raqamni majburiy me’yor deb qo‘llamang.',27,C)

def brief(kind,i):
 rows={'brief':[['Uyqu','3 yotoqxona','Majburiy'],['Ish','Tinch ish joyi','Muhim'],['Mehmon','Ayvon / ovqatlanish','Variant'],['Chegara','Budjet / vaqt / site','Aniqlash'],['Tasdiq','Mijoz qarori','Qayd']],
 'budget':[['Scope','Qanday ish / fayl?','Kelishish'],['Tom','Murakkab tutashuv','Xarajat omili'],['Balkon','Tayanch / servis','Xarajat omili'],['Sodda variant','Foyda / yo‘qotish','Solishtirish'],['Smeta','Manba / sana','Tekshirish']],
 'feedback':[['F01','Oshxona → hovli','Funksional'],['F02','Fasad rangi','Estetik'],['Ta’sir','Quvur / eshik / yo‘l','Tekshirish'],['Revision','R02 → R03','Yangilash'],['Tasdiq','Chizma + mijoz qaydi','Qayta test']],
 'audit':[['Plan','Mebel / eshik / yo‘l','Dalil kerak'],['Site','Sath / orientatsiya','Dalil kerak'],['Model','Geometriya + data','Dalil kerak'],['Hujjat','Revision / PDF','Dalil kerak'],['Ko‘nikma','Mustaqil bajarish','Qayta mashq']],
 'coordination':[['K-01','AR-01 / ST-01 ustun','Konflikt'],['Joy','O‘q / plan / kesim','Dalil'],['Mas’ul','Arxitektor / konstruktor','Savol'],['Revision','Qaror + sana','Yangilash'],['Tekshiruv','Barcha ko‘rinish','Qayta test']]}
 return table(80,205,['Bo‘lim','Namuna','Keyingi ish'],rows[kind],[240,440,305],i)+badge(120,625,i+1)+text(170,635,'Qayd → dalil → qaror → qayta tekshiruv',26,T)

def variants(i):
 out=''
 for x,s in [(110,'A: MEHMON AJRALGAN'),(635,'B: HOVLI ALOQASI')]:
  out+=rect(x,230,410,270,P,T,5)+rect(x+15,245,170,110,G,T)+rect(x+230,245,160,110,BLUE,T)+text(x+25,200,s,23,T)+arrow(x+195,470,x+195,365)+arrow(x+195,365,x+300,365)
 out+=text(135,615,'Bir xil mezon: privacy / yo‘l / hovli / texnik murakkablik',25,C)
 return out+badge(150+185*i,680,i+1)

def portfolio(i):
 out=''
 for x,s in [(100,'TOR SITE'),(425,'OILA / PLAN'),(750,'BIM / HUJJAT')]:
  out+=rect(x,210,285,390,P,T)+rect(x+20,255,245,180,G,T)+line(x+35,380,x+140,285,T,4)+line(x+140,285,x+225,370,T,4)+text(x+20,480,s,23,T)+text(x+20,530,'Vazifa / qaror',21,T)+text(x+20,575,'Dalil / hissa',21,C)
 return out+badge(130+185*i,625,i+1)+text(210,685,'Chizma bosh rolni, matn qisqa izohni bajaradi.',24,T)

def presentation(i):
 out=rect(130,205,865,355,P,T,5)+rect(160,235,445,270,G,T)+rect(650,255,305,65,BLUE,T)+text(675,298,'EHTIYOJ → QAROR',22,T)+text(675,375,'Chizma — dalil',25,T)+text(675,435,'Ochiq savol — qayd',23,C)
 out+=line(195,460,380,285,T,5)+line(380,285,565,460,T,5)+badge(160+175*i,625,i+1)
 return out+text(135,690,'Uch asosiy qarorni ko‘rsating; xonalar ro‘yxatini o‘qib bermang.',23,T)

# Every entry is intentional. Five recipes may override a module's base diagram
# when the teaching stage changes topic (e.g. final integrated projects).
MODULE_RECIPES={
 'L01_M01':'composition','L01_M02':'proportion','L01_M03':'rhythm','L01_M04':'symmetry','L01_M05':'massing','L01_M06':'style',
 'L02_M01':'ergonomic','L02_M02':'adjacency','L02_M03':'circulation','L02_M04':'living','L02_M05':'kitchen','L02_M06':'bed','L02_M07':'kids','L02_M08':'wet','L02_M09':'entry','L02_M10':'storage',
 'L03_M01':'site','L03_M02':'sun','L03_M03':'access','L03_M04':'place','L03_M05':'landscape','L03_M06':'parking','L03_M07':'slope','L03_M08':'genplan',
 'L04_M01':['family','adjacency','family','courtyard','adjacency'],'L04_M02':'adjacency','L04_M03':'courtyard','L04_M04':['living','living','sun','living','entry'],'L04_M05':'summer-kitchen','L04_M06':['banja','banja','waterproof','storage','audit'],'L04_M07':'sun','L04_M08':'local-facade',
 'L05_M01':'ui-basic','L05_M02':'documents','L05_M03':'wall-plan','L05_M04':'slab-model','L05_M05':'openings','L05_M06':['frame','grid','frame','frame','grid'],'L05_M07':'objects','L05_M08':'graphics','L05_M09':'dimensions','L05_M10':['brief','mini-model','openings','dimensions','zone'],
 'L06_M01':'stories','L06_M02':'layers','L06_M03':'materials','L06_M04':'composite','L06_M05':'profile','L06_M06':'roof','L06_M07':'stair','L06_M08':'railing','L06_M09':'slope','L06_M10':'zone',
 'L07_M01':'favorite','L07_M02':'overrides','L07_M03':'mvo','L07_M04':'renovation','L07_M05':'schedule','L07_M06':'property','L07_M07':'classification','L07_M08':'hotlink','L07_M09':['layers','layers','documents','classification','audit'],
 'L08_M01':'foundation','L08_M02':'wall','L08_M03':['frame','frame','grid','grid','coordination'],'L08_M04':'slab','L08_M06':'waterproof','L08_M07':'thermal','L08_M08':'seismic','L08_M09':'coordination',
 'L09_M01':'norm','L09_M02':['norm','adjacency','wet','stories','norm'],'L09_M03':'site','L09_M04':'light','L09_M05':'fire','L09_M06':'escape','L09_M07':'accessible','L09_M08':['norm','norm','genplan','coordination','norm'],
 'L10_M01':'brief','L10_M02':'site','L10_M03':'adjacency','L10_M04':['adjacency','bed','entry','local-facade','zone'],'L10_M05':['variants','variants','entry','stack','audit'],'L10_M06':['brief','grid','mini-model','frame','audit'],'L10_M07':'composition','L10_M08':'roof-plan','L10_M09':'stories','L10_M10':'genplan','L10_M11':'album',
 'L11_M01':'two-storey','L11_M02':'stack','L11_M03':'stair','L11_M04':'shaft','L11_M05':'void','L11_M06':'balcony','L11_M07':'two-facade','L11_M08':['layers','stack','shaft','roof-plan','audit'],'L11_M09':['documents','dimensions','stories','feedback','coordination'],
 'L12_M01':'bim','L12_M02':'info','L12_M03':'schedule','L12_M04':'view','L12_M05':'documents','L12_M06':'stamp','L12_M07':'publisher','L12_M08':'dwg','L12_M09':'ifc','L12_M10':['brief','schedule','documents','publisher','audit'],
 'L13_M01':'brief','L13_M02':'brief','L13_M03':'budget','L13_M04':'variants','L13_M05':'presentation','L13_M06':'feedback','L13_M07':['entry','brief','variants','variants','coordination'],'L13_M08':['brief','variants','presentation','feedback','audit'],
 'L14_M01':'narrow','L14_M02':'odd-site','L14_M03':'slope-advanced','L14_M04':['brief','adjacency','access','massing','audit'],'L14_M05':['brief','adjacency','accessible','kitchen','audit'],'L14_M06':'premium','L14_M07':['audit','entry','local-facade','info','audit'],'L14_M08':['audit','narrow','adjacency','coordination','audit'],
 'L15_M01':['brief','bed','coordination','bim','audit'],'L15_M02':['layers','mini-model','classification','publisher','audit'],'L15_M03':['entry','openings','coordination','schedule','audit'],'L15_M04':'brief','L15_M05':['variants','genplan','coordination','documents','audit'],'L15_M06':'presentation','L15_M07':'portfolio','L15_M08':'audit'}

def special(kind,i):
 if kind=='album':
  out=''
  for j,n in enumerate(['GENPLAN','PLAN','FASAD','KESIM','IZOH']):
   x=75+j*210;out+=rect(x,250,180,320,'#F1DFC6' if i==j else P,T,3)+text(x+15,300,f'A-{j+1:02}',25,T)+text(x+10,380,n,21,T)+line(x+20,445,x+160,445,T,2)+line(x+20,470,x+140,470,T,2)
  return out+text(150,665,'Loyiha albomi: har varaqning vazifasi va manbasi aniq.',25,T)
 if kind=='wall-plan':
  out=rect(190,190,660,510,'#C9AD84',T,4)+rect(220,220,600,450,P,T,3)
  out+=dim(220,180,820,'4 000 mm ichki')+dim(190,745,850,'4 400 mm tashqi')+text(50,465,'3 000 mm',21,T)+text(870,465,'3 400 mm',21,T)
  out+=text(340,390,'ICHKI XONA: 12 m²',27,T)+text(355,460,'DEVOR: 200 mm',25,C)
  out+=badge([220,220,190,850,500][i],[220,670,190,700,550][i],i+1)
  return out
 if kind=='ui-basic':
  out=line(160,345,450,345,T,18)+text(175,275,'FLOOR PLAN: 2D',25,T)
  out+=poly('660,400 950,270 970,290 680,420',G,T,3)+poly('660,400 950,270 950,480 660,610','#C9AD84',T,3)
  out+=text(730,245,'3D: AYNI DEVOR',25,T)+arrow(470,355,620,355)+text(155,675,'Bitta element: asbob → parametr → plan → 3D tekshiruv',25,T)
  return out+badge([175,320,800,450,940][i],[310,310,640,400,520][i],i+1)
 if kind=='family':
  return table(80,220,['Foydalanuvchi','Kundalik ehtiyoj','Makon'],[['Ota-ona','Uyqu / ish / saqlash','Tinch zona'],['Ikki bola','Uyqu / o‘qish / o‘yin','Bola xonasi'],['Mehmon','Suhbat / ovqatlanish','Umumiy zona'],['Oila','Dam / ovqat tayyorlash','Uy + hovli'],['Hammasi','Ertalab / mehmon vaqti','Yo‘llar sinovi']],[230,450,300],i)+badge(150,620,i+1)+text(200,630,'Xona sonini kun tartibidan asoslang.',27,T)
 if kind=='banja':
  out=''
  for j,(x,n) in enumerate([(90,'KIRISH'),(350,'KIYINISH'),(610,'YUVINISH'),(870,'DAM')]):
   out+=rect(x,270,210,200,BLUE if j==2 else G,T)+text(x+25,365,n,22,T)
   if j<3:out+=arrow(x+213,370,x+255,370)
  out+=line(610,240,610,525,C,3,True)+text(270,580,'QURUQ',25,T)+text(635,580,'NAM',25,C)
  return out+badge(130+185*i,630,i+1)+text(220,690,'Nam foydalanish, qaytish yo‘li va xizmatni ajrating.',24,T)
 if kind=='summer-kitchen':
  out=rect(160,220,810,410,P,T,5)
  for x,n in [(195,'SAQLASH'),(380,'YUVISH'),(565,'TAYYORLASH'),(750,'MANGAL')]:
   out+=rect(x,265,160,85,BLUE if n=='YUVISH' else G,T)+text(x+8,310,n,18,T)
  out+=arrow(280,380,820,380)+rect(270,465,230,100,'#E9E1D3')+text(310,525,'TASHQI STOL',23,T)+rect(750,455,170,125,BLUE,T)+text(765,520,'O‘YIN',24,T)
  out+=arrow(760,410,545,425)+arrow(545,425,500,500)+line(720,400,720,600,C,3,True)
  return out+badge([200,370,820,400,710][i],[230,420,215,230,580][i],i+1)+text(180,690,'Issiq idish / tutun / bolalar oqimi: alohida tekshiruv.',24,T)
 if kind=='circulation':
  out=rect(130,235,360,220,G,T)+rect(690,235,330,220,BLUE,T)+rect(130,510,360,110,P,T)+rect(690,510,330,110,P,T)
  out+=text(165,310,'MEHMONXONA',25,T)+text(730,310,'OSHXONA',25,T)+text(180,575,'KIRISH',25,T)+text(730,575,'OVQATLANISH',24,T)
  out+=arrow(330,525,330,410)+arrow(865,410,865,510)+text(375,490,'6 m yo‘l',23,C)+text(885,485,'3 m yo‘l',23,C)
  if i>=3:out+=door(500,405,90)+door(610,405,90,-1)+highlight(485,285,135,135)+text(390,210,'Ikki ochilish yoyi: to‘qnashuvni tekshiring',23,C)
  return out+text(190,700,'Yo‘l uzunligi o‘quv sharti; bu sxema masshtabli plan emas.',23,T)
 raise ValueError(kind)

def draw(kind,i):
 if kind in ('ui-basic','family','banja','summer-kitchen','circulation','wall-plan','album'):return special(kind,i)
 if kind in ('composition','proportion','rhythm','symmetry','style','premium','local-facade','two-facade'):return facade(kind,i)
 if kind=='massing':return massing(i)
 if kind in ('bed','ergonomic','objects','plan','mini-model','zone','living','kitchen','kids','wet','bath','accessible','entry','storage'):return room(kind,i)
 if kind=='adjacency':return bubbles(kind,i)
 if kind in ('site','sun','access','place','courtyard','landscape','genplan','parking','narrow','odd-site','outdoor-kitchen'):return site(kind,i)
 if kind in ('slope','slope-advanced'):return slope(i,kind=='slope-advanced')
 if kind in ('foundation','wall','seismic','frame','slab','void','thermal','waterproof','balcony','shaft','stories','stack','two-storey'):return section(kind,i)
 if kind in ('stair','railing'):return stair(kind,i)
 if kind=='grid':return grid(i)
 if kind in ('composite','profile','materials','layers'):return layers(kind,i)
 if kind in ('schedule','property','classification','bim','info'):return data(kind,i)
 if kind in ('renovation','overrides','mvo','favorite'):return appearance(kind,i)
 if kind=='hotlink':return hotlink(i)
 if kind in ('dimensions','slab-model','openings','graphics'):return drawing(kind,i)
 if kind=='roof':return roof(i)
 if kind=='roof-plan':return roof_plan(i)
 if kind in ('documents','stamp','view','publisher'):return documents(kind,i)
 if kind in ('dwg','ifc'):return exchange(kind,i)
 if kind in ('norm','fire','escape','light'):return norm(kind,i)
 if kind in ('brief','budget','feedback','audit','coordination'):return brief(kind,i)
 if kind=='variants':return variants(i)
 if kind=='portfolio':return portfolio(i)
 if kind=='presentation':return presentation(i)
 raise ValueError(kind)

def build():
 # Preserve the 27 previously authored lessons; add supplements to 653 others.
 existing={f'L00_M{m:02}_{n:03}' for m,c in [(1,3),(2,4),(3,3),(4,6),(5,4)] for n in range(1,c+1)}|{f'L08_M05_{n:03}' for n in range(1,6)}|{'L05_M03_001','L05_M03_002'}
 contents=get_all_lesson_content();records=[]
 for module,w in WORKBOOKS.items():
  for i,u in enumerate(w['units']):
   code=u['code']
   if code in existing:continue
   recipe=MODULE_RECIPES[module];kind=recipe[i] if isinstance(recipe,list) else recipe
   stage=GUIDES[module]['stages'][i]
   # Original authored action/result belong together; worked stage is shown
   # separately so unrelated independent exercise conditions are never mixed.
   asset=f'{code.lower()}.svg'
   body=draw(kind,i)
   reading_note=('Raqamli belgi ushbu darsda tekshiriladigan joyni ajratadi.' if 'r="18"' in body else 'Chizmadagi yozuv va shartli belgilarni yuqoridagi bajarish bosqichi bilan solishtiring.')+' Chizma sxematik; aniq natijani dars sharti va o‘lcham yozuvidan tekshiring.'
   if kind in ('slope','slope-advanced'):
    reading_note+=' Vertikal o‘zgarish ko‘rgazmalilik uchun kattalashtirilgan: rasm burchagidan nishabni o‘lchamang. Nishab = sathlar farqi ÷ gorizontal masofa × 100%.'
   footer=lines(45,875,stage.split('→')[0].strip(),92,22,T)
   svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1150" height="1100" viewBox="0 0 1150 1100"><rect width="1150" height="960" fill="{P}"/><g font-family="DejaVu Sans, Segoe UI, sans-serif">'+text(45,50,code+'  /  O‘QUV NAMUNASI',19,C)+lines(45,92,u['title'],64,29,T)+lines(45,155,GUIDES[module]['case'],112,17,T)+'<g transform="translate(0,80)">'+body+'</g>'+line(45,835,1105,835,T,2)+footer+text(45,1080,'Sxematik tasvir: qurilish detali, normativ minimum yoki haqiqiy Archicad skrinshoti emas.',18,T)+'</g></svg>'
   (D/asset).write_text(svg,encoding='utf-8')
   block=next(j for j,b in enumerate(contents[code]) if b['title']=='Bajarish tartibi va namunaviy xulosa')
   records.append(dict(code=code,asset=asset,title=u['title']+' — ko‘rgazmali namuna',
     explanation=[GUIDES[module]['case'],stage,reading_note],
     exercise=u['action'],solution=u['result'],block=block,recipe=kind,
     boundary='O‘quv sxemasi. Sonlar mashq sharti; majburiy norma yoki tayyor konstruktiv yechim emas. Loyiha talabi va qo‘llanadigan hujjat alohida tekshiriladi.',
     credit='ARCHIPRO UZ — darsning mavjud ishlangan misoli bo‘yicha yaratilgan vektor chizma',
     source_url='https://gov.uz/oz/mc/pages/shaharsozlik-normalari-va-qoidalari' if module.startswith('L09_') else None))
 assert len(records)==653,len(records)
 (D/'lesson_figures.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('Authored:',len(records),'diagrams; recipes:',len({r['recipe'] for r in records}))
if __name__=='__main__':build()
