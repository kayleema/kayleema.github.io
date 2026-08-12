---
layout: minimal-post
title: "保守しやすいDynamoDBのドキュメントと設計"
summary: "DynamoDBの設計を破綻させないための方法"
icon: "/images/favicons/apps.png"
lang: jp
categories:
  - jp
---

DynamoDBを使う場合、どのカラムが何のために使われているかを把握しておく必要があります。これは、単一テーブルに全データをまとめる推奨アプローチを採用した大規模なアプリケーションでは特に難しくなります。カラムはエンティティによって異なる意味を持つように使い回され、LSIやGSIの意味も重複することがあるため、明確な計画とドキュメントが不可欠です。

さらに、PKとSKのカラム名は文字通り「PK」「SK」と命名することをお勧めします。モノテーブル設計を使う場合、これらのカラムの意味は行のエンティティによって変わるためです。DynamoDBはデプロイ後の変更が難しく、リレーショナルデータベースのようにカラム名を変更するといったことができません。

多くのプロジェクトでは、LSIを使わずGSIのみを使う設計が選ばれます。GSIインデックスは結果整合性しか持ちませんが、LSIインデックスよりも後から追加・削除・変更しやすいという利点があります。LSIインデックスを使う場合は、テーブル作成時に定義しておく必要があります。データ構造やクエリパターンがまだ確定していないアジャイルなプロジェクトで、将来的にLSIインデックスが必要になりそうな場合は、データベースを再構築するマイグレーションを行う準備をしておくか、あるいは「LSI1」「LSI2」のような汎用的な名前でLSIインデックスを事前に定義しておき、後から使う、という代替手段もあります。

# おすすめのドキュメント作成方法

各エンティティについて、以下の形式で表を作成します。


## 汎用エンティティの例

| 属性名AttributeName | データー型Type | 説明             | Format                 | GSI Inclusion                         | LSI Inclusion                  |
|------------------|-----------|----------------|------------------------|----------------------------------------|--------------------------------|
| PK               | String    | 主パーティションキー     | Entity-specific format | GSI name as included attribute or PK  | LSI name as included attribute |
| SK               | String    | 主ソートキー         | Entity-specific format | GSI name as sort key or included attr | LSI name as sort key           |
| attribute1       | String    | 属性の説明          | Format if applicable   | GSI name as included attribute        | LSI name as included attribute |
| attribute2       | Number    | 数値フィールドの説明     |                        | GSI name as partition or sort key     |                                |
| attribute3       | Bool      | ブールフラグの説明      |                        | GSI name as included attribute        |                                |


## TodoItem

| 属性名AttributeName | データー型Type | 説明           | Format     | GSI Inclusion                     | LSI Inclusion |
|------------------|-----------|--------------|------------|-----------------------------------|---------------|
| PK               | String    | TodoItem識別番号 | UUIDv4     | TodoItemsByUserのIncludedAttribute |               |
| SK               | String    | 作成時間         | yyyy-mm-dd | TodoItemsByUserのSK                |               |
| content          | String    | TodoItemの内容  |            | TodoItemsByUserのIncludedAttribute |               |
| user             | string    | user id      | UUIDv4     | TodoItemsByUserのPK                |               |
| done             | bool      | 完了かどうかのフラグ   |            | TodoItemsByUserのIncludedAttribute |               |


----------

## 複合キーの例

よく使われるパターンとして、複数の属性をデリミタで区切ってSK（またはPK）に詰め込むことで、1つのクエリで複数の軸によるフィルタリングやソートができるようにする方法があります。TodoItemを拡張して「あるユーザーのTodoを、ステータスでフィルタし、期限でソートして全件取得する」に対応させる例です。

| 属性名AttributeName | データー型Type | 説明             | Format                                      | GSI Inclusion              |
|-------------------|-----------|----------------|----------------------------------------------|------------------------------|
| PK                | String    | TodoItem識別番号   | `TODO#<uuid>`                                |                              |
| SK                | String    | 作成時間           | `yyyy-mm-dd`                                 |                              |
| GSI1PK            | String    | ユーザー識別番号      | `USER#<uuid>`                                | TodoItemsByUserStatusのPK    |
| GSI1SK            | String    | ステータスと日付の複合キー | `STATUS#<done\|pending>#DATE#<yyyy-mm-dd>`   | TodoItemsByUserStatusのSK    |

`GSI1SK = STATUS#pending#DATE#2024-06-01` とすると、以下のようなクエリが可能になります。

- `GSI1PK = USER#123 AND begins_with(GSI1SK, "STATUS#pending")` をクエリ → あるユーザーの未完了のTodoを全件取得し、そのステータス内で自然に日付順にソートされる
- `GSI1PK = USER#123 AND begins_with(GSI1SK, "STATUS#pending#DATE#2024-06")` をクエリ → そのユーザーの2024年6月分の未完了Todo
