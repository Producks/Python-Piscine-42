from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

def	main():
    for elem in ft_tqdm(range(333)):
           sleep(0.005)
    for elem in tqdm(range(333)):
           sleep(0.105)



if __name__ == "__main__":
    main()