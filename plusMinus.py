import os
from argparse import ArgumentParser
g_cs='abcdefghijklmnopqrstuvwxyz'
g_map={'a':0, 'b':1}
def curbFile(vcodes, vfun):
    dst = []
    for k in range(10, len(vcodes)):
        code  = vcodes[k]
        dcode = ''
        for i in range(len(code)):
            c = code[i]
            ot = (k+i*103)%10
            if c<='9' and c>='0':
                if (vfun=='de') : ot = 10 - ot
                n = (int(c) + ot)%10
                dcode+=str(n)
            elif c<='z' and c>='a':
                if (vfun == 'de'): ot = 26 - ot
                index = g_map[c]
                index  = (index+ot)%26
                dcode+= g_cs[index]
            else: dcode +=c
        dst.append(dcode)
    return  dst

def main():
    for root, dirs, fs in os.walk(args.path):
        if len(fs)==0: continue
        for af in fs:
            if af.endswith('.h') or af.endswith('.cpp') or af.endswith('.cu'):
                af = os.path.join(root, af)
                Fin = open(af, 'r')
                try:
                    lines = Fin.readlines()
                    Fin.close()
                except Exception as e:
                    print('Fail to curb the af '+af)
                else:
                    lines=  curbFile(lines, args.curb)
                    Fout = open(af, 'w')
                    Fout.writelines(lines)
                    Fout.close()

if __name__ == '__main__':
    parser = ArgumentParser(description="curb text.")
    parser.add_argument('--path', default="src/")
    args = parser.parse_args()
    args.curb = args.path[-2:]
    args.path = args.path[:-2]
    for i in range(26):
        g_map[g_cs[i]] = i;
    main()
