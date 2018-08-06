import bcrypt
password = "super secret password"
# Hash a password for the first time, with a randomly-generated salt
salt = bcrypt.gensalt()
print("-----salt-------------")
print(salt)
hashed = bcrypt.hashpw(password, salt)
print("-----stored hash------")
print(hashed)
# Check that an unhashed password matches one that has previously been
# hashed192.168.8.187
if bcrypt.checkpw(password, hashed):
     print("It Matches! your password is \""+password+ "\"")
else:
    print("It Does not Match :(")

if bcrypt.checkpw("super Secret password", hashed):
     print("It Matches!")
else:
    print("It Does not Match :(")