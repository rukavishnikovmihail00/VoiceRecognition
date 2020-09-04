
if __name__ == '__main__':
    a = input()
    words = a.split()
    print(words[0])

    root = Tk()
    root.title("Voice Assistant 1.0")
    root.geometry("300x250")
    btn = Button(root, text='Слушать', command=start)
    btn.configure(bd=1, font=('Castellar', 25), bg='green')
    btn.place(x=50, y=60, height=50, width=150)
