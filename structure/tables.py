# -*- coding: utf-8 -*-

import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import *
from sqlalchemy import ForeignKey as FKey
from PyQt4.QtCore import QDate, QDateTime
from .Utils import QDateType, QDateTimeType, QTimeType
Base = declarative_base()


class Account(Base):
    u"""Выставленные счета за оказанные услуги"""
    __tablename__ = 'Account'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    createPerson = relationship('Person', foreign_keys='Account.createPerson_id')
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyPerson = relationship('Person', foreign_keys='Account.modifyPerson_id')
    deleted = Column(Boolean, default='0')
    contract_id = Column(Integer, FKey('Contract.id'), index=True)
    contract = relationship('Contract', foreign_keys='Account.contract_id')
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'))
    orgStructure = relationship(
            'OrgStructure', foreign_keys='Account.orgStructure_id')
    payer_id = Column(Integer, FKey('Organisation.id'), index=True)
    payer = relationship('Organisation', foreign_keys='Account.payer_id')
    settleDate = Column(QDateType)
    number = Column(String(20))
    date = Column(QDateType)
    amount = Column(Float)
    uet = Column(Float)
    sum = Column(Float)
    exposeDate = Column(QDateType)
    payedAmount = Column(Float)
    payedSum = Column(Float)
    refusedAmount = Column(Float)
    refusedSum = Column(Float)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    format_id = Column(Integer, FKey('rbAccountExportFormat.id'), index=True)
    format = relationship(
            'RbAccountExportFormat', foreign_keys='Account.format_id')
    note = Column(String(50))


class AccountItem(Base):
    __tablename__ = 'Account_Item'
    id = Column(Integer, primary_key=True)
    deleted = Column(SmallInteger, default='0', nullable=False)
    master_id = Column(Integer, FKey('Account.id'))
    account = relationship('Account', foreign_keys='AccountItem.master_id')
    serviceDate = Column(QDateType)
    client_id = Column(Integer, FKey('Client.id'))
    client = relationship('Client', foreign_keys='AccountItem.client_id')
    event_id = Column(Integer, FKey('Event.id'))
    event = relationship('Event', foreign_keys='AccountItem.event_id')
    visit_id = Column(Integer, FKey('Visit.id'))
    visit = relationship('Visit', foreign_keys='AccountItem.visit_id')
    action_id = Column(Integer, FKey('Action.id'))
    action = relationship('Action', foreign_keys='AccountItem.action_id')
    price = Column(Float, default='0', nullable=False)
    unit_id = Column(Integer, FKey('rbMedicalAidUnit.id'))
    unit = relationship('RbMedicalAidUnit', foreign_keys='AccountItem.unit_id')
    amount = Column(Float, default='0', nullable=False)
    uet = Column(Float, default='0', nullable=False)
    sum = Column(Float, default='0', nullable=False)
    date = Column(QDateType)
    number = Column(String(20), default='')
    refuseType_id = Column(Integer, FKey('rbPayRefuseType.id'))
    refuseType = relationship('RbPayRefuseType', foreign_keys='AccountItem.refuseType_id')
    reexposeItem_id = Column(Integer, FKey('Account_Item.id'))
    reexposeItem = relationship('AccountItem', foreign_keys='AccountItem.reexposeItem_id')
    note = Column(String(256), default='')
    notUploadAnymore = Column(Boolean, default='0', nullable=False)
    tariff_id = Column(Integer, FKey('Contract_Tariff.id'))
    tariff = relationship('ContractTariff', foreign_keys='AccountItem.tariff_id')
    service_id = Column(Integer, FKey('rbService.id'))
    service = relationship('RbService', foreign_keys='AccountItem.service_id')
    paymentConfirmationDate = Column(QDateType)


class Action(Base):
    __tablename__ = 'Action'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    createPerson = relationship('Person', foreign_keys='Action.createPerson_id')
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyPerson = relationship('Person',
                                foreign_keys='Action.modifyPerson_id')
    deleted = Column(SmallInteger, default='0', nullable=False)
    actionType_id = Column(Integer, FKey('ActionType.id'), index=True)
    actionType = relationship('ActionType', foreign_keys='Action.actionType_id')
    event_id = Column(Integer, FKey('Event.id'), index=True)
    event = relationship('Event', foreign_keys='Action.event_id')
    idx = Column(Integer, default='0')
    directionDate = Column(QDateTimeType)
    status = Column(SmallInteger)
    setPerson_id = Column(Integer, FKey('Person.id'), index=True)
    setPerson = relationship('Person', foreign_keys='Action.setPerson_id')
    isUrgent = Column(SmallInteger)
    begDate = Column(QDateTimeType)
    plannedEndDate = Column(QDateTimeType)
    endDate = Column(QDateTimeType)
    note = Column(Text)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    person = relationship('Person', foreign_keys='Action.person_id')
    office = Column(String(16))
    amount = Column(Float)
    uet = Column(Float)
    expose = Column(SmallInteger, default='1')
    payStatus = Column(Integer)
    account = Column(SmallInteger)
    finance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    finance = relationship('RbFinance', foreign_keys='Action.finance_id')
    prescription_id = Column(Integer, FKey('Action.id'), index=True)
    prescription = relationship('Action', foreign_keys='Action.prescription_id')
    takenTissueJournal_id = Column(Integer, FKey('TakenTissueJournal.id'), index=True)
    takenTissueJournal = relationship(
            'TakenTissueJournal', foreign_keys='Action.takenTissueJournal_id')
    contract_id = Column(Integer, FKey('Contract.id'), index=True)
    contract = relationship('Contract', foreign_keys='Action.contract_id')
    coordDate = Column(QDateTimeType)
    coordAgent = Column(String(128))
    coordInspector = Column(String(128))
    coordText = Column(Text)
    hospitalUidFrom = Column(String(128))
    pacientInQueueType = Column(SmallInteger)
    AppointmentType = Column(Enum('0', 'amb', 'hospital', 'polyclinic',
                                  'diagnostics', 'portal', 'otherLPU',
                                  name='AppointmentType'))
    version = Column(Integer)
    parentAction_id = Column(Integer, FKey('Action.id'), index=True)
    parentAction = relationship(
            'Action', foreign_keys='Action.parentAction_id')


class ActionProperty(Base):
    __tablename__ = 'ActionProperty'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    action_id = Column(Integer, FKey('Action.id'), index=True)
    action = relationship('Action', foreign_keys='ActionProperty.action_id')
    type_id = Column(Integer, FKey('ActionPropertyType.id'), index=True)
    type = relationship(
            'ActionPropertyType', foreign_keys='ActionProperty.type_id')
    unit_id = Column(Integer, FKey('rbUnit.id'), index=True)
    unit = relationship('RbUnit', foreign_keys='ActionProperty.unit_id')
    norm = Column(String(64))
    isAssigned = Column(SmallInteger, default='0')
    evaluation = Column(SmallInteger)


class ActionPropertyAction(Base):
    __tablename__ = 'ActionProperty_Action'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship(
        'ActionProperty', foreign_keys='ActionPropertyAction.id')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyDate(Base):
    __tablename__ = 'ActionProperty_Date'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(QDateType)


class ActionPropertyDouble(Base):
    __tablename__ = 'ActionProperty_Double'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Float)


class ActionPropertyFDRecord(Base):
    __tablename__ = 'ActionProperty_FDRecord'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyHospitalBed(Base):
    __tablename__ = 'ActionProperty_HospitalBed'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyHospitalBedProfile(Base):
    __tablename__ = 'ActionProperty_HospitalBedProfile'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyImage(Base):
    __tablename__ = 'ActionProperty_Image'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Binary)


class ActionPropertyImageMap(Base):
    __tablename__ = 'ActionProperty_ImageMap'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Text)


class ActionPropertyInteger(Base):
    __tablename__ = 'ActionProperty_Integer'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer)


class ActionPropertyJobTicket(Base):
    __tablename__ = 'ActionProperty_Job_Ticket'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyMKB(Base):
    __tablename__ = 'ActionProperty_MKB'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyOrganisation(Base):
    __tablename__ = 'ActionProperty_Organisation'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyOrgStructure(Base):
    __tablename__ = 'ActionProperty_OrgStructure'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyOtherLPURecord(Base):
    __tablename__ = 'ActionProperty_OtherLPURecord'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Text)


