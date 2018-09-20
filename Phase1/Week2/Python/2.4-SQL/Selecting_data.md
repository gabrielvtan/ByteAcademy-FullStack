SQL Tutorial - Selecting Data
===============
# Excercise
Below are commands which accomplish the following task from the data table 'empinfo'.

#### 1) Display everyone's first name and their age for everyone that's in table.

```
select first, 
       age 
  from empinfo;
```

#### 2)Display the first name, last name, and city for everyone that's not from Payson.
```
select first, 
       last, 
       city 
  from empinfo
where city <> 
  'Payson';
```

#### 3)Display all columns for everyone that is over 40 years old.

```
select * from empinfo
       where age > 40;
```

### 4) Display the first and last names for everyone whose last name ends in an "ay".

```
select first, last from empinfo
       where last LIKE '%ay';
```

#### 5)Display all columns for everyone whose first name equals "Mary".
```
select * from empinfo
       where first = 'Mary';
```

### 6) Display all columns for everyone whose first name contains "Mary".
```
select * from empinfo
       where first LIKE '%Mary%';
```


