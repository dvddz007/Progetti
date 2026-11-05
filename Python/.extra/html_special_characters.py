import html

def converti_in_html(test):
    sostituzioni = {
        'à': '&agrave;', 'è': '&egrave;', 'é': '&eacute;', 'ì': '&igrave;',
        'ò': '&ograve;', 'ù': '&ugrave;', 'ç': '&ccedil;', 'À': '&Agrave;',
        'È': '&Egrave;', 'É': '&Eacute;', 'Ù': '&Ugrave;', 'ò': '&ograve;',
        'í': '&iacute;', 'ñ': '&ntilde;', 'ó': '&oacute;', 'â': '&acirc;',
        'ô': '&ocirc;', 'î': '&icirc;', 'ø': '&oslash;', 'æ': '&aelig;',
        "'": "&rsquo;", "‘": "&lsquo;", "’": "&rsquo;", "“": "&ldquo;", "”": "&rdquo;",
        "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "»": "&raquo;",
        "«": "&laquo;"
    }

    testo_convertito = ''.join(sostituzioni.get(c, c) for c in test)
    
    return testo_convertito

def converti_testo_con_spazi(testo):
    righe = testo.splitlines()
    
    righe_convertite = [converti_in_html(riga) if riga.strip() else "" for riga in righe]
    
    return '\n'.join(righe_convertite)

