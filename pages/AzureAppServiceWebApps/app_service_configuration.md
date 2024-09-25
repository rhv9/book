# App Service Configuration

Under configuration, there are 5 main things we can configure

1. Application Settings
2. General Settings
3. Default Documents
4. Path Settings
5. Error pages

## Application Settings

In application settings, you can configure the environment variables that the web app can pickup during runtime. 

With a .NET (7.0 I have tested), we can locally configure a file named ```appsettings.json```. This file is used to configure environment variables locally within the .NET web app project. The configuration can be accessed within the Model if you take in a constructor paramter of type ```IConfiguration```.

Highest priority is given to configuration in application settings, with ```appsettings.json``` as the lowest priority. 

One way you can take advantage of this feature is by providing default values in ```appsettings.json``` and then using application settings to configure different stage specific values for stages such as development, testing and production (e.g. different connection string for dev or production database server).

#### Connection Strings

These are just environment variables that you can provide which is considered more secure as it is encrypted at rest and in transit. The values will appear under ```"ConnectionStrings"``` env variable.

## General Settings

> I don't remember...

This has a lot of important settings, including:

1. Keep application always active: This is useful for when you deploy more than one app service on the same app service plan.
2. 

## Default Documents

## Path Settings

We can configure default pages paths which is typically achieved within modern application so it is for legacy purposes.

#### Virtual paths

We can add virtual paths for web pages

#### File share mounting

We can set a mount point for a File Share container in a storage account which can be accessed by the application. 

> Can test by creating File Share container and mounting it. Then add a virtual path to lets say a jpg file and then can access with the url ```<name of service>.azurewebsites.net/virtual/path/cute.jpg```

All mounting is relative to the ```/mount``` file location in Linux. Not sure about Windows.

## Error pages

Use custom pages for each error status code. 

> Only premium feature?