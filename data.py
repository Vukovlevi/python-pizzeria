from type import Pizza
from type import User

pizza1 = Pizza("Margaréta", "paradicsom szósz, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2390, "Img/Margareta.png")
pizza2 = Pizza("Kukoricás", "paradicsom szósz, kukorica, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2580, "Img/Kukoricas.png")
pizza3 = Pizza("Sonkás", "paradicsom szósz, sonka, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2790, "Img/Sonkas.png")
pizza4 = Pizza("Bolognai", "bolognai szósz, paradicsom szósz, sajt, oregano", "Meg kell csinálni az összetevők segítségével!", "paradicsomszósz,mozarella,sonka,kukorica", 2800, "Img/Bolognai.png")
pizzak = [pizza1, pizza2, pizza3, pizza4]

user = User("Gipsz Jakab", "admin", "admin", "8200 Veszprém, Lóczy Lajos utca 12/B 1/1", "+36301564872", "gipsz.jakab@gmail.com")