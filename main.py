import itertools
import string
import time
import requests

chars = string.digits

images = []

start_time = time.time()


def guess_id(real, length):
    for guess in itertools.product(chars, repeat=length):
        guess = ''.join(guess)

        print(guess)
        response = requests.get("https://cdn.discordapp.com/attachments/853455468504416266/103310" +
                                guess + "/unknown.png")
        if response.status_code == 200:
            images.append(response.content)

        if guess == real:
            return '\nImage id: {}'.format(guess)

# first_part = "https://cdn.discordapp.com/attachments/853455468504416266/"
real_id = '8071989391471'
id_length = len(real_id)

print(guess_id(real_id, id_length))

print("--- %s seconds ---" % (time.time() - start_time))

print("Images received: ", len(images))
with open('C:/Users/user/Desktop/image.jpg', 'wb') as handler:
    handler.write(images[0])
