# -*- coding: utf-8 -*-
from tf.convert.tei import TEI

def main():
    Tei = TEI(verbose=-1, tei=0, tf="0.9.0")
    Tei.task(check=True, verbose=1, validate=True)
    Tei.good = True
    Tei.task(convert=True, verbose=0)

if __name__ == "__main__":
    main()
