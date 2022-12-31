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
            $res = [System.Windows.Forms.MessageBox]::Show("Do you want to quit uninstallation?", [System.Windows.Forms.MessageBoxButtons]::RetryCancel)
            if($res -eq "Cancel")
            {
                return
            }
        }
    }
    $browse.Dispose()
    return $browse.SelectedPath
}

function uninstallvalfe08 {
    Write-Host "`nWelcome to VALFE08 Uninstaller`n"
    Write-Host "[INFO] Please select the folder in which you've installed VALFE08"
    Write-Host "`n[INFO] See more information at https://github.com/code-reaper08/VALFE08#requirements`n"
    $selected_path = Find-Folders

    Write-Host "[.] You've selected $selected_path`n"
    Set-Location $selected_path
    Write-Host "[.] Deleting all and cleaning up...`n"
    # Get-ChildItem -Path ./ -Include *.* -File -Recurse | ForEach-Object { $_.Delete()}
    Remove-Item ./* -Recurse -Force
}
uninstallvalfe08
Write-Host "[SUCCESS] Cleaned up`n"
Write-Host "[SUCCESS] Uninstalled successfully`n"
Write-Host "Hope VALFE08 was useful to you!`n"
Write-Host "If you like the project please consider supporting by giving a star on GitHub`n"
Write-Host "https://github.com/code-reaper08/VALFE08`n"