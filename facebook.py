def open_file():
    ''' Remember the docstring'''
    file_name = input("Please enter a filename").strip()
    while(True):
        try:
            f = open(file_name, "r")
            print("Success")
            return f
        except:
            print("Please enter a valid file name")
            file_name = input ("Please enter a filename").strip()

def read_file(fp):  
    ''' Remember the docstring'''
    # Read n and initizlize the network to have n empty lists -- 
    #    one empty list for each member of the network
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    for line in fp:
        pair = line.strip().split()
        network[int(pair[0])].append(pair[1])
        network[int(pair[1])].append(pair[0])
    # You need to write the code to fill in the network as you read the file
    # Hint: append appropriate values to the appropriate lists.
    # Each iteration of the loop will have two appends -- why?

    return network

def num_in_common_between_lists(list1, list2):
    ''' Remember the docstring'''
    common_friends = 0
    for i in list1:
        if i in list2:
            common_friends += 1
    return common_friends

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Remember the docstring'''
    n = len (network)
    similarity_matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            common_friends = num_in_common_between_lists(network[i],network[j])
            similarity_matrix[i][j] = common_friends
    return similarity_matrix

def recommend(user_id,network,similarity_matrix):
    ''' Remember the docstring'''
    
    
def main():
    # by convention "main" doesn't need a docstring
    file = open_file()
    network = read_file(file)
    similarity_scores = calc_similarity_scores(network)
if __name__ == "__main__":
    main()
