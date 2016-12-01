"""The following needs to be changed to an extreme amount. The following is how I want the DB set up:
cpu =many-to-many> uniqueCPUList =many-to-many> nonuniqueCPUModel
ram =many-to-many> uniqueRAMList =many-to-many> nonuniqueRAMStick
disk =many-to-many> uniquePhysicalDiskList =many-to-many> nonuniqueDiskModel
disk =many-to-many> uniquePhysicalDiskList =many-to-many> uniquePartitionInfo
gpu =many-to-many> uniqueGPUList =many-to-many> nonuniqueGPUModel

And maybe, just maybe:
roles =many-to-many> uniqueRoleList =many-to-many> nonuniqueRoles

This will allow you to grab information about that model much easier, as well as have duplicates of that model

You may turn a code into a human readable name as such:
>>> ComputerType = 0
>>> models.Machine.MACHINE_TYPES[ComputerType][1]
'Desktop'

That being said, not all values start at 0. (Thanks, Microsoft)
Because of this, a new function may be introduced per table, per choice, to retreive the human readable value from code

With the addition of Machine Model, it may be tricky to figure out how the relationship will work between them all.
The following might represent what you would do:
CPU.model = Machine.MachineModel.CPUModel

Before I allow things to get too far, I'll need to really think about the datatypes and lengths for each field.
"""
from django.db import models
from macaddress.fields import MACAddressField
# from djmoney.models.fields import MoneyField


class Location(models.Model):
    campus = models.CharField(max_length=255, blank=True)
    room = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    computers = models.ForeignKey('Machine', null=True, blank=True)

    def __unicode__(self):
        return u"Room {}, at {}".format(self.room, self.campus)

    def __str__(self):
        return self.__unicode__()


