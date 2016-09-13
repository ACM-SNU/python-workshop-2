text = """
Adarniya sabhapati mahodaya, atithi vishesh shikshan mantri shri R D tripati ji, maanyaniya shikshagan aur mere piyaaare sahpatiyo
Aaj agar I.C.E aasmaan ki bulaaandiyo ko chhu raahaa hai to uska shreya sirrf ekinsaan ko jaataahai â€“ Shri Veeru Sahastrabuddhe
Give him a big hand. He is a great guy really.
Peechle buttis saal se inhone nirantar is college mein balatkar pe balatkar kiye. Umeed hai aagey bee karte rahege. Hamein to aashcharya hota hai ki ek insaan apne jeevan kaal mein itni balatkar kaisi kar sakta hai. Inhone kadi tapaasya se apne aapko is kaabil bunaya hai. Waqt ka sahi upyog ghante ka purna istemaal koi inse seeke. Seeke inse seeke. Aaj hum sab chaatra yaha hai, kal desh videsh mein fail jayenge. Waadaa hai aapse jis desh mein honge waha balatkar karenge, I.C.E ka naam roshan karenge. Dika denge sabko jo balatkar Karne ki kshamtaa yaha ke chaatro mein hai wo sansaar ke kisi chaatro mein nahiii. No other chaatra. No other chaatra.
Adarniya mantraji! Namashkar aapne is sansthaan ko wo chees di jiski hamein sakht zaroorat thi. 'Sstunn'! Stunn hota sabi ke paas hai. Sab chupa ke rakte hai, detaa koi nai. Aapne apna stun is balatkari purush ke haat mein diya hai, ab dekiye yeh kaisa iska upyog karta hai
Utthamum dadhdadaath paadam â€“ Madhyam paadam thuchuk chuk â€“ Ghanisthah thud thudi paadam â€“ Surr surri praan gatakam.
"""

def troll(speech, replace_string, replace_with):
	return (speech.replace(replace_string, replace_with))



replace_string = input("enter the string to be replaced:")
replace_with = input("enter the word to replace with: ")

print  (troll(text, replace_string, replace_with))
