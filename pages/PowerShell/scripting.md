# Scripting

```powershell
# Loops
$namesarray = "John","Cow","Jack"
foreach ($name in $namesarray)
{
    Write-Output $name
}
```

```powershell
# Writing a function and using it. 
# Take note of how parameters are defined for function 
# and how parameters are passed to functions
function printAge($j,$c,$d)
{
    Write-Output "John: $j, Cena: $c, Dog: $d"
}

printAge 22 33 44
```

```powershell
# this referes to the current object in the pipeline.
$_
```

```powershell
# THIS DOES NOT WORK ON LINUX
# Read content of file
$filecontent = ${c:/Users/rhv/dev/fox.txt}
write-output $filecontent
# Edit content of file
${c:/Users/rhv/dev/fox.txt} = "New text. Fox said alkjhsdhfs."
```

```powershell
# Taking parameters in a script.ps1 with defaults
param (
    [int]$startNumber = 1,
    [int]$endnumber = 10,
    [string]$message = "Egg"
)

$cnt = $startNumber

while ($cnt -le $endnumber)
{
    if ($cnt -eq 1)
    {
        Write-Output "$cnt ${message}"
    }
    else {
        Write-Output "$cnt ${message}s"
    }
    $cnt++
}

# Run with
./count.ps1 1 10 "ball"
# Or
./count.ps1 -message "ball"

```

## Using .NET objects

Everything in PowerShell is an object. The type String is of type System.String in .NET

### Invoking static members

```powershell 
[String]::Compare("nice","Nice")
"Why Hello There".ToUpper()
"Nice".CompareTo("Nice")
# To get processes from diagnostics classes (.NET API)
[System.Diagnostics.Process]::GetProcesses()
[System.DateTime]::Today
```

Creating objects of Date
```powershell
$date = New-Object -TypeName System.DateTime -ArgumentList @(2036,9,10)
$date.ToLongDateString()
```