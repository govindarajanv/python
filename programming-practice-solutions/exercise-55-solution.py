import pickle

example_dict = {1:"A",2:"B",3:"C"}

#wb stands for bytes

# pickling - serialization

pickle_out = open("dict.pickle","wb")

pickle.dump(example_dict, pickle_out)
pickle_out.close()

# depickling - deserialization

pickle_in = open("dict.pickle","rb")
example_dict = pickle.load(pickle_in)

print (example_dict)
print (example_dict[2])
