dct = {'person': {'in_dict': [1, 2, 3],
                  'after_list': {4, '5'},
                  'after_set': ('hello', )}}

d_v_v = {}
a = {}
d = {}

            
for value in dct.values():
    value['in_dict'] = tuple([1, 2, 3])  
    value['after_list'] = tuple({4, '5'})                        
    lst_key = [i for i in dct.keys()]     
    lst_value = [i for i in value.values()]   
    for key, value in value.items():   
        d_v_v[value] = key
        print(d_v_v)

        a['person'] = d_v_v
        print(a)

        for k in a.values():
            q = a.copy()
            m = dict.fromkeys((1, 2, 3))
            q['in_dict'] =  m 
            l = dict.fromkeys('hello', )
            q['after_set'] = l 
            q['person'] = l
            q['person'] = m
            print(q)
            
        
           
