import wikipedia


print(wikipedia.summary("Python Programming Language"))

result = wikipedia.search("Python Coding")
print("This is the search result of Python Coding':", result)

page = wikipedia.page(result[0])

title = page.title

categories = page.categories

content = page.content

links = page.links

references = page.references

summary = page.summary

print("Page content:\n", content, "\n")
print("Page title:\n", title, "\n")
print("categories:\n", categories, "\n")
print("Link:\n", links, "\n")
print("References:\n", references, "\n")
print("Page summary:\n", summary, "\n")