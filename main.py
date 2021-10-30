# import cmd
#
# class URL_checker(cmd.Cmd):
#     def __init__(self):
#         cmd.Cmd.__init__(self)
#
#     def do_quit(self, args):
#         print('Goodbye :D')
#         return True
#
# if __name__ == "__main__":
#     main = URL_checker()
#     main.cmdloop()

# import itertools, sys
# from time import sleep
# spinner = itertools.cycle(['-', '/', '|', '\\'])
# while True:
#     sys.stdout.write(next(spinner))
#     sleep(0.5)   # write the next character
#     sys.stdout.flush()                # flush stdout buffer (actual character display)
#     sys.stdout.write('\b')

# scan --url https://www.google.com --timeout 6 --span 10 --interval 1 --threshold 54

import datetime
import requests
import argparse
import time

from rich.console import Console
from rich import print as rprint

def response_time(url, timeout, span, interval, threshold):
    print()
    times = []

    try:
        while span > 0:
            span -= 1
            time.sleep(interval)
            response = requests.post(url, timeout=timeout)
            response_time = round((response.elapsed.total_seconds()*1000), 3)
            times.append(response_time)

            console = Console()

            codes= {

            }
            pass_ = "[PASS]"
            pass_o = "[OVERALL PASS]"
            fail_ = "[FAIL]"
            fail_o = "[OVERALL FAIL]"

            if response_time >= threshold:
                line1 = f"~ Response time: [red]{response_time}[/red]ms"
                line2 = fail_.rjust(118-(len(line1[3:])))
                rprint(f"{line1} {line2}")

            else:
                line1 = f"~ Response time: [green]{response_time}[/green]ms"
                line2 = pass_.rjust(122-(len(line1[3:])))
                rprint(f"{line1} {line2}")

            if span == 0:
                print(f"\nCompleted {args.span} checks in {args.span*args.interval} seconds")
                av_resp_time = round((sum(times) / len(times)), 3)

                if av_resp_time > threshold:
                    line1 = f"Average response time: [red]{av_resp_time}[/red]ms"
                    line2 = line2 = fail_o.rjust(118-(len(line1[3:])))
                    rprint(f"{line1} {line2}")
                    break

                else:
                    line1 = f"Average response time: [green]{av_resp_time}[/green]ms"
                    line2 = line2 = pass_o.rjust(122-(len(line1[3:])))
                    rprint(f"{line1} {line2}")
                    break

    except requests.exceptions.HTTPError as err01:
        print ("HTTP error: ", err01)

    except requests.exceptions.ConnectionError as err02:
        print ("Error connecting: ", err02)

    except requests.exceptions.Timeout as err03:
        print ("Timeout error:", err03)

    except requests.exceptions.RequestException as err04:
        print ("Error: ", err04)

parser = argparse.ArgumentParser(prog='PROG', description='description')
parser.add_argument('cmd', choices=['scan','check','help','quit'])
parser.add_argument('--url', type=str, required=True, help="URL to target")
parser.add_argument('--timeout', type=int, required=True, help="Timeout: measured in s")
parser.add_argument('--span', type=int, required=True, help="Number of times to get response time")
parser.add_argument('--interval', type=int, required=True, help="Time between each span")
parser.add_argument('--threshold', type=int, required=True, help="threshold for repsonse time")

while True:
    astr = input('$: ')
    # print astr
    try:
        args = parser.parse_args(astr.split())
    except SystemExit:
        # trap argparse error message
        print('error')
        continue
    if args.cmd in ['scan']:
        print(f'Executing {args.cmd} for URL: {args.url}')
        response_time(args.url, args.timeout, args.span, args.interval, args.threshold)
    elif args.cmd == 'help':
        parser.print_help()
    else:
        print('Goodbye :D!')
        break
