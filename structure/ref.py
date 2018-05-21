from sqlalchemy import ForeignKey as FKey
from .tables import Base
from sqlalchemy import (Column, Integer, CHAR, SmallInteger, String, ForeignKey,
                        DateTime, Date, Time, Enum, Float, Text, Binary)


class RbAcademicDegree(Base):
    __tablename__ = 'rbAcademicDegree'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbAcademicTitle(Base):
    __tablename__ = 'rbAcademicTitle'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbAccountExportFormat(Base):
    __tablename__ = 'rbAccountExportFormat'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    prog = Column(String(128))
    preferentArchiver = Column(String(128))
    emailRequired = Column(SmallInteger)
    emailTo = Column(String(64))
    subject = Column(String(128))
    message = Column(Text)


class RbAccountingSystem(Base):
    __tablename__ = 'rbAccountingSystem'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    isEditable = Column(SmallInteger)
    showInClientInfo = Column(SmallInteger)


class RbAcheResult(Base):
    __tablename__ = 'rbAcheResult'
    id = Column(Integer, primary_key=True)
    eventPurpose_id = Column(Integer, index=True)
    code = Column(String(3))
    name = Column(String(64))


class RbActionShedule(Base):
    __tablename__ = 'rbActionShedule'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    period = Column(SmallInteger)


class RbActionSheduleItem(Base):
    __tablename__ = 'rbActionShedule_Item'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('rbActionShedule.id'), index=True)
    idx = Column(Integer)
    offset = Column(SmallInteger)
    time = Column(Time)


class RbActivity(Base):
    __tablename__ = 'rbActivity'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    regionalCode = Column(String(8), index=True)


class RbAgreementType(Base):
    __tablename__ = 'rbAgreementType'
    id = Column(Integer, primary_key=True)
    code = Column(String(32), index=True)
    name = Column(String(64), index=True)
    quotaStatusModifier = Column(Integer)


class RbAnalysisStatus(Base):
    __tablename__ = 'rbAnalysisStatus'
    id = Column(Integer, primary_key=True)
    statusName = Column(String(80), index=True)


class RbAnalyticalReports(Base):
    __tablename__ = 'rbAnalyticalReports'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), index=True)
    groupName = Column(String(45), index=True)
    PrintTemplate_id = Column(Integer)


class RbAntibiotic(Base):
    __tablename__ = 'rbAntibiotic'
    id = Column(Integer, primary_key=True)
    code = Column(String(128), index=True)
    name = Column(String(256), index=True)


class RbAppointmentOrder(Base):
    __tablename__ = 'rbAppointmentOrder'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(128), index=True)
    TFOMScode_hosp = Column(String(16))
    TFOMScode_account = Column(String(16))


class RbAPTable(Base):
    __tablename__ = 'rbAPTable'
    id = Column(Integer, primary_key=True)
    code = Column(String(50), index=True)
    name = Column(String(256), index=True)
    tableName = Column(String(256))
    masterField = Column(String(256))


class RbAPTableField(Base):
    __tablename__ = 'rbAPTableField'
    id = Column(Integer, primary_key=True)
    idx = Column(Integer)
    master_id = Column(Integer, FKey('rbAPTable.id'), index=True)
    name = Column(String(256))
    fieldName = Column(String(256))
    referenceTable = Column(String(256))


class RbAttachType(Base):
    __tablename__ = 'rbAttachType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    temporary = Column(SmallInteger)
    outcome = Column(SmallInteger)
    finance_id = Column(Integer, index=True)


class RbBlankActions(Base):
    __tablename__ = 'rbBlankActions'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)
    doctype_id = Column(Integer, FKey('ActionType.id'), index=True)
    checkingSerial = Column(SmallInteger)
    checkingNumber = Column(SmallInteger)
    checkingAmount = Column(SmallInteger)


class RbBlankTempInvalids(Base):
    __tablename__ = 'rbBlankTempInvalids'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)
    doctype_id = Column(Integer, FKey('rbTempInvalidDocument.id'), index=True)
    checkingSerial = Column(SmallInteger)
    checkingNumber = Column(SmallInteger)
    checkingAmount = Column(SmallInteger)


class RbBloodType(Base):
    __tablename__ = 'rbBloodType'
    id = Column(Integer, primary_key=True)
    code = Column(String(32), index=True)
    name = Column(String(64), index=True)


class RbBloodComponentType(Base):
    __tablename__ = 'rbBloodComponentType'
    id = Column(Integer, primary_key=True)
    code = Column(String(32))
    name = Column(String(256))


