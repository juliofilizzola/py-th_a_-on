user = ("Cássio", "Botaro", 42);

permissions = {"Member", "Group"}

print('Permissions:', permissions);

permissions.add("root");

print('Permissions add:', permissions);

permissions.add("Member");

print('Permissions add itens ja existente:', permissions);

permissions.union({"user"});

print('Permissions union:', permissions.union({user}));

permissions.intersection({"user", "Member"})

print('Permissions intersection:', permissions);

print('Permissions difference:', permissions.difference({user}));
