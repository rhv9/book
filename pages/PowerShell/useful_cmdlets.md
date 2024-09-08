# Useful Cmdlets

Over the years, there are new aliases added to each commands to give power users shortcuts to them. Such as ```?``` for ```Where-Object```

We can differentiate between them based on the version it was introduced.

> Note: Using PowerShell in **Linux** does bring some issues. Aliases such as ```ls``` or ```ps``` run actual linux binaries rather than aliasing PowerShell cmdlets. This is especially important for ```ps``` as piping its output will not work normally, if the expectation in PowerShell is to receive objects than the string that Linux ```ps``` gives.

## Basic commands

| Cmdlet | Description/Useful examples |
|--------|-----------------------------|
|Where-Object| Pipe objects into it and filter objects based on its parameters|
|| ```Get-Process \| Where-Object { $_.ProcessName -like "hypr*"}``` |
|| ```Get-Process \| ? ProcessName -like "hypr*"``` |
