import sys
import hashlib

BUF_SIZE = 0x10000

def hashFile(name):
    print(f'Hashing: {name}')
    hash = hashlib.sha256()
    with open(name, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            hash.update(data)
            
    with open(name + '.sha256', 'w') as file:
        file.write(hash.hexdigest())
        
def main():
    hashFile('client.jar')
    hashFile('libs.jar')
    hashFile('natives.jar')
    
if __name__ == '__main__':
    main()
