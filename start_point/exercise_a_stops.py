stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

# stops.append ("Edinburgh Waverley")
# stops.insert(0, "Glasgow Queen St") 
# stops.insert(4, "Polmont")
print(stops[5])
stops.remove("Livingston")
del (stops[1])
print(len(stops))
stops.sort()
stops.reverse()

for stop in range(len(stops)):
    print(stops)
    

#1. Add "Edinburgh Waverley" to the end of the list                                     DONE
#2. Add "Glasgow Queen St" to the start of the list                                     DONE
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")    DONE
#4. Print out the index position of "Linlithgow" DONE
#5. Remove "Livingston" from the list using its name                                    DONE
#6. Delete "Cumbernauld" from the list by index                                         DONE
#7. Print the number of stops there are in the list                                     DONE
#8. Sort the list alphabetically                                                        DONE
#9. Reverse the positions of the stops in the list                                      DONE
#10 Print out all the stops using a for loop                                            DONE

print(stops)
