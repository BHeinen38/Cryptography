import subprocess


def des_encrypt(text, key):
    #Use openssl to encrypt the data
    command = "/bin/echo -n " + text + " | openssl enc -a -des-cbc -nosalt -iv 0000000000000000 -K " + key + " -A  | xxd"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.stdout.readlines()

    base64String = ""
    for i in range(len(output)):
        #We must parse the ciphertext out of the outout
        #output[i] = [b'00000000: 3172 3973 5850 6644 5431 4737 7737 4149  1r9sXPfDT1G7w7AI\n']
        line = str(output[i]).split(" ")
        string = str(line[len(line)-1])
        base64String = base64String + string[:-3]
    return base64String
  


def des_decrypt(ciphertext, key):
    #Use openssl to decrypt the data
    command = "/bin/echo -n " + ciphertext + " | openssl enc -d -a -des-cbc -nosalt -iv 0000000000000000 -A -K " + key + " | xxd"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = proc.stdout.readlines()
    
    base64String = ""
    for i in range(len(output)):
        #We must parse the ciphertext out of the outout
        #output[i] = [b'00000000: 3172 3973 5850 6644 5431 4737 7737 4149  1r9sXPfDT1G7w7AI\n']
        line = str(output[i]).split(" ")
        string = str(line[len(line)-1])
        base64String = base64String + string[:-3]
    return base64String



def main():
     
    #TODO: Implement code here
    #You may write additional functions as needed
    knownPlainText = "Tatooine"
    k1 = "319df2f409baee"
    k2 = "64abc398ac4fee"
    ciphertext = "tm97RIBRG3eY8fkb0iU696gHGhfGxnYZGVcB2sJRDK4="
    secretMSG = "eM+KmLs+5TFQEknuRX2fzhigcZPCkSho7bf/73mh8bFaHaCFLW7AoQ=="
    K1Final = ""

    print()
    print("Grab some popcorn because it is going to be a minute...")
    print("It will work I promise :)")

    # k1 = k1 + hex(15)[2::]
    # print(k1)

    print("The algorithm is starting!")

    for i in range(0, 256):
        if(K1Final != ""):
            print(i)
            break

        k1Add = str(hex(i)[2::])
        if(len(k1Add) < 2):
            k1Add = "0" + k1Add

        for j in range(0,256):
            k2Add = str(hex(j)[2::])
            if(len(k2Add) < 2):
                k2Add =  "0" + k2Add

            if(str(des_encrypt(knownPlainText, k1 + k1Add)) == str(des_decrypt(ciphertext, k2 + k2Add))):
                K1Final = k1 + k1Add
                K2Final = k2 + k2Add
                print("key found \n")
                print("Key 1: " + K1Final)
                print("Key 2: " + K2Final)
                break

    print("Begining decrypting your text...")
    print("Step 1:")
    iter1 = str(des_decrypt(secretMSG, K2Final))
    print(iter1)
    print("Step  2")
    iter2 = str(des_decrypt(iter1, K1Final))
    print(iter2)
    print ("Program finished")
            

if __name__ == '__main__':
    main()
