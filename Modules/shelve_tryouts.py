import shelve

phone = shelve.open('phonebook')

phone['Tom'] = ('Tom', '0912-112112', 'Taipei')
phone['John'] = ('John', '0928-888888', 'Taichung')

print(phone['Tom'])
print(phone['John'])

print()

for name in phone: 
    print(phone[name])

phone.close()