# Extensions

These are post-deployment installation or configuration of VM. There are several built-in extensions that allow you to do achieve many different tasks such as running a custom script, changing admin password, and more.

#### Custom Script Extension

This is an extension that when created, will run the script specified on creation of the extension. It is only run once in its lifetime. You want to a script to run on every startup, you can write a scheduled task for Windows or equivalent in Linux.

We can either provide a public file uri to download and run, or use a blob file in a storage container to download and run.

When the script is being stored on the storage account, here are two ways in which you can access the script file. Either make the container public and the pass the file uri, or provide the storage account key when running script. Azure portal makes this process easier.

When using a public uri, we can execute an Azure PowerShell cmdlet as such:

```powershell
Set-AzVMCustomScriptExtension `
    -ResourceGroupName "..." `
    -VMName "..." `
    -Name "MyCustomScript" `
    -FileUri "https://www.github.com/deeznuts/epic.ps1" `
    -Run "epic.ps1" `
    -Location "East US"
```

There is also a general extension script which you can specify in parameters the exact extension.

Some facts:
- Timeout after 90 minutes.