---
layout: minimal-post
title: "Secure random password generation locally in the terminal"
summary: "For when you just need a quick and secure password"
icon: "/images/favicons/apps.png"
---


# Generate with data from `/dev/random` filtering to a safe character set with the `tr` (transliterate) command.

24 alphanumeric characters without symbols:
```
echo $(LC_ALL=C  tr -dc 'A-Za-z0-9' < /dev/random | head -c 24)
```

24 alphanumeric characters with symbols:
```
echo $(LC_ALL=C  tr -dc 'A-Za-z0-9.!@^*_/' < /dev/random | head -c 24)
```

# Generate with openSSL output as base64

```
openssl rand -base64 32
```


