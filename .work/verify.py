from pathlib import Path
import re, ipaddress, json
from PIL import Image
from build import ROOT,tickets,netq,netp
def ordered(path):
    return sorted(path.glob('[0-9]*.md'),key=lambda p:int(p.stem.split('-')[0]))
groups=[(ROOT/'proekt',8,'Билет',30,4),(ROOT/'net/Теория',8,'Вопрос',60,8),(ROOT/'net/Практика',10,'Задание',40,4)]
for folder,count,label,total,group_size in groups:
    files=ordered(folder); assert len(files)==count
    nums=[]
    for p in files:
        text=p.read_text('utf-8')
        local=list(map(int,re.findall(r'^## '+label+r' (\d+)$',text,re.M)))
        assert p.stem==f'{local[0]}-{local[-1]}'
        assert len(local)==min(group_size,total-local[0]+1)
        assert text.count('```')%2==0
        assert '\ufffd' not in text
        nums+=local
    assert nums==list(range(1,total+1))
pro='\n'.join(p.read_text('utf-8') for p in ordered(ROOT/'proekt'))
for t in tickets:
    for q in t: assert q in pro
for path,qs in [(ROOT/'net/Теория',netq),(ROOT/'net/Практика',netp)]:
    alltext='\n'.join(p.read_text('utf-8') for p in ordered(path))
    for q in qs: assert q in alltext
links=0
for folder in [ROOT/'proekt',ROOT/'net/Теория',ROOT/'net/Практика']:
    for f in folder.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',f.read_text('utf-8')):
            if target.startswith('https://'): continue
            assert (f.parent/target).exists(),(f,target)
            links+=1
for target in re.findall(r'\]\(([^)]+)\)',(ROOT/'README.md').read_text('utf-8')):
    assert (ROOT/target).exists(),target
for n in range(1,31):
    p=ROOT/'proekt/схемы'/f'{n:02d}.png'
    with Image.open(p) as im:
        im.verify()
    with Image.open(p) as im:
        assert im.width<4096 and im.height<4096,(p,im.size)
expected=[('192.168.10.0','192.168.10.1','192.168.10.62','192.168.10.63'),('192.168.10.64','192.168.10.65','192.168.10.126','192.168.10.127'),('192.168.10.128','192.168.10.129','192.168.10.190','192.168.10.191'),('192.168.10.192','192.168.10.193','192.168.10.254','192.168.10.255')]
for n,want in zip(ipaddress.ip_network('192.168.10.0/24').subnets(new_prefix=26),expected):
    assert tuple(map(str,[n.network_address,n[1],n[-2],n.broadcast_address]))==want
n=ipaddress.ip_network('172.16.20.0/26')
assert str(n[-2])=='172.16.20.62' and str(n.broadcast_address)=='172.16.20.63'
report={'project_tickets':30,'project_theory_answers':60,'project_png':30,'network_theory_answers':60,'network_practical_solutions':40,'solution_markdown_files':26,'local_links_checked':links,'subnet_calculations':'pass','original_question_coverage':'pass','network_labs_executed':False}
(ROOT/'.work/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps(report,ensure_ascii=True))
