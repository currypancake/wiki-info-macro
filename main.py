import json

print("is this Non-transactionable card? input y or n")
notrade = input()
print("Input names")
chara_list = input().split(" ")
print("Input card num")
num_list = input().split(" ")
print("Input event name")
event = input()

def default_card() :
	print("Input rarity")
	rare_list = input().split(" ")
	print("Input scout route")
	scout = input().split(" ")

	with open('chara_info.json', encoding='UTF-8') as json_file:
		json_data = json.load(json_file)
		
		f = open("result.txt", "w")
		fscript = open("script.txt", "r")
		fcard = open("card.txt", "r")
	
		script = fscript.read()
		card = fcard.read()
	
		fscript.close()
		fcard.close()
	
		num = 0
		for i in chara_list:
			chara_data = json_data[i]
			if rare_list[num] == "SR":
				cost = "16"
			elif scout[num] == "포인트":
				cost = "8"
			elif rare_list[num] == "R":
				if scout[num] == "가챠":
					cost = "10"
				elif scout[num] == "랭킹":
					cost = "9"

			if scout[num] != "가챠":
				scout[num] = "%s 보상" % scout[num]

			f.write(card.replace("k_name", chara_data["k_name"])
				.replace("j_name", chara_data["j_name"])
				.replace("e_name", chara_data["e_name"])
				.replace("_rare", rare_list[num])
				.replace("_count", num_list[num])
				.replace("cost", cost)
				.replace("specialization", "%s 대 UP" % chara_data["specialization"] if rare_list[num] == "SR" else "%s 중 UP" % chara_data["specialization"])
				.replace("event", "%s 「[[%s]]」 %s" %('기간한정' if scout[num]=='가챠' else '이벤트', event if scout[num]!='가챠' else "%s|가챠명" % event, scout[num])))
			f.write("\n\n")
			f.write(script.replace("k_name", chara_data["k_name"])
				.replace("j_name", chara_data["j_name"])
				.replace("e_name", chara_data["e_name"])
				.replace("_rare", rare_list[num])
				.replace("_count", num_list[num]))
			f.write("\n\n=================\n\n")
			num += 1;
		f.close()

def one_card() :
	with open('chara_info.json', encoding='UTF-8') as json_file:
		json_data = json.load(json_file)

		f = open("result.txt", "w")

		fscript = open("one_script.txt", "r")
		fcard = open("one_card.txt", "r")

		script = fscript.read()
		card = fcard.read()

		fscript.close()
		fcard.close()

		num = 0
		for i in chara_list:
			chara_data = json_data[i]
			f.write(card.replace("k_name", chara_data["k_name"])
				.replace("j_name", chara_data["j_name"])
				.replace("e_name", chara_data["e_name"])
				.replace("_count", num_list[num])
				.replace("specialization", "%s 대 UP" % chara_data["specialization"])
				.replace("event", event))
			f.write("\n\n")
			f.write(script.replace("k_name", chara_data["k_name"])
				.replace("j_name", chara_data["j_name"])
				.replace("e_name", chara_data["e_name"])
				.replace("_count", num_list[num]))
			f.write("\n\n=================\n\n")
			num += 1;
		f.close()

if notrade == "n" :
	default_card();
else :
	one_card();