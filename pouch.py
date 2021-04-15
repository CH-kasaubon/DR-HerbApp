import herb


class Pouch:
    def __init__(self):
        self.herbs = {}

    def add_herbs(self, herbs_to_add):
        for h in herbs_to_add:
            self.add_amount_of_herb(h, 1)

    def add_amount_of_herb(self, herb_to_add, quantity):
        if herb_to_add in self.herbs.keys():
            self.herbs[herb_to_add] = self.herbs[herb_to_add] + quantity
        else:
            self.herbs[herb_to_add] = quantity

    def remove_herbs(self, herbs_to_remove):
        remset = set(herbs_to_remove)
        remdict = {h: herbs_to_remove.count(h) for h in remset}

        for h in remdict.keys():
            if remdict[h] > self.herbs[h]:
                return False

        for h in remdict.keys():
            self.herbs[h] = self.herbs[h] - remdict[h]
            if self.herbs[h] == 0:
                del self.herbs[h]

        return True

    def total_value(self):
        total = 0
        for h in self.herbs:
            total += h.cost * self.herbs[h]
        return total

    def what_can_be_made(self):
        return possible_remedies(self.herbs.keys())

    def get_name_count_list(self):
        return [(h.name, self.herbs[h]) for h in self.herbs.keys()]

    def get_contents_string(self):
        cs = ""
        if len(self.herbs.keys()) == 0:
            cs = "Herb pouch is empty.\n"
        else:
            for h in self.herbs.keys():
                print(f"{h}")
                cs += f"{h.name} ({self.herbs[h]} doses)\n"
        return cs

    def get_suitable_herbs(self, prop):
        return [h for h in self.herbs.keys() if prop in h.prop_set()]

    def write_to_csv_file(self, csv_file):
        with open(csv_file, 'w') as f:
            for h in self.herbs.keys():
                f.write(f"{h.name},{self.herbs[h]}\n")

    def read_from_csv_file(self, csv_file, dh):
        with open(csv_file, 'r') as f:
            for line in f.readlines():
                entry = line.split(',')
                self.herbs[dh.get_herb(entry[0])] = int(entry[1])


def possible_remedies(herb_list):
    herb_prop_list = [h.prop_set() for h in herb_list]
    poss_props = set().union(*herb_prop_list)
    poss_dict = {}

    for p in poss_props:
        count = 0
        for p_list in herb_prop_list:
            if p in p_list:
                count += 1
        poss_dict[p] = count

    return poss_dict