class RbCashOperation(Base):
    __tablename__ = 'rbCashOperation'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)


class RbComplain(Base):
    __tablename__ = 'rbComplain'
    id = Column(Integer, primary_key=True)
    code = Column(String(64), index=True)
    name = Column(String(120), index=True)
    group_id = Column(Integer, FKey('rbComplain.id'), index=True)


class RbContactType(Base):
    __tablename__ = 'rbContactType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbCounter(Base):
    __tablename__ = 'rbCounter'
    id = Column(Integer, primary_key=True)
    code = Column(String(8))
    name = Column(String(64))
    value = Column(Integer, default='0')
    prefix = Column(String(32))
    postfix = Column(String(32))
    separator = Column(String(8))
    reset = Column(SmallInteger, default='0')
    startDate = Column(DateTime)
    resetDate = Column(DateTime)
    sequenceFlag = Column(SmallInteger)


class RbDiagnosisType(Base):
    __tablename__ = 'rbDiagnosisType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    replaceInDiagnosis = Column(String(8))
    flatCode = Column(String(64))


class RbDiet(Base):
    __tablename__ = 'rbDiet'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbDiseaseCharacter(Base):
    __tablename__ = 'rbDiseaseCharacter'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    replaceInDiagnosis = Column(String(8))


class RbDiseasePhases(Base):
    __tablename__ = 'rbDiseasePhases'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    characterRelation = Column(Integer, default='0')


class RbDiseaseStage(Base):
    __tablename__ = 'rbDiseaseStage'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    characterRelation = Column(Integer, default='0')


class RbDispanser(Base):
    __tablename__ = 'rbDispanser'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    observed = Column(SmallInteger)


class RbDocumentType(Base):
    __tablename__ = 'rbDocumentType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    regionalCode = Column(String(16))
    group_id = Column(Integer, FKey('rbDocumentTypeGroup.id'), index=True)
    serial_format = Column(Integer)
    number_format = Column(Integer)
    federalCode = Column(String(8))
    socCode = Column(String(8), index=True)
    TFOMSCode = Column(Integer)


class RbDocumentTypeGroup(Base):
    __tablename__ = 'rbDocumentTypeGroup'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbEventProfile(Base):
    __tablename__ = 'rbEventProfile'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)
    regionalCode = Column(String(16), index=True)


class RbEventTypePurpose(Base):
    __tablename__ = 'rbEventTypePurpose'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    codePlace = Column(String(2))


class RbFinance(Base):
    __tablename__ = 'rbFinance'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbHealthGroup(Base):
    __tablename__ = 'rbHealthGroup'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbHospitalBedProfile(Base):
    __tablename__ = 'rbHospitalBedProfile'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    service_id = Column(Integer, FKey('rbService.id'), index=True)


class RbHospitalBedProfileService(Base):
    __tablename__ = 'rbHospitalBedProfile_Service'
    id = Column(Integer, primary_key=True)
    rbHospitalBedProfile_id = Column(
        Integer, FKey('rbHospitalBedProfile.id'), index=True)
    rbService_id = Column(Integer, FKey('rbService.id'), index=True)


class RbHospitalBedShedule(Base):
    __tablename__ = 'rbHospitalBedShedule'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbHospitalBedType(Base):
    __tablename__ = 'rbHospitalBedType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbHurtFactorType(Base):
    __tablename__ = 'rbHurtFactorType'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(250), index=True)


class RbHurtType(Base):
    __tablename__ = 'rbHurtType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(256), index=True)


class RbImageMap(Base):
    __tablename__ = 'rbImageMap'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    image = Column(Binary)
    markSize = Column(SmallInteger)


class RbJobType(Base):
    __tablename__ = 'rbJobType'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, FKey('rbJobType.id'), index=True)
    code = Column(String(64), index=True)
    regionalCode = Column(String(64), index=True)
    name = Column(String(128), index=True)
    laboratory_id = Column(Integer, FKey('rbLaboratory.id'), index=True)
    isInstant = Column(SmallInteger, default='0')


class RbLaboratory(Base):
    __tablename__ = 'rbLaboratory'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)
    protocol = Column(Integer)
    address = Column(String(128))
    ownName = Column(String(128))
    labName = Column(String(128))


class RbLaboratoryTest(Base):
    __tablename__ = 'rbLaboratory_Test'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('rbLaboratory_Test.id'), index=True)
    test_id = Column(Integer, FKey('rbTest.id'), index=True)
    book = Column(String(64), index=True)
    code = Column(String(64), index=True)


