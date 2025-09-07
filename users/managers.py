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
                    identification_type,
                    role,
                    password, 
                    is_superuser=False
                  ):
        """
        Create and save a User with the given email and password.
        """
        if not document_id:
            raise ValueError('The document must be set')
        email = self.normalize_email(email)
        
        if role.id == 1:
            is_superuser = True
     
     
        user = self.model(document_id=document_id, 
                          first_name=first_name, 
                          last_name=last_name, 
                          department=department, 
                          email=email,
                          identification_type=identification_type,
                          role=role,
                          is_superuser=is_superuser
                          )
        user.set_password(str(password))
        user.save()
        return user    
    
    def create_superuser(self, 
                    document_id, 
                    first_name, 
                    last_name, 
                    email,
                    department, 
                    identification_type,
                    role,
                    password, 
                    is_superuser=True
                   ):
        """
        Create and save a SuperUser with the given email and password.
        """
        if role == 2:
            raise ValueError('User is not superuser')
        return self.create_user(document_id, first_name, last_name, email, role,department,identification_type, password, is_superuser=is_superuser)    

