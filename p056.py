import pydot

dot_string = """digraph Philosophers {
    size="7,8";
    node [fontsize=24, shape = plaintext];

    400 -> 350 -> 300;
    300 -> 250 -> 200;

    node [fontsize=20, shape = box];
    { rank=same;  400 SOCRATES DEMOCRITUS; }
    { rank=same;  300 EPICURUS; }
    { rank=same;  200 "CHRYSIPPUS"; }

    
    //master-pupil tie
    edge [style=solid];
    DEMOCRITUS -> 40 -> "57(at)" -> PYRRHO -> EPICURUS;
    SOCRATES -> {PLATO;"(Isocrates)-rh";Antisthenes;Aristippus;Phaedo;Euclides}
    PLATO -> ARISTOTLE -> THEOPHRASTUS -> Strato -> Ariston;
    Phaedo -> "53-5(El)" -> "Menedemus"
    "58(at)" -> EPICURUS;
    PYRRHO -> "58(at)"
    Eudoxus -> "78(mth)" -> "80(mth)" -> ARCESILAUS
    PLATO -> {"Heraclides\nPoniticus";"Speusippus(Ac)";"Xenocrates(Ac)"}
    "Speusippus(Ac)" -> "Xenocrates(Ac)" -> "Polemon(Ac)" -> ZENO
    Aristippus -> "48(Cr)" -> "50(Cr)" -> "51(Cr)";
    Aristippus -> "49(Cr)" -> "52(Cr)";
    "87(Ac)" -> ARCESILAUS;
    THEOPHRASTUS -> {ARCESILAUS; "88(Ac)"};
    "88(Ac)" -> ARCESILAUS -> "97(Ac)";
    "88(Ac)" -> "97(Ac)";
    "97(Ac)" -> CHRYSIPPUS;
    "ARCESILAUS" -> CHRYSIPPUS;
    Euclides -> "Eubulides(Mg)"
    "Eubulides(Mg)"-> {"(Demosthenes)"; "62(Mg)";"Stilpo(Mg)"};
    "Stilpo(Mg)" -> {Menedemus;ZENO};
    Menedemus -> ZENO;
    "62(Mg)" -> {"Diodorus\nCronus(Mg)";ZENO};
    "Diodorus\nCronus(Mg)" -> "91(Mg)" -> ZENO;
    "Diodorus\nCronus(Mg)" -> ZENO;
    PYRRHO -> Timon
    ZENO -> Ariston;
    ZENO -> "Cleanthes(St)" -> CHRYSIPPUS;
    
    
    //probable master-pupil tie
    edge [style=dotted];
    DEMOCRITUS -> 39 -> "(x)" -> "58(at)";
    Antisthenes -> DIOGENES
    "57(at)" -> "58(at)";
    "Polemon(Ac)" -> "68(Ac)"
    "51(Cr)" -> "Hegesius(Cr)";
    "52(Cr)" -> "Theodorus(Cr)";
    "Stilpo(Mg)" -> PYRRHO;
    "68(Ac)" -> EPICURUS;
    
    //acquaintance tie
    edge [dir=none];
    PLATO -> "Euclides"
    PLATO -> {Eudoxus;"Archytas(Py)"}
    THEOPHRASTUS -> "Crates(Cn)";
    
    //probable acquaintance tie
    edge [style=dotted,dir=none];
    ARISTOTLE -> "Eudoxus";
    
    //conflictual tie
    edge [style=bold,arrowhead=tee,arrowtail=tee,dir=both];
    PLATO -> DIOGENES;
    "Polemon(Ac)" -> "87(Ac)";
    "Stilpo(Mg)" -> "Diodorus\nCronus(Mg)";
    Ariston -> "Cleanthes(St)"
    Timon -> ARCESILAUS;
    
    ARCESILAUS [label="ARCESILAUS(Ac,Sk)"]
    "Eudoxus" [label="Eudoxus(Ac,mth)"]
    "Euclides" [label="Euclides\nof Megara"]
    DIOGENES [label="DIOGENES\nof Sinope"]
    "Menedemus" [label="Menedemus\nof Eretria"]
    ZENO [label="ZENO\nof Citium"]
    Ariston [label="Ariston\nof Chios(St)"]
    CHRYSIPPUS [label="CHRYSIPPUS(St)"]
}"""

graphs = pydot.graph_from_dot_data(dot_string)
graphs[0].write_svg('p056.svg')