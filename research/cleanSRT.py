def clean_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if line is not empty and is not a number
        if line and not line.isdigit():
            # Check if the line is a timestamp
            if '-->' in line:
                timestamp = line
                # Get the next line which is the dialogue
                if i + 1 < len(lines):
                    dialogue = lines[i + 1].strip()
                    cleaned_lines.append(f"{timestamp} : {dialogue}")
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for cleaned_line in cleaned_lines:
            file.write(cleaned_line + '\n')

# Usage
clean_srt('moviesub.srt', 'cleaned_moviesub.srt')