class RbMealTime(Base):
    __tablename__ = 'rbMealTime'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    begTime = Column(Time)
    endTime = Column(Time)


class RbMedicalAidProfile(Base):
    __tablename__ = 'rbMedicalAidProfile'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    regionalCode = Column(String(16), index=True)
    name = Column(String(64), index=True)


class RbMedicalAidType(Base):
    __tablename__ = 'rbMedicalAidType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbMedicalAidUnit(Base):
    __tablename__ = 'rbMedicalAidUnit'
    id = Column(Integer, primary_key=True)
    code = Column(String(10), index=True)
    name = Column(String(64), index=True)
    descr = Column(String(64))
    regionalCode = Column(String(1), index=True)


class RbMedicalKind(Base):
    __tablename__ = 'rbMedicalKind'
    id = Column(Integer, primary_key=True)
    code = Column(String(1), index=True)
    name = Column(String(64), index=True)


class RbMenu(Base):
    __tablename__ = 'rbMenu'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbMenuContent(Base):
    __tablename__ = 'rbMenu_Content'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('rbMenu_Content.id'), index=True)
    mealTime_id = Column(Integer, FKey('rbMealTime.id'), index=True)
    diet_id = Column(Integer, FKey('rbDiet.id'), index=True)


class RbMesSpecification(Base):
    __tablename__ = 'rbMesSpecification'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    regionalCode = Column(String(16), index=True)
    name = Column(String(64), index=True)
    done = Column(SmallInteger)


class RbMethodOfAdministration(Base):
    __tablename__ = 'rbMethodOfAdministration'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)


class RbMicroorganism(Base):
    __tablename__ = 'rbMicroorganism'
    id = Column(Integer, primary_key=True)
    code = Column(String(128), index=True)
    name = Column(String(256), index=True)


class RbMKBSubclass(Base):
    __tablename__ = 'rbMKBSubclass'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(128), index=True)


class RbMKBSubclassItem(Base):
    __tablename__ = 'rbMKBSubclass_Item'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('rbMKBSubclass.id'), index=True)
    code = Column(String(8), index=True)
    name = Column(String(128), index=True)


class RbNet(Base):
    __tablename__ = 'rbNet'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    sex = Column(SmallInteger, default='0')
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)


class RbNomenclature(Base):
    __tablename__ = 'rbNomenclature'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, FKey('rbNomenclature.id'), index=True)
    code = Column(String(64), index=True)
    regionalCode = Column(String(64), index=True)
    name = Column(String(128), index=True)


class RbOKFS(Base):
    __tablename__ = 'rbOKFS'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    ownership = Column(SmallInteger, default='0')


class RbOKPF(Base):
    __tablename__ = 'rbOKPF'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbOKVED(Base):
    __tablename__ = 'rbOKVED'
    id = Column(Integer, primary_key=True)
    code = Column(String(10), index=True)
    div = Column(String(10))
    class_ = Column(String(2), name='class')
    group_ = Column(String(2))
    vid = Column(String(2))
    OKVED = Column(String(8), index=True)
    name = Column(String(250), index=True)


class RbOperationClass(Base):
    __tablename__ = 'rbOperationClass'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(200), index=True)


class RbOperationType(Base):
    __tablename__ = 'rbOperationType'
    id = Column(Integer, primary_key=True)
    cd_r = Column(Integer)
    cd_subr = Column(Integer)
    code = Column(String(10), index=True)
    ktso = Column(Integer)
    name = Column(String(100), index=True)
    operationClass_id = Column(Integer, FKey('rbOperationClass.id'), index=True)
    TFOMSCode = Column(String(20))


class RbPacientModel(Base):
    __tablename__ = 'rbPacientModel'
    id = Column(Integer, primary_key=True)
    code = Column(String(32))
    name = Column(Text)
    quotaType_id = Column(Integer, FKey('QuotaType.id'), index=True)


class RbPayRefuseType(Base):
    __tablename__ = 'rbPayRefuseType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(128), index=True)
    finance_id = Column(Integer, FKey('rbFinance.id'), index=True)
    rerun = Column(SmallInteger)


class RbPayType(Base):
    __tablename__ = 'rbPayType'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), index=True)
    name = Column(String(64), index=True)


class RbPlanningHospitalActivitis(Base):
    __tablename__ = 'rbPlanningHospitalActivitis'
    id = Column(Integer, primary_key=True)
    year = Column(Integer, default='0')
    month = Column(Integer, default='0')
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)
    profile_id = Column(Integer, FKey('rbHospitalBedProfile.id'), index=True)
    plan = Column(Integer, default='0')
    bedDays = Column(Integer, default='0')


