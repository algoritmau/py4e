# Quiz: Regular Expressions

> TODO: Add options and answers to questions 2 and 4

## Question 1

Which of the following regular expressions would extract `'uct.ac.za'` from
this string using `re.findall`?

```txt
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```

- `@\S+`
- `F.+:`
- `@(\S+)`
- `..@\S+..`

  > Answer: `@(\S+)`

## Question 2

Which of the following is the way we match the "start of a line" in a regular
expression?

## Question 3

What would the following mean in a regular expression? `[a-z0-9]`

- Match a lowercase letter or a digit
- Match anything but a lowercase letter or digit
- Match any number of lowercase letters followed by any number of digits
- Match any text that is surrounded by square braces
- Match an entire line as long as it is lowercase letters or digits

  > Answer: Match a lowercase letter or a digit

## Question 4

What is the type of the return value of the `re.findall()` method?

## Question 5

What is the "wild card" character in a regular expression (i.e., the character
that matches any character)?

- `.`
- `+`
- `$`
- `?`
- `*`
- `^`

  > Answer: `.`

## Question 6

What is the difference between the `+` and `*` characters in regular
expressions?

- The `+` matches at least one character and the `*` matches zero or more characters
- The `+` matches upper case characters and the `*` matches lowercase characters
- The `+` matches the beginning of a line and the `*` matches the end of a line
- The `+` matches the actual plus character and the `*` matches any character
- The `+` indicates "start of extraction" and the `*` indicates the "end of extraction"

  > Answer: The `+` matches at least one character and the `*` matches zero or more characters

## Question 7

What does `[0-9]+` match in a regular expression?

- One or more digits
- Any number of digits at the beginning of a line
- Zero or more digits
- Several digits followed by a plus sign
- Any mathematical expression

  > Answer: One or more digits

## Question 8

What does the following Python sequence print out?

```py
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
```

- `^F.+:`
- `['From: Using the :']`
- `From:`
- `:`
- `['From:']`

  > Answer: `['From: Using the :']`

## Question 9

What character do you add to the `+` or `*` to indicate that the match is
to be done in a non-greedy manner?

- `$`
- `**`
- `?`
- `++`
- `\g`
- `^`

  > Answer: `?`

## Question 10

Given the following line of text:

```txt
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
```

What would the regular expression `\S+?@\S+` match?

- `\@\`
- `stephen.marquard@uct.ac.za`
- `From`
- `marquard@uct`
- `d@uct.ac.za`

  > Answer: `stephen.marquard@utc.ac.za`
