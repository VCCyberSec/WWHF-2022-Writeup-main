These are my write-ups for the WWHF 2022 CTF run on the MetaCTF platform.
Competition was held on
Wed, October 12th 5pm-9pm
Thursday, October 13th 10am-6:30pm
Friday, October 14th 9am-4pm

# What's a CTF?
>In a jeopardy-style CTF (Capture the Flag) competition, teams compete to solve challenges covering a variety of cybersecurity categories and topics. For each challenge, your goal is to find a "flag", which often looks like a *MetaCTF{str1ng_separ4ted_by_und3rscores_like_this}* (this is also the flag for this challenge). There are exceptions.
>You may have to find this flag by analyzing provided materials (a log file, an encrypted message) or breaking into a vulnerable application (an simulated online banking app). You're expected to research and use the internet during the competition to figure out how to solve the challenges.

## Solution
MetaCTF{str1ng_separ4ted_by_und3rscores_like_this}

# Clients Are Always Right!
> We are a company that fully believes that the customer is always right. This is such a core value to our company that we have extended this belief to the clients that access our site! We hope everyone can see how much we care about our clients.
> Have a great day! 

## Solution
Navigating to the hyperlink opens up a username / password prompt. Using the Firefox debugger, we can see that the password is stored within the metadata of the client in Base64 encoding.

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

# Middleman
> You managed to get access to a device (indicated in red) on the network shown below. One of the hosts on that network is sending the flag over HTTPS to another host every ~5 seconds. Can you intercept it?
> This environment is somewhat limited. Look through the tools available to you on the machine. The network you connect to is not shared with other participants.
> Connect with ssh 'ctf-eefe14d3d512@44.203.75.158 -p 7000'

![](images\middleman.png)

## Solution
