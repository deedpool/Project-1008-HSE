reader = open('ResCont.txt', 'r')
data = reader.read()
reader.close()

def clear_row(original):
    result = original

    for count in range(5, 1, -1):
        result = result.replace(' ' * count, ' ')

    return result.replace('\n','').strip()

def check_rule(row, start, end):
    row_items = row.split(' ')

    number = int(row_items[2])

    return number >= start and number <= end

def find_entries(text, start, end):
    result = []
    current_pos = -1
    text_end = len(text)
    
    while current_pos <= text_end:
        next_dot = text.find(',', current_pos + 1)

        if next_dot == -1:
            break

        original_row = text[current_pos + 1 : next_dot]
        row = clear_row(original_row)
        
        is_correct = check_rule(row, start, end)
        if is_correct:
            result.append(original_row)

        current_pos = next_dot

    return result

strings = find_entries(data, 210, 250)

with open('result.txt', 'w') as writer:
    for item in strings:
        writer.write(item+'\n')
