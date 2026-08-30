---
layout: minimal-post
title: "Arch Install Quick Reference"
summary: "A dense list of things to get a system running"
icon: "/images/favicons/apps.png"
---

<style>
.language-shell {
    margin-block-end: 10px;
}
pre {
    margin: 6px;
}
</style>

<br/>

```shell
setfont ter-132b
cat /sys/firmware/efi/fw_platform_size
ip link
ping ping.archlinux.org
timedatectl
fdisk -l
free -h
```

```shell
fdisk /dev/sda
    g    n <enter> <enter> +1G    t <enter> 1
         n <enter> <enter> +16G   t <enter> 19
         n <enter> <enter> <enter>
    p w
```

```shell
mkfs.ext4 /dev/sda3
mkswap /dev/sda2
mkfs.fat -F32 /dev/sda1
mount /dev/sda3 /mnt
mount --mkdir /dev/sda1 /mnt/boot
swapon /dev/sda2
lscpu
```

```shell
pacstrap -K /mnt base base-devel linux linux-firmware \
                 vim sudo networkmanager openssh man-db man-pages texinfo intel-ucode
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot -S /mnt
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
hwclock --systohc
passwd
bootctl install
```

```shell
vim /boot/loader/loader.conf
    default arch.conf
    timeout 3
    console-mode max
    editor no
```

```shell
vim /boot/loader/entries/arch.conf
    title Arch Linux
    linux /vmlinuz-linux
    initrd /initramfs-linux.img
    options root=UUID=... rw
```

```shell
bootctl update
vim /etc/hostname
systemctl enable NetworkManager
sudo systemctl enable sshd
reboot
EDITOR=vim visudo
useradd -m -G wheel -s /bin/bash <username>
passwd <username>
```

## Add ZFS Support

```shell
sudo pacman -S --needed git base-devel
mkdir repos
cd repos
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -S zfs-utils zfs-dkms
sudo modprobe zfs
```
```shell
sudo vim /etc/pacman.conf
    IgnorePkg = linux linux-headers
```

## Add KDE DE
```shell
sudo pacman -S plasma-meta plasma-login-manager dolphin konsole ark gwenview
sudo systemctl isolate graphical
sudo systemctl enable plasma-login-manager
sudo systemctl set-default multi-user
```

## Add Tailscale

```shell
sudo pacman -S tailscale
sudo systemctl enable --now tailscaled
sudo tailscale up
tailscale status
```

## More fun things:

```shell
vim .bashrc
    MAGENTA="\[$(tput setaf 5)\]"
    YELLOW="\[$(tput setaf 3)\]"
    RESET="\[$(tput sgr0)\]"
    PS1='['"$MAGENTA"'\u@\h'"$RESET"' '"$YELLOW"'\W'"$RESET"']\$ '
```

```shell
sudo vim /etc/ssh/sshd_config
    Banner /etc/issue.net
sudo vim /etc/issue.net
```

## Fun Apps

```shell
sudo pacman -S fastfetch btop
sudo pacman -S inkscape gimp rawtherapee blender
sudo pacman -S kicad kicad-library kicad-library-3d
sudo pacman -S anki
yay -S visual-studio-code-bin
```

## Dev tools

```shell
sudo pacman -S ruby
echo 'export PATH="$HOME/.local/share/gem/ruby/3.4.0/bin:$PATH"' >> ~/.bashrc
```

## Docker/Kubernetes

...
