def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread = [0] * n
    time = 0
    process = 0

    while process < m:
        for i in range(n):
            if thread[i] == 0 and process < m:
                thread[i] = data[process]
                output.append([i, time])
                process += 1

            if thread[i] > 0:
                thread[i] -= 1

        time += 1

    return output

def main():
    # TODO: create input from keyboard
    f_line = list(map(int,input().split()))
    n = f_line[0]
    m = f_line[1]
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)

    for i,j in result:
        print(i, j)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()