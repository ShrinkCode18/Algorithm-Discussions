<!DOCTYPE html>
<html>
<head>
	<h1>Longest Palindromic Subsequence(LPS)</h1>
</head>
<body>
	<h2>Objective:</h2>
    <p>Finding out the length of the longest palindromic (strings that can be read the same from both the directions) subsequence of a given sequence or string.<br>A subsequence is any sequence obtained by deleting 0 or more characters from the original string.</p>
    <p>Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1].	
    If last and first characters of X are same, then,
    L(0, n-1) = L(1, n-2) + 2.
	Else,
	L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).</p>
	
</body>
</html>