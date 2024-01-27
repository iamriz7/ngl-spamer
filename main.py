try:
    import requests
    import random
    import time
    import string
    import argparse
    from urllib.parse import urlparse
except Exception as e:
	sys.exit("Import modulenya dulu dek")

url = "https://ngl.link/api/submit"

def get_random_user_agent():
    with open('useragent.txt', 'r') as file:
        user_agents = file.read().splitlines()

    random_user_agent = random.choice(user_agents)

    return random_user_agent.strip()

def generate_random_device_id():
    return '-'.join([''.join(random.choices(string.ascii_letters + string.digits, k=4)) for _ in range(4)])

def extract_username_from_url(url):
    path = urlparse(url).path
    username = path.strip("/")
    return username

def send_request(request_count, question, username):
    user_agent = get_random_user_agent()
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "ngl.link",
        "Origin": "https://ngl.link",
        "Referer": "https://ngl.link/",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": user_agent,
        "X-Requested-With": "XMLHt"
    }
    body = {
        "username": username,
        "question": question,
        "deviceId": generate_random_device_id(),
        "gameSlug": "",
        "referrer": "https://ngl.link/"
    }
    proxy_url = "http://gdhulxeh-rotate:4m8ubemwj1ry@p.webshare.io:80"
    proxieJawa = {"http": proxy_url, "https": proxy_url}
    response = requests.post(url, headers=headers, data=body)
    question_id = response.json()["questionId"]
    userRegion_id = response.json()["userRegion"]
    print(f"------------------------------------------------------------------")
    print(f"Request #{request_count}")
    print(f"Username: {username}")
    print(f"Device ID: {generate_random_device_id()}")
    print(f"Question ID: {question_id}")
    print(f"User Region: {userRegion_id}")
    print(f"User Agent: {user_agent}")
    print(f"------------------------------------------------------------------")


def input_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")
        

def input_positive_number(prompt, upper_limit=None):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            if upper_limit is not None and int(value) > upper_limit:
                print("Jumlah pengulangan tidak boleh lebih dari 20")
                pass
            else:
                return int(value)
        elif not value.isdigit():
            print("Masukkan angka positif.")


def input_float_min(prompt, min_value, default_value):
    while True:
        value = input(prompt).strip()
        if not value:
            return default_value
        try:
            float_value = float(value)
            if float_value >= min_value:
                return float_value
            print(f"Value should be at least {min_value}.")
        except ValueError:
            print("Please enter a valid number.")
    

if __name__ == "__main__":
    print("\033[95m"+"===================================================================================================")
    print(f"=  =======  ===      ===  ==============      ===       ======  =====  =====  ==        ==       ==")
    print(f"=   ======  ==   ==   ==  =============  ====  ==  ====  ====    ====   ===   ==  ========  ====  =")
    print(f"=  ==  ===  ==  ========  ==============  =======  ====  ==  ====  ==  == ==  ==  ========  ===   =")
    print(f"=  ===  ==  ==  ========  ================  =====       ===  ====  ==  =====  ==      ====      ===")
    print(f"=  ====  =  ==  ===   ==  ==================  ===  ========        ==  =====  ==  ========  ====  =")
    print(f"=  =====    ==  ====  ==  =============  ====  ==  ========  ====  ==  =====  ==  ========  ====  =")
    print(f"=  ======   ==   ==   ==  =============  ====  ==  ========  ====  ==  =====  ==  ========  ====  =")
    print(f"=  =======  ===      ===        ========      ===  ========  ====  ==  =====  ==        ==  ====  =")
    print(f"===================================================================================================")
    print(f"Note: Mungkin ada beberapa pesan yang tidak akan masuk ke inbox penerima")
    print(f"script: https://github.com/iamriz7/nglSpammer")
    repetitions = 0
    repetitions = input_positive_number("Enter the repetitions:", 20)
    delay = input_float_min("Enter the delay in seconds (minimum 5.5, default 5.5): ", 5.5, 5.5)

    if delay < 5.5:
        print("Delay should be at least 5.5 seconds. Setting delay to 5.5 seconds.")
        delay = 5.5

    user_input = input_non_empty_string("Enter the username/link: ")
    if user_input.startswith("https://ngl.link/"):
        username = extract_username_from_url(user_input)
    else:
        username = user_input
    question = input_non_empty_string("Enter the question: ")

    for count in range(1, repetitions + 1):
        send_request(count, question, username)

        if count % 5 == 0 and count < repetitions:
            print(f"Delaying for {delay} seconds...")
            time.sleep(delay)