class MachineModel(models.Model):
    DESKTOP = 0
    LAPTOP = 1
    SERVER = 2
    MACHINE_TYPES = (
        (DESKTOP, 'Desktop'),
        (LAPTOP, 'Laptop'),
        (SERVER, 'Server'),
    )
    compType = models.PositiveSmallIntegerField(
        choices=MACHINE_TYPES,
        default=DESKTOP
    )
    manufacturer = models.CharField(max_length=255, blank=True)
    compModel = models.CharField(max_length=255, blank=True)
    cpu = models.ForeignKey('CPUModel')
    ram = models.ForeignKey('RAMModel')
    disks = models.ForeignKey('PhysicalDiskModel')
    gpu = models.ForeignKey('GPUModel')
    network = models.ForeignKey('NetworkModel')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Machine(models.Model):
    model = models.ForeignKey('MachineModel')
    name = models.CharField(max_length=255, unique=True)
    os = models.CharField(max_length=255, blank=True)  # Change to a seperate table of some kind
    activation = models.OneToOneField('Activation', null=True, blank=True)  # Licences have parent-child relationship
    cloudID = models.PositiveSmallIntegerField(null=True, blank=True, unique=True)
    roles = models.ManyToManyField('Role', blank=True)  # Roles are not unique

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class CPUModel(models.Model):
    X86 = 0
    MIPS = 1
    ALPHA = 2
    POWERPC = 3
    ARM = 5
    IA64 = 6
    X64 = 9
    CPU_ARCHS = (
        (X86, 'x86'),
        (MIPS, 'MIPS'),
        (ALPHA, 'Alpha'),
        (POWERPC, 'PowerPC'),
        (ARM, 'ARM'),
        (IA64, 'ia64'),
        (X64, 'x64'),
    )
    OTHER = 1
    UNKNOWN = 2
    N8086 = 3
    N80286 = 4
    N80386 = 5
    N80486 = 6
    N8087 = 7
    N80287 = 8
    N80387 = 9
    N80487 = 10
    PENTIUMBRAND = 11
    PENTIUMPRO = 12
    PENTIUMII = 13
    PENTIUMPROCESSORWITHMMXTECHNOLOGY = 14
    CELERON = 15
    PENTIUMIIXEON = 16
    PENTIUMIII = 17
    M1FAMILY = 18
    M2FAMILY = 19
    K5FAMILY = 24
    K6FAMILY = 25
    K62 = 26
    K63 = 27
    AMDATHLONPROCESSORFAMILY = 28
    AMDDURONPROCESSOR = 29
    AMD29000FAMILY = 30
    K62P = 31
    POWERPCFAMILY = 32
    POWERPC601 = 33
    POWERPC603 = 34
    POWERPC603P = 35
    POWERPC604 = 36
    POWERPC620 = 37
    POWERPCX704 = 38
    POWERPC750 = 39
    ALPHAFAMILY = 48
    ALPHA21064 = 49
    ALPHA21066 = 50
    ALPHA21164 = 51
    ALPHA21164PC = 52
    ALPHA21164A = 53
    ALPHA21264 = 54
    ALPHA21364 = 55
    MIPSFAMILY = 64
    MIPSR4000 = 65
    MIPSR4200 = 66
    MIPSR4400 = 67
    MIPSR4600 = 68
    MIPSR10000 = 69
    SPARCFAMILY = 80
    SUPERSPARC = 81
    MICROSPARCII = 82
    MICROSPARCIIEP = 83
    ULTRASPARC = 84
    ULTRASPARCII = 85
    ULTRASPARCIII = 86
    ULTRASPARCIII2 = 87
    ULTRASPARCIIII = 88
    N68040 = 96
    N68XXXFAMILY = 97
    N68000 = 98
    N68010 = 99
    N68020 = 100
    N68030 = 101
    HOBBITFAMILY = 112
    CRUSOETM5000FAMILY = 120
    CRUSOETM3000FAMILY = 121
    EFFICEONTM8000FAMILY = 122
    WEITEK = 128
    ITANIUMPROCESSOR = 130
    AMDATHLON64PROCESSORFAMILY = 131
    AMDOPTERONFAMILY = 132
    PARISCFAMILY = 144
    PARISC8500 = 145
    PARISC8000 = 146
    PARISC7300LC = 147
    PARISC7200 = 148
    PARISC7100LC = 149
    PARISC7100 = 150
    V30FAMILY = 160
    PENTIUMIIIXEON = 176
    PENTIUMIIIPROCESSORWITHINTELSPEEDSTEPTECHNOLOGY = 177
    PENTIUM4 = 178
    INTELXEON = 179
    AS400FAMILY = 180
    INTELXEONPROCESSORMP = 181
    AMDATHLONXPFAMILY = 182
    AMDATHLONMPFAMILY = 183
    INTELITANIUM2 = 184
    INTELPENTIUMMPROCESSOR = 185
    K7 = 190
    INTELCOREI72760QM = 198
    IBM390FAMILY = 200
    G4 = 201
    G5 = 202
    G6 = 203
    ZARCHITECTUREBASE = 204
    I860 = 250
    I960 = 251
    SH3 = 260
    SH4 = 261
    ARM = 280
    STRONGARM = 281
    S6X86 = 300
    MEDIAGX = 301
    MII = 302
    WINCHIP = 320
    DSP = 350
    VIDEOPROCESSOR = 500
    CPU_FAMILIES = (
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
        (N8086, '8086'),
        (N80286, '80286'),
        (N80386, '80386'),
        (N80486, '80486'),
        (N8087, '8087'),
        (N80287, '80287'),
        (N80387, '80387'),
        (N80487, '80487'),
        (PENTIUMBRAND, 'Pentium brand'),
        (PENTIUMPRO, 'Pentium Pro'),
        (PENTIUMII, 'Pentium II'),
        (PENTIUMPROCESSORWITHMMXTECHNOLOGY, 'Pentium processor with MMX technology'),
        (CELERON, 'Celeron'),
        (PENTIUMIIXEON, 'Pentium II Xeon'),
        (PENTIUMIII, 'Pentium III'),
        (M1FAMILY, 'M1 Family'),
        (M2FAMILY, 'M2 Family'),
        (K5FAMILY, 'K5 Family'),
        (K6FAMILY, 'K6 Family'),
        (K62, 'K6-2'),
        (K63, 'K6-3'),
        (AMDATHLONPROCESSORFAMILY, 'AMD Athlon Processor Family'),
        (AMDDURONPROCESSOR, 'AMD Duron Processor'),
        (AMD29000FAMILY, 'AMD29000 Family'),
        (K62P, 'K6-2+'),
        (POWERPCFAMILY, 'Power PC Family'),
        (POWERPC601, 'Power PC 601'),
        (POWERPC603, 'Power PC 603'),
        (POWERPC603P, 'Power PC 603+'),
        (POWERPC604, 'Power PC 604'),
        (POWERPC620, 'Power PC 620'),
        (POWERPCX704, 'Power PC X704'),
        (POWERPC750, 'Power PC 750'),
        (ALPHAFAMILY, 'Alpha Family'),
        (ALPHA21064, 'Alpha 21064'),
        (ALPHA21066, 'Alpha 21066'),
        (ALPHA21164, 'Alpha 21164'),
        (ALPHA21164PC, 'Alpha 21164PC'),
        (ALPHA21164A, 'Alpha 21164a'),
        (ALPHA21264, 'Alpha 21264'),
        (ALPHA21364, 'Alpha 21364'),
        (MIPSFAMILY, 'MIPS Family'),
        (MIPSR4000, 'MIPS R4000'),
        (MIPSR4200, 'MIPS R4200'),
        (MIPSR4400, 'MIPS R4400'),
        (MIPSR4600, 'MIPS R4600'),
        (MIPSR10000, 'MIPS R10000'),
        (SPARCFAMILY, 'SPARC Family'),
        (SUPERSPARC, 'SuperSPARC'),
        (MICROSPARCII, 'microSPARC II'),
        (MICROSPARCIIEP, 'microSPARC IIep'),
        (ULTRASPARC, 'UltraSPARC'),
        (ULTRASPARCII, 'UltraSPARC II'),
        (ULTRASPARCIII, 'UltraSPARC IIi'),
        (ULTRASPARCIII2, 'UltraSPARC III'),
        (ULTRASPARCIIII, 'UltraSPARC IIIi'),
        (N68040, '68040'),
        (N68XXXFAMILY, '68xxx Family'),
        (N68000, '68000'),
        (N68010, '68010'),
        (N68020, '68020'),
        (N68030, '68030'),
        (HOBBITFAMILY, 'Hobbit Family'),
        (CRUSOETM5000FAMILY, 'Crusoe TM5000 Family'),
        (CRUSOETM3000FAMILY, 'Crusoe TM3000 Family'),
        (EFFICEONTM8000FAMILY, 'Efficeon TM8000 Family'),
        (WEITEK, 'Weitek'),
        (ITANIUMPROCESSOR, 'Itanium Processor'),
        (AMDATHLON64PROCESSORFAMILY, 'AMD Athlon 64 Processor Family'),
        (AMDOPTERONFAMILY, 'AMD Opteron Family'),
        (PARISCFAMILY, 'PA-RISC Family'),
        (PARISC8500, 'PA-RISC 8500'),
        (PARISC8000, 'PA-RISC 8000'),
        (PARISC7300LC, 'PA-RISC 7300LC'),
        (PARISC7200, 'PA-RISC 7200'),
        (PARISC7100LC, 'PA-RISC 7100LC'),
        (PARISC7100, 'PA-RISC 7100'),
        (V30FAMILY, 'V30 Family'),
        (PENTIUMIIIXEON, 'Pentium III Xeon'),
        (PENTIUMIIIPROCESSORWITHINTELSPEEDSTEPTECHNOLOGY, 'Pentium III Processor with Intel SpeedStep Technology'),
        (PENTIUM4, 'Pentium 4'),
        (INTELXEON, 'Intel Xeon'),
        (AS400FAMILY, 'AS400 Family'),
        (INTELXEONPROCESSORMP, 'Intel Xeon processor MP'),
        (AMDATHLONXPFAMILY, 'AMD AthlonXP Family'),
        (AMDATHLONMPFAMILY, 'AMD AthlonMP Family'),
        (INTELITANIUM2, 'Intel Itanium 2'),
        (INTELPENTIUMMPROCESSOR, 'Intel Pentium M Processor'),
        (K7, 'K7'),
        (INTELCOREI72760QM, 'Intel Core i7-2760QM'),
        (IBM390FAMILY, 'IBM390 Family'),
        (G4, 'G4'),
        (G5, 'G5'),
        (G6, 'G6'),
        (ZARCHITECTUREBASE, 'z/Architecture base'),
        (I860, 'i860'),
        (I960, 'i960'),
        (SH3, 'SH-3'),
        (SH4, 'SH-4'),
        (ARM, 'ARM'),
        (STRONGARM, 'StrongARM'),
        (S6X86, '6x86'),
        (MEDIAGX, 'MediaGX'),
        (MII, 'MII'),
        (WINCHIP, 'WinChip'),
        (DSP, 'DSP'),
        (VIDEOPROCESSOR, 'Video Processor'),
    )
    DAUGHTERBOARD = 3
    ZIFSOCKET = 4
    REPLACEMENTPIGGYBACK = 5
    NONE = 6
    LIFSOCKET = 7
    SLOT1 = 8
    SLOT2 = 9
    N370PINSOCKET = 10
    SLOTA = 11
    SLOTM = 12
    SOCKET423 = 13
    SOCKETASOCKET462 = 14
    SOCKET478 = 15
    SOCKET754 = 16
    SOCKET940 = 17
    SOCKET939 = 18
    UPGRADE_METHODS = (
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
        (DAUGHTERBOARD, 'Daughter Board'),
        (ZIFSOCKET, 'ZIF Socket'),
        (REPLACEMENTPIGGYBACK, 'Replacement/Piggy Back'),
        (NONE, 'None'),
        (LIFSOCKET, 'LIF Socket'),
        (SLOT1, 'Slot 1'),
        (SLOT2, 'Slot 2'),
        (N370PINSOCKET, '370 Pin Socket'),
        (SLOTA, 'Slot A'),
        (SLOTM, 'Slot M'),
        (SOCKET423, 'Socket 423'),
        (SOCKETASOCKET462, 'Socket A (Socket 462)'),
        (SOCKET478, 'Socket 478'),
        (SOCKET754, 'Socket 754'),
        (SOCKET940, 'Socket 940'),
        (SOCKET939, 'Socket 939'),
    )
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    partnum = models.CharField(max_length=255, null=True, blank=True)
    arch = models.PositiveSmallIntegerField(
        choices=CPU_ARCHS,
        default=X64
    )
    family = models.PositiveSmallIntegerField(
        choices=CPU_FAMILIES,
        default=UNKNOWN
    )
    upgradeMethod = models.PositiveSmallIntegerField(
        choices=UPGRADE_METHODS,
        default=UNKNOWN
    )
    cores = models.PositiveSmallIntegerField(null=True, blank=True)
    threads = models.PositiveSmallIntegerField(null=True, blank=True)
    speed = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return u"{}, {}".format(self.name, self.arch)

    def __str__(self):
        return self.__unicode__()


