import params

class Herb:
    def __init__(self, herb_entry):
        self.name = herb_entry['Name']
        self.biome = herb_entry['Biome']
        self.rarity = herb_entry['Rarity']
        self.cost = herb_entry['Cost (copper)']
        diffs = [str(x) for x in range(1, 8)]
        self.prop_dict = {herb_entry[x]: int(x) for x in diffs
                          if isinstance(herb_entry[x], str) and len(herb_entry[x]) > 2}
        self.diff_dict = {self.prop_dict[x]:x for x in self.prop_dict.keys()}

    def __str__(self):
        return f"{self.name}"

    def prop_set(self):
        return set(self.prop_dict.keys())

    def details_text(self):
        dt = f"{self.name}\n"
        dt += f"Found in {self.biome}\n"
        dt += f"Rarity: {self.rarity}\n"
        dt += f"Cost: {self.cost} coppers\n"
        for p in self.prop_dict.keys():
            dt += f"{p} - {self.prop_dict[p]}\n"
        return dt

    def difficulty(self, prop):
        if prop in self.prop_dict:
            return self.prop_dict[prop]
        else:
            return None

    def chance_to_find(self, skill):
        roll_required = self.rarity - params.LEVELS_DICT[skill]
        if roll_required > 4:
            return 0
        elif roll_required < -3:
            return 1
        else:
            return params.FUDGE_PROBS[roll_required]



    def get_info_string(self, name_len, prop_len):
        rarity_len = 8
        cost_len = 6
        fill = ' '
        align = '<'
        info_str = f"{self.name:{fill}{align}{name_len+1}}"
        info_str += f"{self.rarity:{fill}{align}{rarity_len+1}}"
        info_str += f"{self.cost:{fill}{align}{cost_len+1}}"
        for diff in range(1, 8):
            if diff in self.diff_dict.keys():
                info_str += f"{self.diff_dict[diff]:{fill}{align}{prop_len}}"
            else:
                info_str += f"{fill:{fill}{align}{prop_len}}"
        return info_str
