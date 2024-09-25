# Publish using Profile

## Downloaded Profile

You can download a publish profile for Visual Studio directly from Azure portal. Once downloaded, you can import the profiles, which are typically: FTP Deploy, Web Deploy, Zip Deploy.


## Not supported options

[//]: # "TODO:"

1. (THIS IS WRONG) You cannot publish both Windows and Linux app service into the same resource group and deploy into the same location. Either resource group are different, or loation is different, when mixing Windows and Linux app.

2. Web Deploy: not supported in Linux as it is a Microsoft IIS feature.

## Advanced Developer Tools

Going to ```<name of app service>.scm.azurewebsites.net``` *(take not of .scm.)* or under Advanced Tools in Portal, you can find some advanced tools for the app service.

In the .scm site, you can find:

1. Configuration information about the App Service and the VM on which it is running
    - So this includes Environment Variables, paths, OS info, etc.
2. Access to console to the VM.
3. (Only Windows) Tools tab which has ZIP Push deploy option from which you can drag and drop zip package of published app from Visual Studio.