class ActionPropertyPerson(Base):
    __tablename__ = 'ActionProperty_Person'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyRbBloodComponentType(Base):
    __tablename__ = 'ActionProperty_rbBloodComponentType'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer)


class ActionPropertyRbFinance(Base):
    __tablename__ = 'ActionProperty_rbFinance'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyRbReasonOfAbsence(Base):
    __tablename__ = 'ActionProperty_rbReasonOfAbsence'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Integer, index=True)


class ActionPropertyString(Base):
    __tablename__ = 'ActionProperty_String'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(Text)


class ActionPropertyTime(Base):
    __tablename__ = 'ActionProperty_Time'
    id = Column(Integer, FKey('ActionProperty.id'), primary_key=True)
    act_prop = relationship('ActionProperty')
    index = Column(Integer)
    value = Column(QTimeType)


class ActionPropertyTemplate(Base):
    __tablename__ = 'ActionPropertyTemplate'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    group_id = Column(Integer,
                      FKey('ActionPropertyTemplate.id'), index=True)
    parentCode = Column(String(20))
    code = Column(String(64), index=True)
    federalCode = Column(String(64), index=True)
    regionalCode = Column(String(64))
    name = Column(String(120), index=True)
    abbrev = Column(String(64))
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    service_id = Column(Integer, FKey('rbService.id'), index=True)
    service = relationship(
            'RbService', foreign_keys='ActionPropertyTemplate.service_id')


class ActionPropertyType(Base):
    __tablename__ = 'ActionPropertyType'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, index=True)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    actionType_id = Column(Integer, FKey('ActionType.id'), index=True)
    actionType = relationship(
            'ActionType', foreign_keys='ActionPropertyType.actionType_id')
    idx = Column(Integer)
    template_id = Column(Integer, FKey('ActionPropertyTemplate.id'), index=True)
    template = relationship(
            'ActionPropertyTemplate',
            foreign_keys='ActionPropertyType.template_id')
    name = Column(String(128))
    descr = Column(String(128))
    unit_id = Column(Integer, FKey('rbUnit.id'), index=True)
    unit = relationship(
            'RbUnit', foreign_keys='ActionPropertyType.unit_id')
    typeName = Column(String(64))
    valueDomain = Column(Text)
    defaultValue = Column(String(250))
    isVector = Column(SmallInteger)
    norm = Column(String(64))
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    penalty = Column(Integer)
    visibleInJobTicket = Column(SmallInteger)
    isAssignable = Column(Boolean)
    test_id = Column(Integer, FKey('rbTest.id'))
    defaultEvaluation = Column(SmallInteger)
    toEpicrisis = Column(SmallInteger)
    code = Column(String(25), index=True)
    mandatory = Column(SmallInteger)
    readOnly = Column(SmallInteger)


class ActionTemplate(Base):
    __tablename__ = 'ActionTemplate'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    group_id = Column(Integer, FKey('ActionTemplate.id'), index=True)
    code = Column(String(64))
    name = Column(String(255))
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    owner_id = Column(Integer, FKey('Person.id'), index=True)
    owner = relationship('Person', foreign_keys='ActionTemplate.owner_id')
    speciality_id = Column(Integer, FKey('rbSpeciality.id'), index=True)
    speciality = relationship(
            'RbSpeciality', foreign_keys='ActionTemplate.speciality_id')
    action_id = Column(Integer, FKey('Action.id'), index=True)
    action = relationship('Action', foreign_keys='ActionTemplate.action_id')


class ActionTissue(Base):
    __tablename__ = 'ActionTissue'
    action_id = Column(Integer, FKey('Action.id'), primary_key=True, index=True)
    tissue_id = Column(Integer, primary_key=True, index=True)


class ActionType(Base):
    __tablename__ = 'ActionType'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    hidden = Column(SmallInteger, default='0')
    class_ = Column(SmallInteger, name="class", index=True)
    group_id = Column(Integer, FKey('ActionType.id'), index=True)
    group = relationship('ActionType', foreign_keys='ActionType.group_id')
    code = Column(String(25))
    name = Column(String(255))
    title = Column(String(255))
    flatCode = Column(String(64), index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    office = Column(String(32))
    showInForm = Column(SmallInteger)
    genTimetable = Column(SmallInteger)
    service_id = Column(Integer, FKey('rbService.id'), index=True)
    service = relationship('RbService', foreign_keys='ActionType.service_id')
    quotaType_id = Column(Integer, FKey('QuotaType.id'), index=True)
    quotaType = relationship(
            'QuotaType', foreign_keys='ActionType.quotaType_id')
    context = Column(String(64))
    amount = Column(Float, default='1')
    amountEvaluation = Column(Integer, default='0')
    defaultStatus = Column(SmallInteger, default='0')
    defaultDirectionDate = Column(SmallInteger, default='0')
    defaultPlannedEndDate = Column(SmallInteger, default='0')
    defaultEndDate = Column(SmallInteger, default='0')
    defaultExecPerson_id = Column(Integer, FKey('Person.id'), index=True)
    defaultPersonInEvent = Column(SmallInteger, default='0')
    defaultPersonInEditor = Column(SmallInteger, default='0')
    maxOccursInEvent = Column(Integer, default='0')
    showTime = Column(SmallInteger, default='0')
    isMES = Column(Boolean)
    nomenclativeService_id = Column(Integer, FKey('rbService.id'), index=True)
    nomenclativeService = relationship(
            'RbService', foreign_keys='ActionType.service_id')
    isPreferable = Column(Boolean, default='1')
    prescribedType_id = Column(Integer, FKey('ActionType.id'), index=True)
    prescribedType = relationship(
            'ActionType', foreign_keys='ActionType.prescribedType_id')
    shedule_id = Column(Integer, FKey('rbActionShedule.id'), index=True)
    shedule = relationship(
            'RbActionShedule', foreign_keys='ActionType.shedule_id')
    isRequiredCoordination = Column(Boolean, default='0')
    isAuxiliary = Column(Boolean, default='0')
    isRequiredTissue = Column(Boolean, default='0')


class ActionTypeEventTypeCheck(Base):
    __tablename__ = 'ActionType_EventType_check'
    id = Column(Integer, primary_key=True)
    actionType_id = Column(Integer, index=True)
    eventType_id = Column(Integer, index=True)
    related_actionType_id = Column(Integer, index=True)
    relationType = Column(Integer)


class ActionTypeQuotaType(Base):
    __tablename__ = 'ActionType_QuotaType'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, index=True)
    idx = Column(Integer)
    quotaclass = Column(SmallInteger)
    finance_id = Column(Integer, index=True)
    quotaType_id = Column(Integer, index=True)


class ActionTypeService(Base):
    __tablename__ = 'ActionType_Service'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, index=True)
    idx = Column(Integer)
    finance_id = Column(Integer, index=True)
    service_id = Column(Integer, index=True)


class ActionTypeTissueType(Base):
    __tablename__ = 'ActionType_TissueType'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, index=True)
    idx = Column(Integer)
    tissueType_id = Column(Integer, index=True)
    amount = Column(Integer)
    unit_id = Column(Integer, index=True)


class ActionTypeUser(Base):
    __tablename__ = 'ActionType_User'
    id = Column(Integer, primary_key=True)
    actionType_id = Column(Integer, index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    profile_id = Column(Integer, index=True)


class Address(Base):
    __tablename__ = 'Address'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    house_id = Column(Integer, index=True)
    flat = Column(String(6), index=True)


class AddressAreaItem(Base):
    __tablename__ = 'AddressAreaItem'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    LPU_id = Column(Integer, index=True)
    struct_id = Column(Integer, index=True)
    house_id = Column(Integer, index=True)
    flatRange = Column(SmallInteger)
    begFlat = Column(Integer)
    endFlat = Column(Integer)
    begDate = Column(QDateType)
    endDate = Column(QDateType)


class AddressHouse(Base):
    __tablename__ = 'AddressHouse'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    KLADRCode = Column(String(13), index=True)
    KLADRStreetCode = Column(String(17), index=True)
    number = Column(String(8), index=True)
    corpus = Column(String(8), index=True)


class AppLock(Base):
    __tablename__ = 'AppLock'
    id = Column(Integer, primary_key=True)
    lockTime = Column(TIMESTAMP)
    retTime = Column(TIMESTAMP)
    connectionId = Column(Integer, index=True)
    person_id = Column(Integer, FKey('Person.id'))
    addr = Column(String(255))


class AppLockDetail(Base):
    __tablename__ = 'AppLock_Detail'
    master_id = Column(BigInteger, primary_key=True)
    tableName = Column(String(64), index=True)
    recordId = Column(Integer, index=True)
    recordIndex = Column(Integer)


class Bank(Base):
    __tablename__ = 'Bank'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    BIK = Column(String(10), index=True)
    name = Column(String(100), index=True)
    branchName = Column(String(100))
    corrAccount = Column(String(20))
    subAccount = Column(String(20))


class BlankActionsMoving(Base):
    __tablename__ = 'BlankActions_Moving'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType)
    blankParty_id = Column(Integer, index=True)
    numberFrom = Column(String(16))
    numberTo = Column(String(16))
    serial = Column(String(8))
    orgStructure_id = Column(Integer, index=True)
    person_id = Column(Integer, index=True)
    received = Column(Integer, default='0')
    used = Column(Integer, default='0')
    returnDate = Column(QDateType)
    returnAmount = Column(Integer, default='0')


