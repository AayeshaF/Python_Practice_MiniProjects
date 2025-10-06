total_urls = 0
urls = []
while total_urls <5:
    new_website = input("Enter the new website: ")
    new_url = f"https://www.{new_website}"
    total_urls += 1
    urls.append(new_url)

    print("The website has been successfully added")
    print(f"You have {5-total_urls} slots left to add websites")
    print("Your favourite websites: ")
    print("\n".join(urls))

print("Bookmark Is Full, You Can't Add More")
if len(urls)>1:
    urls.sort()
print("Your favourite websites: ")
print("\n".join(urls))

