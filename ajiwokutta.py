import random
import time

def nier_fishing():
  '''
  釣りを開始するかを選択

  釣りを開始した場合はrandom.fishingを実行
  
  '''
  answer = input('釣りを開始しますか？y/n')
  if answer == 'y':
    print('了解。釣りを開始。')
    random_fishing()
  elif answer == 'n':
    print('了解。通信終了。')

def random_fishing():
  '''
  メイン処理

  ランダムな時間待機後、リストから釣果物を取得する。
  アジを取得した場合のみ食べるか否かの選択を表示する。

  '''
  while True:
    sec = random.uniform(0.5, 2)
    time.sleep(sec)
    drop = ['フグ', 'アジ', 'カジキ', 'カブトガニ', 'ヒトデ', 'タイ']
    item = random.choice(drop)
    print(item + 'を取得しました')
    if item == 'アジ':
      time.sleep(1.0)
      eat = input('アジを食べるy/n')
      if eat == 'y':
        ajiwokutta()
    answer = input('釣りを続けるy/n')
    if answer != 'y':
      print('了解。釣りを終了。')
      break

def ajiwokutta():
  '''
  Kエンド

  アジを食べる選択をした時の特殊演出。
  ゲーム内演出に従いコードの実行を停止する。
  警告：このコードを実行した場合、ヨルハ機体9Sの生命維持活動に重大な支障を及ぼす可能性。

  '''
  time.sleep(0.5)
  print('興味を抑えきれずアジを食べてしまった。')
  print('直ちに体液の凝固が始まり、全身の筋肉が硬直し始めたのが分かる')
  time.sleep(0.5)
  print('…確かに旨い 人類が食用にしていたのも頷ける')
  print('薄れゆく意識の中アンドロイドはそんなことを思っていた')
  time.sleep(1.0)
  print('aji wo [k]utta')
  exit()

nier_fishing()