import re
import pickle

be_regex = '([0-9]+\s*(:|\.)\s*[0-9]+\.*)|([0-9]+\s*\.)|([0-9]+)'
re_regex = '([0-9]+\s*:\s*[0-9]+\.*)'

def extract_verses_from_BE(filename):
    chapters = pickle.load(open("chapters.pk","rb"))
    pattern = re.compile(be_regex)
    bible = dict()
    ch, v1, v2 = -1, 0, 0
    lines = open(filename, "r").readlines()
    for i in range(len(lines)):
        line = lines[i]
        if line.strip() == "":
            continue
        match = re.search(pattern, line)
        if not match:
            bible[chapters[ch]][v1][v2] += " " + line
            continue
        info = match.group(0).replace(' ','').strip('.').replace('.',':')
        if info == "1:1":
            ch += 1
            bible[chapters[ch]] = dict()
        if ":" in info:
            nv1, nv2 = info.split(':')
            v1 = int(nv1)
            v2 = int(nv2)
        elif any(i.isdigit() for i in info):
            v2 = int(info)
            if v2 == 1:
                v1 += 1

        if v1 not in bible[chapters[ch]]:
            bible[chapters[ch]][v1] = dict()
        
        bible[chapters[ch]][v1][v2] = line.replace(match.group(0),"").strip()
    
    return bible
        

def extract_verses_from_RE(filename):
    input_file = open(filename, "r").read().replace("\n", " ")
    pattern = re.compile(re_regex)

    chapters = pickle.load(open("chapters.pk","rb"))
    bible = dict()
    ch, v1, v2 = -1, 0, 0
    lp = 0

    for match in pattern.finditer(input_file):
        info = match.group(0).replace('.','').replace(' ','')

        lch, lv1, lv2 = ch, v1, v2

        if info == "1:1":
            ch += 1
            bible[chapters[ch]] = dict()

        nv1, nv2 = info.split(':')
        v1 = int(nv1)
        v2 = int(nv2)

        if v1 not in bible[chapters[ch]]:
            bible[chapters[ch]][v1] = dict()
        
        if lch!=-1:
            bible[chapters[lch]][lv1][lv2] = input_file[lp:match.start()].strip()
        
        lp = match.end()

    return bible

def extract_verses_from_file(filename):
    input_file = open(filename, "r").read().replace("\n", " ")
    pattern = re.compile(re_regex)

    chapters = pickle.load(open("chapters.pk","rb"))
    current_chapter_id = -1

    sentences = dict()
    sentences[chapters[current_chapter_id]] = dict()
    ch, v, lp = 0, 0, 0
    new_ch, new_v = 0, 0

    for match in pattern.finditer(input_file):
        if match.group().strip() == "1:1":
            current_chapter_id += 1
            sentences[chapters[current_chapter_id]] = dict()
            ch, v = 0, 0
        
        if ":" in match.group():
            new_ch, new_v = match.group().split(":")
            new_ch = int(new_ch.strip(".").strip())
            new_v = int(new_v.strip(".").strip())
        else:
            new_v = int(match.group().strip(".").strip())
            new_ch = ch

        if ch not in sentences[chapters[current_chapter_id]]:
            sentences[chapters[current_chapter_id]][ch] = dict()

        if new_ch == ch and new_v == v + 1:
            sentences[chapters[current_chapter_id]][ch][v] = input_file[lp:match.start()].strip()
            v = new_v
            lp = match.end()
        elif new_ch == ch + 1 and new_v == 1:
            sentences[chapters[current_chapter_id]][ch][v] = input_file[lp:match.start()].strip()
            v = new_v
            lp = match.end()
            ch = new_ch

    return sentences

def extract_verses_from_chapter(filename):
    input_file = open(filename, "r").read().replace("\n", " ")
    pattern = re.compile(regex)

    sentences = {}
    ch, v, lp = 0, 0, 0

    for match in pattern.finditer(input_file):
        if ":" in match.group():
            new_ch, new_v = match.group().split(":")
            new_ch = int(new_ch.strip(".").strip())
            new_v = int(new_v.strip(".").strip())
        else:
            new_v = int(match.group().strip(".").strip())
            new_ch = ch

        if ch not in sentences:
            sentences[ch] = dict()

        if new_ch == ch and new_v == v + 1:
            sentences[ch][v] = input_file[lp:match.start()].strip()
            v = new_v
            lp = match.end()
        elif new_ch == ch + 1 and new_v == 1:
            sentences[ch][v] = input_file[lp:match.start()].strip()
            v = new_v
            lp = match.end()
            ch = new_ch

    del(sentences[0])
    return sentences