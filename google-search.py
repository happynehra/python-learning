from googlesearch import search

query = input("Enter what you want to search: ")
result = int(input("How many results do you want: "))

search_results = []
counter = 0

for url in search(query, stop=result, pause=2.0):
    search_results.append(url)
    counter += 1
    if counter >= result:
        break

print("Search Result:")
for url in search_results:
    print(url)