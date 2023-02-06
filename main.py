from cable_functions import color_pair_to_string, get_color_from_pair_number, get_pair_number_from_color, test_number_to_pair, test_pair_to_number
from cable_reference_manual import print_reference_manual

if __name__ == '__main__':
  print_reference_manual()
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  print('Done :)')
