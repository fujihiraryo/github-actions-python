# Pythonのテストと静的コード解析のサンプルリポジトリ

mainブランチにプルリクエストを出したときに自動的にpytestによるテストとflake8による静的コード解析が行われます。

## テスト

テストコードは `src/test/` 以下に置き、 `test_` から始まるファイル名にします。  
`test_` で始まる関数がテストの対象になります。

```bash
python -m pytest
```

## 静的コード解析

コーディング規約の設定は `.flake8` に記載します。

```bash
flake8 (--show-source --statistics)
```

## プルリクエストの例

- [成功例](https://github.com/fujihiraryo/github-actions-python/pull/4)  
- [失敗例(lint)](https://github.com/fujihiraryo/github-actions-python/pull/5)  
- [失敗例(test)](https://github.com/fujihiraryo/github-actions-python/pull/6)  
