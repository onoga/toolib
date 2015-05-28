# - *- coding: Cp1251 -*-

from Unit import Unit

ZERO = u"����"
MINUS = u"�����"

S20 = (
	[
		None,
		u"����", 
		u"���", 
		u"���",
		u"������",
		u"����",
		u"�����",
		u"����",
		u"������",
		u"������",
		u"������",
		u"�����������",
		u"����������",
		u"����������",
		u"������������",
		u"����������",
		u"�����������",
		u"����������",
		u"������������",
		u"������������",
	],
	[],
	[],
)

S20[1].extend(S20[0])
S20[2].extend(S20[0])

S20[Unit.FEMALE][1] = u"����"
S20[Unit.FEMALE][2] = u"���"

S20[Unit.NEUTER][1] = u"����"
S20[Unit.NEUTER][2] = u"���"

S90 = (
	None,
	None,
	u"��������",
	u"��������",
	u"�����",
	u"���������",
	u"����������",
	u"���������",
	u"�����������",
	u"���������",
)

S900 = (
	None,
	u"���",
	u"������",
	u"������",
	u"���������",
	u"�������",
	u"��������",
	u"�������",
	u"���������",
	u"���������",
)

UNIT = (
	Unit(Unit.FEMALE,	u"������",		u"������",			u"�����"),
	Unit(Unit.MALE,		u"�������",		u"��������",		u"���������"),
	Unit(Unit.MALE,		u"��������",	u"���������",		u"����������"),
	Unit(Unit.MALE,		u"��������",	u"���������",		u"����������"),
	Unit(Unit.MALE,		u"�����������",	u"������������",	u"�������������"),
	Unit(Unit.MALE,		u"�����������",	u"������������",	u"�������������"),
	Unit(Unit.MALE,		u"����������",	u"����������",		u"������������"),
	Unit(Unit.MALE,		u"���������",	u"����������",		u"�����������"),
	Unit(Unit.MALE,		u"��������",	u"���������",		u"����������"),
	Unit(Unit.MALE,		u"��������",	u"���������",		u"����������"),
	Unit(Unit.MALE,		u"��������",	u"���������",		u"����������"),
)                   

del Unit
