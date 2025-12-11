def loadStock(stockFile):
    '''
    Load data from stock file into data list.
    '''
    data = []
    with open(stockFile) as f:
        for line in f:
            if line.strip() == "": continue
            ls = line.split(',')
            if len(ls) == 3:
                data.append([ls[0].strip(), float(ls[1].strip()), int(ls[2].strip()) ])

    return data



if __name__ == '__main__':
    print(loadStock('stock.txt'))
