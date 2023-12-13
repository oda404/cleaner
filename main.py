from bs4 import BeautifulSoup;
from selenium import webdriver;
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import requests;
import argparse
import base64
import os

url = "https://mangaclash.com/manga";
lang = "en";
chapters = [1]

def parse_chapters(s):

    idx = s.find('-');
    if idx == -1:
        return (int(s), int(s))

    first = s[0:idx]
    second = s[idx + 1:]

    return (int(first), int(second))

def main():

    parser = argparse.ArgumentParser();
    parser.add_argument("--chapters", help="chapter numbers", required=True)
    parser.add_argument("--outdir", help="out dir", required=True);
    parser.add_argument("--manga", help="manga name", required=True);
    args = parser.parse_args();

    chapters = parse_chapters(args.chapters);

    driver = webdriver.Chrome();

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir);
    
    #for chapter in range(chapters[0], chapters[1] + 1):
    for chapter in ["1", "2-1", "2-2", "2-3", "2-4", "3-1", "3-2", "4", "5", "6-1", "6-2", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]:

        full_url = f"{url}/{args.manga}/chapter-{chapter}";
        print(full_url);
        driver.get(full_url);

        print("Return when ready");
        input()

        soup = BeautifulSoup(driver.page_source, "html.parser")
        # content = soup.find_all("canvas", { "class": "image-vertical" });
        main_div = soup.find("div", { "class": "reading-content" })

        images = main_div.find_all("img");
        images = [x["data-src"] for x in images];

        print(images);
        # print(len(images));

        i = 0
        for img_url in images:
            print(img_url);
            # headers = {
            #     "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            #     "accept-language": "en-US,en;q=0.9",
            #     "cache-control": "no-cache",
            #     "pragma": "no-cache",
            #     "sec-ch-ua": "\"Brave\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            #     "sec-ch-ua-mobile": "?0",
            #     "sec-ch-ua-platform": "\"Linux\"",
            #     "sec-fetch-dest": "image",
            #     "sec-fetch-mode": "no-cors",
            #     "sec-fetch-site": "cross-site",
            #     "sec-gpc": "1",
            #     "Referer": "https://mangakakalot.com/",
            #     "Referrer-Policy": "strict-origin-when-cross-origin"
            # }

            print(img_url)
            output_image = requests.get(img_url);

            base_dir = f"{args.outdir}/chap{chapter}"
            if not os.path.exists(base_dir):
                os.makedirs(base_dir);

            with open(f"{base_dir}/image{i}.jpg", 'wb') as f:
                f.write(output_image.content)
            
            i += 1


if __name__ == "__main__":
    main();
