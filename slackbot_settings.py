# coding: utf-8

import os

#slackbotのAPIトークンを入力
API_TOKEN = os.getenv("SLACK_BOT_TOKEN")#"xoxb-198313998002-378884809812-4nATocYuiR6TObYZXWOx6Gqz"

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "こらドテン！しっかり稼ぐのじゃ！"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
