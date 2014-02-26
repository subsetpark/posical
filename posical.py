#! usr/bin/env python #
# -*- coding: utf-8 -*-

import datetime
from calendar import isleap

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

	d_i_week = int(raw_input("How many days in a week? "))
	w_i_month = int(raw_input("How many weeks in a month? "))
	m_i_year = 365 / (d_i_week * w_i_month)
	year_1 = int(raw_input("When is year 1? "))
	return AlternateCal(m_i_year, w_i_month, d_i_week, year_1)

class AlternateCal(object):
	"""
	>>> cal = AlternateCal()
	>>> cal.date(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> cal.date(datetime.date(2014, 2, 22))
	positivist date(226, 2, 25)
	>>> print cal.date(2001, 1, 1)
	Monday, Moses 1, 213: Prometheus
	>>> print cal.date(2001, 5, 10)
	Thursday, Caesar 18, 213: Hannibal
	>>> print cal.date(2001, 12, 31)
	Festival of All the Dead, 213
	>>> print cal.date(2000, 2, 29)
	Thursday, Aristotle 4, 212: Anaxagoras
	>>> print cal.date(2000, 12, 31)
	Festival of Holy Women, 212
	>>> print cal.date(2014, 2, 22).to_gregorian()
	2014-02-22
	>>> class New_cal(AlternateCal):
	...  days_in_a_month = 26
	>>> cal2 = New_cal()
	>>> cal.date(2014, 2, 22)
	positivist date(226, 2, 25)
	>>> print cal
	The Positivist calendar, consisting of 7-day weeks, 28-week months, and 13-month years, with 1 intercalary day(s).
	"""
	
	def __init__(calendar, m_i_year=28, w_i_month=4, d_i_week=7, year_1=1788):
		name_choices = ('New Adjusted', 'Utilitarian', 'Lycurgian', 'Multi-Manifold', 'Crepuscular', 'Positivist', 'Adamantine', 'Organic Non-Repeating', 'Antediluvian', 'Re-Corresponding', 'Urquhart')
		calendar.name = name_choices[(m_i_year ** w_i_month / d_i_week + year_1) % 11]
		calendar.days_in_a_month = d_i_week * w_i_month
		calendar.days_in_a_week = d_i_week
		calendar.months_in_a_year = 365 / calendar.days_in_a_month
		calendar.intercalary_days = 365 % calendar.days_in_a_month
		calendar.year_offset = year_1
		if calendar.name is 'Positivist':
			calendar.MONTHS = POSIMONTHS
		else:
			calendar.MONTHS = REGMONTHS
		calendar.DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
		calendar.SAINTS = ('Prometheus', 'Hercules', 'Orpheus', 'Ulysses', 'Lycurgus', 'Romulus', 'NUMA', 'Belus', 'Sesostris', 'Menu', 'Cyrus', 'Zoroaster', 'The Druids', 'BUDDHA', 'Fo-Hi', 'Lao-Tseu', 'Meng-Tseu', 'Theocrats of Tibet', 'Theocrats of Japan', 'Mano-Capac', 'CONFUCIUS', 'Abraham', 'Samuel', 'Solomon', 'Isaiah', 'St. John  the Baptist', 'Haroun-al-Raschid', 'MUHAMMAD', 'Hesiod', 'Tyrt&#230us', 'Anacreon', 'Pindar', 'Sophocles', 'Theocritus', '&#198SCHYLUS', 'Scopas', 'Zeuxis', 'Ictinus', 'Praxiteles', 'Lysippus', 'Apelles', 'PHIDIAS', '&#198sop', 'Plautus', 'Terence', 'Phaedrus', 'Juvenal', 'Lucian', 'ARISTOPHANES', 'Ennius', 'Lucretius', 'Horace', 'Tibullus', 'Ovid', 'Lucan', 'VIRGIL', 'Anaximander', 'Anaximenes', 'Heraclitus', 'Anaxagoras', 'Democritus', 'Herodotus', 'THALES', 'Solon', 'Xenophanes', 'Empodocles', 'Thucydides', 'Archytas', 'Apollonius of Tyana', 'PYTHAGO- RAS', 'Aristippus', 'Antisthenes', 'Zeno', 'Cicero', 'Epictetus', 'Tacitus', 'SOCRATES', 'Xenocrates', 'Philo of Alexandria', 'St. John the Evangelist', 'St. Justin', ' St.Clement of Alexandria', 'Origen', 'PLATO', 'Theophrastus', 'Herophilus', 'Erasistratus', 'Celsus', 'Galen', 'Avicenna', 'HIPPOC- RATES', 'Euclid', 'Arist\u0230us', 'Theodisius of Bithynia', 'Hero', 'Pappus', 'Diophantus', 'APOLLONIUS', 'Eudoxus', 'Pytheas', 'Aristarchus', 'Eratos- thenes', 'Ptolemy', 'Albategnius', 'HIPPARCHUS', 'Varro', 'Columella', 'Vitruvius', 'Strabo', 'Frontinus', 'Plutarch', 'PLINY THE ELDER', 'Miltiades', 'Leonidas', 'Aristides', 'Cimon', 'Xenophon', 'Phocion', 'THEMISTOCLES', 'Pericles', 'Philip', 'Demos- thenes', 'Ptolemy Lagus', 'Philopoemen', 'Polybius', 'ALEXANDER', 'Junius Brutus', 'Camillus', 'Fabricius', 'Hannibal', 'Paulus Aemilius', 'Marius', 'SCIPIO', 'Augustus', 'Vespasian', 'Hadrian', 'Antonius', 'Papinian', 'Alexander Severus', 'TRAJAN', 'St. Luke', 'St. Cyprian', ' St.Athanasius', 'St. Jerome', 'St. Ambrose', 'St. Monica', ' St.AUGUSTINE', 'Constantine', 'Theodosius', 'St. Chrysos- tom', ' St.Genevieve of Paris', 'St. Pulcheria', 'St. Gregory the Great', 'HILDEBRAND', 'St. Benedict', 'St. Boniface', 'St. Isidore of Seville', 'Lanfranc', 'Heloise', "Arch'ts of Middle Ages", ' St.BERNARD', 'St. Francis Xavier', 'St. Charles Borromeo', 'St. Theresa', 'St. Vincent de Paul', 'Bourdaloue', 'William Penn', 'BOSSUET', 'Theodoric the Great', 'Pelayo', 'Otho the Great', 'St. Henry', 'Villers', 'Don John of Austria', 'ALFRED', 'Charles Martel', 'The Cid', 'Richard I', 'Joan of Arc', 'Albuquerque', 'Bayard', 'GODFREY', 'St. Leo the Great', 'Gerbert', 'Peter the Hermit', 'Suger', 'Alexander III', 'St. Francis of Assisi', 'INNOCENT III', 'St. Clotilde', 'St. Bathilda', 'St. Stephen of Hungary', 'St. Elizabeth of Hungary', 'Blanche of Castille', 'St. Ferdi- nand III', 'ST. LOUIS', 'The Trouba- dours', 'Boccaccio', 'Rabelais', 'Cervantes', 'La Fontain', 'De Foe', 'ARISTO', 'Leonardo da Vinci', 'Michael Angelo', 'Holbein', 'Poussin', 'Velásquez', 'Teniers', 'RAPHAEL', 'Froissart', 'Camoens', 'The Spanish Romancers', 'Chateau- briand', 'Walter Scott', 'Manzoni', 'TASSO', 'Petrarca', 'Thomas &agrave Kempis', 'Mme. de Lafayette', 'F&eacuten&eacutelon', 'Klopstock', 'Byron', 'MILTON', 'Marco Polo', 'Jacques Coeur', 'Vasco de Gama', 'Napier', 'Lacaille', 'Cook', 'COLUMBUS', 'Benvenuto Cellini', 'Amontons', 'Harrison', 'Dollond', 'Arkwright', 'Cont\u00e9', 'VAUCANSON', 'Stevin', 'Mariotte', 'Papin', 'Black', 'Jouffroy', 'Dalton', 'WATT', 'Bernard de Palissy', 'Guglielmini', 'Duhamel (du Monceau)', 'Saussure', 'Coulomb', 'Carnot', 'MONTGOLFIER', 'Lope de Vega', 'Moreto', 'Rojas', 'Otway', 'Lessing', 'Goethe', 'CALDERON', 'Tirso', 'Vondel', 'Racine', 'Voltaire', 'Metastasio', 'Schiller', 'CORNEILLE', 'Almarcon', 'Mme. de Motteville', 'Mme. de S&eacutevign&eacute', 'Lesage', 'Mme. de Staal', 'Fielding', 'MOLIERE', 'Pergolese', 'Sacchini', 'Gluck', 'Beethoven', 'Rossini', 'Bellini', 'MOZART', 'Albertus Magnus', 'Roger Bacon', 'St. Bonaven- tura', 'Ramus', 'Montaigne', 'Campanella', 'ST. THOMAS AQUINAS', 'Hobbes', 'Pascal', 'Locke', 'Vauvenar- gues', 'Diderot', 'Cabanis', 'LORD BACON', 'Grotius', 'Fontenelle', 'Vico', 'Fr&eacuteret', 'Montesquieu', 'Buffon', 'LEIBNITZ', 'Robertson', 'Adam Smith', 'Kant', 'Condercet', 'Joseph de Maistre', 'Hegel', 'HUME', 'Marie de Molina', 'Cosmo de Medici the Elder', 'Philippe de Comines', 'Isabella of Castille', 'Charles V', 'Henry IV', 'LOUIS XI', "L'H/u0244pital", 'Barneveldt', 'Gustavus Adolphus', 'De Witt', 'Ruyter', 'William III', 'WILLIAM THE SILENT', 'Ximenes', 'Sully', 'Mazarin', 'Colbert', "D'Aranda", 'Turgot', 'RICHELIEU', 'Sidney', 'Franklin', 'Washington', 'Jefferson', 'Bolivar', 'Francia', 'CROMWELL', 'Copernicus', 'Kepler', 'Huyghens', 'James Bernouilli', 'Bradley', 'Volta', 'GALILEO', 'Vieta', 'Wallis', 'Clairaut', 'Euler', "D'Alembert", 'Lagrange', 'NEWTON', 'Bergmann', 'Priestley', 'Cavendish', 'Guyton Morveau', 'Berthollet', 'Berzelius', 'LAVOISIER', 'Harvey', 'Bo/u0235rhaave', 'Linn/u0230us', 'Haller', 'Lamarck', 'Broussais', 'GALL', 'Festival of All the Dead', 'Festival of Holy Women')
		calendar.LEAPSAINTS = ('Cadmus', 'Theseus', 'Tiresias', '', '', '', '', 'Semiramus', '', '', '', '', 'Ossian', '', '', '', '', '', '', 'Tameha-meha', '', 'Joseph', '', 'David', '', '', 'Abderrah-man', '', '', 'Sappho', '', '', 'Euripides', 'Longus', '', '', '', '', '', '', '', '', 'Pilpay', '', 'Menander', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Leucippus', '', '', '', '', '', '', 'Philolaus', '', '', '', '', '', 'Pliny the Younger', 'Arrian', '', '', '', '', '', 'St. Iren&#230us', '', 'Tertullian', '', '', '', '', '', '', 'Averrhoes', '', '', '', '', 'Ctesibius', '', '', '', 'Aratus', 'Nearchus', 'Berosus', 'Sosigenes', '', 'Nasir-Eddin', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Epaminon-das', '', '', '', '', '', '', '', '', '', 'Cincinnatus', 'Regulus', '', '', 'The Gracchi', '', 'M&#230cenas', 'Titus', 'Nerva', 'Marcus Aurelius', 'Ulpian', 'Aetius', '', 'St. James', '', '', '', '', '', '', '', '', 'St. Basil', '', 'Marcian', '', '', 'St. Anthony', 'St. Austin', 'St. Bruno', 'St. Anselm', 'Beatrice', 'St. Benezet', '', 'Ignatius Loyola', 'Fredrick Borromeo', 'St.Catharineof Siena', "Abb&eacute de l'Ep&eacutee", 'ClaudeFleury', 'George Fox', '', '', '', 'Henry the Fowler', '', 'La Valette', 'JohnSobieski', '', '', 'Tancred', 'Saladin', 'Marina', 'Sir Walter Raleigh', '', '', 'Leo IV', 'PeterDamian', '', 'St. Eligius', 'Becket', 'St. Dominic', '', '', 'St. Mathilda of Tuscany', 'Mathias Corvinus', '', '', 'Alfonso X', '', '', 'Chaucer', 'Swift', '', 'Burns', 'Goldsmith', '', 'Titian', 'Paul Veronese', 'Rembrandt', 'Lesueuer', 'Murillo', 'Rubens', '', 'Joinville', 'Spenser', '', '', 'James Fenimore Cooper', '', '', '', 'L. of Grana-da & Bunyan', 'Mme. de Sta&#235l', 'St. Francisof Sales', 'Gessner', '&Eacute. Mercoeur & Shelly', '', 'Chardin', 'Gresham', 'Magellan', 'Briggs', 'Delambre', 'Tasman', '', '', 'Wheatstone', 'Pierre Leroy', 'Graham', 'Jacquard', '', '', 'Torricelli', 'Boyle', 'Worcester', '', 'Fulton', 'Thilorier', '', '', 'Riquet', 'Bourgelat', 'Bouguer', 'Borda', 'Vauban', '', 'Montalvan', 'Guillem de Castro', 'Guevara', '', '', '', '', '', '', '', '', 'Alfieri', '', '', '', 'Mme. Roland', 'Lady Montagu', 'Sterne', 'Miss Edgeworth', 'Richardson', '', 'Palestrina', 'Gr&eacutetry', 'Lully', 'Handel', 'Weber', 'Donizeti', '', 'John of Salisbury', 'Raymond Lully', 'Joachim', 'The Cardinal of Cusa', 'Erasmus', 'Sir Thomas More', '', 'Spinoza', 'Giordano Bruno', 'Male-branche', 'Mme. de Lambert', 'Duclos', 'GeorgeLeroy', '', 'Cujas', 'Maupertuis', 'Herder', 'Winckle-mann', "D'Aguesseau", 'Oken', '', 'Gibbon', 'Dunoyer', 'Fichte', 'Ferguson', 'Bonald', 'Sophie Germain', '', '', '', 'Guicciardini', '', 'Sixtus V', '', '', '', '', '', '', '', '', '', '', 'Oxenstiern', 'Walpole', 'Louis XIV', 'Pombal', 'Campo-manes', '', 'Lambert', 'Hampden', 'Kosciusko', 'Madison', "Toussaint L'Ouverture", '', '', 'Tycho Brah&eacute', 'Halley', 'Varignon', 'John Bernouilli', 'R&#246mer', 'Sauveur', '', 'Harriot', 'Fermat', 'Poinsot', 'Monge', 'Daniel Bernouilli', 'Joseph Fourier', '', 'Scheele', 'Davy', '', 'Geoffroy', '', 'Ritter', '', 'Charles Bell', 'Stahl & Barthez', 'Bernard de Jussieu', "Vicq-d'Azyr", 'Blainville', 'Morgagni', '', '', 'Festival of Holy Women')



		class AlternateDate(object):
			def __init__(self, gregorian, calendar):
				self.calendar = calendar
				self.year = gregorian.year - calendar.year_offset
				self.is_leap = False
				if isleap(gregorian.year):
					self.is_leap = True
					
				self.day_of_year = gregorian.timetuple().tm_yday
				self.month = ((self.day_of_year - 1) / calendar.days_in_a_month) + 1
				self.day = self.day_of_year % calendar.days_in_a_month or calendar.days_in_a_month
				
				if self.month > len(calendar.MONTHS):
					self.month_name = ordinal(n) + " Month"
				else:
					self.month_name = calendar.MONTHS[(self.month - 1)]
				if self.is_leap and calendar.LEAPSAINTS[self.day_of_year - 1]:
					self.day_name = calendar.LEAPSAINTS[self.day_of_year - 1]
				else:
					self.day_name = calendar.SAINTS[self.day_of_year - 1]
				self.weekday = self.day % calendar.days_in_a_week or calendar.days_in_a_week
				if self.weekday > len(calendar.DAYS):
					self.weekday_name = ordinal(n) + " Month"
				else:
					self.weekday_name = calendar.DAYS[self.weekday - 1]

				self.downcast = self.to_gregorian();
				
			def to_gregorian(self):
				# get ordinal value of the year, then add the 
				# ordinal of the day in the year, then form a date
				year = self.year + calendar.year_offset
				return datetime.date.fromordinal(datetime.date(year, 1, 1).toordinal() + self.day_of_year - 1)
			
			def __str__(self):
				if self.month is calendar.months_in_a_year + 1:
					return "%s, %d" % (self.day_name, self.year)
				else:
					return "%s, %s %d, %d: %s" % (self.weekday_name, self.month_name, 
												   self.day, self.year, self.day_name)
				
			def __repr__(self):
				return '%s date(%d, %d, %d)' % (calendar.name.lower(), self.year, self.month, self.day)
			
			def __add__(self, timedelta):
				return self.calendar.date((self.downcast + timedelta))
				
			def __sub__(self, timedelta):
				return self.calendar.date((self.downcast - timedelta))

			def __eq__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.downcast == othercast
			
			def __gt__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.downcast > othercast
			
			def __lt__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.downcast < othercast	
			
			def __ge__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.downcast >= othercast
				
			def __le__(self, other_date):
				othercast = (other_date.to_gregorian())
				return self.downcast <= othercast

		calendar.date_class = AlternateDate

	def date(self, *args):
		if not args:
			return self.date_class(datetime.date.today(), self)
		else:
			try:
				# import pdb
				# pdb.set_trace()
				year, month, day = args
				return self.date_class(datetime.date(year, month, day), self)
			except Exception:
				try:
					return self.date_class(args[0], self)
				except Exception:
					raise

	def print_cal(self):
		print (self.days_in_a_week * '+------------')
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '|            ')+'|'
		print (self.days_in_a_week * '+------------')

	def __str__(self):
		return "The %s calendar, consisting of %d-day weeks, %d-week months, and %d-month years, with %d intercalary day(s)." % (self.name, self.days_in_a_week, self.days_in_a_month / self.days_in_a_week, self.months_in_a_year, self.intercalary_days)

if __name__ == "__main__":	
	import doctest
	doctest.testmod()
	