###Example###
from hashing_algorythm import hash

hash_start = "$#"
char_str = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ'
hash_length = 128
key1 = 7
key2 = 3

string = input("Plaintext: ")

print(hash(string, key1, key2, char_str, hash_start, hash_length))
