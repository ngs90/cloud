$path = "C:\working\azure\keys\vm-ngs-playground-ubuntu_key.pem"
icacls.exe $path /reset
icacls.exe $path /GRANT:R "$($env:USERNAME):(R)"
icacls.exe $path /inheritance:r