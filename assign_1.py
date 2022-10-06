class Solution:
    def solve(self, list_maps: list):
        word_dict = dict()
        for data in list_maps:
            for key, value in data.items():
                if word_dict.get(value):
                    word_dict[value].append(key)
                    continue
                word_dict[key] = [value]
        print(word_dict)


Solution().solve(
    [
        {"Organization": "Organisation"},
        {"Dg set": "Diesel generator"},
        {"Group": "Organization"},
        {"Orange": "Kinnu"},
        {"naragi": "Orange"},
    ]
)