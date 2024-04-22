---
layout: minimal-post
title: "Just Some Useful Shell Tips and Snippets"
summary: "For Various Things"
icon: "/images/favicons/apps.png"
---

<link href="/css/syntax.css" rel="stylesheet">

## Using OBS Virtual Camera in Discord

```shell
sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"
sudo codesign --sign - "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"
```

### Using OBS Virtual Camera in Zoom

```shell
sudo codesign --remove-signature "/Applications/zoom.us.app"
sudo codesign --sign - "/Applications/zoom.us.app"
```

## Find app listening on given port

```shell
lsof -i :<port number>
```

To kill the app use `kill <PID>` with `<PID>` substituted with the PID number returned by the command above.

## Show the MacOSX App Switcher on all Monitors

```shell
defaults write com.apple.Dock appswitcher-all-displays -bool true
killall Dock
```

## Generate a random uuid
```shell
uuidgen
```
to generate 10 of them
```shell
for run in {1..10}; do uuidgen; done
```

## Enable OBS Virtual Cameras for Discord/Zoom on Mac OSX
For Discord:
```shell
sudo codesign --remove-signature "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"
sudo codesign --sign -           "/Applications/Discord.app/Contents/Frameworks/Discord Helper (Renderer).app"
```

For Zoom:
```shell
sudo codesign --remove-signature "/Applications/zoom.us.app"
sudo codesign --sign -           "/Applications/zoom.us.app"
```

## Mount a usb drive in linux
```shell
sudo mkdir /mnt/usb-drive
sudo chown <myusername>:<myusername> /mnt/usb-drive/
sudo fdisk -l # to find the device name.  For Example "/dev/sde1" 
sudo mount -o uid=<myusername>,gid=<myusername> <devicename> /mnt/usb-drive
# to unmount
sudo umount /mnt/usb-drive
```

