#! usr/bin/env python #
# -*- coding: utf-8 -*-

"""
Posical is a Python 3 module that models a generalized calendar reform with regularly-sized weeks and months and an intercalary period, based on August Comte's Positivist Calendar.

Copyright (c) 2014, Z. D. Smith
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import datetime,operator
import calendar

POSIMONTHS = ('Moses', 'Homer', 'Aristotle', 'Archimedes', 'Caesar', 
			  'Saint Paul', 'Charlemagne', 'Dante', 'Gutenberg', 
			  'Shakespeare', 'Descartes', 'Frederick', 'Bichat', 
			  'Complementary')
REGMONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 
			 'October', 'November', 'December', 'Intercalary')

# Ordinal code stolen from stack overflow.
def ordinal(n):
	return "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def horicat(strings):
	lines = ["".join(line) for line in list(zip(*strings))]
	return "\n".join(lines)

def design_calendar():
	"""
	A simple interactive function that asks the user for input in creating a 
	calendar reform. If no input is given it defaults to the settings for
	Comte's Positivist Calendar.
	"""

	d_i_week = int(input("How many days in a week? ") or 7)
	w_i_month = int(input("How many weeks in a month? ") or 4)
	year_1 = int(input("When is year 1? ") or 1789)
	return AlternateCal(w_i_month, d_i_week, year_1)

class AlternateCal(object):
	"""
	A class to generate Alternate Date objects. An AlternateDate object
	Represents a date (day, month, year) in an idealized calendar, extending
	Without disruption in both directions, with the following property: it 
	Consists of n months, all of the same size, with 365 % n epagomenal days 
	At the end of the year that are not days of the week and belong to no month.

	>>> cal = AlternateCal()
	>>> bad_cal = AlternateCal(w_i_month=3, d_i_week=8, year_1=1789)
	>>> cal.from_gregorian(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> cal.from_gregorian(datetime.date(2014, 2, 22))
	positivist date(226, 2, 25)
	>>> print(cal.from_gregorian(2001, 1, 1))
	Monday, 1st of Moses, 213: Prometheus
	>>> print(cal.from_gregorian(2001, 12, 31))
	Festival of All the Dead, 213
	>>> print(cal.from_gregorian(2000, 2, 29))
	Thursday, 4th of Aristotle, 212: Anaxagoras
	>>> print(cal.from_gregorian(2000, 12, 31))
	Festival of Holy Women, 212
	>>> print(cal.from_gregorian(2014, 2, 22).gregorian)
	2014-02-22
	>>> cal.from_gregorian(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> print(cal)
	The Positivist calendar, consisting of 7-day weeks, 4-week months, and 13-month years, with 1 epagomenal day(s).
	>>> print(bad_cal)
	The Antediluvian calendar, consisting of 8-day weeks, 3-week months, and 15-month years, with 5 epagomenal day(s).
	>>> print(bad_cal.from_gregorian(2014, 3, 5))
	8th Weekday, 16th of March, 226: Solon
	>>> next_day = datetime.timedelta(days = 1)
	>>> print(bad_cal.from_gregorian(2011,3,11) + next_day)
	Sunday, 23rd of March, 223: Aristippus
	>>> cal.date(101, 1, 1) + next_day
	positivist date(101, 1, 2)
	>>> cal.date(101, 1, 1) - next_day
	positivist date(100, 14, 2)
	>>> cal.date(100, 1, 1) > cal.from_gregorian(2000, 1, 1)
	False
	>>> cal.date(100, 1, 1) == cal.from_gregorian(2000, 1, 1)
	False
	>>> cal.date(100, 1, 1) < cal.from_gregorian(2000, 1, 1)
	True
	>>> cal.from_gregorian(2000, 1, 1) - cal.from_gregorian(1500, 1, 1)
	datetime.timedelta(182621)
	>>> import datetime
	>>> datetime.date(2000, 1, 1) > cal.today()
	False
	"""
	
	def __init__(calendar, w_i_month=4, d_i_week=7, year_1=1789):
		calendar.days_in_a_month = d_i_week * w_i_month
		calendar.days_in_a_week = d_i_week
		calendar.weeks_in_a_month = w_i_month
		calendar.months_in_a_year = 365 // calendar.days_in_a_month
		calendar.epagomenal_days = 365 % calendar.days_in_a_month
		name_choices = ('New Adjusted', 'Utilitarian', 'Lycurgian', 
						'Multi-Manifold', 'Positivist', 'Crepuscular', 
						'Urquhart', 'Adamantine', 'Organic Non-Repeating', 
						'Antediluvian', 'Re-Corresponding')
		calendar.name = name_choices[hash((w_i_month, d_i_week, year_1)) % 11]
		calendar.year_offset = year_1 - 1
		calendar.MINYEAR = -year_1 + 1
		calendar.MAXYEAR = datetime.MAXYEAR - year_1 - 1
		if calendar.name is 'Positivist':
			calendar.MONTHS = POSIMONTHS
		else:
			calendar.MONTHS = REGMONTHS
		calendar.DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
		calendar.SAINTS = ('Prometheus', 'Hercules', 'Orpheus', 'Ulysses', 
			'Lycurgus', 'Romulus', 'NUMA', 'Belus', 'Sesostris', 'Menu', 
			'Cyrus', 'Zoroaster', 'The Druids', 'BUDDHA', 'Fo-Hi', 'Lao-Tseu',
			'Meng-Tseu', 'Theocrats of Tibet', 'Theocrats of Japan', 
			'Mano-Capac', 'CONFUCIUS', 'Abraham', 'Samuel', 'Solomon', 
			'Isaiah', 'St. John  the Baptist', 'Haroun-al-Raschid', 
			'MUHAMMAD', 'Hesiod', 'Tyrt\u00E6us', 'Anacreon', 'Pindar', 
			'Sophocles', 'Theocritus', '\u00C6SCHYLUS', 'Scopas', 'Zeuxis', 
			'Ictinus', 'Praxiteles', 'Lysippus', 'Apelles', 'PHIDIAS', 
			'\u00C6sop', 'Plautus', 'Terence', 'Phaedrus', 'Juvenal', 
			'Lucian', 'ARISTOPHANES', 'Ennius', 'Lucretius', 'Horace', 
			'Tibullus', 'Ovid', 'Lucan', 'VIRGIL', 'Anaximander', 
			'Anaximenes', 'Heraclitus', 'Anaxagoras', 'Democritus', 
			'Herodotus', 'THALES', 'Solon', 'Xenophanes', 'Empedocles', 
			'Thucydides', 'Archytas', 'Apollonius of Tyana', 'PYTHAGORAS', 
			'Aristippus', 'Antisthenes', 'Zeno', 'Cicero', 'Epictetus', 
			'Tacitus', 'SOCRATES', 'Xenocrates', 'Philo of Alexandria', 
			'St. John the Evangelist', 'St. Justin', 
			'St.Clement of Alexandria', 'Origen', 'PLATO', 'Theophrastus', 
			'Herophilus', 'Erasistratus', 'Celsus', 'Galen', 'Avicenna', 
			'HIPPOCRATES', 'Euclid', 'Aristeus', 'Theodisius of Bithynia', 
			'Hero', 'Pappus', 'Diophantus', 'APOLLONIUS', 'Eudoxus', 
			'Pytheas', 'Aristarchus', 'Eratosthenes', 'Ptolemy', 
			'Albategnius', 'HIPPARCHUS', 'Varro', 'Columella', 'Vitruvius', 
			'Strabo', 'Frontinus', 'Plutarch', 'PLINY THE ELDER', 'Miltiades', 
			'Leonidas', 'Aristides', 'Cimon', 'Xenophon', 'Phocion', 
			'THEMISTOCLES', 'Pericles', 'Philip', 'Demosthenes', 
			'Ptolemy Lagus', 'Philopoemen', 'Polybius', 'ALEXANDER', 
			'Junius Brutus', 'Camillus', 'Fabricius', 'Hannibal', 
			'Paulus Aemilius', 'Marius', 'SCIPIO', 'Augustus', 'Vespasian', 
			'Hadrian', 'Antonius', 'Papinian', 'Alexander Severus', 'TRAJAN', 
			'St. Luke', 'St. Cyprian', ' St.Athanasius', 'St. Jerome', 
			'St. Ambrose', 'St. Monica', ' St.AUGUSTINE', 'Constantine', 
			'Theodosius', 'St. Chrysostom', ' St.Genevieve of Paris', 
			'St. Pulcheria', 'St. Gregory the Great', 'HILDEBRAND', 
			'St. Benedict', 'St. Boniface', 'St. Isidore of Seville', 
			'Lanfranc', 'Heloise', "Architects of Middle Ages", ' St.BERNARD', 
			'St. Francis Xavier', 'St. Charles Borromeo', 'St. Theresa', 
			'St. Vincent de Paul', 'Bourdaloue', 'William Penn', 'BOSSUET', 
			'Theodoric the Great', 'Pelayo', 'Otho the Great', 'St. Henry', 
			'Villers', 'Don John of Austria', 'ALFRED', 'Charles Martel', 
			'The Cid', 'Richard I', 'Joan of Arc', 'Albuquerque', 'Bayard', 
			'GODFREY', 'St. Leo the Great', 'Gerbert', 'Peter the Hermit', 
			'Suger', 'Alexander III', 'St. Francis of Assisi', 'INNOCENT III', 
			'St. Clotilde', 'St. Bathilda', 'St. Stephen of Hungary', 
			'St. Elizabeth of Hungary', 'Blanche of Castille', 
			'St. Ferdinand III', 'ST. LOUIS', 'The Troubadours', 'Boccaccio', 
			'Rabelais', 'Cervantes', 'La Fontain', 'De Foe', 'ARISTO', 
			'Leonardo da Vinci', 'Michael Angelo', 'Holbein', 'Poussin', 
			'Velásquez', 'Teniers', 'RAPHAEL', 'Froissart', 'Camoens', 
			'The Spanish Romancers', 'Chateaubriand', 'Walter Scott', 
			'Manzoni', 'TASSO', 'Petrarca', 'Thomas \u00E0 Kempis', 
			'Mme. de Lafayette', 'F\u00E9n\u00E9lon', 'Klopstock', 'Byron', 
			'MILTON', 'Marco Polo', 'Jacques Coeur', 'Vasco de Gama', 
			'Napier', 'Lacaille', 'Cook', 'COLUMBUS', 'Benvenuto Cellini', 
			'Amontons', 'Harrison', 'Dollond', 'Arkwright', 'Cont\u00e9', 
			'VAUCANSON', 'Stevin', 'Mariotte', 'Papin', 'Black', 'Jouffroy', 
			'Dalton', 'WATT', 'Bernard de Palissy', 'Guglielmini', 
			'Duhamel (du Monceau)', 'Saussure', 'Coulomb', 'Carnot', 
			'MONTGOLFIER', 'Lope de Vega', 'Moreto', 'Rojas', 'Otway', 
			'Lessing', 'Goethe', 'CALDERON', 'Tirso', 'Vondel', 'Racine', 
			'Voltaire', 'Metastasio', 'Schiller', 'CORNEILLE', 'Almarcon', 
			'Mme. de Motteville', 'Mme. de S\u00E9vign\u00E9', 'Lesage', 
			'Mme. de Staal', 'Fielding', 'MOLIERE', 'Pergolese', 'Sacchini', 
			'Gluck', 'Beethoven', 'Rossini', 'Bellini', 'MOZART', 
			'Albertus Magnus', 'Roger Bacon', 'St. Bonaventura', 'Ramus', 
			'Montaigne', 'Campanella', 'ST. THOMAS AQUINAS', 'Hobbes', 
			'Pascal', 'Locke', 'Vauvenargues', 'Diderot', 'Cabanis', 
			'LORD BACON', 'Grotius', 'Fontenelle', 'Vico', 'Fr\u00E9ret', 
			'Montesquieu', 'Buffon', 'LEIBNITZ', 'Robertson', 'Adam Smith', 
			'Kant', 'Condercet', 'Joseph de Maistre', 'Hegel', 'HUME', 
			'Marie de Molina', 'Cosmo de Medici the Elder', 
			'Philippe de Comines', 'Isabella of Castille', 'Charles V', 
			'Henry IV', 'LOUIS XI', "L'H\u0244pital", 'Barneveldt', 
			'Gustavus Adolphus', 'De Witt', 'Ruyter', 'William III', 
			'WILLIAM THE SILENT', 'Ximenes', 'Sully', 'Mazarin', 'Colbert', 
			"D'Aranda", 'Turgot', 'RICHELIEU', 'Sidney', 'Franklin', 
			'Washington', 'Jefferson', 'Bolivar', 'Francia', 'CROMWELL', 
			'Copernicus', 'Kepler', 'Huyghens', 'James Bernouilli', 'Bradley', 
			'Volta', 'GALILEO', 'Vieta', 'Wallis', 'Clairaut', 'Euler', 
			"D'Alembert", 'Lagrange', 'NEWTON', 'Bergmann', 'Priestley', 
			'Cavendish', 'Guyton Morveau', 'Berthollet', 'Berzelius', 
			'LAVOISIER', 'Harvey', 'Bo\u0235rhaave', 'Linn\u0230us', 'Haller', 
			'Lamarck', 'Broussais', 'GALL', 'Festival of All the Dead', 
			'Festival of Holy Women')
		calendar.LEAPSAINTS = ('Cadmus', 'Theseus', 'Tiresias', '', '', '', 
			'', 'Semiramus', '', '', '', '', 'Ossian', '', '', '', '', '', '', 
			'Tamehameha', '', 'Joseph', '', 'David', '', '', 'Abderrahman', 
			'', '', 'Sappho', '', '', 'Euripides', 'Longus', '', '', '', '',
			'', '', '', '', 'Pilpay', '', 'Menander', '', '', '', '', '', '',
			'', '', '', '', '', '', '', '', '', 'Leucippus', '', '', '', '',
			'', '', 'Philolaus', '', '', '', '', '', 'Pliny the Younger',
			'Arrian', '', '', '', '', '', 'St. Irenaeus', '', 'Tertullian',
			'', '', '', '', '', '', 'Averrhoes', '', '', '', '', 'Ctesibius', 
			'', '', '', 'Aratus', 'Nearchus', 'Berosus', 'Sosigenes', '', 
			'Nasir-Eddin', '', '', '', '', '', '', '', '', '', '', '', '', '',
			'Epaminondas', '', '', '', '', '', '', '', '', '', 'Cincinnatus', 
			'Regulus', '', '', 'The Gracchi', '', 'M&#230cenas', 'Titus', 
			'Nerva', 'Marcus Aurelius', 'Ulpian', 'Aetius', '', 'St. James', 
			'', '', '', '', '', '', '', '', 'St. Basil', '', 'Marcian', '', 
			'', 'St. Anthony', 'St. Austin', 'St. Bruno', 'St. Anselm', 
			'Beatrice', 'St. Benezet', '', 'Ignatius Loyola', 
			'Fredrick Borromeo', 'St.Catharine of Siena', 
			"Abb\u00E9 de l'Ep\u00E9e", 'ClaudeFleury', 'George Fox', '', '', 
			'', 'Henry the Fowler', '', 'La Valette', 'John Sobieski', '', '', 
			'Tancred', 'Saladin', 'Marina', 'Sir Walter Raleigh', '', '', 
			'Leo IV', 'PeterDamian', '', 'St. Eligius', 'Becket', 
			'St. Dominic', '', '', 'St. Mathilda of Tuscany', 
			'Mathias Corvinus', '', '', 'Alfonso X', '', '', 'Chaucer', 
			'Swift', '', 'Burns', 'Goldsmith', '', 'Titian', 'Paul Veronese', 
			'Rembrandt', 'Lesueuer', 'Murillo', 'Rubens', '', 'Joinville', 
			'Spenser', '', '', 'James Fenimore Cooper', '', '', '', 
			'L. of Granada & Bunyan', 'Mme. de Sta\u00EBl', 
			'St. Francis of Sales', 'Gessner', '\u00E9. Mercoeur & Shelly', 
			'', 'Chardin', 'Gresham', 'Magellan', 'Briggs', 'Delambre', 
			'Tasman', '', '', 'Wheatstone', 'Pierre Leroy', 'Graham', 
			'Jacquard', '', '', 'Torricelli', 'Boyle', 'Worcester', '', 
			'Fulton', 'Thilorier', '', '', 'Riquet', 'Bourgelat', 'Bouguer', 
			'Borda', 'Vauban', '', 'Montalvan', 'Guillem de Castro', 
			'Guevara', '', '', '', '', '', '', '', '', 'Alfieri', '', '', '', 
			'Mme. Roland', 'Lady Montagu', 'Sterne', 'Miss Edgeworth', 
			'Richardson', '', 'Palestrina', 'Gr\u00E9try', 'Lully', 'Handel', 
			'Weber', 'Donizeti', '', 'John of Salisbury', 'Raymond Lully', 
			'Joachim', 'The Cardinal of Cusa', 'Erasmus', 'Sir Thomas More', 
			'', 'Spinoza', 'Giordano Bruno', 'Malebranche', 'Mme. de Lambert', 
			'Duclos', 'George Leroy', '', 'Cujas', 'Maupertuis', 'Herder', 
			'Winckle-mann', "D'Aguesseau", 'Oken', '', 'Gibbon', 'Dunoyer', 
			'Fichte', 'Ferguson', 'Bonald', 'Sophie Germain', '', '', '', 
			'Guicciardini', '', 'Sixtus V', '', '', '', '', '', '', '', '', 
			'', '', 'Oxenstiern', 'Walpole', 'Louis XIV', 'Pombal', 
			'Campomanes', '', 'Lambert', 'Hampden', 'Kosciusko', 'Madison', 
			"Toussaint L'Ouverture", '', '', 'Tycho Brah\u00E9', 'Halley', 
			'Varignon', 'John Bernouilli', 'R\u00F5mer', 'Sauveur', '', 
			'Harriot', 'Fermat', 'Poinsot', 'Monge', 'Daniel Bernouilli', 
			'Joseph Fourier', '', 'Scheele', 'Davy', '', 'Geoffroy', '', 
			'Ritter', '', 'Charles Bell', 'Stahl & Barthez', 
			'Bernard de Jussieu', "Vicq-d'Azyr", 'Blainville', 'Morgagni', '', 
			'', 'Festival of Holy Women')

		class AlternateDate(object):
			"""
			A date object that's designed to behave analagously to the standard
			library's datetime date objects.

			To begin creating date objects, first create an AlternateCal 
			object. That can then generate objects using the date() or the 
			from_gregorian() methods.
			"""

			def __init__(self, year, month, day, calendar):
				self.year = year
				self.month = month
				self.day = day
				self.day_of_year = (month - 1) * calendar.weeks_in_a_month * calendar.days_in_a_week + day
				self.gregorian = calendar.to_gregorian(self.total_days())
				if self.day_of_year > 366:
					raise ValueError("Date exceeds days in year")
				if self.year < calendar.MINYEAR:
					raise ValueError("Year is earlier than minimum of {}".format(calendar.MINYEAR))
				if self.year == 0:
					raise ValueError("No such thing as year 0. Look it up")
				if self.month < 1 or self.day < 1:
					raise ValueError("Month and Day must be greater than 1")

				self.is_leap = calendar.is_leap(self.gregorian.year)
								
				self.weekday = calendar.get_weekday(self.day)
				self.month_name = calendar.get_month_name(self.month)
				self.day_name = calendar.get_day_name(self.day_of_year, 
													  self.is_leap)
				self.weekday_name = calendar.get_weekday_name(self.weekday)
				
			def total_days(self):
				"""
				Return the total number of days since year 1.
				"""
				offset = calendar.year_offset if self.year > 0 else calendar.year_offset + 1
				year = self.year + offset
				d_o_year = self.day_of_year - 1
				return datetime.date(year, 1, 1).toordinal() + d_o_year

			def replace(self, year=None, month=None, day=None):
				new_year = year or self.year
				new_month = month or self.month
				new_day = day or self.day
				return calendar.date(new_year, new_month, new_day)

			def timetuple(self):
				return self.gregorian.timetuple()

			def toordinal(self):
				return self.gregorian.toordinal()

			def weekday(self):
				"""
				Following the datetime.date weekday() model, returns 0-indexed weekday int
				"""
				return self.weekday - 1

			def isoweekday(self):
				return self.weekday
			
			def isocalendar(self):
				return self.gregorian.isocalendar()

			def isoformat(self):
				return "{}-{}-{}".format(self.year, self.month, self.day)

			def __str__(self):
				if self.month is calendar.months_in_a_year + 1:
					return "{}, {}".format(self.day_name, self.year)
				else:
					return "{}, {} of {}, {}: {}".format(self.weekday_name,
					 					ordinal(self.day), self.month_name, 
												self.year, self.day_name)
				
			def __repr__(self):
				return '%s date(%d, %d, %d)' % (calendar.name.lower(), 
												self.year, self.month, 
												self.day)
			
			def __add__(self, arg):
				return self.calendar.from_gregorian(arg + self.gregorian)
			__radd__ = __add__
			def __sub__(self, arg):
				return self.calendar.from_gregorian(self.gregorian - arg)
			def __rsub__(self, arg):
				return self.calendar.from_gregorian(arg - self.gregorian)
			def __eq__(self, other_date):
				return other_date == self.gregorian
			def __gt__(self, other_date):
				return self.gregorian > other_date
			def __lt__(self, other_date):
				return self.gregorian < other_date
			def __ge__(self, other_date):
				return self.gregorian >= other_date				
			def __le__(self, other_date):
				return self.gregorian <= other_date			
		
		AlternateDate.calendar = calendar		
		calendar.date_class = AlternateDate
		calendar.min = calendar.date(calendar.MINYEAR, 1, 1)
		calendar.max = calendar.from_gregorian(datetime.date.max)

	def from_gregorian(self, *args):
		"""
		Create an alternate date given one of three formats:

		1. Three integers in Gregorian Y, M, D format.
		2. A datetime date object.
		"""
		if not args:
			raise ValueError("No Gregorian date provided")
		try:
			year, month, day = args
			gregorian = datetime.date(year, month, day)
		except ValueError:
			gregorian = args[0]
			if isinstance(gregorian, datetime.timedelta):
				return gregorian
		unadjusted_year = gregorian.year - self.year_offset
		year = unadjusted_year if unadjusted_year > 0 else unadjusted_year - 1
		day_of_year = gregorian.timetuple().tm_yday
		month = ((day_of_year - 1) // self.days_in_a_month) + 1
		day = day_of_year % self.days_in_a_month or self.days_in_a_month
		return self.date_class(year, month, day, self)

	def to_gregorian(self, days):
		return datetime.date.fromordinal(days)

	def date(self, *args):
		"""
		Create an alternate date given a 'native' input: 
		Three integers in Y, M, D format of the alternate calendar.
		"""
		if not args:
			raise ValueError("Please provide values in Y, M, D format")
		year, month, day = args
		return self.date_class(year, month, day, self)
		
	def today(self):
		return self.from_gregorian(datetime.date.today())

	def fromtimestamp(t):
		return self.from_gregorian(datetime.date.fromtimestamp(t))
	
	def fromordinal(o):
		return self.from_gregorian(datetime.date.fromordinal(o))

	def get_weekday(self, day):
		return day % self.days_in_a_week or self.days_in_a_week
	
	def get_weekday_name(self, weekday):
		if weekday > len(self.DAYS):
			return ordinal(weekday) + " Weekday"
		else:
			return self.DAYS[weekday - 1]				
	
	def get_month_name(self, month):
		if month > len(self.MONTHS):
			return ordinal(month) + " Month"
		else:
			return self.MONTHS[(month - 1)]
	
	def get_day_name(self, day, is_leap):
		if day > len(self.SAINTS):
			return ""
		elif is_leap and self.LEAPSAINTS[day - 1]:
			return self.LEAPSAINTS[day - 1]
		else:
			return self.SAINTS[day - 1]
	
	def is_leap(self, year):
		return calendar.isleap(year + self.year_offset)

	def print_month(self, year=None, month=None):
		"""
		Print out a formatted one-page calendar for the specified year/month.
		"""
		page = []
		maxwidth = max(len(saint) for saint in self.SAINTS + self.LEAPSAINTS)
		if not year or not month:
			today = self.date()
			year = today.year
			month = today.month
		if month == self.months_in_a_year + 1:
			intercal = True
			page.append("THE {} EPAGOMENAL DAYS OF THE YEAR {}".format(
													self.name.upper(), year))
		else:
			intercal = False
			page.append("THE {} MONTH OF {}, {}".format(
									self.name.upper(), 
									self.get_month_name(month).upper(), 
									year))
	
		month_offset = (month - 1) * self.weeks_in_a_month * self.days_in_a_week	
		for week in range(self.weeks_in_a_month):		
			calbox = []
			week_offset = (week * self.days_in_a_week)
			for date in range(1 + week_offset, 
							  week_offset + self.days_in_a_week + 1):
				day_of_year = month_offset + date
				if day_of_year > len(self.SAINTS):
					break
				if not intercal:
					weekday = self.get_weekday(date)
					wkd_name = self.get_weekday_name(weekday)
					datestr = str(date)
				else:
					weekday = 0
					wkd_name = ""
					datestr = ""
				saint = self.get_day_name(day_of_year, self.is_leap(year))
				if day_of_year == self.date().day_of_year:
					saint = "*" + saint + "*"
				
				height = 4
				box = []
				cap = "|" if day_of_year % self.days_in_a_week == 0 else ""
				box.append("+".ljust(maxwidth + 1, '-') + cap)
				if wkd_name:
					box.append("|" + wkd_name.ljust(maxwidth - len(datestr)) 
								   + datestr + cap)
				else:
					box.append("|".ljust(maxwidth + 1) + cap)
				for i in range(height):
					box.append("|".ljust(maxwidth + 1) + cap)
				box.append("|" + saint.rjust(maxwidth) + cap)

				calbox.append(box)
			
			cal_layout = horicat(calbox)
			page.append(cal_layout)
		return "\n".join(page)

	def __str__(self):
		return "The {} calendar, consisting of {}-day weeks, {}-week months, and {}-month years, with {} epagomenal day(s).".format(
				self.name, self.days_in_a_week, self.weeks_in_a_month,
				self.months_in_a_year, self.epagomenal_days)



if __name__ == "__main__":	
	import doctest
	doctest.testmod()