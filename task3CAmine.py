import csv,fileinput
TheStock,lines,reorderArray=[],[],[]
f = open('StockFile.txt')

csv_f = csv.reader(f,delimiter = ',')
for row in csv_f:
    TheStock.append(row)
print TheStock
i=-1
for i in range(len(TheStock)):
	if int(TheStock[i][3]) < int(TheStock[i][4]):
		stockNeeded = int(TheStock[i][5])- int(TheStock[i][3])
		reorder_line = [str(TheStock[i][0]),"\t", str(stockNeeded),"\n"]
		receipt_line =  str(TheStock[i][0]) +"," +str(TheStock[i][1])+"," +str(TheStock[i][2])+","+ str(TheStock[i][5])+"," + str(TheStock[i][4])+"," + str(TheStock[i][5] )
		del TheStock[i][:]
		reorderArray.append(reorder_line)
		TheStock[i].append(receipt_line)

while True:
	GTINin = raw_input("Please enter GTIN or press enter to quit")
	for i in range(len(TheStock)):
		if GTINin == TheStock[i][0]:
			quantity = raw_input('Please also input your quantity required: ')
			if  str(quantity).isdigit() and int(quantity) > 0 and int(quantity) <= int(TheStock[i][3]):
				newStock = int(TheStock[i][3]) - int(quantity) #new current stock level
				stockNeeded = int(TheStock[i][5])- int(newStock)
				receipt_line =  str(TheStock[i][0]) +"," +str(TheStock[i][1])+"," +str(TheStock[i][2])+","+ str(newStock)+"," + str(TheStock[i][4])+"," + str(TheStock[i][5] )
				if newStock < int(TheStock[i][4]):
					receipt_line =  str(TheStock[i][0]) +"," +str(TheStock[i][1])+"," +str(TheStock[i][2])+","+ str(TheStock[i][5])+"," + str(TheStock[i][4])+"," + str(TheStock[i][5] )
					reorder_line = [str(TheStock[i][0]),"\t", str(stockNeeded),"\n"]
					reorderArray.append(reorder_line)
				del TheStock[i][:]
				TheStock[i].append(receipt_line)
			reorder = raw_input("Do you want to Reorder the stock levels Type yes \n Type no if you want to continue shopping \n or press enter to quit")
			with open("StockFile.txt", 'w') as file_stock: #Write changes to file
					for row in TheStock:
						file_stock.write (",".join(row)+"\n")

			if reorder == "yes":
				print reorderArray
				if len(reorderArray) == 0:
					print "No products need restocking at this time"
					quit()
				else:
					with open("order142.txt","a") as file2:
						for row in reorderArray:
							file2.write("".join(map(str,row)))
					print "A text file in your system, called order.txt, contains the product and the amount which need to be reordered "
					quit()


			elif reorder == "no":
				continue
			elif reorder=="":
				quit()
		elif GTINin == "":
			quit()
	else:
		continue


































