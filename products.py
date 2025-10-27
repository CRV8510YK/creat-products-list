# 多項資料輸入

products = []
while True:
	name = input('請輸入產品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入產品價格: ')
	price = int(price)
	p = [name, price]
	products.append(p)
	# products.append([name, price])
print(products)

#列出清單
for p in products:
	print(p[0],'的價格是', p[1])

# 建立.csv資料檔
with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
