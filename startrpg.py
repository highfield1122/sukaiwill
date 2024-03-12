"""
ゲーム名を始める
プレイヤー名を決定する
"""
import PySimpleGUI as sg
def main():
    msg='名前を教えてください：'
    name=input(msg)
    msg='ようこそ'+name
    sg.popup(msg)
    print('出発しましょう、'+name)

if __name__=='__main__':
    main()
