def generate_report(coordinates, area):

    with open("../reporting/report.tex", "w") as f:
        f.write(r"""\documentclass[12 pt, a4paper, notitlepage]{scrreprt}
        \usepackage
        {amssymb}
        \usepackage
        {amsmath}
        \usepackage
        {verbatim, fontenc}
        \usepackage
        {tabulary, float}
        \usepackage[locale = DE, space - before - unit = true, per - mode = symbol]{siunitx}
        \usepackage
        {icomma}
        \usepackage
        {booktabs, multirow}
        \usepackage[breaklinks = true, colorlinks = true, linkcolor = blue, urlcolor = blue, citecolor = blue]{hyperref}
        \usepackage[autostyle]
        {csquotes}
        \usepackage
        {wrapfig}
        \usepackage[format = plain]{caption}
        \usepackage
        {eurosym}
        \usepackage[ngerman]
        {babel}
        \usepackage[backend = biber, style = numeric, sorting = none]{biblatex}
        \usepackage
        {gensymb}
        \DeclareMathOperator
        {\sinc}{sinc}
        \DeclareSIUnit
        {\dBm}{dBm}
        \DeclareSIUnit[per - mode = reciprocal]\WN
        {\per\centi\meter}
        \usepackage
        {chngcntr}
        \usepackage
        {graphicx, subcaption}
        \usepackage[normalem]
        {ulem}
        \useunder
        {\uline}{\ul}{}
        \usepackage[table, xcdraw]
        {xcolor}

        \titlehead
        {\includegraphics[width = 5cm]{logo.jpg}}
        \title
        {\centering Solarpotential Agrivoltaics Bericht}
        \author
        {Luis Reitmeier\thanks {\href {mailto: reitmeierluis @ icloud.com} {reitmeierluis @ icloud.com}}}
        \date{\today}

        \begin
        {document}

        \counterwithout
        {footnote}
        {chapter}

        \maketitle

        \vfill
        \section * {Abstract}
        \thispagestyle
        {empty}

        \tableofcontents

        \thispagestyle
        {empty}
        \cleardoublepage
        \pagenumbering
        {arabic}
        \newpage

        \chapter
        {Potentialanalyse}

        \begin{figure}
        \centering
        \includegraphics[scale = 0.7]{images/Akkumulierter_Ertrag.png}
        \caption
        {}\label{Projektkosten}
        \end
        {figure}

        Und nun zu den Monaten

        \begin{figure}
        \centering
        \includegraphics[scale = 0.7]{images/Stromerzeugung_pro_Monat.png}
        \caption{}
        \label{Stromerzeugung}
        \end
        {figure}



        \end
        {document}""")
