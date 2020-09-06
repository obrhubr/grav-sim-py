import lib.Save
def simulate(sigma, totaltime, numofplan, planetlist):
    save1 = lib.Save.Save()
    for i in range(totaltime):
        if i%1000 == 0:
            print(i)
        for j in range (numofplan):
            for k in range(numofplan):
                if j != k:
                    planetlist[j].move(planetlist[k], sigma)
            save1.save(planetlist[j].positionx, planetlist[j].positiony)
        for l in range(numofplan):
            planetlist[l].positionx += (planetlist[l].accelerationx * sigma)
            planetlist[l].positiony += (planetlist[l].accelerationy * sigma)
    
    save1.export(totaltime, numofplan)
    