class BlankActionsParty(Base):
    __tablename__ = 'BlankActions_Party'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType)
    doctype_id = Column(Integer, index=True)
    person_id = Column(Integer, index=True)
    serial = Column(String(8))
    numberFrom = Column(String(16))
    numberTo = Column(String(16))
    amount = Column(Integer, default='0')
    extradited = Column(Integer, default='0')
    balance = Column(Integer, default='0')
    used = Column(Integer, default='0')
    writing = Column(Integer, default='0')
    returnBlank = Column(Integer)


class BlankTempInvalidMoving(Base):
    __tablename__ = 'BlankTempInvalid_Moving'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType)
    blankParty_id = Column(Integer, index=True)
    serial = Column(String(8))
    orgStructure_id = Column(Integer, index=True)
    person_id = Column(Integer, index=True)
    received = Column(Integer, default='0')
    used = Column(Integer, default='0')
    returnDate = Column(QDateType)
    returnAmount = Column(Integer, default='0')
    numberFrom = Column(String(16))
    numberTo = Column(String(16))


class BlankTempInvalidParty(Base):
    __tablename__ = 'BlankTempInvalid_Party'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType)
    doctype_id = Column(Integer, index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    serial = Column(String(8))
    numberFrom = Column(String(16))
    numberTo = Column(String(16))
    amount = Column(Integer, default='0')
    extradited = Column(Integer, default='0')
    balance = Column(Integer, default='0')
    used = Column(Integer, default='0')
    writing = Column(Integer, default='0')
    returnBlank = Column(Integer)


class BloodHistory(Base):
    __tablename__ = 'BloodHistory'
    id = Column(Integer, primary_key=True)
    bloodDate = Column(QDateType)
    client_id = Column(Integer, FKey('Person.id'))
    bloodType_id = Column(Integer, FKey('rbBloodType.id'))
    person_id = Column(Integer, FKey('Person.id'))


class CalendarExceptions(Base):
    __tablename__ = 'CalendarExceptions'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType, index=True)
    isHoliday = Column(SmallInteger)
    startYear = Column(Integer, index=True)
    finishYear = Column(Integer)
    fromDate = Column(QDateType, index=True)
    text = Column(String(250))


class Client(Base):
    __tablename__ = 'Client'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=lambda: datetime.datetime.now())
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    lastName = Column(String(30), index=True)
    firstName = Column(String(30), index=True)
    patrName = Column(String(30), index=True)
    birthDate = Column(QDateType, index=True)
    sex = Column(SmallInteger)
    SNILS = Column(String(12), index=True)
    bloodType_id = Column(Integer, FKey('rbBloodType.id'))
    bloodDate = Column(QDateType)
    bloodNotes = Column(String(250), default='')
    growth = Column(String(16), default='0')
    weight = Column(String(16), default='0')
    notes = Column(Text, default='')
    birthPlace = Column(String(120))
    embryonalPeriodWeek = Column(String(16), default='0')
    version = Column(Integer, default=0)


class ClientQuoting(Base):
    __tablename__ = 'Client_Quoting'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer)
    identifier = Column(String(16))
    quotaTicket = Column(String(20))
    quotaType_id = Column(Integer)
    stage = Column(Integer)
    directionDate = Column(QDateTimeType)
    freeInput = Column(String(128))
    org_id = Column(Integer)
    amount = Column(Integer, default='0')
    MKB = Column(String(8))
    status = Column(Integer, default='0')
    request = Column(Integer, default='0')
    statment = Column(String(255))
    dateRegistration = Column(QDateTimeType)
    dateEnd = Column(QDateTimeType)
    orgStructure_id = Column(Integer)
    regionCode = Column(String(13), index=True)
    pacientModel_id = Column(Integer)
    treatment_id = Column(Integer)
    dateAddToRegistry = Column(QDateTimeType)
    datePlan = Column(QDateTimeType)
    event_id = Column(Integer, index=True)
    prevTalon_event_id = Column(Integer, index=True)
    version = Column(Integer)


class ClientQuotingDiscussion(Base):
    __tablename__ = 'Client_QuotingDiscussion'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer)
    dateMessage = Column(QDateTimeType)
    agreementType_id = Column(Integer)
    responsiblePerson_id = Column(Integer)
    cosignatory = Column(String(25))
    cosignatoryPost = Column(String(20))
    cosignatoryName = Column(String(50))
    remark = Column(String(128))


class ClientAddress(Base):
    __tablename__ = 'ClientAddress'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    type = Column(SmallInteger, index=True)
    address_id = Column(Integer, FKey('Address.id'), index=True)
    freeInput = Column(String(200))
    version = Column(Integer)
    localityType = Column(Integer)


class ClientAllergy(Base):
    __tablename__ = 'ClientAllergy'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    nameSubstance = Column(String(128))
    power = Column(Integer)
    createDate = Column(QDateType)
    notes = Column(String(128))
    version = Column(Integer)


