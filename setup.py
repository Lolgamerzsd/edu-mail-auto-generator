import subprocess
import sys

try:
    from __dwnldDrivers.versions import get_firefox_version, get_chrome_version, setup_Firefox, setup_Chrome
except ImportError:
    print("Error: Required module '__dwnldDrivers.versions' not found.")
    sys.exit(1)

######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########

def install(name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])
    except subprocess.CalledProcessError as e:
        print(f"Error installing package {name}: {e}")
        sys.exit(1)

def main():
    my_packages = ['requests', 'clint', 'faker', 'selenium', 'colorama']
    installed_browsers = []

    for package in my_packages:
        install(package)
        print('\n')

    print('Firefox')
    firefox_ver = get_firefox_version()
    if firefox_ver:
        installed_browsers.append('Firefox')
        setup_Firefox(firefox_ver)
    else:
        print("Firefox isn't installed")

    print('\nChrome')
    chrome_ver = get_chrome_version()
    if chrome_ver:
        installed_browsers.append('Chrome')
        setup_Chrome(chrome_ver)
    else:
        print("Chrome isn't installed")

    if not installed_browsers:
        print('Error - Setup installation failed \nReason - Please install either Chrome or Firefox browser to complete setup process')
        sys.exit(1)

    print('\nWhich browser do you prefer to run the script on?')

    for index, browser in enumerate(installed_browsers, start=1):
        print(f"\n[*] {index} {browser}")

    while True:
        try:
            user_input = int(input('\nEnter id ex - 1 or 2: '))
            if 1 <= user_input <= len(installed_browsers):
                selected = installed_browsers[user_input - 1]
                with open('prefBrowser.txt', 'w') as fp:
                    fp.write(selected.lower())
                break
            else:
                print('Wrong id, either input 1 or 2')
        except ValueError:
            print('Invalid input, please enter a number')

    print('Setup Completed')

if __name__ == '__main__':
    main()
