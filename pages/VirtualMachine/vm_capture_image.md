# VM Capture Image

VM Capture image is a process to create an image based on a VM that is already created. We can make our adjustments directly into the VM by remote connecting and install our software. Then if we want to copy or scale this setup to multiple instances, we will need an image to copy from. That is where this comes into play.

The image created will capture the disks as well, including data disk and create it for every VM instance made.

#### Creation options

- We create an image into a shared gallery (if you have not made one, then make one).
- We can select expiry date for an image
- A version number
- Which regions to save into and the storage medium:
    - E.g have a replica stored in East US and West US on Standard HDD LRS.
    - Can set replica count? 
- Specialized or Generalized image.

```diff
- I am not sure about how the region affects the copies. 
- Can't I make a VM from an image stored in another region? 
- I suppose there will be additional data transfer cost 
- if a new instance has to fetch from outside region.
-
- What is replica count and why does it matter? one enough?
```

There are two main types of images we can create:

#### Specialized Image

A specialized image is an image that will have all user credentials and data within the image. It will be a carbon copy of the VM.

Therefore, you will not need to input admin account information when creating a VM from this image.

#### Generalized Image

A generalized image is an image with user information/credentials needed to be provided on creation. It provides the OOBE (Out-of-box-experience). There are a few steps in creating a generalized image:

1. Ensure ADE is disabled (Azure Disk Encryption).
2. Use sysprep for windows to strip all user information and create OOBE.
3. Use PowerShell cmdlet ```Set-AzVm -ResourceGroupName "..." -Region "..." -Name "..." -Generalize```
4. Create a Generalized image. 