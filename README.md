# keycard_monitor
A python scripts that tells me when there is available keycards for my local gym.

My local gym as is non profit, this means its very cheap and therefore quite popular with limited vacancies for memeberships.
The memberships are added to the websites sporadically but they never anounce the exakt time. Usually there might be a few days notice on fb page. By using this script i didnt have to open the website several times a day to have chance of grabbing one of those keycards. 

NOTE! If you use gmail and want to make notify_user to work, you have to enable access from less secure apps which is not reccomended for a longer period of time since it makes your account more vulnerable. One could probably solve it with two- factor authentication but i have not tried that.

If you happen to live att Lappis in stockholm and wants to get a keycard all you need to do is create a file called congig.py and set the variables EMAIL_ADRESS = "yourEmialAdressHere" and PASSWORD = "yourEmailPasswordHere". If you dont use gmail it should still work but i have not tried. For example by changing 'smtp.gmail.com' to 'smtp.live.com'
