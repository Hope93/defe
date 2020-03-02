"""
Main CLI
"""

import argparse
import sys

from colorama import Fore, Style, init

from feeders import feeder

from .formatter import defy

contact = """

Available Feed Categories
-------------------------

1. general      [defe general <max_feed_count>]
2. news         [defe news <max_feed_count>]
3. podcasts     [defe podcasts <max_feed_count>]
4. newsletters  [defe newsletters <max_feed_count>]

* By Default defe shows only 7 feed items
* Use [defe feeders] to list available feeders

Contact:
--------

- 📧 varshneybhupesh@gmail.com

More information is available at:

- Home      : https://pypi.org/project/defe/
- Source    : https://github.com/Bhupesh-V/devfeed
- Support   : https://www.patreon.com/bePatron?u=18082750,
"""


def home():
    init(autoreset=True)
    print(
        Fore.RED
        + Style.BRIGHT
        + """
         888           .d888
         888          d88P"
         888          888
     .d88888  .d88b.  888888 .d88b.
    d88" 888 d8P  Y8b 888   d8P  Y8b
    888  888 88888888 888   88888888
    Y88b 888 Y8b.     888   Y8b.
     "Y88888  "Y8888  888    "Y8888

    """
    )
    print(
        Fore.GREEN + Style.BRIGHT + "A Tech feed Aggregator for Developers.", end="\n\n"
    )
    print(Style.BRIGHT + "Welcome to defe 👋", end="\n")
    print("Use" + Style.BRIGHT + " defe --help ", end="")
    print("to see available commands", end="\n\n")


def main():
    init(autoreset=True)
    parser = argparse.ArgumentParser(
        prog="defe",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A Tech feed aggregator for developers",
        epilog=contact,
    )
    parser.add_argument("feed", type=str, help="Feed Category")
    parser.add_argument(
        "max_feed_count",
        nargs="?",
        type=int,
        default=7,
        help="No of feed items to show",
    )

    if len(sys.argv) == 1:
        home()
        sys.exit(1)

    args = parser.parse_args()

    if args.feed == "general":
        for item in feeder.all_feed()[: args.max_feed_count]:
            defy(item["title"], item["link"])
    if args.feed == "news":
        for item in feeder.news_feed()[: args.max_feed_count]:
            defy(item["title"], item["link"], item["feeder_site"])
    if args.feed == "newsletters":
        for item in feeder.newsletters_feeds()[: args.max_feed_count]:
            defy(item["title"], item["link"])
    if args.feed == "podcasts":
        for item in feeder.podcasts_feeds()[: args.max_feed_count]:
            defy(item["title"], item.links[1].href)
    if args.feed == "feeders":
        feeds = ["general", "news", "podcast"]
        print(
            "\n" + Style.BRIGHT + "defe fetches feeds of these popular sites",
            end="\n\n",
        )
        for f in feeds:
            print("\n" + Fore.BLUE + Style.BRIGHT + f.capitalize(), end="\n\n")
            data = feeder.read_data(f)
            for item in data:
                print(Style.BRIGHT + str(data.index(item) + 1), end=". ")
                print(Fore.GREEN + Style.BRIGHT + item["name"])

        print("\n\n" + Style.BRIGHT + "Want to add more ? 🤔")
        print(
            Style.BRIGHT + "Open a PR at https://github.com/Bhupesh-V/devfeed",
            end="\n\n",
        )


if __name__ == "__main__":
    main()