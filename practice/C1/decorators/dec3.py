# 3. Restricting Function Access Based on User Role
# Problem: Create a decorator that restricts access to a 
# function based on a user role. If the user role is 
# not "admin," the function should print "Access 
# denied."

# Function Example: A function that deletes a file 
# (just print a message in this case).

# Expected Output:
# Access denied

def role_required(role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if user_role != role:
                print("Access denied.")
            else:
                func(*args, **kwargs)
        return wrapper
    return decorator
    
@role_required("admin")
def delete_file(fname):
    print(f"Deleting file: {fname}")

# Test
delete_file("user", "example.txt")  
delete_file("admin", "example.txt")