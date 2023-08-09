from typing import Optional

from ..files import read_file_in_chunks


class PaddingLen:
	@staticmethod
	def took_from_padding(rem:str,padding_length:int):
		return len(rem) < padding_length:
	
	@staticmethod
	def can_fit_in(packet_size:int):
		# we need 9 for padding
		return packet_size >=9

data
a , rem = (3,3)

if took_padding(rem):
	can fit in len(data) - len(rem)
	a , rem = (3, CRLF)
