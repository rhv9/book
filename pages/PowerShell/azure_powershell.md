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

## Some tips

All azure command types are prefixed by ```Get-Az*```, ```New-Az*```, ```Remove-Az*```

Most commands, you will find ```-ResourceGroupName``` and ```-Location```. Also ```-Name```. These are common in most Azure services.

## Doing some useful actions

### Managing Resource Group

Create using
```powershell
New-AzResourceGroup -Name "rhv-eastus-rg" -Location "East Us"
```
Delete using
```powershell
# A bit slow to execute
Remove-AzResourceGroup -Name "rhv-eastus-rg"
```

> To get all locations, use ```Get-AzLocation```

### Creating App service plan and App service



