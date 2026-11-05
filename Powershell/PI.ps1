Write-Host "The value of `$PI is now $PI, inside the script"

Param (
  $Path 
)
New-Item $Path
Write-Host "File $Path was created"

Param (
  [Parameter(Mandatory)]
  $Path
)

Param (
  [Parameter(Mandatory)]
  [string]$First,
  [int]$Second
)

Param (
  [string]$Path = './app'
)