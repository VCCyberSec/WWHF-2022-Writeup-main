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
!images\Pasted image 20221013082552.png

Using the Firefox debugger, we can see that the password is stored within the metadata of the client in Base64 encoding.

!images\Pasted image 20221013082934.png

Using Cyberchef, we are able to easily convert the Base64 text back into cleartext revealing the flag.

!images\Pasted image 20221013083517.png