class CPU(models.Model):
    machine = models.ForeignKey('Machine')
    model = models.ForeignKey('CPUModel')
    serial = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"CPU {}, {}".format(self.serial, self.location)

    def __str__(self):
        return self.__unicode__()


class RAMModel(models.Model):
    UNKNOWN = 0
    OTHER = 1
    SIP = 2
    DIP = 3
    ZIP = 4
    SOJ = 5
    PROPRIETARY = 6
    SIMM = 7
    DIMM = 8
    TSOP = 9
    PGA = 10
    RIMM = 11
    SODIMM = 12
    SRIMM = 13
    SMD = 14
    SSMP = 15
    QFP = 16
    TQFP = 17
    SOIC = 18
    LCC = 19
    PLCC = 20
    BGA = 21
    FPBGA = 22
    LGA = 23
    FORM_FACTORS = (
        (UNKNOWN, 'Unknown'),
        (OTHER, 'Other'),
        (SIP, 'SIP'),
        (DIP, 'DIP'),
        (ZIP, 'ZIP'),
        (SOJ, 'SOJ'),
        (PROPRIETARY, 'Proprietary'),
        (SIMM, 'SIMM'),
        (DIMM, 'DIMM'),
        (TSOP, 'TSOP'),
        (PGA, 'PGA'),
        (RIMM, 'RIMM'),
        (SODIMM, 'SODIMM'),
        (SRIMM, 'SRIMM'),
        (SMD, 'SMD'),
        (SSMP, 'SSMP'),
        (QFP, 'QFP'),
        (TQFP, 'TQFP'),
        (SOIC, 'SOIC'),
        (LCC, 'LCC'),
        (PLCC, 'PLCC'),
        (BGA, 'BGA'),
        (FPBGA, 'FPBGA'),
        (LGA, 'LGA'),
    )
    DRAM = 2
    SYNCHRONOUSDRAM = 3
    CACHEDRAM = 4
    EDO = 5
    EDRAM = 6
    VRAM = 7
    SRAM = 8
    RAM = 9
    ROM = 10
    FLASH = 11
    EEPROM = 12
    FEPROM = 13
    EPROM = 14
    CDRAM = 15
    D3RAM = 16
    SDRAM = 17
    SGRAM = 18
    RDRAM = 19
    DDR = 20
    DDR2 = 21
    DDR2FBDIMM = 22
    DDR3 = 24
    FBD2 = 25
    MEMORY_TYPES = (
        (UNKNOWN, 'Unknown'),
        (OTHER, 'Other'),
        (DRAM, 'DRAM'),
        (SYNCHRONOUSDRAM, 'Synchronous DRAM'),
        (CACHEDRAM, 'Cache DRAM'),
        (EDO, 'EDO'),
        (EDRAM, 'EDRAM'),
        (VRAM, 'VRAM'),
        (SRAM, 'SRAM'),
        (RAM, 'RAM'),
        (ROM, 'ROM'),
        (FLASH, 'Flash'),
        (EEPROM, 'EEPROM'),
        (FEPROM, 'FEPROM'),
        (EPROM, 'EPROM'),
        (CDRAM, 'CDRAM'),
        (D3RAM, '3DRAM'),
        (SDRAM, 'SDRAM'),
        (SGRAM, 'SGRAM'),
        (RDRAM, 'RDRAM'),
        (DDR, 'DDR'),
        (DDR2, 'DDR2'),
        (DDR2FBDIMM, 'DDR2 FB-DIMM'),
        (DDR3, 'DDR3'),
        (FBD2, 'FBD2'),
    )
    size = models.BigIntegerField()
    manufacturer = models.CharField(max_length=255)
    partnum = models.CharField(max_length=255, null=True, blank=True)
    speed = models.PositiveSmallIntegerField(null=True, blank=True)
    formFactor = models.PositiveSmallIntegerField(
        choices=FORM_FACTORS,
        default=UNKNOWN
    )
    memoryType = models.PositiveSmallIntegerField(
        choices=MEMORY_TYPES,
        default=UNKNOWN
    )

    def sizeInGB(self):
        return int(self.size) / (1024 * 1024 * 1024)

    def sizeInMB(self):
        return int(self.size) / (1024 * 1024)

    def sizeInKB(self):
        return int(self.size) / 1024

    def __unicode__(self):
        return u"{} GB, {}".format(self.sizeInGB(), self.manufacturer)

    def __str__(self):
        return self.__unicode__()


