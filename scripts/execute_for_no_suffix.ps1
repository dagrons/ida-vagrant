# running <ida_script> for all files without suffix on <folder_path> 
$script_path = $args[1]
$folder_path = $args[2]
echo "running $script_path on $folder_path"
$files = (Get-ChildItem -Path $folder_path -Recurse -File | Where-Object { $_.Name -match "^(?!.*\..*)" })

foreach($f in $files) {
    echo "running $script_path on $($f.fullName)"
    idat64 -A -S"$script_path" "$($f.fullName)"
}