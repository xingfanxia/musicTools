import wget, sys, os
import requests, re

outPath ="midishowDownloads/"

def parse_url(url):
    out = url.replace("/midi", "/midi/file")
    out = out.replace("html", "mid")
    return out

def main():
    url = parse_url(sys.argv[1])
    r = requests.get(url)
    print(r.headers)
    con_disp = r.headers.get('Content-Disposition').encode('utf-8').decode('gbk')
    print(con_disp)
    fname = re.findall("filename\*=(.+)", con_disp)
    print(fname)
    if not os.path.exists(outPath):
        os.mkdir(outPath)
    wget.download(url, outPath+con_disp)

if __name__ == '__main__':
    main()