class RAM(models.Model):
    machine = models.ForeignKey('Machine')
    model = models.ForeignKey('RAMModel')
    serial = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return u"Serial Number: {}".format(self.serial)

    def __str__(self):
        return self.__unicode__()


class PhysicalDiskModel(models.Model):
    name = models.CharField(max_length=255, blank=True)
    size = models.BigIntegerField()
    interface = models.CharField(max_length=5, blank=True)
    manufacturer = models.CharField(max_length=255, blank=True)

    def sizeInGB(self):
        return int(self.size) / (1024 * 1024 * 1024)

    def sizeInMB(self):
        return int(self.size) / (1024 * 1024)

    def sizeInKB(self):
        return int(self.size) / 1024

    def __unicode__(self):
        return u"{} Mount, {} GB".format(self.name, self.sizeInGB())

    def __str__(self):
        return self.__unicode__()


class PhysicalDisk(models.Model):
    machine = models.ForeignKey('Machine')
    model = models.ForeignKey('PhysicalDiskModel')
    name = models.CharField(max_length=255, blank=True)
    serial = models.CharField(max_length=255, blank=True)
    partitions = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u"{} Mount, {} GB".format(self.name, self.serial)

    def __str__(self):
        return self.__unicode__()


class LogicalDisk(models.Model):
    UNKNOWN = 0
    NOROOTDIRECTORY = 1
    REMOVABLEDISK = 2
    LOCALDISK = 3
    NETWORKDRIVE = 4
    COMPACTDISC = 5
    RAMDISK = 6
    DRIVE_TYPES = (
        (UNKNOWN, 'Unknown'),
        (NOROOTDIRECTORY, 'No Root Directory'),
        (REMOVABLEDISK, 'Removable Disk'),
        (LOCALDISK, 'Local Disk'),
        (NETWORKDRIVE, 'Network Drive'),
        (COMPACTDISC, 'Compact Disc'),
        (RAMDISK, 'RAM Disk'),
    )
    disk = models.ForeignKey('PhysicalDisk')
    name = models.CharField(max_length=255)
    mount = models.CharField(max_length=4, null=True, blank=True)
    filesystem = models.CharField(max_length=255, null=True, blank=True)
    size = models.BigIntegerField()
    freesize = models.BigIntegerField(null=True, blank=True)
    type = models.PositiveSmallIntegerField(
        choices=DRIVE_TYPES,
        default=UNKNOWN
    )

    def sizeInGB(self):
        return int(self.size) / (1024 * 1024 * 1024)

    def sizeInMB(self):
        return int(self.size) / (1024 * 1024)

    def sizeInKB(self):
        return int(self.size) / 1024

    def freesizeInGB(self):
        return int(self.freesize) / (1024 * 1024 * 1024)

    def freesizeInMB(self):
        return int(self.freesize) / (1024 * 1024)

    def freesizeInKB(self):
        return int(self.freesize) / 1024

    def __unicode__(self):
        return u"{} Mount, {} GB, {} GB Free".format(self.name, self.size, self.free)

    def __str__(self):
        return self.__unicode__()