testo = """Frodo, Pipino e Sam si avviarono verso il loro salottino. Era
buio: Merry non c'era, e il fuoco era quasi spento. Quando l'ebbero
riattivato, soffiando sulla brace e aggiungendo qualche pezzo
di legna, si accorsero che Grampasso li aveva seguiti. Era tranquillamente
seduto su una sedia accanto alla porta!
 «Ehi!», esclamò Pipino. «Chi siete, e cosa volete?».
 «Mi chiamo Grampasso», rispose: «e benché forse se ne sia
dimenticato, il vostro amico mi ha promesso una chiacchieratina a
quattr'occhi»
 «Se non sbaglio, voi pretendete di potermi dire qualcosa che
mi sarebbe utile», disse Frodo. «Di cosa si tratta?».
 «Informazioni varie», rispose Grampasso. «Ma ho il mio prezzo,
beninteso».
 «Che significa?», chiese seccamente Frodo.
 «Non spaventatevi! Significa solo che vi dirò tutto quel che
so, dandovi anche qualche buon consiglio.... ma desidero una ricompensa».
 «E in che cosa consisterebbe, se non vi dispiace?», disse Frodo.
Sospettava ora di aver a fare con un furfante, e pensò con
rammarico di aver con sé poco denaro. L'intera somma non avrebbe
soddisfatto un criminale, ed egli comunque non poteva assolutamente
privarsene.
 «Non vi chiedo più di quanto voi possiate offrire», rispose
Grampasso sorridendo, come avesse indovinato i pensieri di Frodo.
«Soltanto questo: mi dovete portare con voi, fin quando decido di
lasciarvi».
 «Veramente!», esclamò Frodo, sorpreso ma non molto sollevato.
«Anche se desiderassi un altro compagno di viaggio, non
potrei accettare una simile proposta prima di sapere parecchie altre
cose sul vostro conto e sui vostri affari».
 «Eccellente!», disse Grampasso, incrociando le gambe e appog- giandosi comodamente allo schienale. «Pare che stiate ritrovando un
PO' del vostro buonsenso, e la cosa non può che rallegrarmi. Voi
siete stato finora di gran lunga troppo negligente. Benissimo! Io vi
dirò quel che so, e voi stabilirete la ricompensa. Forse sarete felice
di accettare la mia proposta quando avrete sentito quel che ho da
dirvi».
 «Avanti, allora!», disse Frodo. «Cosa avete da dirmi?».
 «Troppe, troppe cose oscure e sinistre», disse gravemente
Grampasso. «Ma per quel che vi riguarda personalmente...». Si
alzò e si avvicinò alla porta che aprì di colpo guardando fuori.
Quindi la richiuse silenziosamente e tornò a sedere. «Le mie orecchie
sono molto aguzze», proseguì, abbassando la voce, «e benché
non abbia il potere di scomparire, ho dato la caccia a un sì gran
numero di cose selvagge e di esseri guardinghi, che riesco generalmente
a evitare di essere visto, quando lo desidero. Mi trovavo
questa sera dietro la siepe che fiancheggia la Via ad ovest di Brea,
quando vidi quattro Hobbit scendere dai Tumulilande. Inutile ripetere
tutto ciò che dissero al vecchio Bombadil o fra di loro, ma una
cosa in particolare attirò la mia attenzione. Mi raccomando, ricordatevi
bene, disse uno di loro, che il nome Baggins non dev'essere pronunciato
in nessuna circostanza. Se bisogna proprio darmi un nome,
mi chiamo signor Sottocolle. La cosa m'interessò a tal punto che li
seguii fin qui. Scavalcai il cancello appena fu richiuso alle loro
spalle. Forse il signor Baggins ha un motivo onesto per voler lasciare
a casa il proprio nome, nel qual caso consiglierei a lui e ai suoi
amici di essere più prudenti». «Non vedo che interesse possa avere il mio nome per un qualunque
abitante di Brea», ribattè Frodo incollerito, «ed ancor meno
perché interessi tanto voi. Il signor Grampasso ha forse un motivo
onesto per spiare e origliare; nel qual caso gli consiglierei di
spiegarlo».
 «Ottima risposta!», disse ridendo Grampasso. «Ma la spiegazione
è alquanto semplice: cercavo un Hobbit di nome Frodo Baggins.
Lo dovevo trovare al più presto. Sapevo che portava con sé
fuori della Contea un segreto che riguardava me e i miei amici.
Non mi fraintendete!», esclamò, vedendo Frodo balzare in piedi e
Sam saltar su con aria truce. «Saprò conservare il segreto meglio
di voi. E' necessaria molta cautela!». Si chinò in avanti per guardarli
meglio. «Scrutate ogni ombra!», disse in un sussurro. «Cavalieri
vestiti di nero hanno attraversato Brea. Lunedì pare che uno 
abbia percorso il Verdecammino, e che più tardi, dal Sud, ne sia
giunto un altro».
 Seguì un lungo silenzio. Infine Frodo, rivolgendosi a Pipino e a
Sam: «Avrei dovuto immaginarlo», disse, «dal modo in cui siamo
stati accolti dal guardiano del cancello. E anche l'oste pare abbia sentito
qualcosa. Perché ha tanto insistito per farci unire alla compagnia?
E perché diamine ci siamo comportati in modo così sciocco?
Avremmo fatto meglio a rimanercene seduti qui tranquilli».
 «Sarebbe stata una buona idea», disse Grampasso. «Vi avrei
impedito di venire nel salone, se mi fosse stato possibile; ma l'oste
non ne ha voluto sapere di farmi salire da voi, o di portarvi un mio
messaggio».
 «Credete che lui...», incominciò Frodo.
 «No, il vecchio Cactaceo è un uomo a posto. Solo che i vagabondi
misteriosi della mia specie non godono le sue simpatie». Frodo
gli lanciò un'occhiata perplessa. «Be', bisogna riconoscere che
ho un aspetto piuttosto losco, che ne dite?», disse Grampasso con
un sorriso malizioso e uno strano bagliore in fondo agli occhi.
«Spero però che faremo amicizia e allora mi spiegherete quel che è
avvenuto alla fine della canzone, il vostro piccolo scherzetto...».
 «E' stato soltanto un incidente!», interruppe Frodo. «Ho i miei dubbi», disse Grampasso. «Sia, diciamo che è stato
un incidente. Quell'incidente, però, ha reso pericolosa la vostra
situazione».
 «Non più di quanto lo fosse già», ribattè Frodo. «Sapevo che
quei cavalieri mi inseguivano; ma adesso, comunque, pare che mi
abbiano perso, e che se ne siano andati».
 «Non ci contate!», disse seccamente Grampasso. «Torneranno.
E ne verranno altri, tanti altri. So quanti sono: conosco questi
cavalieri». S'interruppe, e i suoi occhi erano freddi e duri. «E
c'è della gente in Brea della quale non bisogna fidarsi», proseguì.
«Billy Felci, per esempio. Gode di una cattiva nomea nella Terra
di Brea e ha sempre gente strana per casa. Lo avrete notato nel
gruppo di questa sera: un tipo scuro dall'aria sarcastica. Confabulava
con uno degli stranieri provenienti dal Sud, e sgusciarono fuori
insieme subito dopo l'"incidente". Quella gente lì del Sud non
è certo benintenzionata e, quanto a Felci, venderebbe l'anima e
farebbe cattiverie per puro divertimento».
 «Che cosa vuole vendere Felci, e che c'entra lui col mio inciden- te?», disse Frodo, risoluto a far finta di non capite le allusioni
di Grampasso.
 «Vuol vendere informazioni sul vostro conto, beninteso», rispose
Grampasso. «Una descrizione della vostra esibizione sarebbe
molto utile a certa gente. Non avrebbero certo più bisogno di scoprire
il vostro vero nome. Credo più che probabile che essi lo sapranno
questa notte stessa. Va bene così? Regolatevi come volete
per la mia ricompensa: potete prendermi come guida o no. Ma vi
posso dire che conosco tutte le terre tra la Contea e le Montagne
Nebbiose, e che vi ho girovagato per parecchi anni. Sono più vecchio
di quanto non sembri, e potrei asservi utile in varie occasioni. Dovrete
abbandonare la strada da domani, perché sarà sorvegliata notte
e giorno dai Cavalieri. Forse riuscirete a fuggire da Brea e a proseguire
il vostro viaggio mentre il sole è ancora alto in cielo: ma
non andrete lontani. Vi assaliranno in posti selvaggi, in luoghi oscuri
e senza scampo. Volete che essi vi trovino? Sono terribili!».
 Gli Hobbit lo guardarono e videro con sorpresa che il suo viso
era come contratto dal dolore e che le sue mani stringevano i braccioli
della sedia. Tutto nella stanza era immobile e silenzioso, e la
luce pareva essersi affievolita. Egli rimase per qualche minuto seduto
con lo sguardo perso nel vuoto, come se stesse rievocando ricordi
lontani o ascoltando suoni nella remota Notte.
 «Ascoltatemi!», disse infine, passandosi una mano sulla fronte.
«Credo di saperne più di voi sui vostri inseguitori. Li temete,
ma non abbastanza. Domani dovete assolutamente fuggire, se vi sarà
possibile. Grampasso può indicarvi sentieri poco frequentati. Può
venire con voi?».
 Seguì un silenzio pesante. Frodo non rispondeva, la sua mente
era confusa dal dubbio e dalla paura. Sam aggrottò le ciglia e guardò
era confusa dal dubbio e dalla paura. Sam aggrottò le ciglia e guardò
il padrone. Infine, non riuscendo più a trattenersi, disse:
 «Col vostro permesso, signor Frodo, io direi no! Questo Grampasso
ci avverte e ci dice di esser prudenti, e su questo punto io
dico sì, e direi d'incominciare da lui. Viene dalle Terre Selvagge, e
non ho mai sentito dire niente di buono sulla gente di quelle contrade.
Sa qualcosa, è chiaro; troppo per i miei gusti. Ma non vedo
perché dovremmo lasciarci condurre in posti selvaggi, in luoghi
oscuri e senza scampo, come li chiama lui».
 Pipino era irrequieto e mostrava il disagio. Grampasso non rispose
a Sam, ma volse lo sguardo penetrante su Frodo."""

testo_convertito = converti_testo_con_spazi(testo)

print(testo_convertito)
