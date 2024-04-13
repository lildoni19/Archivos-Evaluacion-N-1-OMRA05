aclNum = int(input("Cual es e numero IPv4 ACL? "))

if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPv4 estandar.")
elif aclNum >= 100 and aclNum <= 199:
    print("Este es una ACL IPv4 extendida.")
else:
    print ("ESta ACL IPv4 no es extendida ni estandar.")