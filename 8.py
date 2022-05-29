import colorama
a = int(input())
f = open("8.txt")
try:
    f.write("Some text")
    print(10/a)
    print("sucssesful")
except ZeroDivisionError:
    print(colorama.Fore.RED + 'It is not possible to divide by 0')
except TypeError:
    print(colorama.Fore.RED + 'It is not possible to divide by "str"')
except NameError:
    print(colorama.Fore.YELLOW + 'You are accessing an object that does not exist')
except:
    print(colorama.Fore.RED + 'Some Error')

else:
    print(colorama.Fore.GREEN + 'Nothing went wrong')
finally:
    f.close()
    print(colorama.Fore.GREEN + 'The "try except" is finished')
input()