class ClientAttach(Base):
    __tablename__ = 'ClientAttach'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    attachType_id = Column(Integer, index=True)
    LPU_id = Column(Integer, index=True)
    orgStructure_id = Column(Integer, index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    document_id = Column(Integer, FKey('ClientDocument.id'), index=True)


class ClientContact(Base):
    __tablename__ = 'ClientContact'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    contactType_id = Column(Integer, index=True)
    contact = Column(String(48))
    notes = Column(String(80))
    version = Column(Integer)


class ClientDocument(Base):
    __tablename__ = 'ClientDocument'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    documentType_id = Column(Integer, index=True)
    serial = Column(String(8), index=True)
    number = Column(String(16), index=True)
    date = Column(QDateType)
    origin = Column(String(256))
    version = Column(Integer)
    endDate = Column(QDateType)


class ClientIdentification(Base):
    __tablename__ = 'ClientIdentification'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    accountingSystem_id = Column(Integer, index=True)
    identifier = Column(String(16), index=True)
    checkDate = Column(QDateType)
    version = Column(Integer)


class ClientIntoleranceMedicament(Base):
    __tablename__ = 'ClientIntoleranceMedicament'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    nameMedicament = Column(String(128))
    power = Column(Integer)
    createDate = Column(QDateType)
    notes = Column(String(128))
    version = Column(Integer)


class ClientPolicy(Base):
    __tablename__ = 'ClientPolicy'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    insurer_id = Column(Integer, index=True)
    policyType_id = Column(Integer, index=True)
    serial = Column(String(16), index=True)
    number = Column(String(16), index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    name = Column(String(64))
    note = Column(String(200))
    version = Column(Integer)


class ClientRelation(Base):
    __tablename__ = 'ClientRelation'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    relativeType_id = Column(Integer, index=True)
    relative_id = Column(Integer, FKey('Client.id'), index=True)
    version = Column(Integer)


class ClientSocStatus(Base):
    __tablename__ = 'ClientSocStatus'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    socStatusClass_id = Column(Integer, index=True)
    socStatusType_id = Column(Integer, index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    document_id = Column(Integer, index=True)
    version = Column(Integer)
    note = Column(String(256))
    benefitCategory_id = Column(Integer)


class ClientWork(Base):
    __tablename__ = 'ClientWork'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    org_id = Column(Integer, index=True)
    freeInput = Column(String(200))
    post = Column(String(200))
    stage = Column(SmallInteger)
    OKVED = Column(String(10))
    version = Column(Integer)
    rank_id = Column(Integer)
    arm_id = Column(Integer)


class ClientWorkHurt(Base):
    __tablename__ = 'ClientWork_Hurt'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, index=True)
    hurtType_id = Column(Integer, index=True)
    stage = Column(SmallInteger)


class ClientWorkHurtFactor(Base):
    __tablename__ = 'ClientWork_Hurt_Factor'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, index=True)
    factorType_id = Column(Integer, index=True)


class Contract(Base):
    __tablename__ = 'Contract'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    number = Column(String(64))
    date = Column(QDateType)
    recipient_id = Column(Integer, index=True)
    recipientAccount_id = Column(Integer, index=True)
    recipientKBK = Column(String(30))
    payer_id = Column(Integer, index=True)
    payerAccount_id = Column(Integer, index=True)
    payerKBK = Column(String(30))
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    finance_id = Column(Integer, index=True)
    grouping = Column(String(64))
    resolution = Column(String(64))
    format_id = Column(Integer, index=True)
    exposeUnfinishedEventVisits = Column(SmallInteger)
    exposeUnfinishedEventActions = Column(SmallInteger)
    visitExposition = Column(SmallInteger)
    actionExposition = Column(SmallInteger)
    exposeDiscipline = Column(SmallInteger)
    exposeByPeriod = Column(SmallInteger)
    priceList_id = Column(Integer)
    coefficient = Column(Float)
    coefficientEx = Column(Float)
    orgCategory = Column(String(1))
    regionalTariffRegulationFactor = Column(Float)


class ContractContingent(Base):
    __tablename__ = 'Contract_Contingent'
    id = Column(Integer, primary_key=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    client_id = Column(Integer, FKey('Client.id'), index=True)
    attachType_id = Column(Integer, index=True)
    org_id = Column(Integer, index=True)
    socStatusType_id = Column(Integer, index=True)
    insurer_id = Column(Integer, index=True)
    policyType_id = Column(Integer, index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)


class ContractContragent(Base):
    __tablename__ = 'Contract_Contragent'
    id = Column(Integer, primary_key=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    insurer_id = Column(Integer, index=True)
    payer_id = Column(Integer, index=True)
    payerAccount_id = Column(Integer, index=True)
    payerKBK = Column(String(30))
    begDate = Column(QDateType)
    endDate = Column(QDateType)


class ContractSpecification(Base):
    __tablename__ = 'Contract_Specification'
    id = Column(Integer, primary_key=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    eventType_id = Column(Integer, index=True)


class ContractTariff(Base):
    __tablename__ = 'Contract_Tariff'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    eventType_id = Column(Integer, index=True)
    tariffType = Column(SmallInteger)
    service_id = Column(Integer, index=True)
    code = Column(String(64))
    name = Column(String(256))
    tariffCategory_id = Column(Integer, index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    unit_id = Column(Integer, index=True)
    amount = Column(Float)
    uet = Column(Float)
    price = Column(Float)
    limitationExceedMode = Column(Integer)
    limitation = Column(Float)
    priceEx = Column(Float)
    MKB = Column(String(8))
    rbServiceFinance_id = Column(Integer, index=True)


class Diagnosis(Base):
    __tablename__ = 'Diagnosis'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    client_id = Column(Integer, FKey('Client.id'), index=True)
    client = relationship('Client', foreign_keys='Diagnosis.client_id')
    diagnosisType_id = Column(Integer, index=True)
    character_id = Column(Integer, index=True)
    MKB = Column(String(8))
    MKBEx = Column(String(8))
    dispanser_id = Column(Integer, index=True)
    traumaType_id = Column(Integer, index=True)
    setDate = Column(QDateType)
    endDate = Column(QDateType)
    mod_id = Column(Integer, index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    person = relationship('Person', foreign_keys='Diagnosis.person_id')


class Diagnostic(Base):
    __tablename__ = 'Diagnostic'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    event_id = Column(Integer, index=True)
    diagnosis_id = Column(Integer, index=True)
    diagnosisType_id = Column(Integer, index=True)
    character_id = Column(Integer, index=True)
    stage_id = Column(Integer, index=True)
    phase_id = Column(Integer, index=True)
    dispanser_id = Column(Integer, index=True)
    sanatorium = Column(SmallInteger)
    hospital = Column(SmallInteger)
    traumaType_id = Column(Integer, index=True)
    speciality_id = Column(Integer, index=True)
    person_id = Column(Integer, index=True)
    healthGroup_id = Column(Integer, index=True)
    result_id = Column(Integer, index=True)
    setDate = Column(QDateTimeType)
    endDate = Column(QDateTimeType)
    notes = Column(Text)
    rbAcheResult_id = Column(Integer, index=True)
    diagn = Column(String(250))
    version = Column(Integer)
    action_id = Column(Integer, index=True)


class Event(Base):
    __tablename__ = 'Event'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    externalId = Column(String(30))
    eventType_id = Column(Integer, FKey('EventType.id'), index=True)
    eventType = relationship('EventType', foreign_keys='Event.eventType_id')
    org_id = Column(Integer, index=True)
    client_id = Column(Integer, FKey('Client.id'), index=True)
    client = relationship('Client', foreign_keys='Event.client_id')
    contract_id = Column(Integer, FKey('Contract.id'), index=True)
    prevEventDate = Column(QDateTimeType)
    setDate = Column(QDateTimeType, index=True)
    setPerson_id = Column(Integer, FKey('Person.id'), index=True)
    setPerson = relationship('Person', foreign_keys='Event.setPerson_id')
    execDate = Column(QDateTimeType, index=True)
    execPerson_id = Column(Integer, FKey('Person.id'), index=True)
    execPerson = relationship('Person', foreign_keys='Event.execPerson_id')
    isPrimary = Column(SmallInteger)
    order = Column(SmallInteger)
    result_id = Column(Integer, FKey('rbResult.id'), index=True)
    result = relationship('RbResult')
    nextEventDate = Column(QDateTimeType)
    payStatus = Column(Integer)
    typeAsset_id = Column(Integer, index=True)
    note = Column(Text)
    curator_id = Column(Integer, index=True)
    assistant_id = Column(Integer, index=True)
    pregnancyWeek = Column(Integer)
    MES_id = Column(Integer, index=True)
    mesSpecification_id = Column(Integer, index=True)
    rbAcheResult_id = Column(Integer, FKey('rbAcheResult.id'), index=True)
    rbAcheResult = relationship('RbAcheResult', foreign_keys='Event.rbAcheResult_id')
    version = Column(Integer)
    privilege = Column(SmallInteger)
    urgent = Column(SmallInteger)
    addto_vtmp_registry = Column(SmallInteger)
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    orgStructure = relationship('OrgStructure', foreign_keys='Event.orgStructure_id')
    lpu_transfer = Column(String(100))
    localContract_id = Column(Integer, index=True)


class EventFinanceChanges(Base):
    __tablename__ = 'Event_FinanceChanges'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, FKey('Event.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    eventTypeOld_id = Column(Integer, index=True)
    eventTypeNew_id = Column(Integer, index=True)
    financeOld_id = Column(Integer, index=True)
    financeNew_id = Column(Integer, index=True)


class EventLocalContract(Base):
    __tablename__ = 'Event_LocalContract'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    coordDate = Column(QDateTimeType)
    coordAgent = Column(String(128))
    coordInspector = Column(String(128))
    coordText = Column(Text)
    dateContract = Column(QDateType)
    numberContract = Column(String(64))
    sumLimit = Column(Float)
    lastName = Column(String(30), index=True)
    firstName = Column(String(30), index=True)
    patrName = Column(String(30), index=True)
    birthDate = Column(QDateType, index=True)
    documentType_id = Column(Integer, index=True)
    serialLeft = Column(String(8))
    serialRight = Column(String(8))
    number = Column(String(16))
    regAddress = Column(String(64))
    org_id = Column(Integer, index=True)


class EventPayment(Base):
    __tablename__ = 'Event_Payment'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, index=True)
    date = Column(QDateType)
    cashOperation_id = Column(Integer, index=True)
    sum = Column(Float)
    typePayment = Column(SmallInteger)
    settlementAccount = Column(String(64))
    bank_id = Column(Integer, index=True)
    numberCreditCard = Column(String(64))
    cashBox = Column(String(32))
    sumDiscount = Column(Float)
    action_id = Column(Integer, FKey('Action.id'), index=True)
    service_id = Column(Integer, index=True)
    localContract_id = Column(Integer, FKey('Event_LocalContract.id'), index=True)


class EventPersons(Base):
    __tablename__ = 'Event_Persons'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, FKey('Event.id'), index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    begDate = Column(QDateTimeType)
    endDate = Column(QDateTimeType)


class EventType(Base):
    __tablename__ = 'EventType'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    code = Column(String(8), index=True)
    name = Column(String(64))
    purpose_id = Column(Integer, index=True)
    finance_id = Column(Integer, index=True)
    scene_id = Column(Integer, index=True)
    visitServiceModifier = Column(String(128))
    visitServiceFilter = Column(String(32))
    visitFinance = Column(SmallInteger)
    actionFinance = Column(SmallInteger)
    period = Column(SmallInteger)
    singleInPeriod = Column(SmallInteger)
    isLong = Column(SmallInteger)
    dateInput = Column(SmallInteger)
    service_id = Column(Integer, index=True)
    context = Column(String(64))
    form = Column(String(64))
    minDuration = Column(Integer)
    maxDuration = Column(Integer)
    showStatusActionsInPlanner = Column(SmallInteger)
    showDiagnosticActionsInPlanner = Column(SmallInteger)
    showCureActionsInPlanner = Column(SmallInteger)
    showMiscActionsInPlanner = Column(SmallInteger)
    limitStatusActionsInput = Column(SmallInteger)
    limitDiagnosticActionsInput = Column(SmallInteger)
    limitCureActionsInput = Column(SmallInteger)
    limitMiscActionsInput = Column(SmallInteger)
    showTime = Column(SmallInteger)
    medicalAidType_id = Column(Integer, index=True)
    eventProfile_id = Column(Integer, index=True)
    mesRequired = Column(SmallInteger, default='0')
    mesCodeMask = Column(String(64))
    mesNameMask = Column(String(64))
    counter_id = Column(Integer, index=True)
    isExternal = Column(SmallInteger, default='0')
    isAssistant = Column(SmallInteger, default='0')
    isCurator = Column(SmallInteger, default='0')
    canHavePayableActions = Column(SmallInteger, default='0')
    isRequiredCoordination = Column(SmallInteger, default='0')
    isOrgStructurePriority = Column(SmallInteger, default='0')
    isTakenTissue = Column(SmallInteger, default='0')
    sex = Column(SmallInteger, default='0')
    age = Column(String(9))
    rbMedicalKind_id = Column(Integer, index=True)
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    requestType_id = Column(Integer, index=True)


class EventTypeAction(Base):
    __tablename__ = 'EventType_Action'
    id = Column(Integer, primary_key=True)
    eventType_id = Column(Integer, FKey('EventType.id'), index=True)
    idx = Column(Integer, default='0')
    actionType_id = Column(Integer, FKey('EventType.id'), index=True)
    speciality_id = Column(Integer, index=True)
    tissueType_id = Column(Integer, index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    selectionGroup = Column(SmallInteger, default='0')
    actuality = Column(SmallInteger)
    expose = Column(SmallInteger, default='1')
    payable = Column(SmallInteger, default='0')
    academicDegree_id = Column(Integer, index=True)


class EventTypeDiagnostic(Base):
    __tablename__ = 'EventType_Diagnostic'
    id = Column(Integer, primary_key=True)
    eventType_id = Column(Integer, FKey('EventType.id'), index=True)
    idx = Column(Integer, default='0')
    speciality_id = Column(Integer, index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    defaultHealthGroup_id = Column(Integer, index=True)
    defaultMKB = Column(String(5))
    defaultDispanser_id = Column(Integer, index=True)
    selectionGroup = Column(SmallInteger, default='0')
    actuality = Column(SmallInteger)
    visitType_id = Column(Integer, index=True)


class EventTypeForm(Base):
    __tablename__ = 'EventTypeForm'
    id = Column(Integer, primary_key=True)
    deleted = Column(SmallInteger, default='0')
    eventType_id = Column(Integer, FKey('EventType.id'), index=True)
    code = Column(String(8))
    name = Column(String(64))
    descr = Column(String(64))
    pass_ = Column(SmallInteger, name='pass')


class InformerMessage(Base):
    __tablename__ = 'InformerMessage'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    subject = Column(String(128))
    text = Column(Text)


class InformerMessageReadMark(Base):
    __tablename__ = 'InformerMessage_readMark'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('InformerMessage.id'), index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)


class Job(Base):
    __tablename__ = 'Job'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    jobType_id = Column(Integer, index=True)
    orgStructure_id = Column(Integer, index=True)
    date = Column(QDateType)
    begTime = Column(QTimeType)
    endTime = Column(QTimeType)
    quantity = Column(Integer)


class JobTicket(Base):
    __tablename__ = 'Job_Ticket'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('Job.id'), index=True)
    idx = Column(Integer)
    datetime = Column(QDateTimeType)
    resTimestamp = Column(TIMESTAMP)
    resConnectionId = Column(Integer)
    status = Column(SmallInteger)
    begDateTime = Column(QDateTimeType)
    endDateTime = Column(QDateTimeType)
    label = Column(String(64))
    note = Column(String(128))


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    filename = Column(String(256))
    file = Column(Binary)


class MedicalKindUnit(Base):
    __tablename__ = 'MedicalKindUnit'
    id = Column(Integer, primary_key=True)
    rbMedicalKind_id = Column(Integer, index=True)
    eventType_id = Column(Integer, index=True)
    rbMedicalAidUnit_id = Column(Integer, index=True)
    rbPayType_id = Column(Integer, index=True)
    rbTariffType_id = Column(Integer, index=True)


class Meta(Base):
    __tablename__ = 'Meta'
    name = Column(String(100), primary_key=True)
    value = Column(Text)


class MKB(Base):
    __tablename__ = 'MKB'
    id = Column(Integer, primary_key=True)
    ClassID = Column(String(8), index=True)
    ClassName = Column(String(150), index=True)
    BlockID = Column(String(9), index=True)
    BlockName = Column(String(160))
    DiagID = Column(String(8), index=True)
    DiagName = Column(String(160), index=True)
    Prim = Column(String(1))
    sex = Column(SmallInteger)
    age = Column(String(12))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    characters = Column(SmallInteger)
    duration = Column(Integer)
    service_id = Column(Integer, index=True)
    MKBSubclass_id = Column(Integer, index=True)


class MKBQuotaTypePacientModel(Base):
    __tablename__ = 'MKB_QuotaType_PacientModel'
    id = Column(Integer, primary_key=True)
    MKB_id = Column(Integer, index=True)
    pacientModel_id = Column(Integer, index=True)
    quotaType_id = Column(Integer, index=True)


class NotificationOccurred(Base):
    __tablename__ = 'NotificationOccurred'
    id = Column(Integer, primary_key=True)
    eventDatetime = Column(QDateTimeType)
    clientId = Column(Integer, FKey('Client.id'), index=True)
    userId = Column(Integer, index=True)


class Organisation(Base):
    __tablename__ = 'Organisation'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    fullName = Column(String(255))
    shortName = Column(String(255), index=True)
    title = Column(String(255), index=True)
    net_id = Column(Integer, index=True)
    infisCode = Column(String(12), index=True)
    obsoleteInfisCode = Column(String(60))
    OKVED = Column(String(64), index=True)
    INN = Column(String(15), index=True)
    KPP = Column(String(15))
    OGRN = Column(String(15), index=True)
    OKATO = Column(String(15))
    OKPF_code = Column(String(4))
    OKPF_id = Column(Integer, index=True)
    OKFS_code = Column(Integer)
    OKFS_id = Column(Integer, index=True)
    OKPO = Column(String(15))
    FSS = Column(String(10))
    region = Column(String(40))
    Address = Column(String(255))
    chief = Column(String(64))
    phone = Column(String(255))
    accountant = Column(String(64))
    isInsurer = Column(Boolean, index=True)
    compulsoryServiceStop = Column(SmallInteger)
    voluntaryServiceStop = Column(SmallInteger)
    area = Column(String(13))
    isHospital = Column(Boolean)
    notes = Column(Text)
    head_id = Column(Integer, index=True)
    miacCode = Column(String(10))
    isOrganisation = Column(Boolean)
    OID = Column(String(127))


class OrganisationAccount(Base):
    __tablename__ = 'Organisation_Account'
    id = Column(Integer, primary_key=True)
    organisation_id = Column(Integer, FKey('Organisation.id'), index=True)
    bankName = Column(String(128))
    name = Column(String(20))
    notes = Column(Text)
    bank_id = Column(Integer, FKey('Bank.id'), index=True)
    cash = Column(SmallInteger)


class OrganisationPolicySerial(Base):
    __tablename__ = 'Organisation_PolicySerial'
    id = Column(Integer, primary_key=True)
    organisation_id = Column(Integer, FKey('Organisation.id'), index=True)
    serial = Column(String(16))
    policyType_id = Column(Integer, index=True)


class OrgStructure(Base):
    __tablename__ = 'OrgStructure'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    organisation_id = Column(Integer, FKey('Organisation.id'), index=True)
    code = Column(String(255))
    name = Column(String(255))
    parent_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    type = Column(Integer)
    net_id = Column(Integer, index=True)
    chiefPerson_id = Column(Integer, FKey('Person.id'), index=True)
    headNursePerson_id = Column(Integer, FKey('Person.id'), index=True)
    isArea = Column(SmallInteger)
    hasHospitalBeds = Column(Boolean, default='0')
    hasStocks = Column(Boolean, default='0')
    infisCode = Column(String(16))
    infisInternalCode = Column(String(16))
    infisDepTypeCode = Column(String(16))
    infisTariffCode = Column(String(16))
    availableForExternal = Column(SmallInteger, default='1')
    Address = Column(String(255))
    inheritEventTypes = Column(Boolean, default='0')
    inheritActionTypes = Column(Boolean, default='0')
    inheritGaps = Column(Boolean, default='0')
    show = Column(Integer, default='1')  # ?


class OrgStructureActionType(Base):
    __tablename__ = 'OrgStructure_ActionType'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    actionType_id = Column(Integer, FKey('ActionType.id'), index=True)


class OrgStructureAddress(Base):
    __tablename__ = 'OrgStructure_Address'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    house_id = Column(Integer, index=True)
    firstFlat = Column(Integer)
    lastFlat = Column(Integer)


class OrgStructureDisabledAttendance(Base):
    __tablename__ = 'OrgStructure_DisabledAttendance'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    attachType_id = Column(Integer, index=True)
    disabledType = Column(SmallInteger)


class OrgStructureEventType(Base):
    __tablename__ = 'OrgStructure_EventType'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    eventType_id = Column(Integer, FKey('EventType.id'), index=True)


class OrgStructureGap(Base):
    __tablename__ = 'OrgStructure_Gap'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    begTime = Column(QTimeType)
    endTime = Column(QTimeType)
    speciality_id = Column(Integer, index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)


class OrgStructureHospitalBed(Base):
    __tablename__ = 'OrgStructure_HospitalBed'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    code = Column(String(16))
    name = Column(String(64))
    isPermanent = Column(Boolean, default='0')
    type_id = Column(Integer, index=True)
    profile_id = Column(Integer, index=True)
    relief = Column(Integer, default='0')
    schedule_id = Column(Integer, index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    involution = Column(SmallInteger)
    begDateInvolute = Column(QDateType)
    endDateInvolute = Column(QDateType)


class OrgStructureJob(Base):
    __tablename__ = 'OrgStructure_Job'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    jobType_id = Column(Integer, index=True)
    begTime = Column(QTimeType)
    endTime = Column(QTimeType)
    quantity = Column(Integer)


class OrgStructureStock(Base):
    __tablename__ = 'OrgStructure_Stock'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    idx = Column(Integer)
    nomenclature_id = Column(Integer)
    finance_id = Column(Integer)
    constrainedQnt = Column(Float, default='0')
    orderQnt = Column(Float, default='0')


class Person(Base):
    __tablename__ = 'Person'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=QDateTime.currentDateTime())
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    code = Column(String(12))
    federalCode = Column(String(16))
    regionalCode = Column(String(16))
    lastName = Column(String(30), index=True)
    firstName = Column(String(30), index=True)
    patrName = Column(String(30), index=True)
    post_id = Column(Integer, FKey('rbPost.id'), index=True)
    speciality_id = Column(Integer, index=True)
    org_id = Column(Integer, index=True)
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    office = Column(String(8))
    office2 = Column(String(8))
    tariffCategory_id = Column(Integer, index=True)
    finance_id = Column(Integer, index=True)
    retireDate = Column(QDateType, index=True)
    ambPlan = Column(SmallInteger)
    ambPlan2 = Column(SmallInteger)
    ambNorm = Column(SmallInteger)
    homPlan = Column(SmallInteger)
    homPlan2 = Column(SmallInteger)
    homNorm = Column(SmallInteger)
    expPlan = Column(SmallInteger)
    expNorm = Column(SmallInteger)
    login = Column(String(32))
    password = Column(String(32))
    userProfile_id = Column(Integer, index=True)
    retired = Column(Boolean)
    birthDate = Column(QDateType)
    birthPlace = Column(String(64))
    sex = Column(SmallInteger)
    SNILS = Column(String(12))
    INN = Column(String(15))
    availableForExternal = Column(Boolean, default='1')
    primaryQuota = Column(SmallInteger, default='50')
    ownQuota = Column(SmallInteger, default='25')
    consultancyQuota = Column(SmallInteger, default='25')
    externalQuota = Column(SmallInteger, default='10')
    lastAccessibleTimelineDate = Column(QDateType)
    timelineAccessibleDays = Column(Integer, default='0')
    typeTimeLinePerson = Column(Integer)
    academicdegree_id = Column(Integer, FKey('rbAcademicDegree.id'), index=True)
    academicTitle_id = Column(Integer, index=True)
    displayInTimeline = Column(Boolean, default='1')
    maxOverQueue = Column(SmallInteger, default='0')
    maxCito = Column(SmallInteger, default='0')
    quotUnit = Column(SmallInteger, default='0')
    academicDegree = Column(SmallInteger)


class PersonActivity(Base):
    __tablename__ = 'Person_Activity'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('Person.id'), index=True)
    idx = Column(Integer)
    activity_id = Column(Integer, index=True)


class PersonProfiles(Base):
    __tablename__ = 'Person_Profiles'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    userProfile_id = Column(Integer, index=True)


class PersonTimeTemplate(Base):
    __tablename__ = 'Person_TimeTemplate'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, FKey('Person.id'), index=True)
    idx = Column(Integer)
    ambBegTime = Column(QTimeType)
    ambEndTime = Column(QTimeType)
    ambPlan = Column(SmallInteger)
    office = Column(String(8))
    ambBegTime2 = Column(QTimeType)
    ambEndTime2 = Column(QTimeType)
    ambPlan2 = Column(SmallInteger)
    office2 = Column(String(8))
    homBegTime = Column(QTimeType)
    homEndTime = Column(QTimeType)
    homPlan = Column(SmallInteger)
    homBegTime2 = Column(QTimeType)
    homEndTime2 = Column(QTimeType)
    homPlan2 = Column(SmallInteger)


class PersonAddress(Base):
    __tablename__ = 'PersonAddress'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    person_id = Column(Integer, FKey('Person.id'), index=True)
    type = Column(SmallInteger)
    address_id = Column(Integer, FKey('Address.id'), index=True)


class PersonDocument(Base):
    __tablename__ = 'PersonDocument'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    person_id = Column(Integer, FKey('Person.id'), index=True)
    documentType_id = Column(Integer, index=True)
    serial = Column(String(8))
    number = Column(String(16))
    date = Column(QDateType)
    origin = Column(String(64))


class PersonEducation(Base):
    __tablename__ = 'PersonEducation'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    person_id = Column(Integer, FKey('Person.id'), index=True)
    documentType_id = Column(Integer, index=True)
    serial = Column(String(8))
    number = Column(String(16))
    date = Column(QDateType)
    origin = Column(String(64))
    status = Column(String(64))
    validFromDate = Column(QDateType)
    validToDate = Column(QDateType)
    speciality_id = Column(Integer, index=True)
    cost = Column(Float)


class PersonOrder(Base):
    __tablename__ = 'PersonOrder'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    person_id = Column(Integer, FKey('Person.id'), index=True)
    date = Column(QDateType)
    type = Column(String(64))
    documentDate = Column(QDateType)
    documentNumber = Column(String(16))
    documentType_id = Column(Integer, index=True)
    salary = Column(String(64))
    validFromDate = Column(QDateType)
    validToDate = Column(QDateType)
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    post_id = Column(Integer, index=True)


class QuotaType(Base):
    __tablename__ = 'QuotaType'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    class_ = Column(SmallInteger, nullable=False)
    group_code = Column(String(16))
    code = Column(String(16))
    name = Column(String(256))
    teenOlder = Column(SmallInteger)


class Quoting(Base):
    __tablename__ = 'Quoting'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    quotaType_id = Column(Integer, index=True)
    beginDate = Column(QDateTimeType)
    endDate = Column(QDateTimeType)
    limitation = Column(SmallInteger, default='0')
    used = Column(SmallInteger, default='0')
    confirmed = Column(SmallInteger, default='0')
    inQueue = Column(SmallInteger, default='0')


class QuotingRegion(Base):
    __tablename__ = 'Quoting_Region'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    master_id = Column(Integer, FKey('Quoting.id'), index=True)
    region_code = Column(String(13), index=True)
    limitation = Column(SmallInteger, default='0')
    used = Column(SmallInteger, default='0')
    confirmed = Column(SmallInteger, default='0')
    inQueue = Column(SmallInteger, default='0')


class QuotingBySpeciality(Base):
    __tablename__ = 'QuotingBySpeciality'
    id = Column(Integer, primary_key=True)
    speciality_id = Column(Integer, index=True)
    organisation_id = Column(Integer, index=True)
    coupons_quote = Column(Integer)
    coupons_remaining = Column(Integer)


class QuotingByTime(Base):
    __tablename__ = 'QuotingByTime'
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, index=True)
    quoting_date = Column(QDateType)
    QuotingTimeStart = Column(QTimeType)
    QuotingTimeEnd = Column(QTimeType)
    QuotingType = Column(Integer)


class SocStatus(Base):
    __tablename__ = 'SocStatus'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    socStatusClass_id = Column(Integer, FKey('rbSocStatusClass.id'), index=True)
    socStatusType_id = Column(Integer, FKey('rbSocStatusType.id'), index=True)


class StockMotion(Base):
    __tablename__ = 'StockMotion'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    type = Column(SmallInteger, default='0')
    date = Column(QDateTimeType)
    supplier_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    receiver_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    note = Column(Text)
    supplierPerson_id = Column(Integer, FKey('Person.id'), index=True)
    receiverPerson_id = Column(Integer, FKey('Person.id'), index=True)


class StockMotionItem(Base):
    __tablename__ = 'StockMotion_Item'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('StockMotion.id'), index=True)
    idx = Column(Integer, default='0')
    nomenclature_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    finance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    qnt = Column(Float, default='0')
    sum = Column(Float, default='0')
    oldQnt = Column(Float, default='0')
    oldSum = Column(Float, default='0')
    oldFinance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    isOut = Column(SmallInteger, default='0')
    note = Column(Text)


class StockRecipe(Base):
    __tablename__ = 'StockRecipe'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    group_id = Column(Integer, FKey('StockRecipe.id'), index=True)
    code = Column(String(32), index=True)
    name = Column(String(64), index=True)


class StockRecipeItem(Base):
    __tablename__ = 'StockRecipe_Item'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('StockRecipe.id'), index=True)
    idx = Column(Integer, default='0')
    nomenclature_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    qnt = Column(Float, default='0')
    isOut = Column(SmallInteger, default='0')


class StockRequisition(Base):
    __tablename__ = 'StockRequisition'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'),  index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    date = Column(QDateType)
    deadline = Column(QDateTimeType)
    supplier_id = Column(Integer, FKey('OrgStructure.id', onupdate='CASCADE'), index=True)
    recipient_id = Column(Integer, FKey('OrgStructure.id', onupdate='CASCADE'), index=True)
    revoked = Column(SmallInteger, default='0')
    note = Column(Text)


class StockRequisitionItem(Base):
    __tablename__ = 'StockRequisition_Item'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('StockRequisition.id'), index=True)
    idx = Column(Integer, default='0')
    nomenclature_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    finance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    qnt = Column(Float, default='0')
    satisfiedQnt = Column(Float, default='0')


