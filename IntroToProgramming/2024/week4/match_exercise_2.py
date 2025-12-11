access_control = input("What type of access would you like to grant: \n").lower()

# access control for admin, editor, viewer
match access_control:
    case "admin":
        print("Read, Write, Execute")
    case "editor":
        print("Read, Write")
    case "viewer":
        print("Read")
