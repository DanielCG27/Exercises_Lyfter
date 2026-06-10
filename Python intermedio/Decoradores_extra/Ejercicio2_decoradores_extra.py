user_logged_in = True



def requires_login(func):
    def wrapper(*args, **kwargs):

        if not user_logged_in:
            raise PermissionError("User is not authenticated")

        return func(*args, **kwargs)

    return wrapper


@requires_login
def view_profile():
    print("Showing user profile")


view_profile()


user_logged_in = False

try:
    view_profile()
except PermissionError as e:
    print(f"Error: {e}")