class StockTrans(Base):
    __tablename__ = 'StockTrans'
    id = Column(Integer, primary_key=True)
    stockMotionItem_id = Column(Integer, FKey('StockMotion_Item.id'), index=True)
    date = Column(QDateTimeType)
    qnt = Column(Float, default='0')
    sum = Column(Float, default='0')
    debOrgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    debNomenclature_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    debFinance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    creOrgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    creNomenclature_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    creFinance_id = Column(Integer, FKey('rbFinance.id'), index=True)


class TakenTissueJournal(Base):
    __tablename__ = 'TakenTissueJournal'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, FKey('Client.id'), index=True)
    tissueType_id = Column(Integer, FKey('rbTissueType.id'), index=True)
    externalId = Column(String(30))
    amount = Column(Integer, default='0')
    unit_id = Column(Integer, FKey('rbUnit.id'), index=True)
    datetimeTaken = Column(QDateTimeType)
    execPerson_id = Column(Integer, FKey('Person.id'), index=True)
    note = Column(String(128))
    barcode = Column(Integer)
    period = Column(Integer)


class TempInvalid(Base):
    __tablename__ = 'TempInvalid'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    type = Column(SmallInteger, default='0')
    doctype = Column(SmallInteger)
    doctype_id = Column(Integer, FKey('rbTempInvalidDocument.id'), index=True)
    serial = Column(String(8))
    number = Column(String(16))
    client_id = Column(Integer, FKey('Client.id'), index=True)
    tempInvalidReason_id = Column(
        Integer, FKey('rbTempInvalidReason.id'), index=True)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    diagnosis_id = Column(Integer, FKey('Diagnosis.id'), index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    notes = Column(Text)
    duration = Column(Integer)
    closed = Column(SmallInteger)
    prev_id = Column(Integer, FKey('TempInvalid.id'), index=True)
    insuranceOfficeMark = Column(SmallInteger, default='0')
    caseBegDate = Column(QDateType)
    event_id = Column(Integer, FKey('Event.id'), index=True)
    tempInvalidExtraReason_id = Column(
        Integer, FKey('rbTempInvalidExtraReason.id'), index=True)
    busyness = Column(SmallInteger, default='0')
    placeWork = Column(String(64))


class TempInvalidPeriod(Base):
    __tablename__ = 'TempInvalid_Period'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('TempInvalid.id'), index=True)
    diagnosis_id = Column(Integer, FKey('Diagnosis.id'), index=True)
    begPerson_id = Column(Integer, FKey('Person.id'), index=True)
    begDate = Column(QDateType)
    endPerson_id = Column(Integer, FKey('Person.id'), index=True)
    endDate = Column(QDateType)
    isExternal = Column(SmallInteger)
    regime_id = Column(Integer, FKey('rbTempInvalidRegime.id'), index=True)
    break_id = Column(Integer, FKey('rbTempInvalidBreak.id'), index=True)
    result_id = Column(Integer, FKey('rbTempInvalidResult.id'), index=True)
    note = Column(Text)
    numberPermit = Column(String(64))
    begDatePermit = Column(QDateType)
    endDatePermit = Column(QDateType)
    disability_id = Column(Integer, FKey('rbTempInvalidRegime.id'), index=True)
    directDateOnKAK = Column(QDateType)
    expert_id = Column(Integer, FKey('Person.id'), index=True)
    dateKAK = Column(QDateType)


