import os

start_ip = input('Enter the first IP address : ')
end_ip = input('Enter last IP address :  ')

start_ip_split = start_ip.split(".")
end_ip_split = end_ip.split(".")

for i in range(int(start_ip_split[3]), int(end_ip_split[3]) + 1):
    current_ip = start_ip_split[0] + "." + \
        start_ip_split[1] + start_ip_split[2] + "." + str(i)
    response = os.system("ping -c 1 " + current_ip)

    if response == 0:
        print(current_ip, "OK")

    else:
        print(current_ip, "NO")
