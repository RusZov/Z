$renpyRoot = Join-Path $PSScriptRoot 'renpy-8.5.2-sdk'
$renpyExe = Join-Path $renpyRoot 'renpy.exe'

if (-not (Test-Path -LiteralPath $renpyExe)) {
    Write-Error "Ren'Py launcher not found: $renpyExe"
    exit 1
}

Start-Process -FilePath $renpyExe -WorkingDirectory $renpyRoot