class TempInvalidDuplicate(Base):
    __tablename__ = 'TempInvalidDuplicate'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now,
                            onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    tempInvalid_id = Column(Integer, FKey('TempInvalid.id'), index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    date = Column(QDateType)
    serial = Column(String(8))
    number = Column(String(16))
    destination = Column(String(128))
    reason_id = Column(Integer, FKey('rbTempInvalidDuplicateReason.id'), index=True)
    note = Column(Text)
    insuranceOfficeMark = Column(SmallInteger, default='0')
    placeWork = Column(String(64))


class Tissue(Base):
    __tablename__ = 'Tissue'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, FKey('rbTissueType.id'), index=True)
    date = Column(QDateTimeType)
    barcode = Column(String(255))
    event_id = Column(Integer, FKey('Event.id'), index=True)


class Versions(Base):
    __tablename__ = 'Versions'
    id = Column(Integer, primary_key=True)
    table = Column(String(64))
    version = Column(Integer, default='0')


class Visit(Base):
    __tablename__ = 'Visit'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'), index=True)
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'), index=True)
    deleted = Column(SmallInteger, default='0')
    event_id = Column(Integer, FKey('Event.id'), index=True)
    event = relationship('Event', foreign_keys='Visit.event_id')
    scene_id = Column(Integer, FKey('rbScene.id'), index=True)
    date = Column(QDateTimeType)
    visitType_id = Column(Integer, FKey('rbVisitType.id'), index=True)
    person_id = Column(Integer, FKey('Person.id'), index=True)
    person = relationship('Person', foreign_keys='Visit.person_id')
    isPrimary = Column(Boolean)
    finance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    service_id = Column(Integer, FKey('rbService.id'), index=True)
    payStatus = Column(Integer)


