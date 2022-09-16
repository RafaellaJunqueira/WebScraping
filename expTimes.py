from SeleniumSelenium import SeleniumSelenium as exp1selenium
from SeleniumBs4 import SeleniumBs4 as exp2bs4
from Requests import Requests as exp3requests
import time

executions = 100

# Experimento 1 - Selenium
exec_times = []
for execution in range(0, executions):
    start = time.time()

    exp_1 = exp1selenium
    args = {"name": "Vitor Borges"}
    exp_1.search_name(**args)
    
    end = time.time()
    exec_times.append(end - start)
media = sum(exec_times) / executions
print(f'EXP 1\nMedia de tempo: {media}\nNumero de execucoes: {executions}')


# Experimento 2 - Selenium + Bs4
exec_times = []
for execution in range(0, executions):
    start = time.time()

    exp_2 = exp2bs4
    args = {"name": "Vitor Borges"}
    exp_2.search_name(**args)

    end = time.time()
    exec_times.append(end - start)
media = sum(exec_times) / executions
print(f'EXP2\nMedia de tempo: {media}\nNumero de execucoes: {executions}')


# Experimento 3 - Requests
exec_times = []
for execution in range(0, executions):
    start = time.time()

    exp3 = exp3requests.My_Requests()
    in_args = {"name": "Vitor Borges"}
    exp3.search_name(**in_args)
    
    end = time.time()
    exec_times.append(end - start)
media = sum(exec_times) / executions
print(f'EXP3\nMedia de tempo: {media}\nNumero de execucoes: {executions}')
