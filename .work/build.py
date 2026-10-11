from pathlib import Path
from zipfile import ZipFile
from lxml import etree
import re, json
ROOT=Path(__file__).resolve().parent.parent
with ZipFile(next((ROOT/'proekt').glob('*.docx'))) as z:
    root=etree.fromstring(z.read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    ps=[''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in root.xpath('//w:body//w:p',namespaces=ns)]
    ps=[p.strip() for p in ps if p.strip()]
tickets=[]
for p in ps:
    if re.fullmatch(r'Билет №\s*\d+',p): tickets.append([])
    else: tickets[-1].append(p)
assert len(tickets)==30 and all(len(t)==3 for t in tickets)
raw=(ROOT/'net/Вопросы.txt').read_text(encoding='utf-8-sig')
raw=re.sub(r'\[\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}\] Адилет Арманович: ?', '', raw)
parts=raw.split('Практические задания по настройке и администрированию сети')
def questions(s):
    found=re.findall(r'(?m)^(\d+)\.\s*([^\n]+)',s)
    return [q.strip() for n,q in found]
netq,netp=map(questions,parts)
assert len(netq)==60 and len(netp)==40,(len(netq),len(netp))
def chunks_write(folder,entries,size,title):
    folder.mkdir(parents=True,exist_ok=True)
    for start in range(0,len(entries),size):
        end=min(start+size,len(entries))
        (folder/f'{start+1}-{end}.md').write_text(f'# {title} {start+1}–{end}\n\n'+'\n\n---\n\n'.join(entries[start:end])+'\n',encoding='utf-8')
def load_blocks(name):
    return (ROOT/'.work'/name).read_text(encoding='utf-8').strip().split('\n@@@\n')
if __name__=='__main__':
    na=load_blocks('net_theory.txt'); pa=load_blocks('proekt_theory.txt'); pp=load_blocks('proekt_practice.txt'); np=load_blocks('net_practice_beginner.txt' if (ROOT/'.work/net_practice_beginner.txt').exists() else 'net_practice.txt')
    assert (len(na),len(pa),len(pp),len(np))==(60,60,30,40),(len(na),len(pa),len(pp),len(np))
    chunks_write(ROOT/'net/Теория',[f'## Вопрос {i+1}\n\n{q}\n\n### Ответ\n\n{a}' for i,(q,a) in enumerate(zip(netq,na))],8,'Сетевое администрирование · вопросы')
    chunks_write(ROOT/'net/Практика',[f'## Задание {i+1}\n\n{q}\n\n### Решение\n\n{a}' for i,(q,a) in enumerate(zip(netp,np))],4,'Сетевое администрирование · практика')
    entries=[]
    for i,t in enumerate(tickets):
        entries.append(f'## Билет {i+1}\n\n### 1. {t[0]}\n\n{pa[2*i]}\n\n### 2. {t[1]}\n\n{pa[2*i+1]}\n\n### Практическое задание\n\n{t[2]}\n\n### Решение\n\n{pp[i]}\n\n![Диаграмма к билету {i+1}](схемы/{i+1:02d}.png)\n\n[Исходник диаграммы](схемы/{i+1:02d}.puml)')
    chunks_write(ROOT/'proekt',entries,4,'Проектирование ПО · билеты')
    print('Создано: 8 файлов билетов, 8 файлов теории сетей, 10 файлов практики сетей.')
