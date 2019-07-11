for year in range(2000,2009):
    print ("A. Year %s starts"%(year))
    for month in range(1,13):
        print ("A. Year %s, Month %s"%(year,month))

for year in range(2000,2009):
    print ("B. Year %s starts"%(year))
    for month in ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"):
        print ("B. Year %s, Month %s"%(year,month))