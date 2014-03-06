#! usr/bin/env python #
# -*- coding: utf-8 -*-

import datetime, calendar

POSIMONTHS = ('Moses', 'Homer', 'Aristotle', 'Archimedes', 'Caesar', 'Saint Paul', 'Charlemagne', 'Dante', 'Gutenberg', 'Shakespeare', 'Descartes', 'Frederick', 'Bichat', 'Complementary')
REGMONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'October', 'November', 'December', 'Intercalary')

# Ordinal code stolen from stack overflow.
def ordinal(n):
	return "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])

def design_calendar():
	"""
	Reference math from Calca:
	days = 365
	d_i_week = 7
	w_i_month = 4
	m_i_year = round(365 / (d_i_week * w_i_month)) => 13

	ic_days = days - (d_i_week * w_i_month * m_i_year) => 1
	"""

	d_i_week = int(input("How many days in a week? ") or 7)
	w_i_month = int(input("How many weeks in a month? ") or 4)
	year_1 = int(input("When is year 1? ") or 1788)
	return AlternateCal(w_i_month, d_i_week, year_1)

class AlternateCal(object):
	"""
	>>> cal = AlternateCal()
	>>> bad_cal = AlternateCal(w_i_month=3, d_i_week=8, year_1=1788)
	>>> cal.from_date(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> cal.from_date(datetime.date(2014, 2, 22))
	positivist date(226, 2, 25)
	>>> print(cal.from_date(2001, 1, 1))
	Monday, 1st of Moses, 213: Prometheus
	>>> print(cal.from_date(2001, 5, 10))
	Thursday, 18th of Caesar, 213: Hannibal
	>>> print(cal.from_date(2001, 12, 31))
	Festival of All the Dead, 213
	>>> print(cal.from_date(2000, 2, 29))
	Thursday, 4th of Aristotle, 212: Anaxagoras
	>>> print(cal.from_date(2000, 12, 31))
	Festival of Holy Women, 212
	>>> print(cal.from_date(2014, 2, 22).to_gregorian())
	2014-02-22
	>>> class New_cal(AlternateCal):
	...  days_in_a_month = 26
	>>> cal2 = New_cal()
	>>> cal.from_date(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> print(cal)
	The Positivist calendar, consisting of 7-day weeks, 4-week months, and 13-month years, with 1 intercalary day(s).
	>>> print(bad_cal)
	The Crepuscular calendar, consisting of 8-day weeks, 3-week months, and 15-month years, with 5 intercalary day(s).
	>>> print(bad_cal.from_date(2014, 3, 5))
	8th Day, 16th of March, 226: Solon
	>>> next_day = datetime.timedelta(days = 1)
	>>> print(bad_cal.from_date(2011,3,11) + next_day)
	Sunday, 23rd of March, 223: Aristippus
	"""
	
	def __init__(calendar, w_i_month=4, d_i_week=7, year_1=1788):
		calendar.days_in_a_month = d_i_week * w_i_month
		calendar.days_in_a_week = d_i_week
		calendar.weeks_in_a_month = w_i_month
		calendar.months_in_a_year = 365 // calendar.days_in_a_month
		calendar.intercalary_days = 365 % calendar.days_in_a_month
		name_choices = ('New Adjusted', 'Utilitarian', 'Lycurgian', 'Multi-Manifold', 'Crepuscular', 'Urquhart', 'Adamantine', 'Organic Non-Repeating', 'Antediluvian', 'Re-Corresponding', 'Positivist')
		calendar.name = name_choices[hash((w_i_month, d_i_week, year_1)) % 11]
		calendar.year_offset = year_1
		if calendar.name is 'Positivist':
			calendar.MONTHS = POSIMONTHS
		else:
			calendar.MONTHS = REGMONTHS
		calendar.DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
		calendar.SAINTS = ('Prometheus', 'Hercules', 'Orpheus', 'Ulysses', 'Lycurgus', 'Romulus', 'NUMA', 'Belus', 'Sesostris', 'Menu', 'Cyrus', 'Zoroaster', 'The Druids', 'BUDDHA', 'Fo-Hi', 'Lao-Tseu', 'Meng-Tseu', 'Theocrats of Tibet', 'Theocrats of Japan', 'Mano-Capac', 'CONFUCIUS', 'Abraham', 'Samuel', 'Solomon', 'Isaiah', 'St. John  the Baptist', 'Haroun-al-Raschid', 'MUHAMMAD', 'Hesiod', 'Tyrt\u00E6us', 'Anacreon', 'Pindar', 'Sophocles', 'Theocritus', '\u00C6SCHYLUS', 'Scopas', 'Zeuxis', 'Ictinus', 'Praxiteles', 'Lysippus', 'Apelles', 'PHIDIAS', '\u00C6sop', 'Plautus', 'Terence', 'Phaedrus', 'Juvenal', 'Lucian', 'ARISTOPHANES', 'Ennius', 'Lucretius', 'Horace', 'Tibullus', 'Ovid', 'Lucan', 'VIRGIL', 'Anaximander', 'Anaximenes', 'Heraclitus', 'Anaxagoras', 'Democritus', 'Herodotus', 'THALES', 'Solon', 'Xenophanes', 'Empodocles', 'Thucydides', 'Archytas', 'Apollonius of Tyana', 'PYTHAGORAS', 'Aristippus', 'Antisthenes', 'Zeno', 'Cicero', 'Epictetus', 'Tacitus', 'SOCRATES', 'Xenocrates', 'Philo of Alexandria', 'St. John the Evangelist', 'St. Justin', ' St.Clement of Alexandria', 'Origen', 'PLATO', 'Theophrastus', 'Herophilus', 'Erasistratus', 'Celsus', 'Galen', 'Avicenna', 'HIPPOCRATES', 'Euclid', 'Arist\u0230us', 'Theodisius of Bithynia', 'Hero', 'Pappus', 'Diophantus', 'APOLLONIUS', 'Eudoxus', 'Pytheas', 'Aristarchus', 'Eratosthenes', 'Ptolemy', 'Albategnius', 'HIPPARCHUS', 'Varro', 'Columella', 'Vitruvius', 'Strabo', 'Frontinus', 'Plutarch', 'PLINY THE ELDER', 'Miltiades', 'Leonidas', 'Aristides', 'Cimon', 'Xenophon', 'Phocion', 'THEMISTOCLES', 'Pericles', 'Philip', 'Demos- thenes', 'Ptolemy Lagus', 'Philopoemen', 'Polybius', 'ALEXANDER', 'Junius Brutus', 'Camillus', 'Fabricius', 'Hannibal', 'Paulus Aemilius', 'Marius', 'SCIPIO', 'Augustus', 'Vespasian', 'Hadrian', 'Antonius', 'Papinian', 'Alexander Severus', 'TRAJAN', 'St. Luke', 'St. Cyprian', ' St.Athanasius', 'St. Jerome', 'St. Ambrose', 'St. Monica', ' St.AUGUSTINE', 'Constantine', 'Theodosius', 'St. Chrysostom', ' St.Genevieve of Paris', 'St. Pulcheria', 'St. Gregory the Great', 'HILDEBRAND', 'St. Benedict', 'St. Boniface', 'St. Isidore of Seville', 'Lanfranc', 'Heloise', "Arch'ts of Middle Ages", ' St.BERNARD', 'St. Francis Xavier', 'St. Charles Borromeo', 'St. Theresa', 'St. Vincent de Paul', 'Bourdaloue', 'William Penn', 'BOSSUET', 'Theodoric the Great', 'Pelayo', 'Otho the Great', 'St. Henry', 'Villers', 'Don John of Austria', 'ALFRED', 'Charles Martel', 'The Cid', 'Richard I', 'Joan of Arc', 'Albuquerque', 'Bayard', 'GODFREY', 'St. Leo the Great', 'Gerbert', 'Peter the Hermit', 'Suger', 'Alexander III', 'St. Francis of Assisi', 'INNOCENT III', 'St. Clotilde', 'St. Bathilda', 'St. Stephen of Hungary', 'St. Elizabeth of Hungary', 'Blanche of Castille', 'St. Ferdinand III', 'ST. LOUIS', 'The Troubadours', 'Boccaccio', 'Rabelais', 'Cervantes', 'La Fontain', 'De Foe', 'ARISTO', 'Leonardo da Vinci', 'Michael Angelo', 'Holbein', 'Poussin', 'Velásquez', 'Teniers', 'RAPHAEL', 'Froissart', 'Camoens', 'The Spanish Romancers', 'Chateaubriand', 'Walter Scott', 'Manzoni', 'TASSO', 'Petrarca', 'Thomas &agrave Kempis', 'Mme. de Lafayette', 'F\u00E9n\u00E9lon', 'Klopstock', 'Byron', 'MILTON', 'Marco Polo', 'Jacques Coeur', 'Vasco de Gama', 'Napier', 'Lacaille', 'Cook', 'COLUMBUS', 'Benvenuto Cellini', 'Amontons', 'Harrison', 'Dollond', 'Arkwright', 'Cont\u00e9', 'VAUCANSON', 'Stevin', 'Mariotte', 'Papin', 'Black', 'Jouffroy', 'Dalton', 'WATT', 'Bernard de Palissy', 'Guglielmini', 'Duhamel (du Monceau)', 'Saussure', 'Coulomb', 'Carnot', 'MONTGOLFIER', 'Lope de Vega', 'Moreto', 'Rojas', 'Otway', 'Lessing', 'Goethe', 'CALDERON', 'Tirso', 'Vondel', 'Racine', 'Voltaire', 'Metastasio', 'Schiller', 'CORNEILLE', 'Almarcon', 'Mme. de Motteville', 'Mme. de S\u00E9vign\u00E9', 'Lesage', 'Mme. de Staal', 'Fielding', 'MOLIERE', 'Pergolese', 'Sacchini', 'Gluck', 'Beethoven', 'Rossini', 'Bellini', 'MOZART', 'Albertus Magnus', 'Roger Bacon', 'St. Bonaven- tura', 'Ramus', 'Montaigne', 'Campanella', 'ST. THOMAS AQUINAS', 'Hobbes', 'Pascal', 'Locke', 'Vauvenargues', 'Diderot', 'Cabanis', 'LORD BACON', 'Grotius', 'Fontenelle', 'Vico', 'Fr\u00E9ret', 'Montesquieu', 'Buffon', 'LEIBNITZ', 'Robertson', 'Adam Smith', 'Kant', 'Condercet', 'Joseph de Maistre', 'Hegel', 'HUME', 'Marie de Molina', 'Cosmo de Medici the Elder', 'Philippe de Comines', 'Isabella of Castille', 'Charles V', 'Henry IV', 'LOUIS XI', "L'H\u0244pital", 'Barneveldt', 'Gustavus Adolphus', 'De Witt', 'Ruyter', 'William III', 'WILLIAM THE SILENT', 'Ximenes', 'Sully', 'Mazarin', 'Colbert', "D'Aranda", 'Turgot', 'RICHELIEU', 'Sidney', 'Franklin', 'Washington', 'Jefferson', 'Bolivar', 'Francia', 'CROMWELL', 'Copernicus', 'Kepler', 'Huyghens', 'James Bernouilli', 'Bradley', 'Volta', 'GALILEO', 'Vieta', 'Wallis', 'Clairaut', 'Euler', "D'Alembert", 'Lagrange', 'NEWTON', 'Bergmann', 'Priestley', 'Cavendish', 'Guyton Morveau', 'Berthollet', 'Berzelius', 'LAVOISIER', 'Harvey', 'Bo\u0235rhaave', 'Linn\u0230us', 'Haller', 'Lamarck', 'Broussais', 'GALL', 'Festival of All the Dead', 'Festival of Holy Women')
		calendar.LEAPSAINTS = ('Cadmus', 'Theseus', 'Tiresias', '', '', '', '', 'Semiramus', '', '', '', '', 'Ossian', '', '', '', '', '', '', 'Tameha-meha', '', 'Joseph', '', 'David', '', '', 'Abderrah-man', '', '', 'Sappho', '', '', 'Euripides', 'Longus', '', '', '', '', '', '', '', '', 'Pilpay', '', 'Menander', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Leucippus', '', '', '', '', '', '', 'Philolaus', '', '', '', '', '', 'Pliny the Younger', 'Arrian', '', '', '', '', '', 'St. Iren&#230us', '', 'Tertullian', '', '', '', '', '', '', 'Averrhoes', '', '', '', '', 'Ctesibius', '', '', '', 'Aratus', 'Nearchus', 'Berosus', 'Sosigenes', '', 'Nasir-Eddin', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Epaminon-das', '', '', '', '', '', '', '', '', '', 'Cincinnatus', 'Regulus', '', '', 'The Gracchi', '', 'M&#230cenas', 'Titus', 'Nerva', 'Marcus Aurelius', 'Ulpian', 'Aetius', '', 'St. James', '', '', '', '', '', '', '', '', 'St. Basil', '', 'Marcian', '', '', 'St. Anthony', 'St. Austin', 'St. Bruno', 'St. Anselm', 'Beatrice', 'St. Benezet', '', 'Ignatius Loyola', 'Fredrick Borromeo', 'St.Catharineof Siena', "Abb\u00E9 de l'Ep\u00E9e", 'ClaudeFleury', 'George Fox', '', '', '', 'Henry the Fowler', '', 'La Valette', 'JohnSobieski', '', '', 'Tancred', 'Saladin', 'Marina', 'Sir Walter Raleigh', '', '', 'Leo IV', 'PeterDamian', '', 'St. Eligius', 'Becket', 'St. Dominic', '', '', 'St. Mathilda of Tuscany', 'Mathias Corvinus', '', '', 'Alfonso X', '', '', 'Chaucer', 'Swift', '', 'Burns', 'Goldsmith', '', 'Titian', 'Paul Veronese', 'Rembrandt', 'Lesueuer', 'Murillo', 'Rubens', '', 'Joinville', 'Spenser', '', '', 'James Fenimore Cooper', '', '', '', 'L. of Grana-da & Bunyan', 'Mme. de Sta\u00EBl', 'St. Francisof Sales', 'Gessner', '\u00E9. Mercoeur & Shelly', '', 'Chardin', 'Gresham', 'Magellan', 'Briggs', 'Delambre', 'Tasman', '', '', 'Wheatstone', 'Pierre Leroy', 'Graham', 'Jacquard', '', '', 'Torricelli', 'Boyle', 'Worcester', '', 'Fulton', 'Thilorier', '', '', 'Riquet', 'Bourgelat', 'Bouguer', 'Borda', 'Vauban', '', 'Montalvan', 'Guillem de Castro', 'Guevara', '', '', '', '', '', '', '', '', 'Alfieri', '', '', '', 'Mme. Roland', 'Lady Montagu', 'Sterne', 'Miss Edgeworth', 'Richardson', '', 'Palestrina', 'Gr\u00E9try', 'Lully', 'Handel', 'Weber', 'Donizeti', '', 'John of Salisbury', 'Raymond Lully', 'Joachim', 'The Cardinal of Cusa', 'Erasmus', 'Sir Thomas More', '', 'Spinoza', 'Giordano Bruno', 'Male-branche', 'Mme. de Lambert', 'Duclos', 'GeorgeLeroy', '', 'Cujas', 'Maupertuis', 'Herder', 'Winckle-mann', "D'Aguesseau", 'Oken', '', 'Gibbon', 'Dunoyer', 'Fichte', 'Ferguson', 'Bonald', 'Sophie Germain', '', '', '', 'Guicciardini', '', 'Sixtus V', '', '', '', '', '', '', '', '', '', '', 'Oxenstiern', 'Walpole', 'Louis XIV', 'Pombal', 'Campo-manes', '', 'Lambert', 'Hampden', 'Kosciusko', 'Madison', "Toussaint L'Ouverture", '', '', 'Tycho Brah\u00E9', 'Halley', 'Varignon', 'John Bernouilli', 'R\u00F5mer', 'Sauveur', '', 'Harriot', 'Fermat', 'Poinsot', 'Monge', 'Daniel Bernouilli', 'Joseph Fourier', '', 'Scheele', 'Davy', '', 'Geoffroy', '', 'Ritter', '', 'Charles Bell', 'Stahl & Barthez', 'Bernard de Jussieu', "Vicq-d'Azyr", 'Blainville', 'Morgagni', '', '', 'Festival of Holy Women')



		class AlternateDate(object):
			def __init__(self, year, month, day, calendar):
				self.year = year
				self.month = month
				self.day = day
				self.day_of_year = (month - 1) * calendar.weeks_in_a_month * calendar.days_in_a_week + day
				if self.day_of_year > 366:
					raise ValueError("This day cannot exist.")

				self.calendar = calendar
				self.is_leap = calendar.is_leap(self.to_gregorian().year)
								
				self.weekday = calendar.get_weekday(self.day)
				self.month_name = calendar.get_month_name(self.month)
				self.day_name = calendar.get_day_name(self.day_of_year, self.is_leap)
				self.weekday_name = calendar.get_weekday_name(self.weekday)
				
			def total_days(self):
				year = self.year + calendar.year_offset
				return datetime.date(year, 1, 1).toordinal() + self.day_of_year - 1

			def to_gregorian(self):
				return datetime.date.fromordinal(self.total_days())
			
			def __str__(self):
				if self.month is calendar.months_in_a_year + 1:
					return "{}, {}".format(self.day_name, self.year)
				else:
					return "{}, {} of {}, {}: {}".format(self.weekday_name, ordinal(self.day), self.month_name, 
												    self.year, self.day_name)
				
			def __repr__(self):
				return '%s date(%d, %d, %d)' % (calendar.name.lower(), self.year, self.month, self.day)
			
			def __add__(self, timedelta):
				return self.calendar.from_date((self.to_gregorian() + timedelta))
			
			def __sub__(self, arg):
				if isinstance(arg, datetime.timedelta):
					return self.calendar.from_date(self.to_gregorian() - arg)
				elif "AlternateDate" in str(type(arg)):
					return datetime.timedelta(days=self.total_days() - arg.total_days())

			def __eq__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.to_gregorian() == othercast
			
			def __gt__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.to_gregorian() > othercast
			
			def __lt__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.to_gregorian() < othercast	
			
			def __ge__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.to_gregorian() >= othercast
				
			def __le__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.to_gregorian() <= othercast

		calendar.date_class = AlternateDate

	# create a date from gregorian date
	def from_date(self, *args):
		if not args:
			gregorian = datetime.date.today()
		else:
			try:
				year, month, day = args
				gregorian = datetime.date(year, month, day)
				# return self.date_class(datetime.date(year, month, day), self)
			except Exception:
				try:
					gregorian = args[0]
					# return self.date_class(args[0], self)
				except Exception:
					raise
		year = gregorian.year - self.year_offset
		day_of_year = gregorian.timetuple().tm_yday
		month = ((day_of_year - 1) // self.days_in_a_month) + 1
		day = day_of_year % self.days_in_a_month or self.days_in_a_month
		return self.date_class(year, month, day, self)

	# create "native" date
	def date(self, *args):
		if not args:
			return self.from_date()
		else:
			year, month, day = args
			return self.date_class(year, month, day, self)
	
	def get_weekday(self, day):
		return day % self.days_in_a_week or self.days_in_a_week
	def get_weekday_name(self, weekday):
		if weekday > len(self.DAYS):
			return ordinal(weekday) + " Day"
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
		maxwidth = max(max(map(len, self.SAINTS)),(max(map(len, self.LEAPSAINTS))))
		if not year or not month:
			today = self.date()
			year = today.year
			month = today.month
		
		print("THE {} MONTH OF {}, {}".format(self.name.upper(), self.get_month_name(month).upper(), year))
		
		month_offset = (month - 1) * self.weeks_in_a_month * self.days_in_a_week
		# for date in range(1, self.days_in_a_month + 1):
		# 	week = date // self.days_in_a_week
		# 	week_offset = (week - 1) * self.days_in_a_week	
		# 	weekday = self.get_weekday(date)
		# 	wkd_name = self.get_weekday_name(weekday)
		# 	datestr = str(date)
		# 	saint = self.get_day_name(month_offset + date, self.is_leap(year))
		# 	print("""
		# 		+{}
		# 		|{}{}{}
		# 		|{}
		# 		|{}
		# 		|{}
		# 		|{}
		# 		|{}{}
		# 		""".format(maxwidth * '-', wkd_name, ((maxwidth - (len(wkd_name) + len(datestr))) * " "), datestr,
		# 					maxwidth * " ", maxwidth * " ", maxwidth * " ", maxwidth * " ",
		# 					(maxwidth - len(saint)) * " ", saint), end=" ")
				

		for week in range(1, self.weeks_in_a_month + 1):
			week_offset = (week - 1) * self.days_in_a_week	
			print(('+' + maxwidth * '-') * self.days_in_a_week)
			
			weekdays = ""
			for weekday in range(1, self.days_in_a_week + 1):
				wkd_name = self.get_weekday_name(weekday)
				date = week_offset + weekday
				weekdays += ('|' + wkd_name + (maxwidth -(len(wkd_name) + len(str(date)))) 
					* " " + str(date))
			weekdays += '|'
			print(weekdays)
			
			height = 4
			for i in range(height):
				print(('|' + maxwidth * " ") * self.days_in_a_week + '|')
			
			saints = ""
			for day in range(1, self.days_in_a_week + 1):
				saint = self.get_day_name(month_offset + week_offset + day, self.is_leap(year))
				saints += ('|' + ((maxwidth - len(saint)) * " ") + saint)
			saints += '|'
			print(saints)

		print(('+' + maxwidth * "-") * self.days_in_a_week)

	def __str__(self):
		return "The %s calendar, consisting of %d-day weeks, %d-week months, and %d-month years, with %d intercalary day(s)." % (self.name, self.days_in_a_week, self.days_in_a_month // self.days_in_a_week, self.months_in_a_year, self.intercalary_days)

if __name__ == "__main__":	
	import doctest
	doctest.testmod()
	