import hashlib
import pathlib
from pathlib import Path


def hash_line_convert(line, selected_hash):
    if(selected_hash == 0):
        return hashlib.sha1(line.encode("utf-8")).hexdigest()
    elif(selected_hash == 1):
        return hashlib.sha256(line.encode("utf-8")).hexdigest()
    elif(selected_hash == 2):
        return hashlib.sha512(line.encode("utf-8")).hexdigest()
    elif(selected_hash == 3):
        return hashlib.md5(line.encode("utf-8")).hexdigest()
    else:
        raise Exception('Unknown Hash Identifier')


def inputf(filename):
    path = str(pathlib.Path().parent.absolute()) + "/" + filename
    noext_filename = Path(path).resolve().stem
    ext = str(pathlib.Path(filename).suffix)
    return noext_filename, ext


def hash_select():
    return input("""
            Tool for mass converting into a selected hash type:
                0 -\tSHA-1
                1 -\tSHA-256
                2 -\tSHA-512
                3 -\tMD5
                
                Your choice:   """)


def indention_select():
    return input("""
            Choose which indention format:
                0 -\thash
                1 -\trow_id | hash
                2 -\tword | hash
                3 -\trow_id | word | hash
                
                Your choice:   """)


def hash_format(hash_count, selected_indention, line, curr_hash):
    if(selected_indention == 0):
        return "curr_hash\n"
    elif(selected_indention == 1):
        return ("%i - %s\n") % (hash_count, curr_hash)
    elif(selected_indention == 2):
        return ("%s - %s\n") % (line.rstrip(), curr_hash)
    elif(selected_indention == 3):
        return ("%i - %s - %s\n") % (hash_count, line.rstrip(), curr_hash)
    else:
        raise Exception('Unknown Indention Identifier')


def hash_print(noext_filename, filename, selected_hash, ext, selected_indention):
    hash_count = 1
    f_out = open(str(noext_filename) + "-hashed" + ext, 'w')
    with open(filename, 'r') as f_in:
        for line in f_in:
            curr_hash = hash_line_convert(line, selected_hash)
            f_out.write(hash_format(
                hash_count, selected_indention, line, curr_hash))
            # print(hash_format(hash_count,selected_indention, line, curr_hash))             #   REMOVE FOR STDOUT PRINT
            hash_count += 1
    print(str(hash_count) + " have been converted succesfully")
    f_in.close()
    f_out.close()


def main():
    selected_hash = int(hash_select())
    if(not(0 <= selected_hash <= 3)):
        raise Exception('Input Error')
    selected_indention = int(indention_select())
    if(not(0 <= selected_indention <= 3)):
        raise Exception('Input Error')
    filename = input("Type here your file name: ")
    noext_filename, ext = inputf(filename)
    hash_print(noext_filename, filename,
               selected_hash, ext, selected_indention)


if (__name__ == '__main__'):
    main()
