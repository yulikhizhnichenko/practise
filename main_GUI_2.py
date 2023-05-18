import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def check_group(word):
    word_group = 0
    ######## CHECK word in base ########################
    f = open("A:\\diploma_y\\practika\\practise\\base.txt", 'r', encoding="utf-8")
    base = f.read()
    base_mass = base.split("#")
    for i in base_mass:
        word_ = i.split("\n")
        for f in range(1, len(word_) - 1, 1):
            if word == word_[f]:
                base_group_number = int(word_[0])
                word_group = 3
                break

    if word_group == 3:
        if base_group_number == 1:
            print("qwe")
            je = word[:-4] + "us"
            tu = word[:-4] + "us"
            il_elle = word[:-4] + "ut"
            nous = word[:-4] + "lvons"
            vous = word[:-4] + "lvez"
            ils_elles = word[:-4] + "lvent"

            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 2:
            je = word[:-4] + "iers"
            tu = word[:-4] + "iers"
            il_elle = word[:-4] + "iert"
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-4] + "ièrent"
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 3:
            je = 'vais'
            tu = 'vas'
            il_elle = 'va'
            nous = 'allons'
            vous = 'allez'
            ils_elles = 'vont'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 4:
            je = word[:-2] + 'e'
            tu = word[:-2] + 'es'
            il_elle = word[:-2] + 'e'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 5:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 6:
            je = word[:-2] + 'le'
            tu = word[:-2] + 'les'
            il_elle = word[:-2] + 'le'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'lent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 7:
            print("qwe")
            je = word[:-4] + 'èle'
            tu = word[:-4] + 'èles'
            il_elle = word[:-4] + 'èle'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-4] + 'èlent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 8:
            je = word[:-2] + 'te'
            tu = word[:-2] + 'tes'
            il_elle = word[:-2] + 'te'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'tent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 9:
            je = word[:-4] + 'ète'
            tu = word[:-4] + 'ètes'
            il_elle = word[:-4] + 'ète'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-4] + 'ètent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 10:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 11:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 12:
            je = 'assois'
            tu = 'assois'
            il_elle = 'assoit'
            nous = 'assoyons'
            vous = 'assoyez'
            ils_elles = 'assoient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 13:
            je = 'rassois'
            tu = 'rassois'
            il_elle = 'rassoit'
            nous = 'rassoyons'
            vous = 'rassoyez'
            ils_elles = 'rasseyent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 14:
            je = 'ai'
            tu = 'as'
            il_elle = 'a'
            nous = 'avons'
            vous = 'avez'
            ils_elles = 'sont'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 15:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-4] + 'uvons'
            vous = word[:-4] + 'uvez'
            ils_elles = word[:-2] + 'vent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 16:
            je = word[:-5] + 's'
            tu = word[:-5] + 's'
            il_elle = word[:-5] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 17:
            je = word[:-1] + 's'
            tu = word[:-1] + 's'
            il_elle = word[:-1] + 't'
            nous = word[:-2] + 'yons'
            vous = word[:-2] + 'yez'
            ils_elles = word[:-2] + 'ient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 18:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-3] + 'ôt'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 19:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 20:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 21:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 22:
            je = 'fris'
            tu = 'fris'
            il_elle = 'frit'
            nous = '-'
            vous = '-'
            ils_elles = '-'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 23:
            je = word[:-4] + 'is'
            tu = word[:-4] + 'is'
            il_elle = word[:-4] + 'ît'
            nous = word[:-4] + 'issons'
            vous = word[:-4] + 'issez'
            ils_elles = word[:-4] + 'issent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 24:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-3] + 'sons'
            vous = word[:-3] + 'sez'
            ils_elles = word[:-3] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 25:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 26:
            je = word[:-2] + 'e'
            tu = word[:-2] + 'es'
            il_elle = word[:-2] + 'e'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 27:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-4] + 'gnons'
            vous = word[:-4] + 'gnez'
            ils_elles = word[:-4] + 'gnent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 28:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-3] + 'yons'
            vous = word[:-3] + 'yez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 29:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-2]
            nous = word[:-4] + 'issons'
            vous = word[:-4] + 'issez'
            ils_elles = word[:-4] + 'issent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 30:
            je = word[:-2] + 'e'
            tu = word[:-2] + 'es'
            il_elle = word[:-2] + 'e'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 31:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 32:
            je = word[:-5] + 'ois'
            tu = word[:-5] + 'ois'
            il_elle = word[:-5] + 'oit'
            nous = word[:-3] + 'ons'
            vous = word[:-3] + 'ez'
            ils_elles = word[:-5] + 'oivent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 33:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'tes'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 34:
            je = 'maudis'
            tu = 'maudis'
            il_elle = 'maudit'
            nous = 'maudissons'
            vous = 'maudissez'
            ils_elles = 'maudissent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 35:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 36:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'vons'
            vous = word[:-2] + 'vez'
            ils_elles = word[:-2] + 'vent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 37:
            je = 'suis'
            tu = 'es'
            il_elle = 'est'
            nous = 'sommes'
            vous = 'êtes'
            ils_elles = 'sont'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 38:
            je = 'faux'
            tu = 'faux'
            il_elle = 'faut'
            nous = 'faillons'
            vous = 'faillez'
            ils_elles = 'faillent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 39:
            je = '-'
            tu = '-'
            il_elle = 'faut'
            nous = '-'
            vous = '-'
            ils_elles = '-'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 40:
            je = 'fuis'
            tu = 'fuis'
            il_elle = 'fuit'
            nous = 'fuyons'
            vous = 'fuyez'
            ils_elles = 'fuient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 41:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'tes'
            ils_elles = word[:-4] + 'ont'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 42:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-4] + 'gnons'
            vous = word[:-4] + 'gnez'
            ils_elles = word[:-4] + 'gnent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 43:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 44:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 45:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 46:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-3] + 'lons'
            vous = word[:-3] + 'lez'
            ils_elles = word[:-3] + 'lent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 47:
            je = 'meurs'
            tu = 'meurs'
            il_elle = 'meurt'
            nous = 'mourons'
            vous = 'mourez'
            ils_elles = 'meurent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 48:
            je = word[:-6] + 'eus'
            tu = word[:-6] + 'eus'
            il_elle = word[:-6] + 'eut'
            nous = word[:-3] + 'ons'
            vous = word[:-3] + 'ez'
            ils_elles = word[:-6] + 'euvent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 49:
            je = word[:-4] + 'is'
            tu = word[:-4] + 'is'
            il_elle = word[:-2]
            nous = word[:-4] + 'issons'
            vous = word[:-4] + 'issez'
            ils_elles = word[:-4] + 'issent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 50:
            je = 'ois'
            tu = 'ois'
            il_elle = 'oit'
            nous = 'oyons'
            vous = 'oyez'
            ils_elles = 'oient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 51:
            je = 'gis'
            tu = 'gis'
            il_elle = 'gît'
            nous = 'gisons'
            vous = 'gisez'
            ils_elles = 'gisent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 52:
            je = word[:-4] + 'is'
            tu = word[:-4] + 'is'
            il_elle = word[:-2]
            nous = word[:-4] + 'issons'
            vous = word[:-4] + 'issez'
            ils_elles = word[:-4] + 'issent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 53:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-4] + 'gnons'
            vous = word[:-4] + 'gnez'
            ils_elles = word[:-4] + 'gnent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 54:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-3] + 'ît'
            nous = word[:-2] + 'sons'
            vous = word[:-2] + 'sez'
            ils_elles = word[:-2] + 'sent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 55:
            je = 'tais'
            tu = 'tais'
            il_elle = 'tait'
            nous = 'taisons'
            vous = 'taisez'
            ils_elles = 'taisent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 56:
            je = '-'
            tu = '-'
            il_elle = word[:-4] + 't'
            nous = '-'
            vous = '-'
            ils_elles = '-'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 57:
            je = word[:-2] + 'is'
            tu = word[:-2] + 'is'
            il_elle = word[:-2] + 'it'
            nous = word[:-2] + 'yons'
            vous = word[:-2] + 'yez'
            ils_elles = word[:-2] + 'ient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 58:
            je = 'peux'
            tu = 'peux'
            il_elle = 'peut'
            nous = 'pouvons'
            vous = 'pouvez'
            ils_elles = 'peuvent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 59:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-3] + 'ons'
            vous = word[:-3] + 'ez'
            ils_elles = word[:-3] + 'nent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 60:
            je = word[:-6] + 'çois'
            tu = word[:-6] + 'çois'
            il_elle = word[:-6] + 'çoit'
            nous = word[:-3] + 'ons'
            vous = word[:-3] + 'ez'
            ils_elles = word[:-6] + 'çoivent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 61:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 62:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 63:
            je = 'fous'
            tu = 'fous'
            il_elle = 'fout'
            nous = 'foutons'
            vous = 'foutez'
            ils_elles = 'foutent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 64:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 65:
            je = 'sais'
            tu = 'sais'
            il_elle = 'sait'
            nous = 'savons'
            vous = 'savez'
            ils_elles = 'savent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 66:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-2]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 67:
            je = word[:-4] + 'ieds'
            tu = word[:-4] + 'ieds'
            il_elle = word[:-4] + 'ied'
            nous = word[:-3] + 'yons'
            vous = word[:-3] + 'yez'
            ils_elles = word[:-4] + 'iéent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 68:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 69:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 70:
            je = 'sursois'
            tu = 'sursois'
            il_elle = 'sursoit'
            nous = 'sursoyons'
            vous = 'sursoyez'
            ils_elles = 'sursoient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 71:
            je = word[:-4] + 'iens'
            tu = word[:-4] + 'iens'
            il_elle = word[:-4] + 'ient'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-4] + 'iennent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 72:
            je = word[:-4] + 'iens'
            tu = word[:-4] + 'iens'
            il_elle = word[:-4] + 'ient'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-4] + 'iennent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 73:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2] + 't'
            nous = word[:-3] + 'yons'
            vous = word[:-3] + 'yez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 74:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-3] + 'quons'
            vous = word[:-3] + 'quez'
            ils_elles = word[:-3] + 'quent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 75:
            je = word[:-4] + 'ux'
            tu = word[:-4] + 'ux'
            il_elle = word[:-4] + 'ut'
            nous = word[:-3] + 'ons'
            vous = word[:-3] + 'ez'
            ils_elles = word[:-3] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 76:
            je = word[:-2] + 's'
            tu = word[:-2] + 's'
            il_elle = word[:-2]
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 77:
            je = word[:-3] + 's'
            tu = word[:-3] + 's'
            il_elle = word[:-3] + 't'
            nous = word[:-2] + 'ons'
            vous = word[:-2] + 'ez'
            ils_elles = word[:-2] + 'ent'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 78:
            je = word[:-2] + 'is'
            tu = word[:-2] + 'is'
            il_elle = word[:-2] + 'it'
            nous = word[:-2] + 'yons'
            vous = word[:-2] + 'yez'
            ils_elles = word[:-2] + 'ient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif base_group_number == 79:
            je = 'veux'
            tu = 'veux'
            il_elle = 'veut'
            nous = 'voulons'
            vous = 'voulez'
            ils_elles = 'veulent'
            return (je, tu, il_elle, nous, vous, ils_elles)
    ####################################################

    ######## CHECK word in first group #################
    if word_group == 0:
        if word[-3:] == 'cer':
            je = word[:-1]
            tu = word[:-1] + 's'
            il_elle = word[:-1]
            nous = word[:-3] + 'çons'
            vous = word[:-1] + 'z'
            ils_elles = word[:-1] + 'nt'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif word[-3:] == 'ger':
            je = word[:-1]
            tu = word[:-1] + 's'
            il_elle = word[:-1]
            nous = word[:-3] + 'geons'
            vous = word[:-1] + 'z'
            ils_elles = word[:-1] + 'nt'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif (word[-4:] == 'oyer') or (word[-4:] == 'ayer') or (word[-4:] == 'uyer'):
            je = word[:-3] + 'ie'
            tu = word[:-3] + 'ies'
            il_elle = word[:-3] + 'ie'
            nous = word[:-2] + 'ons'
            vous = word[:-1] + 'z'
            ils_elles = word[:-3] + 'ient'
            return (je, tu, il_elle, nous, vous, ils_elles)

        elif word[-2:] == 'er':
            je = word[:-1]
            tu = word[:-1] + 's'
            il_elle = word[:-1]
            nous = word[:-2] + 'ons'
            vous = word[:-1] + 'z'
            ils_elles = word[:-1] + 'nt'
            return (je, tu, il_elle, nous, vous, ils_elles)
    ####################################################

    ######## CHECK word in second group #################
    if word_group == 0:
        if word[-2:] == 'ir':
            je = word[:-1] + 's'
            tu = word[:-1] + 's'
            il_elle = word[:-1] + 't'
            nous = word[:-1] + 'ssons'
            vous = word[:-1] + 'ssez'
            ils_elles = word[:-1] + 'ssent'
            return (je, tu, il_elle, nous, vous, ils_elles)

    if word_group == 0:
        je = 'error'
        tu = 'error'
        il_elle = 'error'
        nous = 'error'
        vous = 'error'
        ils_elles = 'error'
        return (je, tu, il_elle, nous, vous, ils_elles)
