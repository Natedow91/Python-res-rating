"""Restaurant rating lister."""


open_file = open("scores.txt")
dict_file = {}
rlist = []
for line in open_file:
  line = line.rstrip('\n').split(':')
  dict_file[line[0]] = int(line[1])
  # rlist.append(dict_file)
  # dict_file.sort()
def sort_keys():
  sort_keys = dict_file.items()
  new_items = sorted(sort_keys)
  for ea in new_items:
    print(ea[0], "is rated at", ea[1])
  new_rate = input("Would you like to add another? type y or n\n")
  if new_rate == "y":
    new_input()

def new_input():
  new_res = input("Enter new Restaurant\n")
  new_rat = input("give rating\n")
  dict_file[new_res] = new_rat
  sort_keys()

new_input()