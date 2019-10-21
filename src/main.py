# main.py

while True:
    print("数値を入力してください")
    input_num = int(input()) # 入力コマンド

    if input_num == 0:
        print('プログラムを終了します')
        break
    elif input_num > 0 and input_num <= 10:
        print("Hello World")
        break
    elif input_num > 10:
        print("king matsuzaka")
        break
    # -- ここに処理を追加してみよう --
    else:
        print('該当するコマンドがありません')
