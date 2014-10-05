import func as f
def constant(f):
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f(self)
    return property(fget, fset)
class _Initials(object):
    @constant
    def AII(self): #Service Capital Initial (dollar)
        return 5*10**9
    @constant
    def AIOPCI(self): #
        return self.IOPCI
    @constant
    def ALI(self): #Service Capital Initial (dollar)
        return 0.9*10**9
    @constant
    def DIOPCI(self): #
        return self.IOPCI
    @constant
    def EHSPCI(self): #
        return self.HSAPCI
    @constant
    def FALMI(self): #
        return f.f126(self.PFRI)
    @constant
    def FCAPCI(self): #
        cuf = 1
        scor = 1
        SOPC = (self.SCI * cuf/scor)
        MTF = 12 * f.f34(self.LEI)
        FIE = (self.IOPCI - self.AIOPCI)/self.AIOPCI
        DCFS = 4*f.f41(FIE)*f.f39(self.DIOPCI)
        DTF = DCFS * f.f36(self.LEI)
        return SOPC*f.f48(MTF/DTF -1) 
    @constant
    def FCFPCI(self):
        return self.FCAPCI
    @constant
    def FI(self): #Service Capital Initial (dollar)
        AIPH = self.AII * (1 - self.FALMI) / self.ALI
        LY = self.LFERTI * f.f102(AIPH) * f.f106(self.IOI)
        return LY * self.ALI * 0.63
    @constant
    def FIOAAI(self): #Service Capital Initial (dollar)
        IFPC = f.f90(self.IOI/self.POPI)
        FPC = self.FI / self.POPI
        return f.f94(FPC/IFPC)
    @constant
    def HSAPCI(self): #Combine formula for io from capital_simple and IOPC from population using the initial values
        return f.f21(self.SOI/self.POPI)
    @constant
    def ICI(self): #Industrial Capital Initial (dollar)
        return  2.1*10**11
    @constant
    def IOI(self):
        return (self.ICI * (1 - f.f135(self.NRI/self.NRI)) /3)
    @constant
    def IOPCI(self): #Combine formula for io from capital_simple and IOPC from population using the initial values
        return self.IOI / self.POPI
    @constant
    def LFERTI(self): #Service Capital Initial (dollar)
        return 600
    @constant
    def LEI(self): #
        FPC = self.FI/self.POPI
        LMC = 1 - f.f27(self.IOPCI)* f.f26(self.POPI)
        return 28*f.f25(self.EHSPCI)*f.f20(FPC/230)*f.f29(self.PPOLXI)*LMC
    @constant
    def NRI(self): #Non-Renewable Resources Initial (resource unit)
        return 1*10**12
    @constant
    def PALI(self): #Service Capital Initial (dollar)
        return 2.3*10**9
    @constant
    def PFRI(self): #Service Capital Initial (dollar)
        return 1
    @constant
    def PLEI(self):
        return self.LEI
    @constant
    def POPI(self): #Population (persons)
        return 1.6*10**9
    @constant
    def PPASRI(self): #Service Capital Initial (dollar)
        return self.PPGRI
    @constant
    def PPOLI(self): #Service Capital Initial (dollar)
        return 2.5*10**7
    @constant
    def PPGAOI(self): #Service Capital Initial (dollar)
        return 0.001 * self.AII * (1 - self.FALMI)
    @constant
    def PPGIOI(self): #Service Capital Initial (dollar)
        return 0.02 * self.POPI * f.f132(self.IOI / self.POPI)
    @constant
    def PPGRI(self): #Service Capital Initial (dollar)
        return self.PPGIOI + self.PPGAOI
    @constant
    def PPOLXI(self): #Service Capital Initial (dollar)
        return self.PPOLI/(1.36*10**8)
    @constant
    def SCI(self): #Service Capital Initial (dollar)
        return 1.4*10**11
    @constant
    def SOI(self):
        cuf = 1
        scor = 1
        return (self.SCI * cuf/scor)
    @constant
    def UILI(self): #Service Capital Initial (dollar)
        return 8.2*10**6
class _Returns(object):
    @constant
    def AI(self):
        return "ai"
    @constant
    def F(self):
        return "f"
    @constant
    def FALM(self):
        return "falm"
    @constant
    def FIOAA(self):
        return "fioaa"
    @constant
    def IO(self):
        return "io"
    @constant
    def POP(self):
        return "pop"
    @constant
    def PPOLX(self):
        return "ppolx"
    @constant
    def SO(self):
        return "so"
class _Capital(object):
    @constant
    def YEAR(self):
        return 0
    @constant
    def NR(self):
        return 1
    @constant
    def IC(self):
        return  2
    @constant
    def SC(self):
        return 3
class _Population(object):
    @constant
    def YEAR(self):
        return 0
    @constant
    def POP(self):
        return 1
    @constant
    def EHSPC(self):
        return  2
    @constant
    def AIOPC(self):
        return 3
    @constant
    def DIOPC(self):
        return 4
    @constant
    def FCFPC(self):
        return 5
    @constant
    def PLE(self):
        return 6
    @constant
    def DELAYED_dDIOPC(self):
        return 7
    @constant
    def DELAYED_dFCFPC(self):
        return 8
    @constant
    def DELAYED_dPLE(self):
        return 9
class _Agriculture(object):
    @constant
    def YEAR(self):
        return 0
    @constant
    def IO(self):
        return 1
    @constant
    def POP(self):
        return  2
    @constant
    def PPOLX(self):
        return 3
    @constant
    def AL(self):
        return 4
    @constant
    def PAL(self):
        return 5
    @constant
    def UIL(self):
        return 6
    @constant
    def LFERT(self):
        return 7
    @constant
    def AI(self):
        return 8
    @constant
    def PFR(self):
        return 9
class _Const(object):
    def __init__(self):
        self.capital = _Capital()
        self.population = _Population()
        self.agriculture = _Agriculture()
        self.initial = _Initials()
        self.returns = _Returns()
    @constant
    def START_YEAR(self):
        return 1900
    @constant
    def YEAR_RANGE(self):
        return 200
    @constant
    def YEAR_STEP_SIZE(self):
        return 1
    
    @constant
    def CAPITAL(self):
        return self.capital
    @constant
    def POPULATION(self):
        return self.population
    @constant
    def AGRICULTURE(self):
        return self.agriculture
    
    @constant
    def RETURNS(self):
        return self.returns
    @constant
    def INITIAL(self):
        return self.initial
    
    @constant
    def FIOAA(self): #Fraction of Inputs Allocated to Agriculture (dimensionless)
        return 0.1