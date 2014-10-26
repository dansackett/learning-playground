string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
        sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# string = 'map'

alpha = 'abcdefghijklmnopqrstuvwqyz' * 2
new_string = ''

for index in range(len(string)):
    if alpha.find(string[index].lower()) == -1:
        new_string += string[index]
    else:
        new_string += alpha[alpha.find(string[index].lower()) + 2]

print new_string
