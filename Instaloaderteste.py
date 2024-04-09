import instaloader
import csv

insta = instaloader.Instaloader()
profile = instaloader.Profile.from_username(insta.context, 'vinigogh')
print("Número de seguidores: ", profile.followers)
print("Biografia: ", profile.biography)
perfil = profile.get_posts

user = 'iatesterjune'
senha = 'toficandolouco'

insta.login(user, senha)



