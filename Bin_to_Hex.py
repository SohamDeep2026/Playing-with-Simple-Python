# This program converts user-inputted binary code into hexadecimal form.
# NOTE: This program has certain bugs to debug.

input_val = input('Enter binary code').split()

for p in input_val:
	num_bin = p
	if len(num_bin) % 4:
		num_bin = '0'*(4 - len(num_bin) % 4) + num_bin

	num_bin_list = []
	for i in range(0, len(num_bin), 4):
		num_bin_list.append(num_bin[i:i+4])

	num_decimal_list = []
	for i in num_bin_list:
		decimal = 0
		for j, k in enumerate(i[::-1]):
			decimal += int(k)*2**j
		num_decimal_list.append(decimal)

	num_hex_list = []
	dec_hex = {
		10: 'A',
		11: 'B',
		12: 'C',
		13: 'D',
		14: 'E',
		15: 'F'
	}
	for i in num_decimal_list:
		if i >= 10:
			num_hex_list.append(dec_hex.get(i))
		else:
			num_hex_list.append(str(i))
	print('The number in hex form is', ''.join(num_hex_list))
