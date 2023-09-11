# Create a title logic
txt = "welcome to the jungle"

x = txt.split()


text_list = []
incr = 0

for i in x:
    words = i.capitalize()
    incr += 1
    text_list.insert(incr, words)

title = " ".join(text_list)
print(title)
