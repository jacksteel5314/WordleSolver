'''
Unit testing for roman numerals library
'''
import unittest
import suggestion

def calculate_response(secret_word, guess):
    response = ['b','b','b','b','b']
    for i in range(5):
        c = guess[i]
        if secret_word[i] == c:
            response[i] = 'g'
        else:
            if c in secret_word:
                response[i] = 'y'
    return ''.join(response)

class TestRomanToDecimal(unittest.TestCase):
    '''
    TODO
    '''

    def test_sanity(self):
        '''
        TODO
        '''
        self.assertEqual(len(suggestion.best_guess()), 10)

    # def test_error_cases(self):
    #     '''
    #     TODO
    #     '''
    #     error_cases = ["IXI","VV","IIII","IM","VXV","A","IIA"]
    #     for case in error_cases:
    #         with self.assertRaises(ValueError):
    #             roman_nums.convert(case)

    def test_walkthrough_case(self):
        '''
        TODO
        '''
        guesses_made = []
        hints_offered = []
        responses = []
        secret_word = 'vivid'
        for i in range(5):
            hints = suggestion.best_guess()
            guess = hints[0]
            hints_offered.append(guess)
            guesses_made.append(guess)
            response = calculate_response(secret_word, guess)
            responses.append(response)
            suggestion.suggestions(response, guess)
            print(f'{hints[0]} {response}')



if __name__ == '__main__':
    unittest.main()
