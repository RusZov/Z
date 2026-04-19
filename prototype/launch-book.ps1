$projectRoot = Join-Path $PSScriptRoot 'gorny_prototype'
$workspaceRoot = Split-Path -Parent $PSScriptRoot
$renpyRoot = Join-Path $workspaceRoot 'setup\renpy-8.5.2-sdk'
$renpyExe = Join-Path $renpyRoot 'renpy.exe'

if (-not (Test-Path -LiteralPath $projectRoot)) {
    Write-Error "Ren'Py project not found: $projectRoot"
    exit 1
}

if (-not (Test-Path -LiteralPath $renpyExe)) {
    Write-Error "Ren'Py launcher not found: $renpyExe"
    exit 1
}

Start-Process -FilePath $renpyExe -ArgumentList @($projectRoot) -WorkingDirectory $renpyRoot