class Window2(QMainWindow):                           # <===
    def __init__(self,  je, tu, il_elle, nous, vous, ils_elles):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.je = je
        self.tu = tu
        self.il_elle = il_elle
        self.nous = nous
        self.vous = vous
        self.ils_elles = ils_elles
        self.setWindowTitle("VERB TABLE")
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.add_text()

    def add_text(self):

        self.label_1 = QLabel("je {}".format(self.je), self)
        self.label_1.setFont(QFont('Arial', 20))
        self.label_1.move(100, 100)
        self.label_1.adjustSize()

        self.label_2 = QLabel("tu {}".format(self.tu), self)
        self.label_2.setFont(QFont('Arial', 20))
        self.label_2.move(100, 150)
        self.label_2.adjustSize()

        self.label_3 = QLabel("il/elle {}".format(self.il_elle), self)
        self.label_3.setFont(QFont('Arial', 20))
        self.label_3.move(100, 200)
        self.label_3.adjustSize()

        self.label_4 = QLabel("nous {}".format(self.nous), self)
        self.label_4.setFont(QFont('Arial', 20))
        self.label_4.move(100, 250)
        self.label_4.adjustSize()

        self.label_5 = QLabel("vous {}".format(self.vous), self)
        self.label_5.setFont(QFont('Arial', 20))
        self.label_5.move(100, 300)
        self.label_5.adjustSize()

        self.label_6 = QLabel("ils/elles {}".format(self.ils_elles), self)
        self.label_6.setFont(QFont('Arial', 20))
        self.label_6.move(100, 350)
        self.label_6.adjustSize()
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'INPUT VERB'
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('ENTER', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        je, tu, il_elle, nous, vous, ils_elles = check_group(textboxValue)
        print(je, tu, il_elle, nous, vous, ils_elles)
        self.w = Window2(je, tu, il_elle, nous, vous, ils_elles)
        self.w.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
