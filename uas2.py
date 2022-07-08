def down(x, xmin, xmax):
    return (xmax - x) / (xmax - xmin)


def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)


class SuhuBadan():
    tinggi = 40
    rendah = 30

    def Rendah(self, x):
        if x >= self.tinggi:
            return 0
        elif x <= self.rendah:
            return 1
        else:
            return down(x, self.rendah, self.tinggi)

    def Tinggi(self, x):
        if x >= self.tinggi:
            return 1
        elif x <= self.rendah:
            return 0
        else:
            return up(x, self.rendah, self.tinggi)


class Suhu():
    sangatpanas = 40
    panas = 36
    normal = 30
    sejuk = 24
    dingin = 16

    def Dingin(self, x):
        if x >= self.sejuk:
            return 0
        elif x <= self.dingin:
            return 1
        else:
            return down(x, self.dingin, self.sejuk)

    def Sangatpanas(self, x):
        if x >= self.sangatpanas:
            return 1
        elif x <= self.panas:
            return 0
        else:
            return up(x, self.panas, self.sangatpanas)

    def Sejuk(self, x):
        if x >= self.sangatpanas or x <= self.dingin:
            return 0
        elif self.dingin < x < self.sejuk:
            return up(x, self.dingin, self.sejuk)
        elif self.sejuk < x < self.normal:
            return down(x, self.sejuk, self.normal)
        elif self.normal < x < self.panas:
            return down(x, self.normal, self.panas)
        elif self.panas < x < self.sangatpanas:
            return down(x, self.panas, self.sangatpanas)
        else:
            return 1

    def Normal(self, x):
        if x >= self.sangatpanas or x <= self.dingin:
            return 0
        elif self.dingin < x < self.sejuk:
            return up(x, self.dingin, self.sejuk)
        elif self.sejuk < x < self.normal:
            return up(x, self.sejuk, self.normal)
        elif self.normal < x < self.panas:
            return down(x, self.normal, self.panas)
        elif self.panas < x < self.sangatpanas:
            return down(x, self.panas, self.sangatpanas)
        else:
            return 1

    def Panas(self, x):
        if x >= self.sangatpanas or x <= self.dingin:
            return 0
        elif self.dingin < x < self.sejuk:
            return up(x, self.dingin, self.sejuk)
        elif self.sejuk < x < self.normal:
            return up(x, self.sejuk, self.normal)
        elif self.normal < x < self.panas:
            return up(x, self.normal, self.panas)
        elif self.panas < x < self.sangatpanas:
            return down(x, self.panas, self.sangatpanas)
        else:
            return 1


class Kondisi():
    maximum = 35
    minimum = 25
    suhu1 = 20  # suhu cuaca
    suhu2 = 34  # suhu badan

    def _minus(self, a):
        return self.maximum - a*(self.maximum - self.minimum)

    def _plus(self, a):
        return a*(self.maximum - self.minimum) + self.minimum

    def _inferensi(self, s=Suhu(), sb=SuhuBadan()):
        Hasil = []
        a1 = min(s.Dingin(self.suhu1), sb.Tinggi(self.suhu2))
        z1 = self._minus(a1)
        Hasil.append((a1, z1))
        a2 = min(s.Dingin(self.suhu1), sb.Rendah(self.suhu2))
        z2 = self._minus(a1)
        Hasil.append((a2, z2))
        a3 = min(s.Sejuk(self.suhu1), sb.Tinggi(self.suhu2))
        z3 = self._minus(a3)
        Hasil.append((a3, z3))
        a4 = min(s.Sejuk(self.suhu1), sb.Rendah(self.suhu2))
        z4 = self._minus(a4)
        Hasil.append((a4, z4))
        a5 = min(s.Normal(self.suhu1), sb.Tinggi(self.suhu2))
        z5 = self._minus(a5)
        Hasil.append((a5, z5))
        a6 = min(s.Normal(self.suhu1), sb.Rendah(self.suhu2))
        z6 = self._plus(a6)
        Hasil.append((a6, z6))
        a7 = min(s.Panas(self.suhu1), sb.Tinggi(self.suhu2))
        z7 = self._plus(a7)
        Hasil.append((a7, z7))
        a8 = min(s.Panas(self.suhu1), sb.Rendah(self.suhu2))
        z8 = self._plus(a8)
        Hasil.append((a8, z8))
        a9 = min(s.Sangatpanas(self.suhu1), sb.Tinggi(self.suhu2))
        z9 = self._plus(a9)
        Hasil.append((a9, z9))
        a10 = min(s.Sangatpanas(self.suhu1), sb.Rendah(self.suhu2))
        z10 = self._plus(a10)
        Hasil.append((a10, z10))
        return Hasil

    def defuzifikasi(self, data_inferensi=[]):
        # (α1∗z1+α2∗z2+α3∗z3+α4∗z4) / (α1+α2+α3+α4)
        data_inferensi = data_inferensi if data_inferensi else self._inferensi()
        res_a_z = 0
        res_a = 0
        for data in data_inferensi:
            # data[0] = a
            # data[1] = z
            res_a_z += data[0] * data[1]
            res_a += data[0]
        return res_a_z/res_a
