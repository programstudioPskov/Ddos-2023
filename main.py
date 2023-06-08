import requests
import time
from colorama import init, Fore
from colorama import Back

print (requests.__version__)
def main():
    link = input('ссылка на сайт :')
    num = int(input('число запросов :'))
    requests_setings(url=link,num_requests=num)

def TrueSendGetRequests(url,num_requests):
    init(autoreset=True)
    true = 0
    false = 0
    for num_requests in range(num_requests):
        response = requests.get(url)
        to = response.status_code
        if to == 200:
            true += 1
            print(Fore.BLUE + 'запрос принят')
        else:
            false += 1
            print(Fore.RED + 'запрос откланён')
    print('\n\n')
    print(Back.WHITE + Fore.BLACK + f"успешных запросов - {true}\nошибочных запросов - {false}")
    a = input('\nнажмите ENTER для выхода или введите рандомный символ а затем ENTER:')
    if a == '' :
        exit()
    else:
        main()

def FalseSendGetRequests():
    main()

def requests_setings(url, num_requests):
    try:
        TrueSendGetRequests(url,num_requests)
    except Exception as err:
        init(autoreset=True)
        print(Fore.RED + f'ERROR link settings,more :\n{err}')
        FalseSendGetRequests()

if __name__ == '__main__' :
    print('run\n\n')
    time.sleep(2)
    hallo = """
    ██████╗░██████╗░░█████╗░░██████╗░░░░░░██████╗░░█████╗░██████╗░██████╗░
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░╚════██╗██╔══██╗╚════██╗╚════██╗
    ██║░░██║██║░░██║██║░░██║╚█████╗░█████╗░░███╔═╝██║░░██║░░███╔═╝░█████╔╝
    ██║░░██║██║░░██║██║░░██║░╚═══██╗╚════╝██╔══╝░░██║░░██║██╔══╝░░░╚═══██╗
    ██████╔╝██████╔╝╚█████╔╝██████╔╝░░░░░░███████╗╚█████╔╝███████╗██████╔╝
    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░░░░╚══════╝░╚════╝░╚══════╝╚═════╝░
    """
    print(hallo)
    main()
