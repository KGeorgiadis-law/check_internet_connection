import socket
from time import sleep, time, gmtime, strftime

# taken from: https://stackoverflow.com/a/33117579

def time_now():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def internet(host="8.8.8.8", port=53, timeout=3):
    global outage_time
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))        
        if outage_time != 0:
            with open("log.txt", "a") as log_file:
                log_file.write("Internet has returned... The time now is {} and the internet was out for {} seconds\n""".format(time_now(), round(time() - outage_time), 5))
                print("{}: Internet back on!".format(time_now()))
                outage_time = 0
                return True
        else:
            return True
    except Exception as ex:
        print(ex)
        if outage_time == 0:
            with open("log.txt", "a") as log_file:
                log_file.write("Internet is gone! {}\n".format(time_now()))
                outage_time = time()
        #print(ex.message)
        return False


outage_time = 0
print("Starting...")
while True:
    internet_boolean = internet()
    #print(internet_boolean)
    if internet_boolean != False:
        #print("Internet is okay at {}. Checking again in 5...".format(time_now()))
        sleep(5)
    else:
        print("{}: Internet is off! Checking again...".format(time_now()))
        sleep(1)
