def authenticate_user(email, password):
    # Replace with DB / Firebase / Supabase later
    if email == "admin@company.com" and password == "admin123":
        return True
    return False
