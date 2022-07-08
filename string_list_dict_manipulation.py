import logging
logging.basicConfig(filename="string_op.log", level=logging.INFO, format = "%(levelname)s %(asctime)s %(name)s %(message)s")
class string_manipulation():
    logging.info("constructor method is staring")

    def __init__(self,s):
        self.s = s
        logging.info("constructor method is completed")


    def extract_data(self,a,b,c):
        logging.info("the string entered is--- %s \n", s)
        self.a=  a
        self.b = b
        self.c = c

        try:
            if len(s)==0:
                raise ValueError("string is empty")
                logging.error()
            else:
                logging.info("the string extraction method is started")
                s1= self.s[a:b:c]
                logging.info("the string extraction method is completed")
                return s1
        except Exception as e:
            logging.exception(e)
       #finally: logging.info("data extraction from string is completed")

    def string_reverse(self):
        logging.info("we are in the body of string_reverse method")
        try:
            if len(s)==0:
                raise ValueError("empty string")
                logging.error()
            else:
                logging.info("string_reverse method is started")
                s1= s[-1::-1]
                logging.info("string_reverse method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def split_in_upper(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the split_in_upper method is started ")
                s1 = s.upper()
                s2 = s1.split()
                logging.info(" the split_in_upper method is completed")
                return s2
        except Exception as e:
            logging.exception(e)

    def string_in_lower(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_in_lower method is started ")
                s1 = s.lower()
                logging.info(" the string_in_lower method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_capitalize(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_capitalize method is started ")
                s1 = s.capitalize()
                logging.info(" the string_capitalize method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_expandtab(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_expandtab method is started ")
                s1 = s.expandtabs()
                logging.info(" the string_expandtab method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_strip(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_strip method is started ")
                s1 = s.strip()
                logging.info(" the string_strip method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_lstrip(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_lstrip method is started ")
                s1 = s.lstrip()
                logging.info(" the string_lstrip method is completed")
                return s1
        except Exception as e:
            logging.exception(e)


    def string_rstrip(self):
        logging.info("the entered string is----- %s",s)
        try:
            if len(s) ==0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                logging.info("the string_rstrip method is started ")
                s1 = s.rstrip()
                logging.info(" the string_rstrip method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_replace(self,a,b):
        logging.info("the entered string is----- %s", s)
        try:
            if len(s) == 0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                self.a = a
                self.b = b
                logging.info("the string_replace method is started ")
                s1 = s.replace(a,b)
                logging.info(" the string_replce method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

    def string_center(self,a):
        logging.info("the entered string is----- %s", s)
        try:
            if len(s) == 0:
                raise ValueError("string is empty")
                logging.error("empty string")
            else:
                self.a = a
                logging.info("the string_center method is started ")
                s1 = s.center(a,'@')
                logging.info(" the string_center method is completed")
                return s1
        except Exception as e:
            logging.exception(e)

class list_manipulation():
    logging.info("we are inside list_manipulation class")
    def __init__(self, l):
        self.l = l
        logging.info("list_manipulation constructor is completed")

    def extract_list_entity(self):
        try:
            if bool(l)==False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:


                    logging.info("extract_list_entity method is starting")
                    lists = []
                    for i in l:
                        if type(i) == list:
                            lists.append(i)
                    logging.info("extract_list_entity method is completed")
                    return lists
        except Exception as e:
            logging.exception(e)

    def extract_dict_entity(self):
        try:
            if bool(l)==False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                    logging.info("extract_dict_entity method is starting")
                    dicts=[]
                    for i in l:
                        if type(i) == dict:
                            dicts.append(i)
                    logging.info("extract_dict_entity method is completed")
                    return dicts
        except Exception as e:
            logging.exception(e)

    def extract_tuple_entity(self):
        try:
            if bool(l)==False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                    logging.info("extract_tuple_entity method is starting")
                    tuples = []
                    for i in l:
                        if type(i) == tuple:
                            tuples.append(i)
                    logging.info("extract_tuple_entity method is completed")
                    return tuples
        except Exception as e:
            logging.exception(e)


    def extract_numeric_data(self):
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("extract_numeric_data method is starting")
                numeric_data =[]
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                numeric_data.append(j)
                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int:
                                numeric_data.append(k)
                            if type(v) == int:
                                numeric_data.append(v)
                logging.info("extract_numeric_data method is completed")
                return numeric_data
        except Exception as e:
            logging.exception(e)


    def sum_numeric_data(self):
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("sum_numeric_data method is starting")
                sum =0
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                sum += j
                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int:
                                sum += k
                            if type(v) == int:
                                sum += v
                logging.info("sum_numeric_data method is completed")
                return sum
        except Exception as e:
            logging.exception(e)

    def filter_list(self):
        #  try to filter out all the odd values out all numeric data which is a part of a list
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("filter_list method is starting")
                filter_out=[]
                for i in l:
                    if type(i) == list:
                        for j in i:
                            if (type(j) == int) and (j % 2 == 1):
                                filter_out.append(j)

                logging.info("filter-list method is completed")
                return filter_out
        except Exception as e:
            logging.exception(e)

    def extract_ineuron(self):
          # try to extract "ineuron" out of this data
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("extract_ineuron method is starting")
                filter_out=[]
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == str and j == "ineuron":
                                filter_out.append(j)
                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == str and k == "ineuron":
                                filter_out.append(k)
                            if type(v) == str and v == "ineuron":
                                filter_out.append(v)

                logging.info("extract_ineuron method is completed")
                return filter_out
        except Exception as e:
            logging.exception(e)


    def extract_each_data(self):
          # try to find out a number of occurances of all the data
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("extract_each_data method is starting")
                numbers = []
                strings = []
                # extract all numeric data in the code
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                numbers.append(j)
                            if type(j) == str:
                                strings.append(j)

                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int:
                                numbers.append(k)
                            if type(k) == str:
                                strings.append(k)
                            if type(v) == int:
                                numbers.append(v)
                            if type(v) == str:
                                strings.append(v)
                number_each=[]
                string_each=[]
                total =[]

                for i in set(numbers):
                    number_each.append(("number,", i, ": counts= ", numbers.count(i)))

                for i in set(strings):
                    string_each.append(("string,", i, ": counts= ", strings.count(i)))

                total.append(number_each+string_each)


                logging.info("extract_each_data method is completed")
                return total
        except Exception as e:
            logging.exception(e)

    def exctract_keys(self):
        # q11: try to find out number of keys in dict element
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("extract_keys method is starting")
                s = []
                for i in l:
                    if type(i) == dict:
                        for k in i.items():
                            s.append(k)
                no_of_keys = 0
                for i in s:
                    no_of_keys += 1

                logging.info("extract_keys method is completed")
                return no_of_keys
        except Exception as e:
            logging.exception(e)

    def filter_strings(self):
        #  extract all numeric data in the code
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("filter_string method is starting")
                strings = []
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == str:
                                strings.append(j)

                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == str:
                                strings.append(k)
                            if type(v) == str:
                                strings.append(v)
                logging.info("filter_string method is completed")
                return strings
        except Exception as e:
            logging.exception(e)

    def filter_alphanumeric(self):
        #  try to find out alphanumeric in data
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("filter_alphanumeric method is starting")
                strings = []
                alpha_numeric=[]
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == str:
                                strings.append(j)

                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == str:
                                strings.append(k)
                            if type(v) == str:
                                strings.append(v)
                for i in strings:
                    if i.isalnum() == True:
                        alpha_numeric.append(i)

                logging.info("filter_alphanumeric method is completed")
                return alpha_numeric
        except Exception as e:
            logging.exception(e)

    def mul_numeric(self):
        # try to find out multiplication of all numeric value in the individual collection inside dataset
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("mul_numeric method is starting")
                numbers = []
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                numbers.append(j)

                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int:
                                numbers.append(k)
                            if type(v) == int:
                                numbers.append(v)
                j = 1
                for i in numbers:
                    j = j * i
                logging.info("mul_numeric method is completed")
                return j
        except Exception as e:
            logging.exception(e)


    def extract_flat_list(self):
        # try to unwrape all the collection inside collection and create a flat list
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("flat_list method is starting")
                numbers = []
                strings = []
                for i in l:
                    if type(i) == list or type(i) == tuple or type(i) == dict or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                numbers.append(j)
                            if type(j) == str:
                                strings.append(j)

                    if type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int:
                                numbers.append(k)
                            if type(k) == str:
                                strings.append(k)
                            if type(v) == int:
                                numbers.append(v)
                            if type(v) == str:
                                strings.append(v)
                flat_list = []
                for i in numbers:
                    flat_list.append(i)
                for j in strings:
                    flat_list.append(j)
                logging.info("flat_list method is completed")
                return flat_list
        except Exception as e:
            logging.exception(e)
    def reverse_list(self):
        # Try to reverse a list
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("index_list method is starting")
                reverse_l = l[::-1]

                logging.info("index_list method is completed")
                return reverse_l
        except Exception as e:
            logging.exception(e)

    def index_456_list(self):
        # try to access 456 out of this list
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("index_456_list method is starting")
                desired_element = l[5][1]
                logging.info("index_456_list method is completed")
                return desired_element
        except Exception as e:
            logging.exception(e)

    def extract_list_only(self):
        # try to access 234 out of this list
        try:
            if bool(l) == False:
                raise ValueError("list is empty")
                logging.exception("list is empty")
            else:
                logging.info("reverse_list method is starting")
                lists=[]
                for i in l:
                    if type(i) == list:
                        lists.append(i)
                logging.info("reverse_list method is completed")
                return lists
        except Exception as e:
            logging.exception(e)



s = "this is my first python programming class and i am learning python string and its function"
string_data =string_manipulation(s)
out = string_data.extract_data(1,300,3)
print(out)
out_re= string_data.string_reverse()
print(out_re)
out_split = string_data.split_in_upper()
print(out_split)
out_lower = string_data.string_in_lower()
print(out_lower)
out_capital = string_data.string_capitalize()
print(out_capital)
out_expand = string_data.string_expandtab()
print(out_expand)




s = " shubham "
string_data1 = string_manipulation(s)
out_strip = string_data1.string_strip()
print(out_strip)
out_lstrip = string_data1.string_lstrip()
print(out_lstrip)
out_rstrip = string_data1.string_rstrip()
print(out_rstrip)
out_replace = string_data1.string_replace('h','r')
print(out_replace)
out_center = string_data1.string_center(26)
print(out_center)

l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1':"sudh", "k2":"ineuron", "k3":" Kumar", 3:6, 7:8}, ["ineuron", "data science"]]
list_object= list_manipulation(l)
out_list = list_object.extract_list_entity()
print(out_list)
out_dict =list_object.extract_dict_entity()
print(out_dict)
out_tuple =list_object.extract_tuple_entity()
print(out_tuple)
out_numeric_data = list_object.extract_numeric_data()
print(out_numeric_data)
out_sum_data = list_object.sum_numeric_data()
print(out_sum_data)
out_list_filter = list_object.filter_list()
print(out_list_filter)

out_ineuron = list_object.extract_ineuron()
print(out_ineuron)
out_each_data = list_object.extract_each_data()
print(out_each_data)
out_no_keys = list_object.exctract_keys()
print(out_no_keys)
out_strings = list_object.filter_strings()
print(out_strings)
out_alphanumeric = list_object.filter_alphanumeric()
print(out_alphanumeric)
out_mul = list_object.mul_numeric()
print(out_mul)
out_flat_list = list_object.extract_flat_list()
print(out_flat_list)


l = [3,4,5,6,7,[23, 456, 67, 8,78, 78 ], [345, 56,87,8, 98, 9 ], (234, 6657, 6),{"key1":"subh",234:[23, 45, 656]}]
list_object= list_manipulation(l)
out_reverse=list_object.reverse_list()
print(out_reverse)
out_index = list_object.index_456_list()
print(out_index)
out_list = list_object.extract_list_only()
print(out_list)
