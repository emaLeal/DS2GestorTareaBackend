from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where code is the unique identifiers
    for authentication instead of usernames.
    """
    
    def create_user(self, 
                    document_id, 
                    first_name, 
                    last_name, 
                    email,
                    department, 
                    role,
                    password, 
                    is_active=True ):
        """
        Create and save a User with the given email and password.
        """
        if not document_id:
            raise ValueError('The document must be set')
        email = self.normalize_email(email)
        user = self.model(document_id=document_id, 
                          firts_name=first_name, 
                          last_name=last_name, 
                          department=department, 
                          email=email,
                          role=role,
                          is_active=is_active)
        user.set_password(password)
        user.save()
        return user    
    
    def create_superuser(self, 
                    document_id, 
                    first_name, 
                    last_name, 
                    email,
                    department, 
                    role,
                    password, 
                    is_active=True ):
        """
        Create and save a SuperUser with the given email and password.
        """
        is_active.set_default('True')    

        if role == 2:
            raise ValueError('User is not superuser')
        return self.create_user(document_id, first_name, last_name, email, role,department, password,  is_active=is_active )    

