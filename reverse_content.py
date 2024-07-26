def reverse_file_content(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        reversed_content = content[::-1]
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(reversed_content)
        
        print(f"Content from {input_file} has been reversed and saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

reverse_file_content('input.txt', 'output.txt')