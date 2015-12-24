def phrase_is_palindrome( aphrase ):

	 n = len( aphrase )
	 non_alphabetics = string.punctuation + string.digits + string.whitespace
     compressed_phrase = aphrase.encode( 'utf-8' ).translate( None, non_alphabetics )

     return is_palindrome( compressed_phrase )


 