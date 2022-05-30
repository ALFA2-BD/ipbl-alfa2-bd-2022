class DictHelper:

    def __init__(self) -> None:
        super().__init__()

    def list_dict_with_id(self, *args, **kwargs):

        if 'list_dict' in kwargs:

            list_dict:list

            list_dict = kwargs['list_dict']
            key_id = 'id' if 'key_id' not in kwargs else kwargs['key_id']
            print(list_dict)

            list_size = len(list_dict)
            start = 1
            end = list_size + 1

            for i in range(start, end):
                list_dict[i][key_id] = i

            return list_dict

        return []
