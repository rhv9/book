# Azure PowerShell

## Installing Azure PowerShell Module

Works for both Windows and Linux.

```powershell
# Install
Install-Module -Name Az -Repository PSGallery -Force
# Update Az PowerShell module
Update-Module -Name Az -Force
```

Checking all modules installed
```powershell
Get-Module -ListAvailable
```

## Logging In

To login, run the following command. It should open up a webpage/popup to help you login your Microsoft Account.

```PowerShell
Login-AzAccount
```

Check your subscription is correct using the following commands. If they are wrong, you can switch to the correct one.
```PowerShell 
# Check your current context
Get-AzContext
# Get list of subscriptions
Get-AzSubscription
# Switch subscription
Set-AzContext -Subscription "<Name of subscription>"
```

## Some Tips and Tricks

Most azure command types for handling Azure services are prefixed by ```Get-Az*```, ```New-Az*```, ```Remove-Az*```

Most commands, you will find ```-ResourceGroupName``` and ```-Location```. Also ```-Name```. These are common in most Azure services.

### Azure Predictor

Azure Predictor in combination with PSReadLine, allows providing suggestions for commands based on AI suggestions. The full documentation and commands can be found [here](https://learn.microsoft.com/en-us/powershell/azure/az-predictor).

The steps to get it working is simple: 

1. Install the ```Az.Tools.Predictor``` module (see the documentation for the latest cmdlets). 
2. New PowerShell versions have PSReadLine already installed and active. 
3. Enable the Az Predictor.
4. Then set the view style to inline or list view (default is inline). 

*Tip: ```Alt + A``` keybinding allows you to cycle through arguments which is convenient.*

## Doing some useful actions

### Managing Resource Group

- Create using
```powershell
New-AzResourceGroup -Name "rhv-eastus-rg" -Location "East Us"
```
- Delete using
```powershell
# A bit slow to execute
Remove-AzResourceGroup -Name "rhv-eastus-rg"
```

> To get all locations, use ```Get-AzLocation```

- Get all Resource Groups starting with the name *"rhv-\*"* and group output by location

```powershell
Get-AzResourceGroup -Name rhv-* | Sort-Object Location,ResourceGroupName | Format-Table -GroupBy Location
```

### Creating App service plan and App service


### Storage Account

- Creating

- Setting context

- Updating a parameter

- Create container



