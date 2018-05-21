# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from PyQt4.QtCore import QDateTime
from sqlalchemy import func, and_, or_, alias
from sqlalchemy.orm import aliased
from structure import ref, tables as tbl, database as db, kladr


db.dal.connect()

def getActionTypeIdList2(flatCode):
    session = db.dal.Session()
    stmt = session.query(
        tbl.ActionType.id
    ).filter(
        tbl.ActionType.flatCode.like(flatCode),
        tbl.ActionType.deleted == 0
    ).all()
    return [rec[0] for rec in stmt]



def getDataOrgStructure2(nameProperty, orgStructureIdList):
    orgStructureList = [None]
    for orgStructureId in orgStructureIdList:
        orgStructureList.append(orgStructureId)

    tblAPT = aliased(tbl.ActionPropertyType)
    tblAP = aliased(tbl.ActionProperty)
    tblAPOS = aliased(tbl.ActionPropertyOrgStructure)
    tblOS = aliased(tbl.OrgStructure)

    session = db.dal.Session()
    stmt = session.query(tblAPOS.value)\
        .select_from(tblAPT)\
        .join(tblAP, tblAP.type_id == tblAPT.id)\
        .join(tblAPOS, tblAPOS.id == tblAP.id)\
        .join(tblOS, tblOS.id == tblAPOS.value)\
        .filter(tblAPT.actionType_id == tbl.Action.actionType_id,
                tblAP.action_id == tbl.Action.id,
                tblAPT.deleted == 0,
                tblAPT.name.like(nameProperty),
                tblOS.deleted == 0,
                tblAPOS.value.in_(orgStructureIdList)
                ).exists()
    print(stmt)
    return stmt


def isValidAPHB2(permanent=0, type=None, profile=None):
    session = db.dal.Session()
    tblAPT = aliased(tbl.ActionPropertyType)
    tblAP = aliased(tbl.ActionProperty)
    tblAPHB = aliased(tbl.ActionPropertyHospitalBed)
    tblOSHB = aliased(tbl.OrgStructureHospitalBed)
    stmt = session.query(tblAPHB.value)\
        .select_from(tblAPT)\
        .join(tblAP, tblAP.type_id == tblAPT.id)\
        .join(tblAPHB, tblAPHB.id == tblAP.id)\
        .join(tblOSHB, tblOSHB.id == tblAPHB.value)\
        .filter(tblAPT.actionType_id == tbl.Action.actionType_id,
                tblAP.action_id == tbl.Action.id,
                tblAP.deleted == 0,
                tblAPT.deleted == 0,
                tblAPT.name.like('HospitalBed')
                ).exists()

    if permanent and permanent > 0:
        stmt = stmt.filter(tblOSHB.isPermanent == permanent-1)
    if type:
        stmt = stmt.filter(tblOSHB.type_id == type)
    if profile:
        stmt = stmt.filter(tblOSHB.profile_id == profile)

    print(stmt)
    return stmt


orgStructureIdList = [19]
currentDate = QDateTime.currentDateTime()

session = db.dal.Session()

queryTable = session.query(
    tbl.Action.id,
    tbl.Event.id.label('eventId'),
    tbl.Event.client_id,
    tbl.Client.lastName,
    tbl.Client.firstName,
    tbl.Client.patrName,
    tbl.Client.sex,
    tbl.Client.birthDate,
    tbl.Action.begDate,
    tbl.Action.endDate,
    tbl.Action.plannedEndDate,
    tbl.VrbPersonWithSpeciality.name.label('namePerson'),
    func.IF(and_(tbl.OrgStructure.id.isnot(None), tbl.OrgStructure.deleted == 0),
            tbl.OrgStructure.code, None).label('nameOS'),
    func.IF(and_(tbl.Contract.id.isnot(None), tbl.Contract.deleted == 0),
            ref.RbFinance.code, None).label('codeFinance'),
    func.IF(and_(tbl.Contract.id.isnot(None), tbl.Contract.deleted == 0),
            ref.RbFinance.name, None).label('nameFinance')
).select_from(tbl.Action)\
    .join(tbl.ActionType)\
    .join(tbl.Event)\
    .join(tbl.Client)\
    .join(tbl.ActionPropertyType)\
    .join(tbl.ActionProperty)\
    .join(tbl.VrbPersonWithSpeciality, tbl.VrbPersonWithSpeciality.id == tbl.Action.person_id)\
    .join(tbl.ActionPropertyOrgStructure, tbl.ActionPropertyOrgStructure.id == tbl.ActionProperty.id)\
    .join(tbl.OrgStructure, tbl.OrgStructure.id == tbl.ActionPropertyOrgStructure.value)\
    .filter(tbl.Action.actionType_id.in_(getActionTypeIdList2('moving%')),
            tbl.Action.deleted == 0,
            tbl.Event.deleted == 0,
            tbl.ActionProperty.deleted == 0,
            tbl.Client.deleted == 0,
            tbl.ActionProperty.action_id == tbl.Action.id
            )

queryTable = queryTable\
    .join(tbl.Contract, tbl.Contract.id == tbl.Event.contract_id)\
    .join(ref.RbFinance, ref.RbFinance.id == tbl.Contract.finance_id)

if orgStructureIdList:
    queryTable = queryTable.filter(
        tbl.OrgStructure.deleted == 0,
        getDataOrgStructure2('Отделение пребывания', orgStructureIdList)
    )
queryTable = queryTable\
    .filter(tbl.ActionPropertyType.name.like('Отделение пребывания'))\
    .filter(tbl.Action.endDate.is_(None))\
    .filter(tbl.Action.begDate < currentDate.addDays(1))

queryTable = queryTable.filter(isValidAPHB2())

records = queryTable.order_by(tbl.Client.lastName).all()

for rec in records:
    print(records)