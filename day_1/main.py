import unittest


class TestFrequencyMethod(unittest.TestCase):

    '''
    def test_first(self):
        self.assertEqual(1, frequency_method('+1'))

    def test_second(self):
        self.assertEqual(2, frequency_method('+2'))

    def test_third(self):
        self.assertEqual(-1, frequency_method('-1'))
'''
    def test_fourth(self):
        self.assertEqual(-1, frequency_method())


def frequency_method():
    current_frequency = 0
    seen_frequencies = [0]
    with open('input', 'r') as input_file:
        while True:
            for frequency_change in input_file:
                current_frequency = current_frequency + int(frequency_change)
                if current_frequency not in seen_frequencies:
                    seen_frequencies.append(current_frequency)
                else:
                    return current_frequency
            input_file.seek(0)


def fast_frequency_method():
    current_frequency = 0
    seen_frequencies = [0]

    with open('input', 'r') as input_file:
        for frequency_change in input_file:
            current_frequency = current_frequency + int(frequency_change)
            if current_frequency not in seen_frequencies:
                seen_frequencies.append(current_frequency)
            else:
                return current_frequency
        total_frequency_sum = current_frequency



        while True:

            new_iteration_frequencies
            seen_frequencies[:] = [frequency_change + total_frequency_sum for frequency_change in seen_frequencies]

            for index, frequency_change in enumerate(seen_frequencies):
                current_frequency = frequency_change + total_frequency_sum
                if current_frequency not in seen_frequencies:
                    seen_frequencies[index] = current_frequency
                else:
                    return current_frequency




if __name__ == '__main__':
    #unittest.main()
    print(fast_frequency_method())
