import instaloader

bot=instaloader.Instaloader()
username=str(input("Enter the name of the user: "))
print(bot.download_profile(username, profile_pic_only=True))