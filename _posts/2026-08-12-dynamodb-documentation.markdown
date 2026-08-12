---
layout: minimal-post
title: "Maintainable DynamoDB Documentation and Design"
summary: "How to keep your DynamoDB architecture from going off the rails"
icon: "/images/favicons/apps.png"
---

Using DynamoDB means that you have to keep track of which columns are used for what. This is difficult in a large
application using the recommended approach of using a single table for all data. Columns are overloaded to mean 
different things depending on the entity and the meaning of LSIs and GSIs can also overlap necessitating clear
planning and documentation.

Furthermore, I recommend always naming the PK and SK columns to be literally "PK" and "SK" as the meaning of these
columns depends on the specific entity of the row when using a mono-table design approach. DymamoDB is difficult to
modify once deployed as you can't do things like rename columns like you can with a relational database.

For many projects, the design choice is made to forgo use of LSI and instead use GSI. GSI indexes are only eventually
consistent but can be added/removed/renamed more easily than LSI indexes. If LSI indexes are used, they must be defined
when the table is first created. When working on an agile project for which the structure of the data and query patterns
is not yet known, but LSI indexes are likely to be needed in the future, one must be prepared to perform migrations
that rebuild the database or can alternatively pre-define LSI indexes with generic names such as "LSI1" and "LSI2" to 
be used later.

# My Recommended Documentation Approach

Make a table for each entity in the following format:


## Generic Entity Example

| Attribute Name | Type   | Description                  | Format                 | GSI Inclusion                         | LSI Inclusion                  |
|----------------|--------|------------------------------|------------------------|---------------------------------------|--------------------------------|
| PK             | String | Primary partition key        | Entity-specific format | GSI name as included attribute or PK  | LSI name as included attribute |
| SK             | String | Primary sort key             | Entity-specific format | GSI name as sort key or included attr | LSI name as sort key           |
| attribute1     | String | Description of attribute     | Format if applicable   | GSI name as included attribute        | LSI name as included attribute |
| attribute2     | Number | Description of numeric field |                        | GSI name as partition or sort key     |                                |
| attribute3     | Bool   | Description of boolean flag  |                        | GSI name as included attribute        |                                |


## TodoItem

| Attribute Name | Type   | Description            | Format     | GSI Inclusion                     | LSI Inclusion |
|----------------|--------|------------------------|------------|-----------------------------------|---------------|
| PK             | String | TodoItem identifier    | UUIDv4     | TodoItemsByUser IncludedAttribute |               |
| SK             | String | Creation time          | yyyy-mm-dd | TodoItemsByUser SK                |               |
| content        | String | TodoItem content       |            | TodoItemsByUser IncludedAttribute |               |
| user           | string | user id                | UUIDv4     | TodoItemsByUser PK                |               |
| done           | bool   | Completion status flag |            | TodoItemsByUser IncludedAttribute |               |


----------

## Compound Keys Example

A common pattern is packing multiple attributes into SK (or PK) using a delimiter, so a single query can filter/sort by more than one dimension. Extending TodoItem to support "get all of a user's todos, filtered by status, sorted by due date":

| Attribute Name | Type   | Description           | Format                                      | GSI Inclusion              |
|-----------------|--------|------------------------|----------------------------------------------|------------------------------|
| PK              | String | TodoItem identifier    | `TODO#<uuid>`                                |                              |
| SK              | String | Creation time          | `yyyy-mm-dd`                                 |                              |
| GSI1PK          | String | User identifier        | `USER#<uuid>`                                | TodoItemsByUserStatus PK    |
| GSI1SK          | String | Compound status+date   | `STATUS#<done\|pending>#DATE#<yyyy-mm-dd>`   | TodoItemsByUserStatus SK    |

With `GSI1SK = STATUS#pending#DATE#2024-06-01`, you can:

- Query `GSI1PK = USER#123 AND begins_with(GSI1SK, "STATUS#pending")` → all pending todos for a user, naturally sorted by date within that status
- Query `GSI1PK = USER#123 AND begins_with(GSI1SK, "STATUS#pending#DATE#2024-06")` → pending todos for that user in June 2024