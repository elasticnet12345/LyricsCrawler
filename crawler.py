import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import os

#
#   実行例
#   $ python crawler.py http://j-lyric.net/artist/a0018f8/l00c342.html .
#
#
#
#
#


if __name__ == "__main__":
    
    # 引数設定
    usage = "$ python url"# usage = "$ python url path"
    argparser = ArgumentParser(usage = usage)
    argparser.add_argument("url", type=str, default=None, help="copy adn pase url")
    argparser.add_argument("dir_path", type=str, help="distination directory path, default current directory")
    args = argparser.parse_args()

    # URLの指定
    URL = args.url
    
    # 出力先の指定
    dist_dir_path =  args.dir_path

    # JLyricsのサイトかチェック
    flag_JLyrics, flag_KashiMap, flag_KashiTime = False, False, False
    if "j-lyric.net" in URL:
        flag_JLyrics = True
    else:
        pass

    # リクエスト
    resp = requests.get(URL)

    # オブジェクトに分解
    html = resp.content
    try:
        soup = BeautifulSoup(html, "lxml")
    except:
        soup = BeautifulSoup(html, "html5lib")

    # h1タグからタイトルの取得
    contetns_h1_tag = soup.find_all("h1")
    for i, content in enumerate(contetns_h1_tag):
        tmp = content.text
        title = tmp.replace(" ", "_")    

    # pタグの取得
    contents_p_tag = soup.find_all("p")
    for i, content in enumerate(contents_p_tag):
        if content.get("id") == "Lyric":
            print(content.text)
            lyric = content.text
            break

    # 保存
    file_path = os.path.join(dist_dir_path, title + ".txt")
    with open(file_path, mode="w") as f:
        f.write(lyric)
    



    
