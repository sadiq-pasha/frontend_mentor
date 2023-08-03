logfile = open("./SyncLogErrorsCSV.txt", "r")
file_lines = logfile.readlines()
print(len(file_lines))
tag_map = {}

def remove_brackets(tag_number):
  unbaracket_tag = ''
  for character in tag_number:
    if character == '[' or character == ']':
      continue
    unbaracket_tag += character
  return unbaracket_tag

for line in file_lines:
  split_line = line.split(',')
  tag = remove_brackets(split_line[1])
  if tag in tag_map:
    tag_map[tag].append(split_line[0])
  else:
    tag_map[tag] = [split_line[0]]

print(len(tag_map))

# csv = []
# for line in file_lines:
#     row = []
#     split_line = line.split()
#     time_stamp = split_line[0].split(':')[1] + ':' + split_line[1]
#     row.append(time_stamp.replace(',',':'))
#     row.append(split_line[-3])
#     csv.append(row)    
# print(csv)
# with open("./SyncLogErrorsCSV.txt", 'w') as linefor row in csv:
#       f.write(row[0])
#       f.write(',')
#       f.write(row[1])
#       f.write(',')
#       f.write('\n')