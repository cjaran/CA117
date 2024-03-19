class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self) -> str:
        return '{} {} {}'.format(self.name, self.phone, self.email)
