def main():
    msg='名前を教えてください：'
    name=input(msg)
    msg='ようこそ'+name
    print(msg,flush=True)
    print(msg)
    print('出発しましょう'+name)

if __name__=='__main__':
    main()