class RbPolicyType(Base):
    __tablename__ = 'rbPolicyType'
    id = Column(Integer, primary_key=True)
    code = Column(String(64), index=True)
    name = Column(String(256), index=True)
    TFOMSCode = Column(String(8))
    isPolicySerialRequired = Column(SmallInteger, default='0')
    isPolicyNumberCheckRequired = Column(SmallInteger, default='0')
    policyNumberLength = Column(Integer, default='16')


class RbPost(Base):
    __tablename__ = 'rbPost'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    regionalCode = Column(String(8))
    key = Column(String(6), index=True)
    high = Column(String(6))
    flatCode = Column(String(64))


class RbPrintTemplate(Base):
    __tablename__ = 'rbPrintTemplate'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(128), index=True)
    context = Column(String(64), index=True)
    fileName = Column(String(128))
    default = Column(Text)
    dpdAgreement = Column(SmallInteger, default='0')
    render = Column(SmallInteger, default='0')
    templateText = Column(Text)


class RbQuotaStatus(Base):
    __tablename__ = 'rbQuotaStatus'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(50), index=True)


class RbReasonOfAbsence(Base):
    __tablename__ = 'rbReasonOfAbsence'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbRefusalReason(Base):
    __tablename__ = 'rbRefusalReason'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(128), index=True)


class RbRelationType(Base):
    __tablename__ = 'rbRelationType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    leftName = Column(String(64))
    rightName = Column(String(64))
    isDirectGenetic = Column(SmallInteger, default='0')
    isBackwardGenetic = Column(SmallInteger, default='0')
    isDirectRepresentative = Column(SmallInteger, default='0')
    isBackwardRepresentative = Column(SmallInteger, default='0')
    isDirectEpidemic = Column(SmallInteger, default='0')
    isBackwardEpidemic = Column(SmallInteger, default='0')
    isDirectDonation = Column(SmallInteger, default='0')
    isBackwardDonation = Column(SmallInteger, default='0')
    leftSex = Column(SmallInteger, default='0')
    rightSex = Column(SmallInteger, default='0')
    regionalCode = Column(String(64))
    regionalReverseCode = Column(String(64))


class RbRequestType(Base):
    __tablename__ = 'rbRequestType'
    id = Column(Integer, primary_key=True)
    code = Column(String(32), index=True)
    name = Column(String(64), index=True)
    relevant = Column(SmallInteger, default='1')


class RbResult(Base):
    __tablename__ = 'rbResult'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    eventPurpose_id = Column(Integer, FKey('rbEventTypePurpose.id'), index=True)
    continued = Column(SmallInteger)
    regionalCode = Column(String(8))


class RbScene(Base):
    __tablename__ = 'rbScene'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    serviceModifier = Column(String(128))


class RbService(Base):
    __tablename__ = 'rbService'
    id = Column(Integer, primary_key=True)
    code = Column(String(31), index=True)
    name = Column(String(255), index=True)
    eisLegacy = Column(SmallInteger, index=True)
    nomenclatureLegacy = Column(SmallInteger, default='0')
    license = Column(SmallInteger)
    infis = Column(String(31), index=True)
    begDate = Column(Date)
    endDate = Column(Date)
    medicalAidProfile_id = Column(
        Integer, FKey('rbMedicalAidProfile.id'), index=True)
    rbMedicalKind_id = Column(Integer, FKey('rbMedicalKind.id'), index=True)
    UET = Column(Float, default='0')
    departCode = Column(String(3))
    adultUetDoctor = Column(Float, default='0')
    adultUetAverageMedWorker = Column(Float, default='0')
    childUetDoctor = Column(Float, default='0')
    childUetAverageMedWorker = Column(Float, default='0')
    qualityLevel = Column(Float, default='1')
    superviseComplexityFactor = Column(Float, default='1')


class RbServiceProfile(Base):
    __tablename__ = 'rbService_Profile'
    id = Column(Integer, primary_key=True)
    idx = Column(Integer, default='0')
    master_id = Column(Integer, FKey('rbService.id'), index=True)
    speciality_id = Column(Integer, FKey('rbSpeciality.id'), index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    mkbRegExp = Column(String(64))
    medicalAidProfile_id = Column(
        Integer, FKey('rbMedicalAidProfile.id'), index=True)


class RbServiceClass(Base):
    __tablename__ = 'rbServiceClass'
    id = Column(Integer, primary_key=True)
    code = Column(String(3), index=True)
    name = Column(String(200), index=True)
    section = Column(CHAR)


class RbServiceFinance(Base):
    __tablename__ = 'rbServiceFinance'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), index=True)
    name = Column(String(64), index=True)


