from flask import Flask, request, redirect, url_for
import time

DEBUG = True

app = Flask(__name__)

remember_user = False
users_to_remember = {}
MAX_REMEMBER_TIME = 30
FAILED_LOGIN = "Login Failed, Please Try Again"

users = {
    "Lucky": "GG!",
    "Laksh": "A",
    "2": "B",
    "3": "C",
    "4": "D",
    "5": "E",
    "6": "F",
    "7": "G"
}


class User:
    def __init__(self, username, pwd, ip):
        self.username = username
        self.pwd = pwd
        self.ip = ip


def get_client_ip():
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    print(client_ip)
    return client_ip


def checkLogin(username, pwd):
    for key in users.keys():
        if username == key and pwd == users[key]:
            return redirect(url_for('home'))

    return "Login Failed, Please Try Again"


def check_remember_times():
    current_time = time.time()
    users_to_remove = []
    for user in users_to_remember.keys():
        elapsed_time = current_time - users_to_remember[user]
        if elapsed_time > MAX_REMEMBER_TIME:
            users_to_remove.append(user)

    for user in users_to_remove:
        users_to_remember.pop(user)


def check_remember(username, ip):
    for keys in users_to_remember.keys():
        if keys.username == username and keys.ip == ip:
            return "Welcome %s" % username

    return ""


def add_user_to_remember_list(username, pwd, ip):
    if DEBUG:
        print("Adding Users")

    user = User(username, pwd, ip)
    users_to_remember[user] = time.time()

    if DEBUG:
        print(users_to_remember)


@app.route('/')
def main():
    ret = open('HTML_Files/login.html').read()
    return ret


@app.route('/home')
def home():
    return open('HTML_Files/Home.html').read()


@app.route('/login', methods=['POST'])
def login():
    global remember_user
    current_ip = get_client_ip()

    check_remember_times()

    for key in request.form.keys():
        if key == 'remember_user':
            remember_user = request.form['remember_user']
            if DEBUG:
                print("remember_user = " + remember_user)
    username = request.form['username']
    password = request.form['pass']

    ret_string = check_remember(username, current_ip)
    if ret_string != "":
        return home()

    if remember_user == 'on':
        ret_string = checkLogin(username, password)
        if ret_string == FAILED_LOGIN:
            return ret_string
        new_user = True
        for saved_user in users_to_remember.keys():
            if saved_user.username == username and saved_user.ip == current_ip:
                new_user = False
        if new_user:
            add_user_to_remember_list(username, password, current_ip)
            ret_string = checkLogin(username, password)
    else:
        if DEBUG:
            print("remember_user = off")
        ret_string = checkLogin(username, password)

    return ret_string


if __name__ == '__main__':
    app.run(host="0.0.0.0")
