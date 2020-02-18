[Web Lookup] SDK.
Introduction
[Weblookup] is the sdk that provides an interface to lookup a given webaddress.

Supported Features
[Get website details]
[Web site check]
[Error hanndling]
[Output format.]

Installation

git clone git@github.com:websitecheck

Usage

source /home/.virtualenvs/vtest/bin/activate

python websitecheck.py -web <WEB_ADDRESS>

or 

./websitecheck.py -web <WEB_ADDRESS>

Example

./websitecheck.py -web "https://www.google.com/"

Output will be:

Website is reachable or Website is not reachable.
