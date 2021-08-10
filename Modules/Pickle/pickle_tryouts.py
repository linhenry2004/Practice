import pickle

game_info = {
    'position_x':'100',
    'position_y':'200',
    'money':300,
    'pocket':['Gold', 'Key', 'Knife']
}

filename = '/Users/henrylin/Python/Modules/Pickle/pickle_tryout.dat'
filename_obj = open(filename, 'wb')
pickle.dump(game_info, filename_obj) #dump() - Serialize 序列化
filename_obj.close()

filename_obj = open(filename, 'rb')
game_info = pickle.load(filename_obj)
filename_obj.close()
print(game_info)