import platform
import psutil
import time
import random

def print_logo():
    logotype = random.randint(0,4)
    if logotype == 0:
        logo = r'''
              $$\  $$$$$$\   $$$$$$\  
              \__|$$  __$$\ $$  __$$\ 
              $$\ $$ /  $$ |$$$$$$$$ |
              $$ |$$ |  $$ |$$   ____|
              $$ |\$$$$$$  |\$$$$$$$\ 
              $$ | \______/  \_______|
        $$\   $$ |                    
        \$$$$$$  |                    
         \______/                     
        '''
    elif logotype == 1:
        logo = r'''
            ___          ___           ___     
           /  /\        /  /\         /  /\    
          /  /:/       /  /::\       /  /:/_   
         /__/::\      /  /:/\:\     /  /:/ /\  
         \__\/\:\    /  /:/  \:\   /  /:/ /:/_ 
            \  \:\  /__/:/ \__\:\ /__/:/ /:/ /
             \__\:\ \  \:\ /  /:/ \  \:\/:/ /:/
             /  /:/  \  \:\  /:/   \  \::/ /:/ 
            /__/:/    \  \:\/:/     \  \:\/:/  
            \__\/      \  \::/       \  \::/   
                        \__\/         \__\/    
        '''
    elif logotype == 2:
        logo = r'''
   _            
  (_) ___   ___ 
  | |/ _ \ / _ /
  | | (_) |  __/
 _/ |\___/ \___|
|__/            

'''
    elif logotype == 3: 
        logo = r'''
            
 o          
    __   _  
 | /  \_|/  
 |/\__/ |__/
/|          
\|          
'''
    elif logotype == 4:
        logo = r'''
________            
______(_)__________ 
_____  /_  __ \  _ /
____  / / /_/ /  __/
___  /  \____/\___/ 
/___/               
'''
    print(logo)

def get_os():
    return platform.system()

def get_kernel():
    return platform.release()

def get_uptime():
    try:
        uptime_seconds = int(time.time() - psutil.boot_time())
        days, seconds = divmod(uptime_seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return f"{days}d {hours}h {minutes}m {seconds}s"
    except Exception as e:
        return str(e)

def get_memory():
    mem = psutil.virtual_memory()
    used = mem.total - mem.available
    return f"{used // (1024 * 1024)} MB used / {mem.total // (1024 * 1024)} MB total"

def get_cpus():
    return psutil.cpu_count()

def get_cpu_usage():
    return f"{psutil.cpu_percent(interval=1):.2f}%"

def get_hostname():
    return platform.node()

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return f"{disk.percent}% used ({disk.used // (1024 * 1024)} MB used / {disk.total // (1024 * 1024)} MB total)"

def print_info(label, value):
    print(f"joe{label}: {value}")

def main():
    print_logo()
    print_info("Hostname", get_hostname())
    print_info("OS", get_os())
    print_info("Kernel", get_kernel())
    print_info("Uptime", get_uptime())
    print_info("Memory", get_memory())
    print_info("CPUs", get_cpus())
    print_info("CPU Usage", get_cpu_usage())
    print_info("Disk Usage", get_disk_usage())

if __name__ == "__main__":
    main()
