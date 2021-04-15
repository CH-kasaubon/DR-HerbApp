import pandas
import herb
import params


def fudge_dice_chance(skill, target):
    roll_required = target - params.LEVELS_DICT[skill]
    if roll_required > 4:
        return 0
    elif roll_required < -3:
        return 1
    else:
        return float(params.FUDGE_PROBS[roll_required])


def value(herbs):
    return sum([h.cost for h in herbs])


def sort_herb_list_by_criteria(hlist_in, criteria, prop='Any'):
    if criteria == 'Name':
        hlist_out = sorted(hlist_in, key=lambda h: h.name)
    elif criteria == 'Rarity':
        hlist_out = sorted(hlist_in, key=lambda h: h.rarity)
    elif criteria == 'Cost':
        hlist_out = sorted(hlist_in, key=lambda h: h.cost)
    elif criteria == 'Difficulty':
        if prop == 'Any':
            hlist_out = hlist_in
        else:
            hlist_out = sorted(hlist_in, key=lambda h: h.prop_dict[prop])
    else:
        hlist_out = hlist_in

    return hlist_out


class DataHandler:
    def __init__(self, fname):
        df = pandas.read_csv(fname)
        idict = df.to_dict('index')
        self.herb_dict = {idict[k]['Name']: idict[k] for k in idict.keys()}
        self.herbs = [herb.Herb(self.herb_dict[h]) for h in self.herb_dict.keys()]
        self.biomes = set(df['Biome'].to_list())
        prop_set = set()
        cols = [str(x) for x in range(1, 8)]
        for i in cols:
            prop_set.update(set(df[i].to_list()))
        self.properties = sorted([x for x in prop_set if isinstance(x, str) and len(x) > 2])

        self.biome_opt_dict = {b: self.herb_names_by_biome(b) for b in self.biomes}
        self.max_len_herb_name = self.calc_max_len_herb_name()
        self.max_len_prop_name = self.calc_max_len_prop_name()

    def herbs_by_biome(self, biome):
        return [h for h in self.herbs if h.biome == biome]

    def herb_names_by_biome(self, biome):
        return [h.name for h in self.herbs_by_biome(biome)]

    def herbs_by_property(self, prop):
        return [h for h in self.herbs if prop in h.prop_set()]

    def get_herb(self, name):
        hfound = [h for h in self.herbs if name == h.name]
        if len(hfound) > 0:
            return hfound[0]
        else:
            print(f"{name} not found")

    def search_for_name(self, search_str):
        hfound = [h for h in self.herbs if h.name.find(search_str) != -1]
        return hfound

    def calc_max_len_herb_name(self):
        max_len = 0
        for h in self.herbs:
            if len(h.name) > max_len:
                max_len = len(h.name)
        return max_len + 1

    def calc_max_len_prop_name(self):
        max_len = 0
        for p in self.properties:
            if len(p) > max_len:
                max_len = len(p)
        return max_len + 1

    def build_herb_info_table(self, hlist):
        rarity_len = 8
        cost_len = 6
        fill = ' '
        align = '<'
        header = "Herb Name".ljust(self.max_len_herb_name + 1) + "Rarity".ljust(rarity_len + 1) \
                 + "Cost".ljust(cost_len + 1)
        for diff in range(1, 8):
            header += f"{diff}".center(self.max_len_prop_name)
        header += "\n"

        herb_table = ""
        for h in hlist:
            herb_table += h.get_info_string(self.max_len_herb_name, self.max_len_prop_name) + "\n"

        return header + herb_table
