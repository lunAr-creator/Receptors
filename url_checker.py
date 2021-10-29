# import datetime
# import requests
# import time
# import typer
#
# app = typer.Typer()
#
# from rich.console import Console
# from rich import print as rprint
#
# @app.command()
# # @click.argument('url')
# # @click.option('--timeout', type=int)
# # @click.option('--span', type=int)
# # @click.option('--interval', type=int)
# # @click.option('--threshold', type=int)
# def main(url: str, timeout: int, span: int, interval: int, threshold: int):
#     print()
#     times = []
#
#     while span > 0:
#         span -= 1
#         time.sleep(interval)
#         response = requests.post(url, timeout=timeout)
#         response_time = round((response.elapsed.total_seconds()*1000), 3)
#         times.append(response_time)
#
#         console = Console()
#         pass_ = "[PASS]"
#         pass_o = "[OVERALL PASS]"
#         fail_ = "[FAIL]"
#         fail_o = "[OVERALL FAIL]"
#
#         if response_time >= threshold:
#             line1 = f"~ Response time: [red]{response_time}[/red]ms"
#             line2 = fail_.rjust(118-(len(line1[3:])))
#             rprint(f"{line1} {line2}")
#
#         else:
#             line1 = f"~ Response time: [green]{response_time}[/green]ms"
#             line2 = pass_.rjust(122-(len(line1[3:])))
#             rprint(f"{line1} {line2}")
#
#         if span == 0:
#             print(f"\nCompleted {args.span} checks in {args.span*args.interval} seconds")
#             av_resp_time = round((sum(times) / len(times)), 3)
#
#             if av_resp_time > threshold:
#                 line1 = f"Average response time: [red]{av_resp_time}[/red]ms"
#                 line2 = line2 = fail_o.rjust(118-(len(line1[3:])))
#                 rprint(f"{line1} {line2}")
#                 break
#
#             else:
#                 line1 = f"Average response time: [green]{av_resp_time}[/green]ms"
#                 line2 = line2 = pass_o.rjust(122-(len(line1[3:])))
#                 rprint(f"{line1} {line2}")
#                 break
#
# if __name__ == '__main__':
#     app()

# player_amount = int(input("How many people are there playing? "))
# players = []
# #player count
#
# if player_amount == 1:
#   print("Not enough players.")
# elif player_amount == 2:
#     for i in range(1, 3):
#        player = input(f"Player {i}: Please state your name: ")
#        players.append(player)
# elif player_amount == 3:
#   for i in range(1, 4):
#      player = input(f"Player {i}: Please state your name: ")
#      players.append(player)
#
# elif player_amount == 4:
#     for i in range(1, 5):
#        player = input(f"Player {i}: Please state your name: ")
#        players.append(player)
# else:
#   print("Not a valid player amount")
#
# print(players)

def get_player_names(players: int):
    players_list = []
    for i in range(1, players+1):
        players_list.append(input(f"Player {i}: Please state your name: "))
    print(players_list)

get_player_names(4)
