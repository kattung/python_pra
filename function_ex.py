#!/usr/bin/python

g_variable = 0
dict_test = {}
test_list = list()

def test_add_list(item):
        test_list.append(item)

def test_add_dict(name, value):
        dict_test.update({name: value})

def modify_g_correct():
        print "This is the correct method"
        global g_variable
        g_variable = 123

def modify_g():
        print "try to modify golbal variable, but fail"
        g_variable = 123

def print_string(number, string):
        print string
        number += 10
        return number

def main():
        num = print_string(1, "aaaa")
        print "function_ex.py", num

        print g_variable
        modify_g()
        print g_variable
        modify_g_correct()
        print g_variable

        print "if it's dictionary, there's no need to use globla to assign in function"
        test_add_dict('aaa', 3)
        test_add_dict('bbb', 11)
        print dict_test

        print "if it's list, there's no need to use globla to assign in function"
        test_add_list('aaa')
        test_add_list('bbb')
        print test_list

if __name__ == "__main__":
        main()
