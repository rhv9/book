# Disk Snapshot

Disk snapshot is a service for managed disk that allows you to create a copy of the disk at a point-in-time. 

The benefit of using a disk snapshot is that you can easily use this for other purposes:

- Create an image to create a VM with.
- Create a VM with it directly
- Download the .vhd file
- Copy the .vhd file to another storage account.


## Cost

The first method to reduce costs is to store the snapshots on a Standard HDD. There are three options: Standard HDD, Premium SSD, and Zone-Redundant storage as highest.

Another way in which it is cost effective is that you can create incremental snapshots after your initial full snapshot. This will save in storage quantity stored.