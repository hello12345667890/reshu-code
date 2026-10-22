FB1 = {"APPLE", "BANANA", "MANGO", "APPLE", "KIWI"}
FB2 = {"APPLE", "GRAPE", "PROMOGERNADE", "KIWI", "GRAPE"}




print("BASKET1:", FB1)
print("BASKET2:", FB2)



FB1.add("ORANGE")
print("FRUIT BASKET 1 AFTER ADDING ORANGE:", FB1)



COMMON_FRUITS = FB1.intersection(FB2)
print("Fruits in both baskets:", COMMON_FRUITS)



import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts array:", fruit_counts)



fruit_counts.insert(0,1)
fruit_counts.append(6)
print("Fruit counts after adding items:", fruit_counts)




count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears:", count_of_4)



fruit_counts.reverse()
print("Reversed fruit counts array:", fruit_counts)




print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("Basket 1:", FB1)
print("Basket 2:", FB2)
print("Shared fruits:", COMMON_FRUITS)
print("Fruit counts:", fruit_counts)
print("===========================================")