class VBalanceOfGoods(Base):
    __tablename__ = 'vBalanceOfGoods'
    id = Column(Integer, primary_key=True)
    rlsNomen_id = Column(Integer, FKey('rlsNomen.id'))
    value = Column(Float)
    bestBefore = Column(QDateType)
    disabled = Column(Boolean, default='0')
    updateDateTime = Column(QDateTimeType)
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'))


class VClientQuoting(Base):
    __tablename__ = 'vClient_Quoting'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'))
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'))
    deleted = Column(Boolean, default='0')
    master_id = Column(Integer)
    identifier = Column(String(16))
    quotaTicket = Column(String(20))
    quotaType_id = Column(Integer)
    stage = Column(Integer)
    directionDate = Column(QDateTimeType)
    freeInput = Column(String(128))
    org_id = Column(Integer)
    amount = Column(Integer, default='0')
    MKB = Column(String(8))
    status = Column(Integer, default='0')
    request = Column(Integer, default='0')
    statment = Column(String(255))
    dateRegistration = Column(QDateTimeType)
    dateEnd = Column(QDateTimeType)
    orgStructure_id = Column(Integer)
    regionCode = Column(String(13))
    pacientModel_id = Column(Integer)
    treatment_id = Column(Integer)
    event_id = Column(Integer)
    prevTalon_event_id = Column(Integer)


