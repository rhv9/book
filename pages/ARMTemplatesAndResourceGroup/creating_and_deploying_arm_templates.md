# Creating and Deploying ARM Templates

## How to write ARM Templates

### Format of ARM Template

ARM templates are natively written in JSON format. This JSON file details parameters of resource so that the ARM can execute and create the resource. 

An ARM template typically has the following main properties:

1. schema - version of ARM template
2. contentVersion - for you to version your templates
3. parameters - template parameters that you can provide values for when using template.
4. resources - resources to create with values specified for properties
5. output - output after deployment is successful.

If using your own paramters to use template with different values, two files will be needed. A ```<name of template>.json``` and ```<name of template>-parameters.json```.

### Writing your own ARM template

Start from an example template found online and modify values yourself. Visual Studio Code has extensions that provide a Language Server to provide auto-completion in writing ARM templates or Bicep.

The reference documentation provided by Microsoft on all Microsoft Resource Provider resources can be found [here](https://learn.microsoft.com/en-us/azure/templates/). It provides an example for creating any template, an explanation of all parameters, and how to write it for Bicep, ARM template and Terraform.

You can also start writing a template by creating the resource in Azure portal and then export either individual resources or the whole resource group as template.

## Deploying ARM Templates

There are many ways to deploy an ARM template. Some of the methods are:

1. PowerShell
2. Azure Cli
3. Cloud Shell
4. Template Spec service
5. Template service

### PowerShell

Ensure the Resource Group is already created. Then a new resource group deployment can be made as such.

```powershell
New-AzResourceGroupDeployment -TemplateFile /path/to/template.json -TemplateParameterFile /path/to/template-parameters.json
```

Can also use ```Test-AzResourceGroupDeployment``` to see if the schema is formatted correctly.

#### Passing parameters

There are a couple ways to pass parameter values to template:

- Passing ```<name of template>-parameter.json``` when running cmdlet.
- Passing arguments as such ```-ParameterName1 <value1> -ParameterName2 <value2>```
- Passing template parameter object as such

```powershell
$templateObj = @{"ParameterName1" : "value1", "ParameterName2" "value2",}
New-AzResourceGroupDeployment -TemplateFile /path/to/template.json `
    -TemplateParameterObject $templateObj
```

### Azure Cli

Go read documentation online

### Cloud Shell

Use powershell or azure cli commands from cloud shell.

### Template Spec Service

Store your ARM templates on the cloud and deploy from Azure Portal.

> The major advantage is it provides version control.

## Deployment Modes

There is Incremental and Complete deployment. The default for deployment commands is Incremental. The difference is that with Complete deployment, it will delete any resources that already exist in the resource group but not specified in the ARM template. 

So if resource group already contains resources A, B, C and template contains A, B, D, then after running deployment in complete mode, then C will be deleted, A and B parameters will be updated and D will be created.