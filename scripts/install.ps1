function Find-Folders {
    [Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") | Out-Null
    [System.Windows.Forms.Application]::EnableVisualStyles()
    $browse = New-Object System.Windows.Forms.FolderBrowserDialog
    $browse.SelectedPath = "C:\"
    $browse.ShowNewFolderButton = $false
    $loop = $true
    while($loop)
    {
        if ($browse.ShowDialog() -eq "OK")
        {
        $loop = $false		
        } else
        {
            $res = [System.Windows.Forms.MessageBox]::Show("DO you want to quit installation!", [System.Windows.Forms.MessageBoxButtons]::RetryCancel)
            if($res -eq "Cancel")
            {
                return
            }
        }
    }
    $browse.Dispose()
    return $browse.SelectedPath
}

function downloadFiles {
    Write-Host "`nWelcome to VALFE08 prerequiste builder"
    Write-Host "`nVALFE08 needs ADB and python to operate"
    Write-Host "`n[INFO] See more information at https://github.com/code-reaper08/VALFE08#requirements`n"
    Write-Host "[.] Please select a directory to install VALFE08`n"
    $selected_path = Find-Folders
    Write-Host "[INFO] ADB will be installed in $selected_path`n"
    Set-Location $selected_path
    Write-Host "[.] Trying to download ADB from official source...`n"
    try {
        Invoke-WebRequest -Uri "https://dl.google.com/android/repository/platform-tools-latest-windows.zip" -OutFile "ADB.zip"
    Write-Host "[SUCCESS] Downloaded ADB successfully`n"
    }
    catch {
        Write-Host "[ERROR] ADB download failed, Please check your network connection`n"
    }
    Expand-Archive -Path .\ADB.zip -DestinationPath ./
    Remove-Item .\ADB.zip
    Write-Host "[INFO] Taking necessary backups...`n"
    $Env:PATH >> Env_Path.txt
    Write-Host "[.] Creating powershell session with ADB...`n"
    $Env:PATH = "./platform-tools;$Env:PATH"
    Write-Host "[SUCCESS] Created ADB session successfully`n"
    Write-Host "[SUCCESS] Added ADB to path for this session...`n"
    try {
        Write-Host "[.] Trying to download VALFE08 from the official repository...`n"
        Invoke-WebRequest -Uri "https://github.com/code-reaper08/VALFE08/releases/download/v0.1.0-alpha/valfe08-v0.1.0-alpha-Win64.exe" -OutFile "valfe08.exe"
    Write-Host "[SUCCESS] Downloaded VALFE08 successfully`n"
    }
    catch {
        Write-Host "[ERROR] VALFE08 download failed, Please check your network connection`n"
    }
}
downloadFiles
Write-Host "[SUCCESS] ADB and VALFE08 installed`n"
Write-Host "[INFO] You can initiate VALFE08 by simply calling like below`n"
Write-Host ".\valfe08.exe`n"
Write-Host "[INFO] You can also double click on the valfe08.exe to run it`n"
Write-Host "Thanks for downloading VALFE08`n"
Write-Host "If you like the project please consider supporting by giving a star on GitHub`n"
Write-Host "https://github.com/code-reaper08/VALFE08`n"