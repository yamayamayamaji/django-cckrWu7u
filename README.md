> **レビュアーの方へ**: 開発者からのメモを[こちらのドキュメント](docs/DEVELOPER_NOTE.md)に記載しています。  
  
  
---
# Image Analysis Development Environment

このリポジトリは、Image Analysis Projectの開発環境を提供します。開発環境は、アプリケーションとライブラリを含むDjangoプロジェクトと、それらを実行するためのDockerコンテナで構成されています。

## 技術スタック

- Django
- Docker
- MySQL
- Python
- pytest

## 環境構築

### 前提条件

- Docker
- Docker Compose

### 手順

1. このリポジトリをクローンします。

```bash
git clone https://github.com/yamayamayamaji/kadai-cckrWu6u.git
```

2. 開発環境のルートディレクトリに移動します。

```bash
cd kadai-cckrWu6u
```

3. Docker Composeを使用して、アプリケーションとデータベースのコンテナを起動します。

```bash
docker-compose up -d
```

4. アプリケーションが起動したら、ブラウザで `http://localhost:8000/admin` にアクセスし、表示されればOKです。

## 開発環境の構成

- `containers`: Dockerコンテナの設定ファイルが含まれています。
  - `image-analysis-app`: アプリケーション用のDockerfile。
  - `mysql`: MySQL用のDockerfile。
- `image_analysis_project`: Djangoプロジェクトのルートディレクトリ。
  - `image_analysis`: プロジェクト全体の設定ファイルが含まれています。
  - `image_analysis_app`: 画像分析アプリケーション用のDjangoアプリケーション。
    - `tests`: アプリケーションのテスト。
  - `image_analysis_lib`: 画像分析ライブラリ。
    - `entities`: ドメインエンティティ。
    - `gateway`: 外部のAI画像分析サービスとのインターフェース。
    - `interactors`: ユースケース（ビジネスロジック）。
    - `repositories`: リポジトリのインターフェース。
    - `tests`: ライブラリのテスト。

## テスト

開発環境には、pytestを使用したテストが含まれています。テストを実行するには、以下のコマンドを実行します。

```bash
docker-compose exec image-analysis-app pytest
```
