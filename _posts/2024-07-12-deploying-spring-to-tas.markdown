---
layout: minimal-post
title: "Deploying spring to TAS"
summary: "Tanzu application service"
icon: "/images/favicons/apps.png"
---

## Login to the CLI

```bash
cf login -a https://my.tas.api.url.com
```

Enter username and password

## Get help in the CLI

```bash
cf help
```

## Start a spring app

https://start.spring.io

**Language:** Kotlin

**Dependencies:**  Spring Web, PostgreSQL Driver, Spring Security, Flyway Migration, H2 Database, Spring Data JPA)

[//]: # (Spring Data JPA)

_Click Generate_

## Implement your first API

DemoController.kt

```kotlin
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api")
class DemoController {
    @GetMapping("/hello")
    fun hello(): String {
        return "Hello, world!"
    }
}
```

## Push it to the CLOUD!

Choose a `<APP-NAME>` for your app that will be used by TAS.

Build the JAR

```bash
./gradlew build
```

Note the jar file that is build in the `build/libs` directory like `build/libs/<my-bundle-name>-0.0.1-SNAPSHOT.jar`.

Configure TAS to use the appropriate JDK version as was selected in the Spring Initializr.

```bash
cf set-env <app-name> JBP_CONFIG_OPEN_JDK_JRE '{jre: { version: 17.+ }}'
```

Push the app to TAS

```bash
cf set-env <app-name> JBP_CONFIG_OPEN_JDK_JRE '{jre: { version: 17.+ }}'
cf push <APP-NAME> -p build/libs/<my-bundle-name>-0.0.1-SNAPSHOT.jar
```

In the apps manager web UI, after selecting your org, and space,
you can see the app in status running.

Or you can run `cf apps` and see your app running as follows
cf apps
Getting apps in org dig / space demo as kaylee.mann@broadcom.com...

```bash
$ cf apps

name             requested state   processes           routes
...
<APP-NAME>       started           web:1/1, task:0/0   <APP-NAME>.tas.app.url.com
...
```

You should be able to see that your app is running by opening `<APP-NAME>.tas.app.url.com`
in the browser and see "Hello World!"

# Add a database

Get information on the available services

```bash
cf marketplace
```

```bash
offering   plans                     description                  broker
postgres   micro-2gb, ...            ...                          ...
```

Create a service instance

```bash
cf create-service postgres micro-2gb <APP-NAME>-db
```

Bind the service to the app

```bash
cf bind-service <APP-NAME> <APP-NAME>-db
```

Create an entity
_Post.kt_

```kotlin
import jakarta.persistence.Entity
import jakarta.persistence.Id
import java.util.*

@Entity
class Post(
    @Id
    var id: UUID,
    var content: String
)
```

Create a repository
_PostRepo.kt_

```kotlin
import org.springframework.data.jpa.repository.JpaRepository
import java.util.UUID

interface PostRepo : JpaRepository<Post, UUID> {
}
```

*V001__create_posts_table.sql*
```sql
CREATE TABLE post
(
    id      UUID PRIMARY KEY,
    content text
);
```

_PostController.kt_
```kotlin
import org.springframework.web.bind.annotation.*
import java.util.*

@RestController
@RequestMapping("/api")
class PostController(val postRepo: PostRepo) {
    @GetMapping("/posts")
    fun allPosts(): List<Post> {
        return postRepo.findAll()
    }

    data class NewPostRequest(
        val content: String
    )

    @PostMapping("/posts")
    fun allPosts(@RequestBody newPostRequest: NewPostRequest): Post {
        return postRepo.save(
            Post(
                UUID.randomUUID(),
                newPostRequest.content,
            )
        )
    }
}
```

_manifest.yml_
```yaml
applications:
  - name: tokitalk
    path: ./build/libs/tokitalk-0.0.1-SNAPSHOT.jar
    env:
      JBP_CONFIG_OPEN_JDK_JRE: '{ jre: { version: 17.+ } }'
```

Make the frontend
```bash
npm create vite@latest
```

Choose React and Typescript

Manifest for the frontend manifest.yml
```yaml
applications:
  - name: tokitalk-frontend
    memory: 512M
    instances: 1
    path: ./dist
    buildpacks:
      - staticfile_buildpack
```
