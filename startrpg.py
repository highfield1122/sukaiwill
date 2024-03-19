"""
ゲーム名を始める
プレイヤー名を決定する
"""
import PySimpleGUI as sg
import typewriter
def main():
    typewriter.main()
    msg='名前を教えてください：'
    name=sg.popup_get_text(msg,'名前を入力')
    msg='ようこそ'+name
    sg.popup(msg)
    sg.popup('出発しましょう、'+name)
    msg='しゅっぱつ'
    typewriter.print_type_writer(msg)

if __name__=='__main__':
    main()
