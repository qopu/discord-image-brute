import dispicbrute
import argparse
import os.path

parser = argparse.ArgumentParser(description="Discord image brute")

parser.add_argument("url", nargs='*', type=str,
                    help="debug mode (optional)")
parser.add_argument("--d", nargs='*', metavar="num", type=int,
                    help="All the numbers separated by spaces will be added.")

args = parser.parse_args()

url = args.url[0]

first_link_part = os.path.split(os.path.split(url)[0])[0] + "/"
id_link_part = os.path.split(os.path.split(url)[0])[1]
third_link_part = "/" + os.path.split(os.path.split(url)[1])[1]

if args.d is None:
    dispicbrute.run_normal(first_link_part, id_link_part, third_link_part)
else:
    dispicbrute.run_debug(first_link_part, id_link_part, third_link_part)