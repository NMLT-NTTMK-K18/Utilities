# SCRIPT WAS GENERATED BY CHATGPT
# https://chat.openai.com/share/f7101e1b-8116-4622-8d2a-9a32ca0f4311

# Get data from clipboard
$data = Get-Clipboard -Raw

# Define start_num and end_num as variables
$start_num = "5"
$end_num = "5"

# Define regex pattern
$pattern = "^\d{$start_num,$end_num}\..*"

# Split the data into lines
$lines = $data -split "`r`n"

# Process each line
foreach ($line in $lines) {
    if ($line -match $pattern) {
        # Remove the specified prefix
        $modifiedLine = $line -replace "^\d{$start_num,$end_num}\.", ""

        # Remove the first space if it exists
        if ($modifiedLine -match "^ ") {
            $modifiedLine = $modifiedLine -replace "^ ", ""
        }

        # Append the modified line to the result
        $result += $modifiedLine + "`r`n"
    }
}

# Copy the modified data back to clipboard
$result | Set-Clipboard
