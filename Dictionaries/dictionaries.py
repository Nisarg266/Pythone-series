
#! dictionaries Method

dic = {
    'name': "nisarg",
    3: "painapple",
    4: "banana",
    2: "mango",
    5: "apple",  
}
# for value in dic.keys():
#     print(value,dic[value])
#     print(dic[value])

# print(dic.get('name'))

# print(dic['name'])

# print(dic.keys())


#? new  method 

# for key, value in dic.items():
    # print(f"Thme value correponding {key} is {value}")


#! dictionaries to All methods 


#! dictionaries Upage Method 

# user1 = { 1: 20 , 2: 30 , 3: 50}
# user2 = { 4: 29 , 5: 35 , 6: 520}

# user1.update(user2)
# print(user1)


#! dictionaries pop methods



# user1 = { 1: 20 , 2: 30 , 3: 50}
# user2 = { 4: 29 , 5: 35 , 6: 520}

# user1.pop(2)
# print(user1)


#! dictionaries Items method

# my_dict = {"name": "Rahul", "age": 25, "city": "Ahmedabad"}
# print(my_dict.items())


#! dictionaries get() method

# my_dict = {"name": "Rahul", "age": 25, "city": "Ahmedabad"}
# print(my_dict.get("name"))  #?  Output: Rahul
# print(my_dict.get("salary"))  #?  Output: None (Error નથી આવતી)



#! dictionaries popitem() method

# my_dict = {"name": "Rahul", "age": 25, "city": "Ahmedabad"}
# last_item = my_dict.popitem()
# print(last_item)
# print(my_dict)


#! dictionaries clear() method 

# my_dict = {"name": "Rahul", "age": 25, "city": "Ahmedabad"}
# my_dict.clear()
# print(my_dict)


#! dictionaries copy()

# my_dict = {"name": "Rahul", "age": 25, "city": "Ahmedabad"}
# new_dict = my_dict.copy()
# print(new_dict)


#! dictionaries fromkeys(keys ,value)

# keys = ["a", "b", "c"]
# default_value = 0
# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


#! dictionaries setdefault(keys , default)

# my_dict = {"name": "Rahul", "age": 25 ,}
# city = my_dict.setdefault('city' , "surat")
# print(city)
# print(my_dict)




#? 3. Dictionary ના ઉપયોગ (Use Cases)

#? ડેટા સ્ટોર કરવા (JSON જેવું)
#? ઝડપી લુકઅપ (Key થી Value ફાસ્ટ એક્સેસ)
#? કાઉન્ટર તરીકે (જેમ કે શબ્દોની ગણતરી)
#? ઉદાહરણ: શબ્દોની ગણતરી (Word Counter)


text = "hello world hello python world nisarg nisarg    "
words = text.split()

word_count = {}
for word in words :
    word_count[word] = word_count.get(word,0) + 1

print(word_count)



#?    સારાંશ (Summary)
#?    મેથડ	વર્ણન

#*    keys()	સૌ કી ની લિસ્ટ
#*    values()	સૌ વેલ્યુ ની લિસ્ટ
#*    items()	(key, value) પેર્સ
#*    get(key)	વેલ્યુ મેળવો (ન મળે તો None)
#*    update({key: val})	નવી એન્ટ્રીઝ ઉમેરો
#*    pop(key)	કી દ્વારા એન્ટ્રી ડિલીટ કરો
#*    popitem()	છેલ્લી એન્ટ્રી ડિલીટ કરો
#*    clear()	ડિક્શનરી ખાલી કરો
#*    copy()	ડીપ કોપી બનાવો
#*    fromkeys(keys, val)	નવી ડિક્શનરી બનાવો
#*    setdefault(key, val)	જો કી ન હોય તો ડિફોલ્ટ સેટ કરો