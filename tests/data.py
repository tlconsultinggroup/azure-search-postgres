from fastapi_app.api_models import ItemPublic


class TestData(ItemPublic):
    embeddings: list[float]


test_data = TestData(
    id=1,
    type="Footwear",
    brand="Daybird",
    name="Wanderer Black Hiking Boots",
    description="Daybird's Wanderer Hiking Boots in sleek black are perfect for all your "
    "outdoor adventures. These boots are made with a waterproof leather upper and a durable "
    "rubber sole for superior traction. With their cushioned insole and padded collar, "
    "these boots will keep you comfortable all day long.",
    price=109.99,
    embeddings=[
        -0.010269113,
        -0.01673832,
        0.0025070684,
        -0.009927924,
        0.0075596725,
        0.0073790434,
        -0.0090849865,
        -0.05860419,
        0.013500371,
        -0.050522696,
        -0.022866337,
        0.011172259,
        -0.011747598,
        -0.011346199,
        -0.009192026,
        0.022612117,
        0.01953473,
        0.022745917,
        0.018089695,
        -0.013440161,
        -0.006673251,
        0.025850065,
        -0.0066765957,
        -0.0056363046,
        -0.020457946,
        -0.020136828,
        0.01906643,
        -0.01911995,
        0.010242353,
        -0.022759298,
        0.0061715026,
        0.0006464189,
        -0.013279602,
        -0.009372656,
        -0.010657132,
        0.0026927153,
        0.0042715496,
        -0.0039403955,
        0.014303168,
        0.01376797,
        0.015841862,
        0.00022578667,
        -0.0026609378,
        0.009386036,
        -0.0010185488,
        0.010683891,
        0.00019714521,
        -0.017835476,
        -0.008623378,
        0.026933841,
        -0.003545687,
        -0.0003781927,
        0.004596013,
        0.007646642,
        0.011781047,
        0.0045525283,
        0.0055526798,
        0.013560581,
        0.029783772,
        -0.029676732,
        -0.033369597,
        0.002610763,
        -0.01665804,
        0.008027971,
        -0.0035122372,
        -0.015493983,
        -0.028659856,
        -0.003579137,
        0.008509649,
        0.01917347,
        0.007673402,
        0.00095666654,
        0.015882002,
        -0.0033784376,
        0.011319439,
        -0.019722048,
        -0.024391651,
        0.006041048,
        -0.014182748,
        -0.009278996,
        0.018022794,
        -0.026304984,
        -0.018798832,
        0.016470721,
        0.015601023,
        0.0061547775,
        0.011486689,
        0.0030723712,
        -0.036875147,
        -0.017260138,
        0.00838923,
        0.0048134374,
        0.0053018057,
        0.002868327,
        0.0031743934,
        0.008007901,
        -0.0058938684,
        0.015734823,
        -0.0009968064,
        -0.02480643,
        0.015520743,
        0.010877901,
        0.002376614,
        -0.013426781,
        -0.027335241,
        0.0009993151,
        -0.007459323,
        0.010683891,
        0.02448531,
        -0.0013898425,
        -0.0076198825,
        0.023508575,
        0.032004844,
        -0.031897806,
        0.00077143783,
        -0.010315943,
        -0.011714147,
        0.016109461,
        0.016885499,
        -0.031496406,
        0.024378272,
        0.015734823,
        0.014530627,
        -0.0025137584,
        0.0008613344,
        0.023455055,
        -0.011694077,
        -0.012175756,
        0.011379649,
        0.0036794867,
        0.0070846844,
        0.018879112,
        0.01920023,
        -0.032272443,
        -0.008048041,
        0.014932025,
        -0.018758692,
        0.005833659,
        -0.020163586,
        -0.0056797895,
        -0.014811606,
        0.014329928,
        -0.006536106,
        0.005803554,
        0.012650744,
        0.025743026,
        -0.0053653605,
        0.009499765,
        0.008536409,
        -0.0059841834,
        0.03002461,
        0.005602855,
        0.039551135,
        -0.020324146,
        -0.005469055,
        0.0148651255,
        0.023521954,
        0.018169973,
        -0.012242655,
        -0.026478924,
        -0.0023548715,
        -0.010630371,
        0.01644396,
        -0.02498037,
        0.04329752,
        0.03047953,
        0.005750034,
        0.0016641314,
        -0.0012075406,
        0.0040106406,
        0.005442295,
        0.0166179,
        0.004920477,
        0.042200368,
        0.023307875,
        0.0023314564,
        0.018705172,
        0.0020337526,
        -0.0220234,
        0.010643751,
        -0.03526955,
        -0.009774054,
        0.0118947765,
        0.005820279,
        -0.01886573,
        -0.031309087,
        -0.009379346,
        -0.004331759,
        0.002878362,
        -0.00549916,
        -0.0037731463,
        0.0029268644,
        0.014704566,
        0.008790628,
        -0.6602203,
        0.0036761416,
        -0.0056898245,
        -0.024632491,
        0.032192163,
        0.00034892405,
        0.031014727,
        0.017701676,
        -0.012811303,
        0.009546596,
        0.017019298,
        0.014570767,
        -0.014383447,
        0.009646945,
        -0.024471931,
        -0.010202213,
        0.003331608,
        -0.020819204,
        0.012135616,
        0.0021140324,
        -0.026465544,
        0.010342702,
        -0.007914241,
        -0.01898615,
        -0.013346502,
        -0.0016173016,
        0.004060815,
        -0.0014433622,
        -0.00824205,
        0.009044847,
        -0.039845496,
        0.04412708,
        -0.0056363046,
        -0.007941001,
        0.05477752,
        -0.021421302,
        -0.014289788,
        0.0436454,
        0.028954215,
        0.056570433,
        -0.012971863,
        -0.0042247195,
        0.0041711996,
        -0.0010051689,
        0.009586735,
        0.016082702,
        0.03537659,
        -0.0025137584,
        0.007713542,
        -0.01388839,
        0.0328344,
        0.026024004,
        0.0059674582,
        -0.010195523,
        -0.0051111416,
        -0.008750488,
        0.036473747,
        -0.010790931,
        0.024244472,
        0.015092585,
        -0.017527737,
        0.020029787,
        -0.0019802328,
        -0.006084533,
        -0.014891886,
        0.0070177843,
        -0.031710483,
        -0.019976268,
        0.00828219,
        -0.026144424,
        0.021407923,
        0.021795942,
        -0.0002933136,
        0.009633565,
        0.019601628,
        0.018330533,
        0.005234906,
        -0.0072853835,
        -0.014985546,
        0.00075387664,
        0.013420091,
        0.011533518,
        -0.013058833,
        -0.0169524,
        0.028820416,
        -0.007412493,
        0.019012911,
        -0.0023582163,
        0.031496406,
        -0.0019902678,
        0.012858133,
        0.020872723,
        -0.025060648,
        -0.027669739,
        -0.018571373,
        0.010509952,
        0.0036661066,
        -0.012958483,
        0.0076131923,
        -0.009178647,
        -0.011459928,
        0.0012769491,
        -0.0023080416,
        -0.00038718234,
        0.012637364,
        0.028419016,
        -0.019909367,
        0.0043685543,
        0.0061547775,
        -0.021327643,
        -0.0027713224,
        -0.0070646144,
        -0.0027178025,
        -0.0167517,
        -0.0008149227,
        -0.023669133,
        0.034199156,
        -0.010162073,
        0.034627315,
        -0.026759902,
        0.015333424,
        0.0034854773,
        -0.006843845,
        -0.022946617,
        -0.013507061,
        0.0034419924,
        -0.015627783,
        -0.010302562,
        -0.01097825,
        -0.008723728,
        -0.008636759,
        0.0025605883,
        0.020845965,
        -0.0011255884,
        0.011580348,
        0.025823306,
        -0.00087722304,
        -0.010175453,
        0.043244004,
        0.0023732688,
        -0.01086452,
        0.0006175684,
        -0.010309253,
        -0.01091804,
        -0.00543226,
        -0.032540042,
        -0.041986287,
        0.007111444,
        -0.032540042,
        -0.00021575172,
        0.028097898,
        -0.017099578,
        -0.008998017,
        -0.001103846,
        0.015601023,
        -0.01907981,
        -0.0037296615,
        -0.012731024,
        -0.010643751,
        0.016992537,
        0.019641768,
        0.015052445,
        -0.00011425224,
        -0.023414915,
        -0.019695288,
        -0.0109448,
        -0.000100349636,
        0.025395148,
        0.0005076019,
        -0.048060786,
        -0.018745312,
        -0.011961676,
        -0.010516642,
        0.012256036,
        0.017327037,
        -0.011272609,
        -0.022438178,
        -0.008402609,
        -0.008964567,
        0.002167552,
        -0.0013379952,
        -0.006549486,
        -0.026920462,
        -0.017888995,
        0.0022193994,
        -0.0052516307,
        -0.0056195795,
        0.02511417,
        0.0050877263,
        0.019093191,
        -0.019775568,
        0.015855242,
        -0.0016474065,
        0.009760674,
        0.0040240204,
        -0.036339946,
        0.011794427,
        0.018169973,
        0.009539905,
        0.021541722,
        0.028633095,
        -0.034011837,
        0.010215593,
        -0.0221572,
        0.005298461,
        -0.010329322,
        -0.0167517,
        -0.012062026,
        0.036420226,
        0.014209508,
        0.022625498,
        -0.02498037,
        -0.004970652,
        -0.009332516,
        0.014557387,
        0.008656829,
        0.0018062934,
        0.024190951,
        -0.011386339,
        -0.0138348695,
        0.0022210719,
        -0.0048502325,
        0.008917738,
        -0.007660022,
        -0.00011874707,
        0.0012861479,
        -0.021300882,
        0.013226082,
        -0.003331608,
        -0.0078072017,
        0.019735428,
        0.020350905,
        0.028927455,
        0.011560278,
        0.015788343,
        -0.017741816,
        -0.007954381,
        -0.036875147,
        0.05234237,
        -0.0046127383,
        0.039684936,
        0.009131817,
        -0.0118747065,
        -0.012657434,
        0.0070980643,
        0.023816314,
        0.0021140324,
        0.020524845,
        -0.00059624406,
        -0.00339349,
        -0.0005109469,
        -0.0048401975,
        -0.0034955123,
        0.005549335,
        0.020779064,
        -0.023174075,
        0.025850065,
        0.007399113,
        0.0051278663,
        0.014303168,
        0.017193237,
        0.003010489,
        0.006335407,
        0.0069308146,
        0.026117666,
        -0.005696514,
        0.00045700895,
        -0.014758087,
        -0.0034118877,
        -0.0012016869,
        0.0037497315,
        -0.005810244,
        0.0025589156,
        -0.009111747,
        -0.011446549,
        0.011486689,
        0.005308496,
        -0.0035590671,
        -0.011312749,
        0.022304378,
        -0.015226385,
        -0.014985546,
        0.018584752,
        0.025970485,
        0.002864982,
        0.0011063548,
        -0.0119549865,
        0.018009415,
        -0.010550092,
        0.04693687,
        0.0019518004,
        0.021474821,
        0.008462819,
        -0.015614403,
        0.031335846,
        0.002881707,
        0.025649367,
        -0.022638878,
        0.017768575,
        -0.014089089,
        -0.012623984,
        -0.0050910716,
        -0.021595242,
        -0.031014727,
        0.050174817,
        -0.026693003,
        -0.010048344,
        -0.007833961,
        0.0013789713,
        0.007238554,
        -0.025569087,
        0.00035665932,
        0.01374121,
        -0.0032078433,
        -0.00016975813,
        0.015895382,
        -0.024003632,
        -0.015413704,
        0.02726834,
        0.019347409,
        -0.019802328,
        -0.008850838,
        0.0042247195,
        -0.002035425,
        0.09697789,
        0.015721442,
        0.0010670511,
        0.01902629,
        0.01116557,
        -0.017139718,
        -0.026987363,
        -0.0009867714,
        -0.0016206466,
        0.014129229,
        0.013527131,
        -0.028204937,
        -0.005786829,
        -0.017888995,
        0.02745566,
        0.0059105936,
        -0.01360072,
        -0.024070533,
        -0.003341643,
        -0.028231697,
        -0.006358822,
        -0.010188833,
        -0.015761582,
        0.015908763,
        0.010048344,
        0.0018330533,
        -0.0024067187,
        -0.014758087,
        0.032245684,
        -0.020993143,
        0.001787896,
        0.0047900225,
        0.0005410518,
        0.022946617,
        -0.008944497,
        5.4983237e-05,
        -0.011734217,
        -0.014396828,
        0.026933841,
        -0.011640558,
        0.02986405,
        0.020779064,
        0.010443052,
        -0.031228807,
        -0.0042682043,
        -0.018772071,
        -0.008496269,
        0.026706383,
        -0.010503261,
        -0.029489413,
        0.01914671,
        0.025609227,
        0.0019451104,
        -0.0139552895,
        -0.0024535486,
        0.0017427386,
        0.013045453,
        -0.0029937641,
        0.007412493,
        -0.026920462,
        -0.012316246,
        -0.037223026,
        0.037330065,
        0.008904357,
        0.0137947295,
        0.013098972,
        -0.021006523,
        0.023856454,
        -0.0274289,
        0.0036995565,
        -0.015333424,
        -0.00045115524,
        -0.003856771,
        0.0070779943,
        0.0018079659,
        0.014985546,
        0.0027579425,
        -0.010489882,
        0.014008809,
        0.0036460368,
        0.0139954295,
        0.0048401975,
        0.022170579,
        0.0009491403,
        0.005228216,
        0.002244487,
        -0.0068405,
        -0.014222888,
        -0.0017527736,
        0.020257246,
        0.016176362,
        -0.0019986301,
        0.0099747535,
        -0.0091853365,
        0.015828483,
        -0.00409092,
        0.029971091,
        0.017032677,
        0.006348787,
        0.019628389,
        0.008656829,
        0.0031392712,
        -0.0059641134,
        -0.0047465377,
        0.01616298,
        -0.0020387701,
        0.0023180766,
        0.010329322,
        0.00822867,
        0.0148651255,
        0.005201456,
        -0.017420696,
        0.0034520274,
        0.014263028,
        -0.015039065,
        0.008897668,
        0.012496875,
        0.001629009,
        0.0074526328,
        -0.047070667,
        0.0064391014,
        -0.020069927,
        0.031737246,
        0.014370068,
        -0.005495815,
        0.019641768,
        0.011372958,
        -0.025809927,
        -0.0274289,
        -0.0009667015,
        0.013132422,
        0.03551039,
        0.004773298,
        -0.020899484,
        -0.004405349,
        -0.032272443,
        -0.020297386,
        -0.003043939,
        0.0016097754,
        0.0014818296,
        0.0077670617,
        0.0219565,
        0.01616298,
        -0.0022495042,
        -0.017286897,
        -0.015386944,
        -0.028579576,
        0.009265617,
        -0.022344518,
        0.059674583,
        -0.008877598,
        0.012797924,
        0.0015980679,
        -0.0025672782,
        -0.013500371,
        -0.019829087,
        -0.009138507,
        -0.007934311,
        0.018450953,
        0.026880322,
        -0.017500976,
        -0.03034573,
        0.028900694,
        0.0167517,
        -0.004114335,
        -0.0031074937,
        -0.039042696,
        0.0020053203,
        -0.019842468,
        0.010108553,
        -0.003258018,
        0.013239462,
        -0.005602855,
        -0.009011397,
        -0.0031392712,
        -0.0029001045,
        -0.013560581,
        -0.008609999,
        -0.018169973,
        -0.03545687,
        0.0139552895,
        -0.033717476,
        -0.0109448,
        0.01907981,
        -0.012630674,
        -0.0040641604,
        0.03604559,
        -0.0020738924,
        0.015092585,
        0.013292981,
        0.030987967,
        -0.0021039974,
        0.025635988,
        -0.0021324297,
        -0.0019735429,
        -0.009071607,
        0.00018177918,
        -0.04091589,
        -0.0021290847,
        0.03773146,
        0.0009365966,
        -0.018036174,
        0.012296176,
        -0.0032396207,
        -0.01911995,
        0.00025672783,
        0.0036828315,
        -0.025207829,
        0.0042581693,
        -0.019548109,
        -0.025395148,
        -0.029088015,
        -0.045572113,
        -0.003142616,
        0.0077603715,
        -0.005830314,
        -0.020819204,
        0.008489579,
        -0.024204332,
        -0.015279904,
        -0.009339206,
        -0.012396525,
        0.024418412,
        -0.0053787404,
        0.0328344,
        0.018089695,
        -0.005489125,
        -0.0043183793,
        -0.003582482,
        0.0055560246,
        0.00037840175,
        -0.0019885954,
        -0.0101553835,
        -0.028017618,
        -0.027040882,
        0.017514355,
        0.0011807807,
        -0.010275803,
        -0.022946617,
        0.025702886,
        0.012851443,
        0.013861629,
        0.009800814,
        0.004381934,
        0.0028181523,
        0.0065294164,
        -0.023588855,
        0.018959392,
        -0.016270021,
        -0.010202213,
        0.0014625959,
        -0.0064758966,
        -0.015922142,
        0.011346199,
        0.0031877735,
        -0.011366269,
        -0.018531233,
        -0.002438496,
        0.020551605,
        0.011493378,
        -0.018651651,
        0.026278224,
        -0.008991327,
        0.0111053595,
        0.01663128,
        0.010677201,
        0.010262422,
        0.005194766,
        0.01105853,
        0.031175287,
        -0.013607411,
        -0.014396828,
        0.0035155823,
        -0.011379649,
        -0.014249648,
        0.0046194284,
        -0.018263634,
        -0.020886105,
        0.017219998,
        -0.013413401,
        0.010302562,
        -0.006683286,
        0.00018648307,
        0.0004666258,
        -0.01640382,
        -0.0033165554,
        -0.020631885,
        -0.023093795,
        0.0010168763,
        -0.008061421,
        -0.023040276,
        -0.002732855,
        -0.017674915,
        0.021046663,
        -0.011774357,
        -0.029221814,
        -0.0016992538,
        0.02515431,
        -0.013032072,
        0.004960617,
        0.015025686,
        0.01926713,
        -0.010182143,
        0.0021223947,
        -0.009479696,
        -0.04682983,
        -0.0028081173,
        0.004438799,
        -0.02436489,
        -0.029409133,
        -0.014169369,
        -0.009854334,
        0.021327643,
        -0.014155989,
        0.008643448,
        -0.0091251265,
        0.02464587,
        -0.003152651,
        -0.028258458,
        0.010376153,
        0.00279641,
        -0.006004253,
        0.023495195,
        -0.011506758,
        0.017848855,
        -0.01636368,
        0.014544007,
        -0.0034754423,
        -0.0139954295,
        -0.020658644,
        -0.0120553365,
        0.020618506,
        -0.011265919,
        -0.048515704,
        0.0015930504,
        0.029516174,
        -0.009693774,
        0.0046127383,
        -0.0053419457,
        -0.0080748005,
        0.026612723,
        0.028659856,
        0.010757481,
        0.022585358,
        -0.011493378,
        0.00010202213,
        -0.0015219694,
        -0.009011397,
        -0.014878506,
        -0.007874101,
        0.0032897955,
        0.059299946,
        -0.0020538226,
        -0.0074660126,
        0.0012710954,
        0.014503867,
        -0.056677476,
        -0.010081793,
        0.02452545,
        0.004585978,
        0.014089089,
        -0.009519835,
        -0.007854031,
        0.035082232,
        -0.0045659086,
        0.031442884,
        -0.006124673,
        -0.017072817,
        -0.0110652195,
        0.023040276,
        -0.0037698012,
        -0.025488807,
        -0.03585827,
        -0.009419486,
        0.01651086,
        -0.026037386,
        0.015427084,
        0.0070579243,
        -0.037945542,
        -0.03807934,
        -0.006104603,
        0.0007037018,
        0.046321392,
        0.013440161,
        0.013038763,
        -0.034948435,
        -0.020551605,
        -0.0045224237,
        -0.011366269,
        -0.0099346135,
        -0.014329928,
        0.013045453,
        0.029034493,
        -0.0018330533,
        -0.020110067,
        -0.01940093,
        -0.005766759,
        -0.012503564,
        0.010202213,
        -0.018838972,
        -0.006890675,
        0.011259229,
        0.0050375517,
        -0.025140928,
        -0.0011180622,
        0.01122578,
        0.0048401975,
        -0.0027930648,
        -0.009513145,
        -0.02745566,
        0.004679638,
        -0.014597527,
        0.020725545,
        -0.0069977148,
        -0.0015621093,
        -0.0167517,
        0.0027445625,
        -0.013466921,
        0.010269113,
        -0.008536409,
        -0.02515431,
        -0.004207995,
        0.012858133,
        0.01364086,
        -0.0015110982,
        0.0008688606,
        -0.026866943,
        -0.020203726,
        0.017541116,
        0.010289183,
        -0.010302562,
        0.007372353,
        0.028606337,
        -0.0016114479,
        0.0019384205,
        0.026800042,
        0.20048518,
        -0.0075730523,
        0.011112049,
        0.02223748,
        0.0033299355,
        0.02211706,
        0.013045453,
        0.013420091,
        0.014998926,
        -0.020043166,
        0.0013396676,
        0.018384052,
        -0.03047953,
        -0.0015880329,
        0.014396828,
        -0.023495195,
        -0.034948435,
        -0.014222888,
        -0.009198717,
        -0.0030255415,
        -0.006776945,
        -0.0025371732,
        0.021474821,
        -0.029917572,
        0.03856102,
        0.017393937,
        -0.00026258154,
        -0.027094401,
        -0.00066481635,
        0.014570767,
        -0.012021886,
        -0.038186383,
        -0.009352586,
        0.020364286,
        0.036821626,
        0.005422225,
        0.017032677,
        0.0018146558,
        -0.001675839,
        0.011961676,
        -0.012082096,
        -0.011961676,
        -0.015012305,
        0.0023933388,
        0.0063855816,
        0.0046528783,
        -0.012831373,
        0.00081784953,
        -0.00038864577,
        0.014544007,
        0.015882002,
        -0.012215896,
        0.018798832,
        -0.015922142,
        -0.006241747,
        -0.009285687,
        0.042521484,
        -0.019695288,
        2.2147478e-05,
        -0.0025204483,
        -0.013339811,
        0.0059674582,
        -0.017059438,
        0.01645734,
        0.0010436362,
        0.011988437,
        0.006081188,
        -0.00545233,
        0.005218181,
        0.0050877263,
        0.021193843,
        0.012637364,
        0.0002535919,
        0.03029221,
        -0.014544007,
        -0.028258458,
        0.0047799875,
        0.016310161,
        0.012296176,
        0.03299496,
        -0.009733914,
        -0.015547504,
        -0.014196129,
        0.014664426,
        -0.017674915,
        -0.014731326,
        -0.0024769634,
        -0.0003294813,
        -0.019467829,
        -0.009988134,
        0.012088786,
        0.011192329,
        0.0001456115,
        0.020712165,
        0.0045291134,
        0.013647551,
        -0.028231697,
        0.0139954295,
        -0.018343912,
        -0.018624892,
        -0.017126339,
        -0.017674915,
        -0.0023214216,
        0.016350301,
        -0.00839592,
        0.0071917237,
        0.018129835,
        -0.006619731,
        -0.0029703493,
        -0.0070378543,
        -0.007733612,
        -0.0276965,
        0.003268053,
        0.0036895217,
        0.009687085,
        -0.0017025988,
        0.007138204,
        -0.009559975,
        -0.01890587,
        -0.019882608,
        0.03636671,
        -0.0061848825,
        0.020083306,
        0.014089089,
        -0.017420696,
        -0.0099948235,
        -0.0070244744,
        0.0028465847,
        -0.0030556463,
        -0.031148527,
        0.015159485,
        -0.0055961646,
        0.0037564214,
        -0.015132725,
        -0.015105965,
        0.015748203,
        0.0034654073,
        -0.023856454,
        -0.02471277,
        0.006051083,
        -0.014530627,
        0.0015646181,
        0.011560278,
        0.0218896,
        0.04982694,
        -0.0162834,
        0.027830299,
        -0.010697271,
        -0.022210719,
        -0.001117226,
        0.0034486824,
        -0.0016649677,
        -0.025488807,
        -0.004365209,
        0.0074526328,
        0.01945445,
        -0.05030862,
        -0.008890978,
        -0.0099546835,
        0.0041611646,
        -0.026693003,
        -0.009031467,
        0.031576686,
        -0.04185249,
        -0.014008809,
        0.014196129,
        -0.17094226,
        0.004662913,
        0.010576852,
        -0.015105965,
        0.02223748,
        -0.014517247,
        0.017554495,
        0.015694683,
        -0.025341628,
        -0.0032329308,
        0.012235966,
        0.0059841834,
        -0.018665032,
        -0.008342399,
        -0.010329322,
        0.031255566,
        0.006506001,
        0.02498037,
        0.014958786,
        0.010570162,
        0.009386036,
        0.0021424647,
        0.0005506686,
        -0.015948903,
        -0.007733612,
        -0.00056237605,
        0.01085114,
        -0.009299066,
        -0.018330533,
        -0.007091374,
        -0.0101152435,
        -0.007706852,
        0.006810395,
        0.004907097,
        0.017327037,
        -0.00421803,
        0.011172259,
        0.0069843344,
        -0.00211905,
        0.02494023,
        0.007238554,
        0.009319136,
        0.03023869,
        -0.025836686,
        0.02237128,
        -0.002617453,
        -0.004973997,
        0.01945445,
        -0.024351511,
        -0.034466755,
        0.015413704,
        1.7737582e-06,
        -0.023000136,
        0.0029251918,
        0.021207223,
        0.0069843344,
        0.014691186,
        0.032941442,
        0.0018096385,
        -0.02986405,
        0.005482435,
        -0.010657132,
        -0.012115546,
        -0.0070110946,
        -0.004669603,
        0.005275046,
        0.0025722957,
        0.00818184,
        -0.0018263634,
        0.00014456619,
        -0.026304984,
        -0.010877901,
        -0.0075262226,
        -0.01118564,
        0.0080145905,
        0.02231776,
        3.0627543e-05,
        -0.035403352,
        -0.017005919,
        -0.018705172,
        -0.0027562699,
        0.042039808,
        -0.025194447,
        0.021595242,
        0.0009357603,
        0.011553588,
        -0.013667621,
        -0.0009140179,
        -0.0028114624,
        -0.024217712,
        0.009379346,
        -0.023936734,
        -0.00271613,
        -0.025528947,
        -0.0055760946,
        0.017888995,
        0.006592971,
        -0.015788343,
        -0.020926245,
        -0.007900861,
        0.009379346,
        0.016551,
        -0.030640088,
        0.013400021,
        0.026037386,
        0.014463727,
        0.0091251265,
        -0.0055861296,
        0.026318364,
        -0.0027278375,
        0.011774357,
        0.0013940237,
        -0.0010745773,
        -0.01086452,
        0.0119349165,
        0.0028114624,
        0.014008809,
        -0.02156848,
        0.0118747065,
        -0.04602703,
        0.014503867,
        0.00093994156,
        -0.03021193,
        0.0035155823,
        -0.020672025,
        -0.014396828,
        -0.08643448,
        -0.0064993114,
        0.01941431,
        -0.013406712,
        -0.029088015,
        -0.015253144,
        0.003162686,
        0.009580045,
        0.021260742,
        -0.0009800814,
        0.014731326,
        0.0006915762,
        0.008576549,
        -0.0036594167,
        0.03874834,
        0.009539905,
        0.01929389,
        -0.00039930793,
        -0.031656966,
        0.0059942184,
        -0.018718552,
        0.00082955696,
        -0.014891886,
        -0.011767667,
        -0.008088181,
        0.00411099,
        -0.01916009,
        -0.0059340084,
        0.0385075,
        0.019681908,
        -0.034948435,
        0.014878506,
        -0.010509952,
        -0.0039638104,
        -0.007900861,
        0.0019685254,
        -0.025850065,
        -0.0050542764,
        0.02718806,
        -0.029328853,
        0.00035937713,
        0.011112049,
        -0.000111325375,
        -0.034172397,
        0.0058470387,
        0.0032379483,
        0.0043049995,
        0.00836916,
        0.008402609,
        -0.0067736004,
        -0.006325372,
        -0.011821187,
        -0.017393937,
        -0.010315943,
        0.034145635,
        -0.023495195,
        -0.024886709,
        -0.0065227263,
        0.009352586,
        -0.0028984318,
        -0.0081417,
        0.0067434954,
        -0.00010526259,
        0.017929135,
        -0.005482435,
        -0.021381162,
        -0.016805219,
        0.036313187,
        0.010275803,
        -0.0069977148,
        0.0024518762,
        0.016551,
        -0.016229881,
        0.028927455,
        -0.0028348772,
        0.009673704,
        -0.025435288,
        0.00079401647,
        -0.0009600115,
        -0.01616298,
        -0.006566211,
        -0.014824986,
        0.026626103,
        -0.026331745,
        0.01357396,
        0.018477714,
        0.019012911,
        -0.007706852,
        0.0039403955,
        -0.030640088,
        -0.0007739466,
        0.01633692,
        0.010670511,
        -0.030506289,
        -0.002204347,
        -0.01103177,
        0.00070746493,
        -0.02472615,
        0.006318682,
        -0.0053720507,
        -0.020872723,
        0.0075396025,
        -0.0716095,
        0.025796546,
        -0.012249346,
        -0.021314263,
        -0.0064223767,
        0.010289183,
        -0.0053720507,
        0.0050475867,
        -0.008810698,
        0.011821187,
        -0.002915157,
        -0.023040276,
        0.0055326098,
        -0.0005305987,
        0.007512843,
        -0.011540208,
        -0.0032964854,
        -0.0016081029,
        0.012891583,
        0.0042882743,
        -0.023615614,
        0.0019484555,
        -0.0001933821,
        0.014891886,
        -0.04313696,
        -0.01355389,
        -0.012644054,
        -0.0073589734,
        0.0218896,
        0.006345442,
        0.012135616,
        -0.015761582,
        0.0216889,
        0.017046059,
        -0.019815708,
        -0.016765079,
        0.020364286,
        0.019922748,
        0.0021140324,
        -0.020404426,
        0.0024535486,
        -0.008429369,
        0.021140324,
        -0.02503389,
        -0.020792445,
        -0.009988134,
        0.032379482,
        0.015467224,
        0.020966385,
        0.010168763,
        0.008362469,
        0.021113563,
        0.026572583,
        -0.020578366,
        -0.029542932,
        -0.01096487,
        -0.003000454,
        -0.01906643,
        -0.020150207,
        -0.03559067,
        0.04102293,
        0.01091804,
        0.008509649,
        0.007874101,
        0.019347409,
        0.020886105,
        0.00550585,
        -0.0024351513,
        0.04123701,
        0.010690581,
        -0.025047269,
        0.018705172,
        0.017594635,
        0.01107191,
        0.00408423,
        -0.01099832,
        -0.007847342,
        -0.022291,
        -0.012844753,
        0.02487333,
        -0.014035569,
        0.0099546835,
        -0.048060786,
        0.0100550335,
        -0.01936079,
        -0.0029536244,
        -0.016310161,
        -0.0129451025,
        0.006843845,
        0.0110786,
        -0.036634307,
        0.0078005116,
        0.0064156866,
        0.0033466604,
        -0.009118437,
        0.00411099,
        0.007124824,
        -0.009406106,
        -0.008469509,
        0.023588855,
        -0.0014592509,
        0.010369462,
        -0.0064959666,
        -0.037704702,
        -0.008870908,
        0.017594635,
        0.025743026,
        -0.010576852,
        -0.03872158,
        0.010897971,
        -0.008730418,
        0.010175453,
        -0.019936128,
        -0.0055961646,
        0.008737109,
        -0.0044421437,
        0.011807807,
        -0.01926713,
        -0.023147317,
        0.022933237,
        0.00104949,
        0.025702886,
        0.0054489854,
        -0.024311371,
        -0.002759615,
        0.003043939,
        0.0053753955,
        0.0033031756,
        0.015333424,
        0.0010545074,
        0.017996034,
        -0.018598132,
        0.0007463504,
        0.026666243,
        -0.013346502,
        0.012764473,
        0.03591179,
        0.051111415,
        -0.02156848,
        0.051486053,
        0.035082232,
        -0.003030559,
        0.0067936704,
        -0.034092117,
        0.003552377,
        0.010530022,
        -0.01910657,
        -0.01355389,
        -0.026425404,
        -0.0013789713,
        -0.016136222,
        -0.034600556,
        0.00680036,
        -0.044501718,
        -5.8798614e-05,
        -0.016096082,
        -0.008496269,
        0.005696514,
        0.007920931,
        0.03604559,
        0.0014550698,
        0.028445777,
        0.004743193,
        -0.022344518,
        -0.040300414,
        0.01667142,
        0.010563471,
        -0.018062934,
        -0.034092117,
        0.015333424,
        0.006817085,
        -0.0055459896,
        -0.01657776,
        -0.001906643,
        -0.018183354,
        -0.019427689,
        0.029007735,
        -0.00043150343,
        0.019347409,
        0.004733158,
        0.020096688,
        -0.0045659086,
        -0.01378135,
        0.016430581,
        0.0034219224,
        -0.028044378,
        -0.020484706,
        0.011727528,
    ],
)
