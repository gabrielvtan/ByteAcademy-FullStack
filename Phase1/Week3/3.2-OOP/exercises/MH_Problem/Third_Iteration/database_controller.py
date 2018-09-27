from read_database import Database
from pprint import pprint

monty_hall_database = 'monty_hall.db'

with Database(monty_hall_database) as db:
    true_count = db.monty_hall_results_true('monty_hall')
    false_count = db.monty_hall_results_false('monty_hall')
    true_count_int = ((true_count[0][0]))
    false_count_int = ((false_count[0][0]))
    total = true_count_int + false_count_int
    wins = true_count_int / total * 100.00
    loses = false_count_int / total * 100.00
    print('Win Percentage: {:.2f}%'.format(wins))
    print('Loss Percentage: {:.2f}%'.format(loses))