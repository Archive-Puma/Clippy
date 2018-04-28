import time
import keyboard
import pyperclip as clipboard

stack = []

def copy():
    time.sleep(1)
    texto = clipboard.paste()
    if texto is not '':
        stack.append(texto)
    # print(stack)

def paste():
    try:
        clipboard.copy(stack.pop())
        # print(stack)
    except IndexError:
        pass

def main():
    keyboard.add_hotkey('ctrl+c', copy)
    keyboard.add_hotkey('ctrl+v', paste)
    keyboard.wait()

if __name__ == '__main__':
    main()
