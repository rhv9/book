# How to...

1. Connect to Windows VM using RDP

## Windows
Pretty straightforward, open Remote Desktop Connection app, plug in the ip address/URL, then username and password, profit! You can also download RDP file and with RDP file (from VM page in Azure Portal) it is even more easier, just double click it in file explorer and put username and password.

## Linux

I have used the freerdp software to connect and it is working flawlessly. Install it using your respective distro package tool. 

The important commands to remember are:

```bash
# /dynamic-resolution for changing window size, /f for fullscreen.
xfreerdp3 /v:<ip or url> /u:<username> /p:<password> /dynamic-resolution
# For example
xfreerdp3 /v:192.168.0.4 /u:joemama /p:1234 /dynamic-resolution
```

With RDP file:

```bash
xfreerdp3 /path/to/file.rdp /dynamic-resolution
```


> Note: After installing freerdp, there is xfreerdp3 and wfreerdp3 for X11 and Wayland respectively. Wayland one was crashing for some reason so I used X11 on my Hyprland Wayland setup (I use arch btw :D).
