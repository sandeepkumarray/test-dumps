# ==========================================
# CONFIG
# ==========================================

$ServiceName   = "CustomerPortal"
$DisplayName   = "Customer Portal Frontend"

$AppRoot       = "C:\apps\customer-portal"
$BuildPath     = Join-Path $AppRoot "build"

$ReleasePath   = "${bamboo.deploy.release.directory}\build"

$Port          = 8080

$NodeExe       = "C:\Program Files\nodejs\node.exe"

$ServeScript   = Join-Path $AppRoot "node_modules\serve\build\main.js"

# ==========================================
# VALIDATE NODE
# ==========================================

if (!(Test-Path $NodeExe)) {
    throw "Node.exe not found: $NodeExe"
}

# ==========================================
# CREATE APP ROOT
# ==========================================

if (!(Test-Path $AppRoot)) {
    New-Item -ItemType Directory -Path $AppRoot -Force
}

# ==========================================
# INSTALL SERVE IF NEEDED
# ==========================================

if (!(Test-Path $ServeScript)) {

    Write-Host "Installing serve package..."

    Push-Location $AppRoot

    if (!(Test-Path ".\package.json")) {
        npm init -y
    }

    npm install serve --save

    Pop-Location
}

# ==========================================
# CREATE SERVICE IF NOT EXISTS
# ==========================================

$service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue

if (!$service) {

    Write-Host "Creating Windows Service..."

    $BinaryPath = "`"$NodeExe`" `"$ServeScript`" -s build -l $Port"

    $result = Invoke-CimMethod `
        -ClassName Win32_Service `
        -MethodName Create `
        -Arguments @{
            Name           = $ServiceName
            DisplayName    = $DisplayName
            PathName       = $BinaryPath
            ServiceType    = 16
            ErrorControl   = 1
            StartMode      = "Automatic"
            DesktopInteract= $false
            StartName      = "LocalSystem"
        }

    if ($result.ReturnValue -ne 0) {
        throw "Failed to create service. Return code: $($result.ReturnValue)"
    }

    Write-Host "Service created successfully."

    # Configure restart on failure
    sc.exe failure $ServiceName reset= 86400 actions= restart/5000
}
else {
    Write-Host "Service already exists."
}

# ==========================================
# STOP SERVICE
# ==========================================

$service = Get-Service $ServiceName

if ($service.Status -eq 'Running') {

    Write-Host "Stopping service..."

    Stop-Service $ServiceName -Force

    $service.WaitForStatus('Stopped','00:00:30')

    Write-Host "Service stopped."
}

# ==========================================
# DEPLOY BUILD FILES
# ==========================================

Write-Host "Deploying React build..."

if (!(Test-Path $BuildPath)) {
    New-Item -ItemType Directory -Path $BuildPath -Force
}

# Recommended for production
robocopy $ReleasePath $BuildPath /MIR /R:2 /W:5

$RobocopyExit = $LASTEXITCODE

# Robocopy success codes
if ($RobocopyExit -gt 7) {
    throw "Robocopy failed with exit code $RobocopyExit"
}

Write-Host "Deployment completed."

# ==========================================
# START SERVICE
# ==========================================

Write-Host "Starting service..."

Start-Service $ServiceName

Start-Sleep -Seconds 5

$service = Get-Service $ServiceName

Write-Host "Current Status: $($service.Status)"

if ($service.Status -ne 'Running') {
    throw "Service failed to start."
}

Write-Host ""
Write-Host "================================="
Write-Host "Deployment Successful"
Write-Host "================================="
Write-Host "Service : $ServiceName"
Write-Host "URL     : http://localhost:$Port"
Write-Host ""