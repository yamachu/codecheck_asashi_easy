import sys
from app.main import main

# http://blog.livedoor.jp/dankogai/archives/51816624.html
# sys.stdin =  open('/dev/stdin',  'r', encoding='UTF-8')
# sys.stdout = open('/dev/stdout', 'w', encoding='UTF-8')
# sys.stderr = open('/dev/stderr', 'w', encoding='UTF-8')
# OSError: [Errno 6] No such device or address: '/dev/stdin'
# えっ，Windowsだったりするのこの実行環境

main(sys.argv[1:])
