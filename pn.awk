$1 ~ /^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$/ {
  gsub(/[0-9]/, "&-", $1)
  for(i=1; i < 11; i++) {
	split($1, num, "-")
	if (i % 2) {
  	if((num[i] * 2) > 9) {
    	valid += substr((num[i] * 2), 1,1)
    	valid += substr((num[i] * 2), 2,2)
	} else {
    	valid += (num[i] * 2)
  	}
	} else {
    	valid += num[i]
  	}
	}
  if ((valid % 2) == 1) {
	print "Swedish Social security number is NOT valid"
  } else {
        print valid
	print "Swedish Social security number is valid"
  }
}

