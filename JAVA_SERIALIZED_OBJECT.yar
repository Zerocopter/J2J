rule JAVA_SERIALIZED_OBJECT {
    meta:
		author = "Maarten Boone / Zerocopter"
	strings:
		$header = { AC ED 00 05 73 72 }
		
    condition:
        $header at 0
}