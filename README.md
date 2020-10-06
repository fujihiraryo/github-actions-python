# Pythonのテストと静的コード解析のサンプル

mainブランチにプルリクエストを出したときに自動的にpytestによるテストとflake8による静的コード解析が行われます。

## 環境

Pythonのバージョンは3.8です。必要なライブラリは

```bash
pip install -r requirements.txt
```

でインストールします。

## テスト

テストコードは `src/test/` 以下に置き、 `test_` から始まるファイル名にします。  
`test_` で始まる関数がテストの対象になります。

```bash
python -m pytest
```

## 静的コード解析

コーディング規約の設定は `.flake8` に記載します。  
ここでは [Black](https://black.readthedocs.io/en/stable/the_black_code_style.html) の設定に準拠しました。  
- 1行あたりの文字数は88字以内
- E203(‘:’の前の空白)を無視

これ以外のコーディング規約は [pycodestyle](https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes) と [pyflakes](https://flake8.pycqa.org/en/latest/user/error-codes.html) を合わせたものになっています。

```bash
flake8 (--show-source --statistics)
```

blackをローカルにインストールしておけば、

```bash
black .
```

で自動的に整形することができます。


## Visual Studio Codeでの設定

```json
{
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--ignore=E203",
    "--max-line-length=88"
  ],
  "python.formatting.provider": "black"
}
```


## プルリクエストの例

- [成功例](https://github.com/fujihiraryo/github-actions-python/pull/4)  
- [失敗例(lint)](https://github.com/fujihiraryo/github-actions-python/pull/5)  
- [失敗例(test)](https://github.com/fujihiraryo/github-actions-python/pull/6)  

![ 2020-10-07 at 4 14 57](https://user-images.githubusercontent.com/49140016/95249511-c11ad100-0853-11eb-9f39-a4ece2fc8f31.png)
