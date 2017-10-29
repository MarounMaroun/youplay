import re
import urllib
import argparse
import webbrowser


BASE_URL = "https://youtube.com/"


def main():
    args = get_args()
    title = build_title(args['play'])
    links = get_links(title)

    webbrowser.open(BASE_URL + links[0], autoraise=False)


def get_args():
    parser = argparse.ArgumentParser(description='Play YouTube videos from your shell')
    parser.add_argument('-p', '--play', help='Video title to play', required=True)
    return vars(parser.parse_args())


def build_title(play):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '+', play)


def get_links(title):
    url = BASE_URL + 'results?search_query={}'.format(title)
    html = urllib.urlopen(url)
    links = re.findall('data-context-item-id="([^"]*)"', html.read())
    return map(lambda s: 'watch?v=' + s, links)


if __name__ == '__main__':
    main()