class VClientQuotingHistory(Base):
    __tablename__ = 'vClient_Quoting_History'
    id = Column(Integer, primary_key=True)
    modifyPerson = Column(String(32))
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    client_id = Column(Integer)
    identifier = Column(String(16))
    quotaTicket = Column(String(20))
    quotaCode = Column(String(16))
    stage = Column(Integer)
    directionDate = Column(QDateTimeType)
    freeInput = Column(String(128))
    organ = Column(String(255))
    amount = Column(Integer)
    MKB = Column(String(8))
    status = Column(String(50))
    request = Column(SmallInteger)
    statment = Column(String(255))
    dateRegistration = Column(QDateTimeType)
    dateEnd = Column(QDateTimeType)
    orgStruct = Column(String(255))
    regionCode = Column(String(13))
    patientModelCode = Column(String(32))
    treatmentCode = Column(String(32))
    event_id = Column(Integer, FKey('Event.id'))
    prevTalon_event_id = Column(Integer, FKey('Event.id'))


class VClientQuotingSub(Base):
    __tablename__ = 'vClient_Quoting_sub'
    id = Column(Integer, primary_key=True)
    createDatetime = Column(QDateTimeType, default=datetime.datetime.now)
    createPerson_id = Column(Integer, FKey('Person.id'))
    modifyDatetime = Column(QDateTimeType, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    modifyPerson_id = Column(Integer, FKey('Person.id'))
    deleted = Column(Boolean, default='0')
    master_id = Column(Integer)
    identifier = Column(String(16))
    quotaTicket = Column(String(20))
    quotaType_id = Column(Integer)
    stage = Column(Integer)
    directionDate = Column(QDateTimeType)
    freeInput = Column(String(128))
    org_id = Column(Integer)
    amount = Column(Integer, default='0')
    MKB = Column(String(8))
    status = Column(Integer, default='0')
    request = Column(Integer, default='0')
    statment = Column(String(255))
    dateRegistration = Column(QDateTimeType)
    dateEnd = Column(QDateTimeType)
    orgStructure_id = Column(Integer)
    regionCode = Column(String(13))
    pacientModel_id = Column(Integer)
    treatment_id = Column(Integer)
    event_id = Column(Integer, FKey('Event.id'))
    prevTalon_event_id = Column(Integer, FKey('Event.id'))


class VHospitalBed(Base):
    __tablename__ = 'vHospitalBed'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('OrgStructure.id'))
    idx = Column(Integer)
    code = Column(String(16))
    name = Column(String(64))
    isPermanent = Column(Boolean, default='0')
    type_id = Column(Integer)
    profile_id = Column(Integer)
    relief = Column(Integer)
    schedule_id = Column(Integer)
    begDate = Column(QDateType)
    endDate = Column(QDateType)
    sex = Column(SmallInteger)
    isTransportable = Column(SmallInteger)
    age = Column(String(9))
    involution = Column(SmallInteger)
    begDateInvolute = Column(QDateType)
    endDateInvolute = Column(QDateType)
    isBusy = Column(SmallInteger)


class VJobTicket(Base):
    __tablename__ = 'vJobTicket'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('Job.id'), index=True)
    idx = Column(Integer)
    datetime = Column(QDateTimeType)
    resTimestamp = Column(TIMESTAMP)
    resConnectionId = Column(Integer)
    isReserved = Column(SmallInteger)
    isUsed = Column(SmallInteger)
    deleted = Column(Boolean)
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'))
    jobType_id = Column(Integer, FKey('rbJobType.id'))
    date = Column(QDateType)


class VNomen(Base):
    __tablename__ = 'vNomen'
    id = Column(Integer, primary_key=True)
    tradeName = Column(String(255))
    tradeLocalName = Column(String(255))
    tradeName_id = Column(Integer)
    actMattersName = Column(String(255))
    actMattersLocalName = Column(String(255))
    actMatters_id = Column(Integer)
    form = Column(String(128))
    packing = Column(String(128))
    filling = Column(String(128))
    unit_id = Column(Integer)
    unitCode = Column(String(256))
    unitName = Column(String(256))
    dosageValue = Column(String(128))
    dosageUnit_id = Column(Integer)
    dosageUnitCode = Column(String(256))
    dosageUnitName = Column(String(256))
    regDate = Column(QDateType)
    annDate = Column(QDateType)
    drugLifetime = Column(Integer)


class VrbBackwardClientRelation(Base):
    __tablename__ = 'vrbBackwardClientRelation'
    id = Column(Integer, primary_key=True)
    code = Column(String(32))
    name = Column(String(128))


class VrbDirectClientRelation(Base):
    __tablename__ = 'vrbDirectClientRelation'
    id = Column(Integer, primary_key=True)
    code = Column(String(32))
    name = Column(String(128))


class VrbMKBZ(Base):
    __tablename__ = 'vrbMKBZ'
    id = Column(Integer, primary_key=True)
    code = Column(String(9))
    name = Column(String(160))


class VrbPerson(Base):
    __tablename__ = 'vrbPerson'
    id = Column(Integer, primary_key=True)
    code = Column(String(12))
    name = Column(String(64))
    speciality_id = Column(Integer)
    org_id = Column(Integer)
    orgStructure_id = Column(Integer)
    retireDate = Column(QDateType)


class VrbPersonWithSpeciality(Base):
    __tablename__ = 'vrbPersonWithSpeciality'
    id = Column(Integer, FKey('Person.id'), primary_key=True)
    person = relationship('Person', foreign_keys='VrbPersonWithSpeciality.id')
    code = Column(String(12))
    deleted = Column(Boolean)
    name = Column(String(128))
    speciality_id = Column(Integer)
    org_id = Column(Integer)
    orgStructure_id = Column(Integer)
    retireDate = Column(QDateType)


class VrbSocStatusType(Base):
    __tablename__ = 'vrbSocStatusType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8))
    name = Column(String(250))
    class_id = Column(Integer)
