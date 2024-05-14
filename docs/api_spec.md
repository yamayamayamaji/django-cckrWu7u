## API仕様

### 画像分析リクエスト
画像分析を依頼し、分析の結果を保存します。

- エンドポイント: `/image_analysis/analyze/`
- メソッド: POST
- リクエストボディ:
  ```json
  {
    "image_path": "/path/to/image.jpg"
  }
  ```
  - `image_path`: 分析対象の画像ファイルパス
- レスポンス:
  - 成功時:
    ```json
    {
      "log_id": 123,
      "image_path": "/path/to/image.jpg"
    }
    ```
    - `log_id`: 記録した分析ログのID
    - `image_path`: 分析対象の画像パス
  - 失敗時:
    - ...

### 分析ログ取得
保存されている分析ログを取得します。

- エンドポイント: `/image_analysis/analysis_log/<log_id>/`
- メソッド: GET
- パスパラメータ:
  - `log_id`: 取得する分析ログのID
- レスポンス:
  - 成功時:
    ```json
    {
      "success": true,
      "image_path": "/path/to/image.jpg",
      "message": "success",
      "class_id": 3,
      "confidence": 0.8683
    }
    ```
    - `success`: 分析の成功フラグ
    - `image_path`: 分析対象の画像パス
    - `message`: 分析結果のメッセージ
    - `class_id`: 分析結果のクラスID（分析が失敗した場合は`null`）
    - `confidence`: 分析結果の信頼度（分析が失敗した場合は`null`）
  - 失敗時:
    - ...
