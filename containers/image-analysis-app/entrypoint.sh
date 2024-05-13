#!/bin/bash
cd /workspace

# 依存ライブラリをインストールする
pip install -r requirements.lock

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
