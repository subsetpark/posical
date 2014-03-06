posical
=======

In 1849 the French philosopher August Comte proposed the *Positivist Calendar*, a new and improved solar calendar with 13 months of 28 days each and 1 intercalary day outside of the months (2 on leap years). This numbering system had the pleasant effect of maintaining regularity throughout the months and years; every month has the same number of days, and that number is divisible by 7 (the number of days in a week, you might recall), such that any given day of the month (and year) is always the same day of the week.

In addition to this delightfully rational reworking, Msr. Comte saw fit to assign every day to a saint of his own canon—dedicating every day of the year to a great figure in the history of humanity. The months, too, were renamed according to his humanist lights.

Sadly this calendar was not to be used—until now!

`posical.py` is a python library that helps you create datetime-like objects that obey Comte's positivist system, while converting easily from and to our standard Gregorian calendar, and playing nicely with timedelta objects for date math.

But that's not all! The far-sighted creators of `posical` have seen fit to build it in the form of an all-purpose rationalist calendar engine—so now you too can test your mettle when it comes to calendar design. posical calendars can be created according to your whims. And of course dates from competing calendars can get along just fine.
```
THE POSITIVIST MONTH OF ARISTOTLE
+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------
|Monday                  1|Tuesday                 2|Wednesday               3|Thursday                4|Friday                  5|Saturday                6|Sunday                  7|
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|              Anaximander|               Anaximenes|               Heraclitus|               Anaxagoras|               Democritus|                Herodotus|                   THALES|
+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------
|Monday                  8|Tuesday                 9|Wednesday              10|Thursday               11|Friday                 12|Saturday               13|Sunday                 14|
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                    Solon|               Xenophanes|               Empodocles|               Thucydides|                 Archytas|      Apollonius of Tyana|               PYTHAGORAS|
+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------
|Monday                 15|Tuesday                16|Wednesday              17|Thursday               18|Friday                 19|Saturday               20|Sunday                 21|
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|               Aristippus|              Antisthenes|                     Zeno|                   Cicero|                Epictetus|                  Tacitus|                 SOCRATES|
+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------
|Monday                 22|Tuesday                23|Wednesday              24|Thursday               25|Friday                 26|Saturday               27|Sunday                 28|
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|                         |                         |                         |                         |                         |                         |                         |
|               Xenocrates|      Philo of Alexandria|  St. John the Evangelist|               St. Justin| St.Clement of Alexandria|                   Origen|                    PLATO|
+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------+-------------------------
>>>
```
