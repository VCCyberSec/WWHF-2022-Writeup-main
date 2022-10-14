These are my write-ups for the WWHF 2022 CTF run on the MetaCTF platform.

# What's a CTF?
>In a jeopardy-style CTF (Capture the Flag) competition, teams compete to solve challenges covering a variety of cybersecurity categories and topics. For each challenge, your goal is to find a "flag", which often looks like a *MetaCTF{str1ng_separ4ted_by_und3rscores_like_this}* (this is also the flag for this challenge). There are exceptions.
>You may have to find this flag by analyzing provided materials (a log file, an encrypted message) or breaking into a vulnerable application (an simulated online banking app). You're expected to research and use the internet during the competition to figure out how to solve the challenges.

## Solution
MetaCTF{str1ng_separ4ted_by_und3rscores_like_this}

# Clients Are Always Right!
> We are a company that fully believes that the customer is always right. This is such a core value to our company that we have extended this belief to the clients that access our site! We hope everyone can see how much we care about our clients.
> Have a great day! 

## Solution
Navigating to the hyperlink opens up a username / password prompt

![](https://github.com/VCCyberSec/WWHF-2022-Writeup-main/blob/main/images/Pasted%20image%2020221013082552.png)

Using the Firefox debugger, we can see that the password is stored within the metadata of the client in Base64 encoding.

![](https://github.com/VCCyberSec/WWHF-2022-Writeup-main/blob/main/images/Pasted%20image%2020221013082934.png)

Using Cyberchef, we are able to easily convert the Base64 text back into cleartext revealing the flag.

![](https://github.com/VCCyberSec/WWHF-2022-Writeup-main/blob/main/images/Pasted%20image%2020221013083517.png)

# Corruption
> Oh no! I tried downloading a picture for my upcoming conference talk but it won't open! Can you see if you can fix it and open it? You can download it here: corrupted.png.

## Solution
Downloaded the file "corrupted.png"
Using the *strings* command against the file and reviewing the header, I noticed that the file is a PDF.  I renamed the file to "corrupted.pdf" and the flag was revealed in the PDF file.

## Flag
MetaCTF{0p3rating_$ystems_1ike_ext3nsions}

# Interactive Protection
> You forgot the password to access your online account at a local bank, but you need to transfer some money ASAP and their support isn't responding. Any way you can access it without a password?

## Solution
Link takes you to a webpage with a username / password prompt. 

# Legit Password Generator
> You've found a useful website that generates random passwords. Something seems off, though, about the information it's asking for. Could the owner of this website be up to something nefarious? Maybe there's a way to see what other website they manage? Check it out.

## Solution
Link takes you to a webpage with a username / password prompt. 

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Password Generator</title>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
        <link href="css/styles.css" rel="stylesheet" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="#">Password Generator</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="/">Home</a></li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container">
            <div class="text-center mt-5">
                <h1>Legit Password Generator</h1>
                    <p class="lead">Completely free!<!-- (No ulterior motive)--></p>
            </div>
            <div class="row">
                <div class="col-md-6 offset-md-3 text-center">
                  <form action="javascript:display()">
                      <label for="website" class="form-label">Help us collect data for our security research! What website are you planning to use the password for?</label>
                      <input type="text" class="form-control mb-3" id="website" required>

                      <label for="website" class="form-label">What is your username on that site?</label>
                      <input type="text" class="form-control mb-3" id="username" required>

                      <button type="submit" class="btn btn-secondary mt-2">Generate Secure Password</button>
                  </form>
                </div>
            </div>
            <div class="row mt-4" id="password_section" style="display:none">
                <div class="col-md-6 offset-md-3 text-center">
                  <h4>Your secure password: <code id="password"></code></h4>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js" ></script>
        <script>
            function display() {
              var pwd = generatePassword();
              document.getElementById("password").innerHTML = pwd;
              $.ajax({
                url: "record.json",
                async: false,
                data: {
                  password: pwd,
                  site: $("#website").val(),
                  user: $("#username").val()
                }
              }
            );
            $("#password_section").slideDown();

            }

            function generatePassword() {
                var result           = '';
                var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';
                var charactersLength = characters.length;
                for ( var i = 0; i < 16; i++ ) {
                  result += characters.charAt(Math.floor(Math.random() * charactersLength));
               }
               return result;
            }
        </script>

    </body>
</html>
```

# Middleman
> You managed to get access to a device (indicated in red) on the network shown below. One of the hosts on that network is sending the flag over HTTPS to another host every ~5 seconds. Can you intercept it?
> This environment is somewhat limited. Look through the tools available to you on the machine. The network you connect to is not shared with other participants.
> Connect with ssh 'ctf-eefe14d3d512@44.203.75.158 -p 7000'

![](images\middleman.png)

## Solution
