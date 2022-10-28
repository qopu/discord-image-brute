import itertools
import string
import time
import requests

chars = string.digits
images = []
id_length = 19


def run_normal(first_link_part, id_link_part, third_link_part):
    usable_digits = int(input("Enter amount of first digits to use:"))

    start_time = time.time()

    # Link Format: first_link_part + (id_link_part[:usable_digits]) + third_link_part
    brute_id_normal(first_link_part, id_link_part, third_link_part, usable_digits)

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Images found: ", len(images))


def run_debug(first_link_part, id_link_part, third_link_part):
    if not len(id_link_part) == id_length:
        print("Invalid ID!")
        exit()

    digits_to_guess = int(input("Enter amount of digits to guess: "))

    start_time = time.time()

    # Link Format: first_link_part + (id_link_part - digits_to_guess) + third_link_part
    brute_id_debug(first_link_part, id_link_part, third_link_part, digits_to_guess)

    print("--- %s seconds ---" % (time.time() - start_time))
    print("Images found: ", len(images))


def brute_id_normal(first_link_part, id_link_part, third_link_part, usable_digits):
    known_id_part = id_link_part[:usable_digits]
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
    with open('image.jpg', 'wb') as handler:
        handler.write(images[0])
