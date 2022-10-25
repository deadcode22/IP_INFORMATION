# Welcome in tool information 
#     color 
lblue = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"
cyn = "\033[95m"
bn = "\033[94m"
#     module 
try:
    from requests import *
    from sys import *
    import geocoder
    import os   

except ModuleNotFoundError:
    print(f'\t{red}[{ylw}!{red}] {bn}https://t.me/black_code_22 \n')
    print(f"\t{red}[{ylw}!{red}] Error {ylw}!!!{bn} Check install pip requests Or geocoder  ")
    exit() 
except:
    pass    

banner = f"""
{lblue}  ▀▄  ▄▀
{lblue} ▄▄▄██▄▄▄▄▄      {red}# {grn}IP Location Finder
{lblue} █      █▀█      {red}# {grn}Coded By DeadCode
{lblue} █      █▀█      {red}# {grn}TeleGrame {red}::: {ylw}Black_Code_22
{lblue} █▄▄▄▄▄▄███      {red}# {ylw}Version {red}2.1
"""
    
help = f"""
    {red}Usage {ylw}: {grn}python IPLocation.py [OPTION] ...
    {ylw}To get IP information

    Mandatory arguments to long options are mandatory for short options too
        {red}-h {ylw}, {red}--help         {grn}display this help and exit
        {red}-I {ylw}, {red}--ip           {grn}To get IP information

    {ylw}Use help 

        {grn}python {red}IP_info.py {ylw}--ip{red}/{ylw}-I {red}[{grn}IP ADDRESS{red}]

"""
def Location(IP):
    
    our_ip = geocoder.ip(IP).latlng
    map_lenr = our_ip[0]
    map_lenl = our_ip[1]

    try:
        print(banner)
        result = get(f'http://ip-api.com/json/{IP}').json()
        print(f"""  
    {grn}[{red}+{grn}] {lblue}COUNTRY {red}::: {ylw}{result['country']}
    {grn}[{red}+{grn}] {lblue}COUNTRY CODE {red}::: {ylw}{result['countryCode']}
    {grn}[{red}+{grn}] {lblue}REGION {red}::: {ylw}{result['region']}
    {grn}[{red}+{grn}] {lblue}REGION NAME {red}::: {ylw}{result['regionName']}
    {grn}[{red}+{grn}] {lblue}CITY {red}::: {ylw}{result['city']}
    {grn}[{red}+{grn}] {lblue}ZIP {red}::: {ylw}{result['zip']}
    {grn}[{red}+{grn}] {lblue}LAT {red}::: {ylw}{result['lat']}
    {grn}[{red}+{grn}] {lblue}LON {red}::: {ylw}{result['lon']}
    {grn}[{red}+{grn}] {lblue}TIME ZONE {red}::: {ylw}{result['timezone']}
    {grn}[{red}+{grn}] {lblue}ISP {red}::: {ylw}{result['isp']}
    {grn}[{red}+{grn}] {lblue}ORG {red}::: {ylw}{result['org']}
    {grn}[{red}+{grn}] {lblue}AS {red}::: {ylw}{result['as']}
    {grn}[{red}+{grn}] {lblue}IP {red}::: {ylw}{result['query']}
    {grn}[{red}+{grn}] {lblue}GOOGLE MAP {red}::: {ylw}https://www.google.com/maps/@{map_lenr},{map_lenl},13z
\n""")
        input(f'\n\t{grn}[{red}+{grn}]{cyn}  Enter Excpress Open Mape ......... ')
        os.system(f'xdg-open https://www.google.com/maps/@{map_lenr},{map_lenl},13z')
        
    except:
        print(f" {red}[{ylw}!{red}] Error {ylw}!!! ")

#--------------------------------
if(len(argv) == 1 ):
    print(banner)
    print(help)        
elif(len(argv) > 1):
    if argv[1] == "--ip" or argv[1] == "-I":
        if (len(argv) >= 2) and (len(argv) <= 3):
            try:
                ip = argv[2]
                Location(ip)
            except:
                print(f"    {red}[{ylw}!{red}] {lblue}Enter the correct IP address ")
        else:
            print(f"    {red}[{ylw}!{red}] {lblue}Enter the arguments correctly")
    elif argv[1] == "--help" or argv[1] == "-h":
            if (len(argv) <= 2):
                print(banner)
                print(help)  
            else:
                print(f"    {red}[{ylw}!{red}] {lblue}Enter the arguments correctly")
    else:
        print(f"    {red}[{ylw}!{red}] {lblue}This is not an argument, get help from a guide")
