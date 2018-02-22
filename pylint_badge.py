from __future__ import absolute_import

import os
import re
import logging


LOG_LEVEL = logging.INFO
OUTPUT_FOLDER = '/tmp/pylint-server'
VALID_REPOS = []
BADGE_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="85" height="20">
  <linearGradient id="a" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <!-- whole rectangle -->
  <rect rx="3" width="85" height="20" fill="#555"/>

  <!-- rating part -->
  <rect rx="3" x="50" width="35" height="20" fill="#{1}"/>
  <path fill="#{1}" d="M50 0h4v20h-4z"/>

  <!-- whole rectangle -->
  <rect rx="3" width="85" height="20" fill="url(#a)"/>

  <g fill="#fff" text-anchor="middle"
                 font-family="DejaVu Sans,Verdana,Geneva,sans-serif"
                 font-size="11">
    <text x="25" y="15" fill="#010101" fill-opacity=".3">pylint</text>
    <text x="25" y="14">pylint</text>
    <text x="67" y="15" fill="#010101" fill-opacity=".3">{0:.2f}</text>
    <text x="67" y="14">{0:.2f}</text>
  </g>
</svg>
"""


def generate_from_report():
    report = open("pylint.html").read()
    match = re.search("Your code has been rated at (.+?)/10", report)
    generate_from_rate(match)


def generate_from_rate(rate):
    match = re.search("Your code has been rated at (.+?)/10", "Your code has been rated at {}/10".format(rate))
    (rating, colour) = get_colour(match)
    output_badge = os.path.join(os.path.dirname(__file__), 'rating.svg')
    save_file(output_badge, BADGE_TEMPLATE.format(rating, colour))


def get_colour(match):
    colour = '9d9d9d'
    rating = 0
    if match:
        rating = float(match.group(1))
        if rating >= 9 and rating <= 10:
            colour = '44cc11'
        elif rating < 9 and rating >= 7:
            colour = 'f89406'
        elif rating >= 0 and rating < 7:
            colour = 'b94947'
        else:
            colour = '9d9d9d'
    return (rating, colour)


def save_file(filename, contents):
    """Save a file anywhere"""
    ensure_path(os.path.dirname(filename))
    print(filename)
    with open(filename, 'w') as thefile:
        thefile.write(contents)


def ensure_path(path):
    """Make sure the path exists, creating it if need be"""
    if not os.path.exists(path):
        os.makedirs(path)
