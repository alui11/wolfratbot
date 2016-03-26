import wrbcommands, requests, send

# First define the functions that the commands call

# A simple test function
def hi(SENDER, TEXT):
	send.send('Hi..')

# A more complex command that grabs a random image from imgur
def img(SENDER, TEXT):
	r = requests.get('http://imgur.com/random')
	uid = r.url.split('/')[4]
	im_url = 'http://i.imgur.com/{}.png'.format(uid)
	send.sendImage(im_url)


# Next, define the call names for commands

wrbcommands.COMMANDS['!img'] = img
wrbcommands.COMMANDS['!hi'] = hi
# Repeats are allowed, and act as aliases
wrbcommands.COMMANDS['!hello'] = hi
