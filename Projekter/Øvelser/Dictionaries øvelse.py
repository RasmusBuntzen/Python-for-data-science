Rasmus = {"firstname":"Rasmus","lastname":"Buntzen","age":"22"}
print(Rasmus)
Rasmus["address"] = "├ůvendingen"
print(Rasmus)
Rasmus["name"] = Rasmus["firstname"]+Rasmus["lastname"]
print(Rasmus)
Rasmus.pop("firstname")
Rasmus.pop("lastname")
print(Rasmus)