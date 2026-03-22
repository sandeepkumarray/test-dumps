from facebook_scraper import get_posts
import requests, os
import argparse

def fb_scrapper(profile):
    save_folder = "downloads"
    os.makedirs(save_folder, exist_ok=True)

    for post in get_posts(profile, pages=100, extra_info=True):
        print("got posts")
        if "images" in post and post["images"]:            
            print("got images")
            for img in post["images"]:
                filename = img.split("/")[-1].split("?")[0]
                path = os.path.join(save_folder, filename)
                with open(path, "wb") as f:
                    f.write(requests.get(img).content)

    print(f"✅ downloaded successfully under: {save_folder}")

def main():
    parser = argparse.ArgumentParser(description="Get posts from facebook page.")
    parser.add_argument("profile", help="facebook profile name")
    args = parser.parse_args()

    fb_scrapper(args.profile)

if __name__ == "__main__":
    main()
