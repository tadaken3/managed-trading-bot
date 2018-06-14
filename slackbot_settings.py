# coding: utf-8

import os

#slackbotのAPIトークンを入力
API_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "こらドテン！しっかり稼ぐのじゃ！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
