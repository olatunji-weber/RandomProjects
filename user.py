class User:
    def __init__(self, userName, userEmail, password, jobTitle):
        self.name = userName
        self.email = userEmail
        self.password = password
        self.currentJobTitle = jobTitle

    def changePassword(self, newPassword):
        self.password = newPassword

    def changeJobTitle(self, newJobTitle):
        self.currentJobTitle = newJobTitle

    def __str__(self):
        return (f"User {self.name}, currently works as a {self.currentJobTitle}. You can reach {self.name} via {self.email}.")

appUser1 = User("Olayinka", "olatunji.weber@gmail.com", "yk1!", "Cloud Developer")
print(appUser1)