class RbServiceGroup(Base):
    __tablename__ = 'rbServiceGroup'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, FKey('rbService.id'), index=True)
    service_id = Column(Integer, FKey('rbService.id'), index=True)
    required = Column(SmallInteger, default='0')


class RbServiceSection(Base):
    __tablename__ = 'rbServiceSection'
    id = Column(Integer, primary_key=True)
    code = Column(CHAR)
    name = Column(String(100))


class RbServiceType(Base):
    __tablename__ = 'rbServiceType'
    id = Column(Integer, primary_key=True)
    code = Column(String(3), index=True)
    name = Column(String(200), index=True)
    section = Column(CHAR)
    description = Column(Text)


class RbServiceUET(Base):
    __tablename__ = 'rbServiceUET'
    id = Column(Integer, primary_key=True)
    rbService_id = Column(Integer, FKey('rbService.id'), index=True)
    age = Column(String(10))
    UET = Column(Float, default='0')


class RbSocStatusClass(Base):
    __tablename__ = 'rbSocStatusClass'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    group_id = Column(Integer, FKey('rbSocStatusClass.id'), index=True)


class RbSocStatusClassTypeAssoc(Base):
    __tablename__ = 'rbSocStatusClassTypeAssoc'
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, FKey('rbSocStatusClass.id'), index=True)
    type_id = Column(Integer, FKey('rbSocStatusType.id'), index=True)


class RbSocStatusType(Base):
    __tablename__ = 'rbSocStatusType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(250), index=True)
    socCode = Column(String(8), index=True)
    TFOMSCode = Column(Integer)
    regionalCode = Column(String(8))


class RbSpeciality(Base):
    __tablename__ = 'rbSpeciality'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    OKSOName = Column(String(60))
    OKSOCode = Column(String(8))
    service_id = Column(Integer, FKey('rbService.id'), index=True)
    sex = Column(SmallInteger)
    age = Column(String(9))
    age_bu = Column(SmallInteger)
    age_bc = Column(SmallInteger)
    age_eu = Column(SmallInteger)
    age_ec = Column(SmallInteger)
    mkbFilter = Column(String(32))
    regionalCode = Column(String(16))
    quotingEnabled = Column(SmallInteger, default='0')


class RbSpecialVariablesPreferences(Base):
    __tablename__ = 'rbSpecialVariablesPreferences'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    query = Column(Text)


class RbStorage(Base):
    __tablename__ = 'rbStorage'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(50), index=True)
    name = Column(String(256))
    orgStructure_id = Column(Integer, FKey('OrgStructure.id'), index=True)


class RbTariffCategory(Base):
    __tablename__ = 'rbTariffCategory'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(64), index=True)


class RbTariffType(Base):
    __tablename__ = 'rbTariffType'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), index=True)
    name = Column(String(64), index=True)


class RbTempInvalidBreak(Base):
    __tablename__ = 'rbTempInvalidBreak'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(80), index=True)
    type = Column(SmallInteger, default='0')


class RbTempInvalidDocument(Base):
    __tablename__ = 'rbTempInvalidDocument'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(80), index=True)
    type = Column(SmallInteger, default='0')
    checkingSerial = Column(Enum('нет', 'мягко', 'жестко', name='checkingSerial'))
    checkingNumber = Column(Enum('нет', 'мягко', 'жестко', name='checkingNumber'))
    checkingAmount = Column(Enum('нет', 'списание', name='checkingAmount'))


class RbTempInvalidDuplicateReason(Base):
    __tablename__ = 'rbTempInvalidDuplicateReason'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbTempInvalidExtraReason(Base):
    __tablename__ = 'rbTempInvalidExtraReason'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(128), index=True)
    type = Column(SmallInteger, default='0')


class RbTempInvalidReason(Base):
    __tablename__ = 'rbTempInvalidReason'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    type = Column(SmallInteger, default='0')
    requiredDiagnosis = Column(SmallInteger)
    grouping = Column(SmallInteger)
    primary = Column(Integer)
    prolongate = Column(Integer)
    restriction = Column(Integer)
    regionalCode = Column(String(3))


