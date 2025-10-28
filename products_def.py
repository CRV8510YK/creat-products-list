import os # 載入 operation system

def read_file(filename):
	products = []
	with open(filename, 'r') as f:  #讀取檔案
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products


# 多項資料輸入
def user_input(products):
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
	return products

#列出清單
def print_products(products):
	for p in products:
		print(p[0],'的價格是', p[1])

# 寫入檔案建立.csv資料檔
def write_file(filename, products):
    with open(filename, 'w') as f:
	    f.write('商品,價格\n')
	    for p in products:
		    f.write(p[0] + ',' + str(p[1]) + '\n')
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  #檢查檔案是否存在
		print('OK! 找到檔案!')
		products = read_file(filename)
	else:
		print('找不到檔案')
		
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()	