class GPUModel(models.Model):
    OTHER = 1
    UNKNOWN = 2
    CGA = 3
    EGA = 4
    VGA = 5
    SVGA = 6
    MDA = 7
    HGC = 8
    MCGA = 9
    N8514A = 10
    XGA = 11
    LINEARFRAMEBUFFER = 12
    PC98 = 160
    VIDEO_ARCHITECTURES = (
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
        (CGA, 'CGA'),
        (EGA, 'EGA'),
        (VGA, 'VGA'),
        (SVGA, 'SVGA'),
        (MDA, 'MDA'),
        (HGC, 'HGC'),
        (MCGA, 'MCGA'),
        (N8514A, '8514A'),
        (XGA, 'XGA'),
        (LINEARFRAMEBUFFER, 'Linear Frame Buffer'),
        (PC98, 'PC-98'),
    )
    VRAM = 3
    DRAM = 4
    SRAM = 5
    WRAM = 6
    EDORAM = 7
    BURSTSYNCHRONOUSDRAM = 8
    PIPELINEDBURSTSRAM = 9
    CDRAM = 10
    D3RAM = 11
    SDRAM = 12
    SGRAM = 13
    MEMORY_TYPES = (
        (OTHER, 'Other'),
        (UNKNOWN, 'Unknown'),
        (VRAM, 'VRAM'),
        (DRAM, 'DRAM'),
        (SRAM, 'SRAM'),
        (WRAM, 'WRAM'),
        (EDORAM, 'EDORAM'),
        (BURSTSYNCHRONOUSDRAM, 'Burst Synchronous DRAM'),
        (PIPELINEDBURSTSRAM, 'Pipelined Burst SRAM'),
        (CDRAM, 'CDRAM'),
        (D3RAM, '3DRAM'),
        (SDRAM, 'SDRAM'),
        (SGRAM, 'SGRAM'),
    )
    name = models.CharField(max_length=255)
    size = models.BigIntegerField()
    refresh = models.PositiveSmallIntegerField(null=True, blank=True)
    arch = models.PositiveSmallIntegerField(
        choices=VIDEO_ARCHITECTURES,
        default=UNKNOWN
    )
    memoryType = models.PositiveSmallIntegerField(
        choices=MEMORY_TYPES,
        default=UNKNOWN
    )

    def sizeInGB(self):
        return int(self.size) / (1024 * 1024 * 1024)

    def sizeInMB(self):
        return int(self.size) / (1024 * 1024)

    def sizeInKB(self):
        return int(self.size) / 1024

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class GPU(models.Model):
    machine = models.ForeignKey('Machine')
    model = models.ForeignKey('GPUModel')
    location = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.location

    def __str__(self):
        return self.__unicode__()


class NetworkModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return u"{}, {}".format(self.name, self.manufacturer)

    def __str__(self):
        return self.__unicode__()


class Network(models.Model):
    machine = models.ForeignKey('Machine')  # One to many, network cards ARE unique and can be moved
    model = models.ForeignKey('NetworkModel')
    mac = MACAddressField(unique=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.mac

    def __str__(self):
        return self.__unicode__()


class Activation(models.Model):
    COAID = models.CharField(max_length=255, null=True, blank=True, unique=True)
    productKey = models.CharField(max_length=255, unique=True)
    securityCode = models.CharField(max_length=255, null=True, blank=True)
    windowsVer = models.CharField(max_length=255)

    def __unicode__(self):
        return self.COAID

    def __str__(self):
        return self.__unicode__()


class Role(models.Model):  # Add/change
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

# https://github.com/django-money/django-money
# https://docs.djangoproject.com/en/1.10/ref/models/fields/#integerfield
# http://stackoverflow.com/questions/3113885/difference-between-one-to-many-many-to-one-and-many-to-many