class RbTempInvalidRegime(Base):
    __tablename__ = 'rbTempInvalidRegime'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    type = Column(SmallInteger, default='0')
    doctype_id = Column(Integer, FKey('rbTempInvalidDocument.id'), index=True)


class RbTempInvalidResult(Base):
    __tablename__ = 'rbTempInvalidResult'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(80), index=True)
    type = Column(SmallInteger, default='0')
    able = Column(SmallInteger)
    closed = Column(SmallInteger, default='0')
    status = Column(SmallInteger)


class RbTest(Base):
    __tablename__ = 'rbTest'
    id = Column(Integer, primary_key=True)
    code = Column(String(16), index=True)
    name = Column(String(128), index=True)
    deleted = Column(SmallInteger, default='0')


class RbTestTubeType(Base):
    __tablename__ = 'rbTestTubeType'
    id = Column(Integer, primary_key=True)
    code = Column(String(64), index=True)
    name = Column(String(128), index=True)
    volume = Column(Float)
    unit_id = Column(Integer, FKey('rbUnit.id'), index=True)
    covCol = Column(String(64))
    image = Column(Binary)
    color = Column(String(8))


class RbThesaurus(Base):
    __tablename__ = 'rbThesaurus'
    id = Column(Integer, primary_key=True)
    code = Column(String(30), index=True)
    name = Column(String(255))
    group_id = Column(Integer, FKey('rbThesaurus.id'), index=True)
    template = Column(String(255))


class RbTimeQuotingType(Base):
    __tablename__ = 'rbTimeQuotingType'
    id = Column(Integer, primary_key=True)
    code = Column(Integer, index=True)
    name = Column(Text)


class RbTissueType(Base):
    __tablename__ = 'rbTissueType'
    id = Column(Integer, primary_key=True)
    code = Column(String(64), index=True)
    name = Column(String(128))
    group_id = Column(Integer, FKey('rbTissueType.id'), index=True)
    sex = Column(SmallInteger, default='0')


class RbTransferDateType(Base):
    __tablename__ = 'rbTransferDateType'
    id = Column(Integer, primary_key=True)
    code = Column(Integer, index=True)
    name = Column(Text)


class RbTraumaType(Base):
    __tablename__ = 'rbTraumaType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)


class RbTreatment(Base):
    __tablename__ = 'rbTreatment'
    id = Column(Integer, primary_key=True)
    code = Column(String(32))
    name = Column(Text)
    pacientModel_id = Column(Integer, FKey('rbPacientModel.id'), index=True)


class RbTrfuBloodComponentType(Base):
    __tablename__ = 'rbTrfuBloodComponentType'
    id = Column(Integer, primary_key=True)
    trfu_id = Column(Integer, index=True)
    code = Column(String(32))
    name = Column(String(256))
    unused = Column(SmallInteger, default='0')


class RbTrfuLaboratoryMeasureTypes(Base):
    __tablename__ = 'rbTrfuLaboratoryMeasureTypes'
    id = Column(Integer, primary_key=True)
    trfu_id = Column(Integer, index=True)
    name = Column(String(256))


class RbUFMS(Base):
    __tablename__ = 'rbUFMS'
    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    name = Column(String(256))


class RbUnit(Base):
    __tablename__ = 'rbUnit'
    id = Column(Integer, primary_key=True)
    code = Column(String(256), index=True)
    name = Column(String(256), index=True)


class RbUserProfile(Base):
    __tablename__ = 'rbUserProfile'
    id = Column(Integer, primary_key=True)
    code = Column(String(20), index=True)
    name = Column(String(128), index=True)
    withDep = Column(SmallInteger, default='0')


class RbUserProfileRight(Base):
    __tablename__ = 'rbUserProfile_Right'
    id = Column(Integer, primary_key=True)
    master_id = Column(Integer, FKey('rbUserProfile.id'), index=True)
    userRight_id = Column(Integer, FKey('rbUserRight.id'), index=True)


class RbUserRight(Base):
    __tablename__ = 'rbUserRight'
    id = Column(Integer, primary_key=True)
    code = Column(String(64), index=True)
    name = Column(String(128), index=True)


class RbVisitType(Base):
    __tablename__ = 'rbVisitType'
    id = Column(Integer, primary_key=True)
    code = Column(String(8), index=True)
    name = Column(String(64), index=True)
    serviceModifier = Column(String(128))


class RdFirstName(Base):
    __tablename__ = 'rdFirstName'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True)
    sex = Column(SmallInteger)


class RdPatrName(Base):
    __tablename__ = 'rdPatrName'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), index=True)
    sex = Column(SmallInteger)
