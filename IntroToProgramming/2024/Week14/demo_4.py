search = input("Search database: ")

google = "Youtube Gmail Outlook Brave Google HTML CSS SystemAdmin Devops Computing"
# google = ["Google", "Youtube", "Gmail", "Outlook", "Brave",  "HTML", "CSS", "SystemAdmin", "Devops", "Computing"]

if google.find(search) > -1:
    print(200)
    print(f"SEO: {google.index(search)}")
else:
    print(404)
    print(f"SEO: {google.find(search)}")
