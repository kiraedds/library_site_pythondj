from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index( request ):
    html = \
        "<style>" \
        "body {font-family: Arial, Helvetica, sans-serif;}" \
        "form {border: 3px solid #f1f1f1;}" \
        "input[type=text], input[type=password] { width: 100%; padding: 12px 20px; margin: 8px 0;" \
        "display: inline-block; border: 1px solid #ccc; box-sizing: border-box;}" \
        "button { background-color: #4CAF50; color: white; padding: 14px 20px; margin: 8px 0; border: none;" \
        "cursor: pointer; width: 100%; }" \
        "</style>" \
        "<center><h1>Library of Applied Computer Science</h1></center>" \
        "<b>Login</b><br />" \
        "<input type='text' placeholder='Enter Username' name='uname' required><br />" \
        "<b>Password</b><br />" \
        "<input type='password' placeholder='Enter Password' name='psw' required><br />" \
        "<button type='submit'>Login</button>"
    return HttpResponse(html)

