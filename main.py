import click
import random

try:
    @click.command()
    @click.option('-l', '--length', prompt="Enter the length of your password")
    def generate(length):
        characters = list(" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
        mylist = []
        for i in range(int(length)):
            mylist.append(random.choice(characters))
        password = ''.join(mylist)
        print(password)
    if __name__ == '__main__':
        generate()
except ValueError:
    print('\033[31m You must enter a integer number.')
except KeyboardInterrupt:
    print('\033[31m Script stopped\n')
    
