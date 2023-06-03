#import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

all_anchor_tags = soup.findAll(name="a")
print(all_anchor_tags)

print("\n")
for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

print("\n")

heading = soup.find(name="h1", id="name")
print(heading.string)

print("\n")
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

print("\n")
company_url = soup.select_one(selector="p a") # se puede seleccionar clases .clase e ids #id
print(company_url)