def any_arrows(arrows):
    for arow in arrows:
        if 'damaged' not in arow or arow['damaged'] == False:
            return True
    return False
       
arrows2 = ([{'damaged': True}, {'damaged': True}])
print(any_arrows(arrows2))