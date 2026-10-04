#!/usr/bin/env python3
"""Builds the Traffik360 static site into ./site from the bilingual strings below.

Run:  python3 tools/build.py
Every visible word lives in STR as {"en": ..., "ar": ...}. Edit text there, rerun, commit.
Anything in [square brackets] is a placeholder waiting for a real fact.
The Arabic copy is a working draft for a native copywriter to review before launch.
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
DOMAIN = "https://traffik360.com"
GLOSSARY = "https://glossary.promo"
LINKEDIN = "https://www.linkedin.com/company/traffik360/"
PHONE_DXB = "+971 4 453 4033"
EMAIL = "[briefs@traffik360.com]"

PAGES = ["", "merchandise", "posm-displays", "activations", "work", "sectors",
         "sustainability", "about", "brief", "privacy"]

STR = {
    # ---------- shared ----------
    "skip": {"en": "Skip to content", "ar": "انتقل إلى المحتوى"},
    "menu": {"en": "Menu", "ar": "القائمة"},
    "nav.services": {"en": "What we do", "ar": "ماذا نقدم"},
    "nav.work": {"en": "Work", "ar": "أعمالنا"},
    "nav.sectors": {"en": "Sectors", "ar": "القطاعات"},
    "nav.sustainability": {"en": "Sustainability", "ar": "الاستدامة"},
    "nav.about": {"en": "About", "ar": "من نحن"},
    "nav.brief": {"en": "Send a brief", "ar": "أرسل طلبك"},
    "nav.label": {"en": "Main", "ar": "القائمة الرئيسية"},
    "lang.other": {"en": "عربي", "ar": "English"},
    "cta.brief": {"en": "Send a brief", "ar": "أرسل طلبك"},
    "cta.work": {"en": "See our work", "ar": "شاهد أعمالنا"},
    "cta.glossary": {"en": "Order on Glossary", "ar": "اطلب عبر Glossary"},
    "foot.tag": {"en": "Branded merchandise, POSM and activations for brands across the GCC and Levant.",
                 "ar": "منتجات ترويجية ومواد نقاط بيع وفعاليات للعلامات التجارية في الخليج والمشرق."},
    "foot.whatsapp": {"en": "WhatsApp us", "ar": "تواصل عبر واتساب"},
    "foot.dubai": {"en": "Dubai", "ar": "دبي"},
    "foot.riyadh": {"en": "Riyadh", "ar": "الرياض"},
    "foot.beirut": {"en": "Beirut", "ar": "بيروت"},
    "foot.dxb.addr": {"en": "Thuraya Tower, Office 805<br>Barsha Heights (TECOM), Dubai",
                      "ar": "برج الثريا، مكتب 805<br>برشا هايتس (تيكوم)، دبي"},
    "foot.addr.tbc": {"en": "[Address]<br>[Phone]", "ar": "[العنوان]<br>[الهاتف]"},
    "foot.privacy": {"en": "Privacy policy", "ar": "سياسة الخصوصية"},
    "foot.rights": {"en": "© 2026 Traffik360", "ar": "© 2026 Traffik360"},
    "doors.h": {"en": "Two ways to start.", "ar": "طريقتان للبدء."},
    "doors.a.h": {"en": "A bespoke project or programme", "ar": "مشروع أو برنامج مخصص"},
    "doors.a.p": {"en": "Custom products, POSM, activations or a recurring programme. A specialist replies within one working day.",
                  "ar": "منتجات مخصصة أو مواد نقاط بيع أو فعاليات أو برنامج متكرر. يرد عليك مختص خلال يوم عمل واحد."},
    "doors.b.h": {"en": "Stock items, priced instantly", "ar": "منتجات جاهزة بأسعار فورية"},
    "doors.b.p": {"en": "Smaller orders of catalogue products with your logo. Browse, price and order online without waiting for a quote.",
                  "ar": "طلبات أصغر من منتجات الكتالوج مع شعارك. تصفّح واطّلع على السعر واطلب عبر الإنترنت دون انتظار عرض سعر."},
    "case.sum": {"en": "[Brief, what we made, quantity, timeline and result in two lines.]",
                 "ar": "[الموجز، ما صنعناه، الكمية، المدة، النتيجة في سطرين.]"},
    "case.kenvue.meta": {"en": "Kenvue · Healthcare · GCC", "ar": "Kenvue · الرعاية الصحية · الخليج"},
    "case.kenvue.h": {"en": "A patient education pouch programme, produced in tens of thousands",
                      "ar": "برنامج أكياس للتوعية الصحية للمرضى، بعشرات الآلاف من القطع"},
    "case.kenvue.ph": {"en": "[Photo: pouches in use]", "ar": "[صورة: الأكياس قيد الاستخدام]"},
    "case.henkel.meta": {"en": "Henkel · FMCG · GCC", "ar": "Henkel · السلع الاستهلاكية · الخليج"},
    "case.henkel.h": {"en": "Ramadan gifting: tote bags and serving trays for a regional launch",
                      "ar": "هدايا رمضان: حقائب قماشية وصوانٍ للتقديم لإطلاق إقليمي"},
    "case.henkel.ph": {"en": "[Photo: Ramadan gift set]", "ar": "[صورة: طقم هدايا رمضان]"},
    "case.mdl.meta": {"en": "MDL Beast · Entertainment · KSA", "ar": "MDL Beast · الترفيه · السعودية"},
    "case.mdl.h": {"en": "Event merchandise delivered on site in AlUla", "ar": "منتجات فعالية سُلّمت في موقع الحدث في العُلا"},
    "case.mdl.ph": {"en": "[Photo: event merchandise on site]", "ar": "[صورة: منتجات الفعالية في الموقع]"},
    "case.tbc.meta": {"en": "[Client] · [Sector] · [Market]", "ar": "[العميل] · [القطاع] · [السوق]"},
    "case.tbc.h": {"en": "[Case study title]", "ar": "[عنوان دراسة الحالة]"},
    "case.tbc.ph": {"en": "[Photo]", "ar": "[صورة]"},

    # ---------- home ----------
    "home.title": {"en": "Traffik360 | Branded merchandise, POSM and activations in the GCC",
                   "ar": "Traffik360 | منتجات ترويجية ومواد نقاط بيع وفعاليات في الخليج"},
    "home.desc": {"en": "Merchandise, retail displays and activations for multinational brands, sourced, produced and delivered across the UAE, Saudi Arabia and the Levant.",
                  "ar": "منتجات ترويجية ووحدات عرض وفعاليات للعلامات التجارية متعددة الجنسيات، نوفّرها وننتجها ونسلّمها في الإمارات والسعودية والمشرق."},
    "home.eyebrow": {"en": "Dubai · Riyadh · Beirut", "ar": "دبي · الرياض · بيروت"},
    "home.h1": {"en": "Merchandise and retail displays for brands that operate at scale.",
                "ar": "منتجات ترويجية ووحدات عرض للعلامات التجارية التي تعمل على نطاق واسع."},
    "home.lead": {"en": "We source, produce and deliver branded merchandise, POSM and activations across the UAE, Saudi Arabia and the Levant, with our own teams on the ground in all three markets.",
                  "ar": "نوفّر وننتج ونسلّم المنتجات الترويجية ومواد نقاط البيع والفعاليات في الإمارات والسعودية والمشرق، عبر فرقنا الموجودة في الأسواق الثلاثة."},
    "home.hero.ph": {"en": "[Hero photo: a large brand programme in production or on shelf. No alcohol brands.]",
                     "ar": "[صورة رئيسية: برنامج كبير لعلامة تجارية قيد الإنتاج أو على الرف. بدون علامات مشروبات كحولية.]"},
    "home.clients": {"en": "Trusted by brand teams at", "ar": "موثوقون لدى فرق العلامات التجارية في"},
    "home.stats.label": {"en": "Traffik360 in numbers", "ar": "Traffik360 بالأرقام"},
    "home.stat1": {"en": "offices with our own teams: Dubai, Riyadh, Beirut", "ar": "مكاتب بفرق خاصة بنا: دبي، الرياض، بيروت"},
    "home.stat2": {"en": "orders delivered every year", "ar": "طلب نسلّمه كل عام"},
    "home.stat3": {"en": "partner companies worldwide through the IGC network", "ar": "شركة شريكة حول العالم عبر شبكة IGC"},
    "home.stat4.b": {"en": "Top 15%", "ar": "أعلى 15%"},
    "home.stat4": {"en": "EcoVadis Silver rating, 2026", "ar": "تصنيف EcoVadis الفضي، 2026"},
    "home.services.h": {"en": "One partner from brief to delivery, in every market you sell in.",
                        "ar": "شريك واحد من الفكرة إلى التسليم، في كل سوق تبيع فيه."},
    "svc.merch.h": {"en": "Branded merchandise and gifting", "ar": "المنتجات الترويجية والهدايا"},
    "svc.merch.p": {"en": "Bespoke products and seasonal programmes that people keep, produced to your brand standards and delivered on time for Ramadan, launches and year end.",
                    "ar": "منتجات مصممة خصيصاً وبرامج موسمية يحتفظ بها الناس، تُنتج وفق معايير علامتك وتصل في موعدها لرمضان وإطلاق المنتجات ونهاية العام."},
    "svc.merch.tags": {"en": "Gift sets · Apparel · Drinkware · Bags and pouches · Packaging",
                       "ar": "أطقم الهدايا · الملابس · أدوات الشرب · الحقائب والأكياس · التغليف"},
    "svc.merch.ph": {"en": "[Photo: branded gift set]", "ar": "[صورة: طقم هدايا]"},
    "svc.posm.h": {"en": "POSM and retail displays", "ar": "مواد نقاط البيع ووحدات العرض"},
    "svc.posm.p": {"en": "Displays that win the shelf and survive the store: designed, prototyped, produced and installed across modern trade in the GCC.",
                   "ar": "وحدات عرض تكسب الرف وتصمد في المتجر: تصميم ونماذج أولية وإنتاج وتركيب في متاجر التجزئة الحديثة في الخليج."},
    "svc.posm.tags": {"en": "Shelf branding · Floor units · Standees · Kiosks · Gondola ends",
                      "ar": "علامات الرفوف · وحدات أرضية · ستاندات · أكشاك · نهايات الممرات"},
    "svc.posm.ph": {"en": "[Photo: in store display]", "ar": "[صورة: وحدة عرض في متجر]"},
    "svc.act.h": {"en": "Activations and events", "ar": "الفعاليات والتفعيل"},
    "svc.act.p": {"en": "Launches, conferences and brand experiences, with the merchandise, builds and staff that make them work on the day.",
                  "ar": "إطلاق المنتجات والمؤتمرات وتجارب العلامة، مع المنتجات والإنشاءات والطاقم الذين يصنعون نجاح اليوم."},
    "svc.act.tags": {"en": "Product launches · Event merchandise · Booths · Sampling",
                     "ar": "إطلاق المنتجات · منتجات الفعاليات · الأجنحة · توزيع العينات"},
    "svc.act.ph": {"en": "[Photo: brand activation]", "ar": "[صورة: تفعيل علامة تجارية]"},
    "home.work.k": {"en": "Selected work", "ar": "أعمال مختارة"},
    "home.work.h": {"en": "Programmes, not one off orders.", "ar": "برامج متكاملة، لا طلبات لمرة واحدة."},
    "home.work.all": {"en": "All case studies", "ar": "جميع دراسات الحالة"},
    "how.k": {"en": "How we work", "ar": "كيف نعمل"},
    "how.h": {"en": "Five steps, one accountable team.", "ar": "خمس خطوات، وفريق واحد مسؤول."},
    "how.1.h": {"en": "Brief", "ar": "الموجز"},
    "how.1.p": {"en": "You tell us the audience, quantity, budget and date. We reply within one working day.",
                "ar": "تخبرنا بالجمهور والكمية والميزانية والموعد. نرد خلال يوم عمل واحد."},
    "how.2.h": {"en": "Design and sourcing", "ar": "التصميم والتوريد"},
    "how.2.p": {"en": "Concepts, materials and factories matched to your budget and compliance rules.",
                "ar": "أفكار ومواد ومصانع تناسب ميزانيتك وقواعد الامتثال لديك."},
    "how.3.h": {"en": "Samples", "ar": "العينات"},
    "how.3.p": {"en": "Physical samples in your hands before anything goes into production.",
                "ar": "عينات فعلية بين يديك قبل أن يبدأ أي إنتاج."},
    "how.4.h": {"en": "Production and QC", "ar": "الإنتاج ومراقبة الجودة"},
    "how.4.p": {"en": "Quality checks at the factory and on arrival, against the approved sample.",
                "ar": "فحص الجودة في المصنع وعند الوصول، مقارنةً بالعينة المعتمدة."},
    "how.5.h": {"en": "Delivery", "ar": "التسليم"},
    "how.5.p": {"en": "To your warehouse, stores or event site, in the UAE, KSA, Lebanon and beyond.",
                "ar": "إلى مستودعك أو متاجرك أو موقع فعاليتك، في الإمارات والسعودية ولبنان وخارجها."},
    "sus.k": {"en": "Sustainability and compliance", "ar": "الاستدامة والامتثال"},
    "sus.h": {"en": "Ready for your procurement checklist.", "ar": "جاهزون لقائمة متطلبات المشتريات لديك."},
    "sus.p": {"en": "Independently rated, certified and audited, so your sustainability and supplier teams can approve us quickly. Lower impact materials are offered on every brief.",
              "ar": "تقييم مستقل وشهادات وتدقيق، ليتمكن فريقا الاستدامة والموردين لديك من اعتمادنا بسرعة. نقدّم خيارات مواد أقل أثراً على البيئة في كل طلب."},
    "sus.link": {"en": "Our standards and certificates", "ar": "معاييرنا وشهاداتنا"},
    "badge.eco.h": {"en": "EcoVadis Silver", "ar": "EcoVadis الفضي"},
    "badge.eco.p": {"en": "Top 15% of rated companies, 2026", "ar": "ضمن أعلى 15% من الشركات المقيّمة، 2026"},
    "badge.iso.h": {"en": "ISO certified", "ar": "شهادات ISO"},
    "badge.iso.p": {"en": "[Standards and certificate numbers]", "ar": "[المعايير وأرقام الشهادات]"},
    "badge.igc.h": {"en": "IGC member", "ar": "عضو في IGC"},
    "badge.igc.p": {"en": "46+ partner companies across MENA, APAC and Europe", "ar": "أكثر من 46 شركة شريكة في الشرق الأوسط وآسيا والمحيط الهادئ وأوروبا"},
    "badge.audit.h": {"en": "Audited sourcing", "ar": "توريد خاضع للتدقيق"},
    "badge.audit.p": {"en": "[Factory audit standard used]", "ar": "[معيار تدقيق المصانع المعتمد]"},

    # ---------- merchandise ----------
    "merch.title": {"en": "Branded merchandise and corporate gifting | Traffik360", "ar": "المنتجات الترويجية والهدايا للشركات | Traffik360"},
    "merch.desc": {"en": "Bespoke branded merchandise and seasonal gifting programmes for brands in the UAE, Saudi Arabia and the Levant.",
                   "ar": "منتجات ترويجية مخصصة وبرامج هدايا موسمية للعلامات التجارية في الإمارات والسعودية والمشرق."},
    "merch.lead": {"en": "Bespoke products and seasonal programmes, produced to your brand standards and delivered on time across the GCC and Levant.",
                   "ar": "منتجات مخصصة وبرامج موسمية، تُنتج وفق معايير علامتك وتُسلَّم في موعدها في الخليج والمشرق."},
    "merch.make.h": {"en": "What we make", "ar": "ما نصنعه"},
    "merch.c1": {"en": "Gift sets and hampers", "ar": "أطقم الهدايا والسلال"},
    "merch.c2": {"en": "Apparel and uniforms", "ar": "الملابس والزي الموحد"},
    "merch.c3": {"en": "Drinkware", "ar": "أدوات الشرب"},
    "merch.c4": {"en": "Bags, pouches and totes", "ar": "الحقائب والأكياس"},
    "merch.c5": {"en": "Tech accessories", "ar": "ملحقات التقنية"},
    "merch.c6": {"en": "Packaging and boxes", "ar": "التغليف والعلب"},
    "merch.c7": {"en": "Stationery and desk items", "ar": "القرطاسية وأدوات المكتب"},
    "merch.c8": {"en": "Event giveaways", "ar": "هدايا الفعاليات"},
    "merch.split.h": {"en": "Bespoke with us, stock on Glossary", "ar": "المخصص معنا، والجاهز عبر Glossary"},
    "merch.bespoke.h": {"en": "Bespoke, with Traffik360", "ar": "مخصص، مع Traffik360"},
    "merch.bespoke.p": {"en": "Custom shapes, materials, packaging and larger runs, designed around your brief and checked against an approved sample.",
                        "ar": "أشكال ومواد وتغليف مخصصة وكميات أكبر، مصممة حول موجزك ومطابقة لعينة معتمدة."},
    "merch.stock.h": {"en": "Stock items, on Glossary", "ar": "منتجات جاهزة، عبر Glossary"},
    "merch.stock.p": {"en": "Catalogue products with your logo in smaller quantities, with prices shown instantly and ordering online.",
                      "ar": "منتجات الكتالوج مع شعارك بكميات أصغر، مع أسعار فورية وطلب عبر الإنترنت."},
    "merch.season.h": {"en": "Seasonal programmes", "ar": "البرامج الموسمية"},
    "merch.season.p": {"en": "Seasonal factory capacity fills early. Brief us as soon as the occasion is confirmed.",
                       "ar": "تمتلئ طاقة المصانع الموسمية مبكراً. أرسل لنا موجزك فور تأكيد المناسبة."},
    "merch.s1": {"en": "Ramadan and Eid", "ar": "رمضان والعيد"},
    "merch.s2": {"en": "UAE National Day", "ar": "اليوم الوطني الإماراتي"},
    "merch.s3": {"en": "Saudi National Day and Founding Day", "ar": "اليوم الوطني السعودي ويوم التأسيس"},
    "merch.s4": {"en": "Year end and client gifting", "ar": "نهاية العام وهدايا العملاء"},
    "merch.s5": {"en": "Product launches", "ar": "إطلاق المنتجات"},
    "merch.s6": {"en": "Employee onboarding and recognition", "ar": "استقبال الموظفين وتكريمهم"},

    # ---------- posm ----------
    "posm.title": {"en": "POSM and retail displays | Traffik360", "ar": "مواد نقاط البيع ووحدات العرض | Traffik360"},
    "posm.desc": {"en": "Point of sale materials and retail displays designed, prototyped, produced and installed across modern trade in the GCC.",
                  "ar": "مواد نقاط البيع ووحدات العرض: تصميم ونماذج أولية وإنتاج وتركيب في متاجر التجزئة الحديثة في الخليج."},
    "posm.lead": {"en": "Displays that win attention at the shelf and hold up in a busy store, from first 3D visual to rollout.",
                  "ar": "وحدات عرض تجذب الانتباه عند الرف وتصمد في المتاجر المزدحمة، من أول تصور ثلاثي الأبعاد حتى التوزيع."},
    "posm.what.h": {"en": "What we deliver", "ar": "ما نقدمه"},
    "posm.c1": {"en": "Shelf branding and wobblers", "ar": "علامات الرفوف والملصقات المتحركة"},
    "posm.c2": {"en": "Floor standing units", "ar": "وحدات العرض الأرضية"},
    "posm.c3": {"en": "Standees and cutouts", "ar": "الستاندات والمجسمات"},
    "posm.c4": {"en": "Kiosks and gondola ends", "ar": "الأكشاك ونهايات الممرات"},
    "posm.c5": {"en": "Counter displays", "ar": "وحدات العرض على الكاونتر"},
    "posm.c6": {"en": "Window and in store graphics", "ar": "رسومات الواجهات والمتاجر"},
    "posm.proc.h": {"en": "From visual to store", "ar": "من التصور إلى المتجر"},
    "posm.p1.h": {"en": "Design and 3D visuals", "ar": "التصميم والتصورات ثلاثية الأبعاد"},
    "posm.p1.p": {"en": "Concepts built around the retailer's planogram and your brand rules.", "ar": "أفكار مبنية حول مخطط عرض المتجر وقواعد علامتك."},
    "posm.p2.h": {"en": "Prototype", "ar": "النموذج الأولي"},
    "posm.p2.p": {"en": "A physical unit to approve before the run.", "ar": "وحدة فعلية للاعتماد قبل الإنتاج."},
    "posm.p3.h": {"en": "Production", "ar": "الإنتاج"},
    "posm.p3.p": {"en": "Materials chosen for store conditions and transport.", "ar": "مواد مختارة لظروف المتجر والنقل."},
    "posm.p4.h": {"en": "Rollout", "ar": "التوزيع"},
    "posm.p4.p": {"en": "Delivery and installation across your store list.", "ar": "التسليم والتركيب في قائمة متاجرك."},

    # ---------- activations ----------
    "act.title": {"en": "Activations and corporate events | Traffik360", "ar": "الفعاليات والتفعيل | Traffik360"},
    "act.desc": {"en": "Product launches, conferences and brand experiences in the UAE and Saudi Arabia, with the merchandise and builds that make them work.",
                 "ar": "إطلاق المنتجات والمؤتمرات وتجارب العلامة في الإمارات والسعودية، مع المنتجات والإنشاءات التي تصنع نجاحها."},
    "act.lead": {"en": "Launches, conferences and brand experiences, delivered with the merchandise, builds and people that make them work on the day.",
                 "ar": "إطلاق المنتجات والمؤتمرات وتجارب العلامة، مع المنتجات والإنشاءات والطاقم الذين يصنعون نجاح اليوم."},
    "act.what.h": {"en": "What we run", "ar": "ما ننفذه"},
    "act.c1.h": {"en": "Product launches", "ar": "إطلاق المنتجات"},
    "act.c1.p": {"en": "Let your audience experience the product first hand.", "ar": "دع جمهورك يجرب المنتج بنفسه."},
    "act.c2.h": {"en": "Conferences and corporate events", "ar": "المؤتمرات وفعاليات الشركات"},
    "act.c2.p": {"en": "Delegate kits, branded spaces and event merchandise.", "ar": "حقائب المشاركين والمساحات المعلَّمة ومنتجات الفعالية."},
    "act.c3.h": {"en": "Booths and exhibition stands", "ar": "الأجنحة ومنصات المعارض"},
    "act.c3.p": {"en": "Designed, built and staffed for trade shows and malls.", "ar": "مصممة ومنفذة ومزودة بالطاقم للمعارض والمراكز التجارية."},
    "act.c4.h": {"en": "Sampling and roadshows", "ar": "توزيع العينات والجولات الترويجية"},
    "act.c4.p": {"en": "Reach shoppers where they are.", "ar": "صل إلى المتسوقين حيث يتواجدون."},
    "act.partner": {"en": "Event production is delivered with our partners at Activate360.", "ar": "يُنفَّذ إنتاج الفعاليات مع شركائنا في Activate360."},

    # ---------- work ----------
    "work.title": {"en": "Case studies | Traffik360", "ar": "دراسات الحالة | Traffik360"},
    "work.desc": {"en": "Merchandise, POSM and activation programmes delivered for brands across the GCC and Levant.",
                  "ar": "برامج منتجات ترويجية ومواد نقاط بيع وفعاليات نفذناها لعلامات تجارية في الخليج والمشرق."},
    "work.h1": {"en": "Programmes we have delivered.", "ar": "برامج نفذناها."},
    "work.lead": {"en": "A selection of recent work. Each case shows the brief, what we made, the scale and the result.",
                  "ar": "مجموعة من أعمالنا الأخيرة. تعرض كل حالة الموجز وما صنعناه والحجم والنتيجة."},
    "work.f.all": {"en": "All", "ar": "الكل"},
    "work.f.merch": {"en": "Merchandise", "ar": "المنتجات الترويجية"},
    "work.f.posm": {"en": "POSM", "ar": "نقاط البيع"},
    "work.f.act": {"en": "Activations", "ar": "الفعاليات"},
    "work.filter": {"en": "Filter by service", "ar": "تصفية حسب الخدمة"},

    # ---------- sectors ----------
    "sec.title": {"en": "Sectors we serve | Traffik360", "ar": "القطاعات التي نخدمها | Traffik360"},
    "sec.desc": {"en": "Merchandise and retail programmes for beauty, FMCG, tourism and entertainment, healthcare, technology and financial services brands.",
                 "ar": "برامج منتجات ترويجية وتجزئة لعلامات التجميل والسلع الاستهلاكية والسياحة والترفيه والرعاية الصحية والتقنية والخدمات المالية."},
    "sec.h1": {"en": "Built around how your sector buys.", "ar": "مصممة حول طريقة الشراء في قطاعك."},
    "sec.lead": {"en": "Every sector has its own approval rules, seasons and compliance needs. We plan for them from the first brief.",
                 "ar": "لكل قطاع قواعد اعتماد ومواسم ومتطلبات امتثال خاصة. نخطط لها من الموجز الأول."},
    "sec.1.h": {"en": "Beauty and personal care", "ar": "التجميل والعناية الشخصية"},
    "sec.1.p": {"en": "Gift with purchase, counter displays and launch kits held to strict brand standards.",
                "ar": "هدايا مع الشراء ووحدات عرض على الكاونتر وحقائب إطلاق وفق معايير علامة صارمة."},
    "sec.2.h": {"en": "FMCG and food", "ar": "السلع الاستهلاكية والأغذية"},
    "sec.2.p": {"en": "Seasonal promotions and POSM rolled out across modern trade at volume.",
                "ar": "عروض موسمية ومواد نقاط بيع تُوزَّع على متاجر التجزئة الحديثة بكميات كبيرة."},
    "sec.3.h": {"en": "Tourism and entertainment", "ar": "السياحة والترفيه"},
    "sec.3.p": {"en": "Event merchandise and destination gifting delivered on site, on tight dates.",
                "ar": "منتجات فعاليات وهدايا وجهات تُسلَّم في الموقع وفي مواعيد ضيقة."},
    "sec.4.h": {"en": "Healthcare and pharma", "ar": "الرعاية الصحية والأدوية"},
    "sec.4.p": {"en": "Patient and HCP materials that respect the sector's compliance rules.",
                "ar": "مواد للمرضى والعاملين في القطاع الصحي تراعي قواعد الامتثال."},
    "sec.5.h": {"en": "Technology", "ar": "التقنية"},
    "sec.5.p": {"en": "Partner, channel and employee programmes across several markets.",
                "ar": "برامج للشركاء والقنوات والموظفين في عدة أسواق."},
    "sec.6.h": {"en": "Financial services", "ar": "الخدمات المالية"},
    "sec.6.p": {"en": "Client gifting and campaign merchandise with supplier due diligence ready.",
                "ar": "هدايا العملاء ومنتجات الحملات مع جاهزية تامة لتدقيق الموردين."},

    # ---------- sustainability ----------
    "susp.title": {"en": "Sustainability and compliance | Traffik360", "ar": "الاستدامة والامتثال | Traffik360"},
    "susp.desc": {"en": "EcoVadis Silver (top 15%, 2026), ISO certification, audited sourcing and lower impact materials on every brief.",
                  "ar": "تصنيف EcoVadis الفضي (أعلى 15%، 2026)، وشهادات ISO، وتوريد خاضع للتدقيق، ومواد أقل أثراً في كل طلب."},
    "susp.h1": {"en": "Responsible by default, documented on request.", "ar": "مسؤولون افتراضياً، وموثقون عند الطلب."},
    "susp.pillars.h": {"en": "Three commitments", "ar": "ثلاثة التزامات"},
    "susp.p1.h": {"en": "Lower footprint", "ar": "أثر بيئي أقل"},
    "susp.p1.p": {"en": "Sustainable practices across our operations, and lower impact material options offered on every brief.",
                  "ar": "ممارسات مستدامة في عملياتنا، وخيارات مواد أقل أثراً في كل طلب."},
    "susp.p2.h": {"en": "Ethical sourcing", "ar": "توريد أخلاقي"},
    "susp.p2.p": {"en": "A transparent, responsible supply chain, with factory audits against [standard].",
                  "ar": "سلسلة توريد شفافة ومسؤولة، مع تدقيق للمصانع وفق [المعيار]."},
    "susp.p3.h": {"en": "Communities", "ar": "المجتمعات"},
    "susp.p3.p": {"en": "Supporting the communities where we operate. [Programmes to add]",
                  "ar": "دعم المجتمعات التي نعمل فيها. [البرامج تُضاف لاحقاً]"},
    "susp.docs.h": {"en": "Documents for your supplier file", "ar": "مستندات لملف الموردين لديك"},
    "susp.docs.p": {"en": "Ask your Traffik360 contact for our EcoVadis scorecard, ISO certificates and supplier questionnaires.",
                    "ar": "اطلب من جهة اتصالك في Traffik360 بطاقة تقييم EcoVadis وشهادات ISO واستبيانات الموردين."},

    # ---------- about ----------
    "about.title": {"en": "About Traffik360", "ar": "من نحن | Traffik360"},
    "about.desc": {"en": "Traffik360 is a merchandise and retail activation partner with teams in Dubai, Riyadh and Beirut, and a member of the IGC global network.",
                   "ar": "Traffik360 شريك في المنتجات الترويجية وتفعيل التجزئة بفرق في دبي والرياض وبيروت، وعضو في شبكة IGC العالمية."},
    "about.h1": {"en": "A regional team with a global network.", "ar": "فريق إقليمي بشبكة عالمية."},
    "about.lead": {"en": "Traffik360 has delivered branded merchandise, POSM and activations for multinational brands since [year], with teams in Dubai, Riyadh and Beirut.",
                   "ar": "تقدّم Traffik360 المنتجات الترويجية ومواد نقاط البيع والفعاليات للعلامات متعددة الجنسيات منذ [السنة]، بفرق في دبي والرياض وبيروت."},
    "about.values.h": {"en": "What we hold ourselves to", "ar": "ما نلتزم به"},
    "about.v1.h": {"en": "Trust", "ar": "الثقة"},
    "about.v1.p": {"en": "We say what we can deliver, then deliver it.", "ar": "نقول ما نستطيع تقديمه، ثم نقدمه."},
    "about.v2.h": {"en": "Care", "ar": "الاهتمام"},
    "about.v2.p": {"en": "For your brand, our people and the places we source from.", "ar": "بعلامتك وبفريقنا وبالأماكن التي نورّد منها."},
    "about.v3.h": {"en": "Innovation", "ar": "الابتكار"},
    "about.v3.p": {"en": "New materials, formats and ways of working.", "ar": "مواد وأشكال وطرق عمل جديدة."},
    "about.v4.h": {"en": "Pride", "ar": "الفخر"},
    "about.v4.p": {"en": "In work that carries your name.", "ar": "بعمل يحمل اسمك."},
    "about.lead.h": {"en": "Leadership", "ar": "القيادة"},
    "about.ceo": {"en": "Founder and CEO", "ar": "المؤسس والرئيس التنفيذي"},
    "about.more": {"en": "[Leadership team to add]", "ar": "[فريق القيادة يُضاف لاحقاً]"},
    "about.igc.h": {"en": "Part of IGC", "ar": "جزء من IGC"},
    "about.igc.p": {"en": "Through IGC, a network of 46+ promotional merchandise companies across MENA, APAC and Europe, we deliver for clients far beyond our three offices.",
                    "ar": "عبر IGC، شبكة تضم أكثر من 46 شركة منتجات ترويجية في الشرق الأوسط وآسيا والمحيط الهادئ وأوروبا، نخدم عملاءنا بعيداً عن مكاتبنا الثلاثة."},
    "about.offices.h": {"en": "Our offices", "ar": "مكاتبنا"},

    # ---------- brief ----------
    "brief.title": {"en": "Send a brief | Traffik360", "ar": "أرسل طلبك | Traffik360"},
    "brief.desc": {"en": "Tell us what you need: quantity, budget, date and markets. A specialist replies within one working day.",
                   "ar": "أخبرنا بما تحتاجه: الكمية والميزانية والموعد والأسواق. يرد عليك مختص خلال يوم عمل واحد."},
    "brief.k": {"en": "Project brief", "ar": "موجز المشروع"},
    "brief.h1": {"en": "Tell us what you need. We take it from here.", "ar": "أخبرنا بما تحتاجه، ونتولى الباقي."},
    "brief.lead": {"en": "Five short sections, about 5 minutes. The more you share, the faster and more accurate our first proposal.",
                   "ar": "خمسة أقسام قصيرة، حوالي 5 دقائق. كلما شاركت أكثر، كان عرضنا الأول أسرع وأدق."},
    "brief.next.h": {"en": "What happens next", "ar": "ماذا يحدث بعد ذلك"},
    "brief.n1": {"en": "A specialist for your market reads the brief and replies within one working day.",
                 "ar": "يقرأ مختص في سوقك الموجز ويرد خلال يوم عمل واحد."},
    "brief.n2": {"en": "We send product options, prices and lead times, or call you to clarify.",
                 "ar": "نرسل خيارات المنتجات والأسعار ومدد التنفيذ، أو نتصل بك للتوضيح."},
    "brief.n3": {"en": "Samples and artwork proofs before anything goes into production.",
                 "ar": "عينات وبروفات تصميم قبل أن يبدأ أي إنتاج."},
    "brief.stock.h": {"en": "Need stock items fast?", "ar": "تحتاج منتجات جاهزة بسرعة؟"},
    "brief.stock.p": {"en": "For catalogue products with your logo and smaller quantities, order on Glossary and see prices instantly.",
                      "ar": "لمنتجات الكتالوج مع شعارك وبكميات أصغر، اطلب عبر Glossary واطّلع على الأسعار فوراً."},
    "brief.stock.a": {"en": "Go to Glossary", "ar": "انتقل إلى Glossary"},
    "brief.slot": {"en": "[The Zoho brief form loads here once it is built.]", "ar": "[يظهر نموذج الموجز من Zoho هنا بعد إنشائه.]"},
    "brief.fallback": {"en": "Prefer email? Send your brief to", "ar": "تفضّل البريد الإلكتروني؟ أرسل موجزك إلى"},

    # ---------- privacy ----------
    "priv.title": {"en": "Privacy policy | Traffik360", "ar": "سياسة الخصوصية | Traffik360"},
    "priv.desc": {"en": "How Traffik360 collects and uses personal data.", "ar": "كيف تجمع Traffik360 البيانات الشخصية وتستخدمها."},
    "priv.h1": {"en": "Privacy policy", "ar": "سياسة الخصوصية"},
    "priv.body": {"en": "<p>[Full policy text pending legal review for UAE and KSA data protection law. It must cover the points below before the brief form goes live.]</p><h2>What we collect</h2><p>[Contact details and project information you send through the brief form or by email.]</p><h2>Why we use it</h2><p>[To answer your brief, prepare proposals and manage orders.]</p><h2>Where it is stored</h2><p>[Zoho CRM and Zoho Forms; hosting provider; retention period.]</p><h2>Your rights</h2><p>[Access, correction and deletion requests, and how to make them.]</p><h2>Contact</h2><p>[Data protection contact email.]</p>",
                  "ar": "<p>[نص السياسة الكامل قيد المراجعة القانونية وفق قوانين حماية البيانات في الإمارات والسعودية، ويجب أن يغطي النقاط التالية قبل تفعيل نموذج الموجز.]</p><h2>ما نجمعه</h2><p>[بيانات الاتصال ومعلومات المشروع التي ترسلها عبر نموذج الموجز أو البريد الإلكتروني.]</p><h2>سبب استخدامها</h2><p>[للرد على موجزك وإعداد العروض وإدارة الطلبات.]</p><h2>مكان حفظها</h2><p>[Zoho CRM وZoho Forms؛ مزود الاستضافة؛ مدة الاحتفاظ.]</p><h2>حقوقك</h2><p>[طلبات الاطلاع والتصحيح والحذف وطريقة تقديمها.]</p><h2>التواصل</h2><p>[بريد مسؤول حماية البيانات.]</p>"},

    # ---------- 404 ----------
    "nf.h": {"en": "This page has moved or no longer exists.", "ar": "تم نقل هذه الصفحة أو لم تعد موجودة."},
    "nf.home": {"en": "Go to the homepage", "ar": "انتقل إلى الصفحة الرئيسية"},
}

CLIENTS = ["L'ORÉAL", "Unilever", "Kenvue", "Saudi Tourism", "MDL Beast", "Konica Minolta", "Visa", "Henkel"]

e = html.escape


def builder(lang):
    ar = lang == "ar"

    def t(key):
        return STR[key][lang]

    def u(slug):
        p = "/ar/" if ar else "/"
        return p + (slug + "/" if slug else "")

    def other_url(slug):
        return ("/" if ar else "/ar/") + (slug + "/" if slug else "")

    def ph(label, cls=""):
        return f'<div class="ph {cls}" role="img" aria-label="{e(label)}"><span>{label}</span></div>'

    def header(slug):
        cur = lambda s: ' aria-current="page"' if s == slug else ""
        other_lang = "en" if ar else "ar"
        return f'''<a class="skip" href="#main">{t("skip")}</a>
<header class="site-header">
<div class="wrap">
<a class="logo" href="{u("")}" dir="ltr">Traffik360</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">{t("menu")}</button>
<nav id="site-nav" class="nav" aria-label="{t("nav.label")}">
<a href="{u("merchandise")}"{cur("merchandise")}>{t("nav.services")}</a>
<a href="{u("work")}"{cur("work")}>{t("nav.work")}</a>
<a href="{u("sectors")}"{cur("sectors")}>{t("nav.sectors")}</a>
<a href="{u("sustainability")}"{cur("sustainability")}>{t("nav.sustainability")}</a>
<a href="{u("about")}"{cur("about")}>{t("nav.about")}</a>
<a class="lang" href="{other_url(slug)}" lang="{other_lang}" hreflang="{other_lang}">{t("lang.other")}</a>
<a class="btn small" href="{u("brief")}">{t("nav.brief")}</a>
</nav>
</div>
</header>'''

    def footer(slug):
        return f'''<footer class="site-footer">
<div class="wrap">
<div class="row gap-lg">
<div class="foot-col wide">
<p class="logo" dir="ltr">Traffik360</p>
<p class="mt-s">{t("foot.tag")}</p>
<p class="mt-s"><a href="mailto:{EMAIL}" class="ltr">{EMAIL}</a><br><a href="#whatsapp">{t("foot.whatsapp")}</a></p>
</div>
<div class="foot-col"><h2>{t("foot.dubai")}</h2><p>{t("foot.dxb.addr")}<br><a class="ltr" href="tel:+97144534033">{PHONE_DXB}</a></p></div>
<div class="foot-col"><h2>{t("foot.riyadh")}</h2><p>{t("foot.addr.tbc")}</p></div>
<div class="foot-col"><h2>{t("foot.beirut")}</h2><p>{t("foot.addr.tbc")}</p></div>
</div>
<div class="foot-bottom">
<span dir="ltr">{t("foot.rights")}</span>
<nav aria-label="Footer"><a href="{u("privacy")}">{t("foot.privacy")}</a><a href="{LINKEDIN}" dir="ltr">LinkedIn</a><a href="{other_url(slug)}" lang="{"en" if ar else "ar"}">{t("lang.other")}</a></nav>
</div>
</div>
</footer>'''

    def doors():
        return f'''<section class="section bg-dark" aria-labelledby="doors-h">
<div class="wrap">
<h2 id="doors-h" class="h2">{t("doors.h")}</h2>
<div class="row mt-m">
<div class="door solid">
<p class="kicker" dir="ltr">Traffik360</p>
<h3 class="h3" style="font-size:30px">{t("doors.a.h")}</h3>
<p style="color:var(--ink-2)">{t("doors.a.p")}</p>
<a class="btn" href="{u("brief")}">{t("cta.brief")}</a>
</div>
<div class="door outline">
<p class="kicker muted" dir="ltr">Glossary</p>
<h3 class="h3" style="font-size:30px">{t("doors.b.h")}</h3>
<p>{t("doors.b.p")}</p>
<a class="btn ghost" href="{GLOSSARY}">{t("cta.glossary")}</a>
</div>
</div>
</div>
</section>'''

    def page_hero(kicker, h1, lead, cta=True):
        btn = f'<div class="btns"><a class="btn" href="{u("brief")}">{t("cta.brief")}</a></div>' if cta else ""
        return f'''<section class="bg-dark page-hero">
<div class="wrap">
<p class="eyebrow">{kicker}</p>
<h1 class="h1 page measure">{h1}</h1>
<p class="lead">{lead}</p>
{btn}
</div>
</section>'''

    def case(key, services):
        return f'''<article class="case" data-service="{services}">
{ph(t("case." + key + ".ph"), "mid")}
<p class="meta">{t("case." + key + ".meta")}</p>
<h3 class="h3">{t("case." + key + ".h")}</h3>
<p class="sum">{t("case.sum")}</p>
</article>'''

    def tile(h, p=""):
        body = f"<p>{p}</p>" if p else ""
        return f'<div class="tile"><h3>{h}</h3>{body}</div>'

    def svc_card(k, slug):
        return f'''<article class="card">
{ph(t("svc." + k + ".ph"))}
<div class="card-body">
<h3 class="h3">{t("svc." + k + ".h")}</h3>
<p>{t("svc." + k + ".p")}</p>
<p class="tags">{t("svc." + k + ".tags")}</p>
<a class="link" href="{u(slug)}">{t("svc." + k + ".h")}</a>
</div>
</article>'''

    def steps():
        items = "".join(
            f'<li><div class="n">0{i}</div><h3>{t(f"how.{i}.h")}</h3><p>{t(f"how.{i}.p")}</p></li>'
            for i in range(1, 6))
        return f'''<section class="section bg-white" aria-labelledby="how-h">
<div class="wrap">
<p class="kicker">{t("how.k")}</p>
<h2 id="how-h" class="h2 measure">{t("how.h")}</h2>
<ol class="steps">{items}</ol>
</div>
</section>'''

    def badges():
        return "".join(tile(t(f"badge.{k}.h"), t(f"badge.{k}.p")) for k in ["eco", "iso", "igc", "audit"])

    # ---------- page bodies ----------
    def home():
        clients = "".join(f'<li dir="ltr">{e(c)}</li>' for c in CLIENTS)
        return f'''<section class="bg-dark hero">
<div class="wrap">
<div class="col">
<p class="eyebrow">{t("home.eyebrow")}</p>
<h1 class="h1">{t("home.h1")}</h1>
<p class="lead">{t("home.lead")}</p>
<div class="btns"><a class="btn" href="{u("brief")}">{t("cta.brief")}</a><a class="btn ghost" href="{u("work")}">{t("cta.work")}</a></div>
</div>
<div class="col">{ph(t("home.hero.ph"), "dark tall")}</div>
</div>
</section>
<section class="clients" aria-label="{t("home.clients")}">
<div class="wrap"><p class="small" style="margin:0">{t("home.clients")}</p><ul class="clients-list">{clients}</ul></div>
</section>
<section class="section tight" aria-label="{t("home.stats.label")}">
<div class="wrap row">
<div class="stat"><b>3</b><p>{t("home.stat1")}</p></div>
<div class="stat"><b class="ltr">600+</b><p>{t("home.stat2")}</p></div>
<div class="stat"><b class="ltr">46+</b><p>{t("home.stat3")}</p></div>
<div class="stat accent"><b>{t("home.stat4.b")}</b><p>{t("home.stat4")}</p></div>
</div>
</section>
<section class="section bg-white" aria-labelledby="svc-h">
<div class="wrap">
<p class="kicker">{t("nav.services")}</p>
<h2 id="svc-h" class="h2 measure">{t("home.services.h")}</h2>
<div class="row mt-l">{svc_card("merch", "merchandise")}{svc_card("posm", "posm-displays")}{svc_card("act", "activations")}</div>
</div>
</section>
<section class="section" aria-labelledby="work-h">
<div class="wrap">
<div class="row center" style="justify-content:space-between">
<div><p class="kicker">{t("home.work.k")}</p><h2 id="work-h" class="h2">{t("home.work.h")}</h2></div>
<a class="link" href="{u("work")}">{t("home.work.all")}</a>
</div>
<div class="row mt-l">{case("kenvue", "merch")}{case("henkel", "merch")}{case("mdl", "merch act")}</div>
</div>
</section>
{steps()}
<section class="section" aria-labelledby="sus-h">
<div class="wrap row gap-lg center">
<div class="col" style="flex-basis:480px">
<p class="kicker">{t("sus.k")}</p>
<h2 id="sus-h" class="h2">{t("sus.h")}</h2>
<p class="lead">{t("sus.p")}</p>
<p class="mt-m"><a class="link" href="{u("sustainability")}">{t("sus.link")}</a></p>
</div>
<div class="col row" style="gap:16px;flex-basis:420px">{badges()}</div>
</div>
</section>
{doors()}'''

    def merchandise():
        cats = "".join(tile(t(f"merch.c{i}")) for i in range(1, 9))
        seasons = "".join(f"<li>{t(f'merch.s{i}')}</li>" for i in range(1, 7))
        return f'''{page_hero(t("nav.services"), t("svc.merch.h"), t("merch.lead"))}
<section class="section" aria-labelledby="make-h">
<div class="wrap"><h2 id="make-h" class="h2">{t("merch.make.h")}</h2><div class="row mt-m" style="gap:16px">{cats}</div></div>
</section>
<section class="section bg-white" aria-labelledby="split-h">
<div class="wrap">
<h2 id="split-h" class="h2">{t("merch.split.h")}</h2>
<div class="row mt-m">
<div class="tile" style="padding:32px"><h3>{t("merch.bespoke.h")}</h3><p>{t("merch.bespoke.p")}</p><p class="mt-s"><a class="btn small" href="{u("brief")}">{t("cta.brief")}</a></p></div>
<div class="tile" style="padding:32px"><h3>{t("merch.stock.h")}</h3><p>{t("merch.stock.p")}</p><p class="mt-s"><a class="btn small ghost light" href="{GLOSSARY}">{t("cta.glossary")}</a></p></div>
</div>
</div>
</section>
<section class="section" aria-labelledby="season-h">
<div class="wrap row gap-lg">
<div class="col"><h2 id="season-h" class="h2">{t("merch.season.h")}</h2><p class="lead">{t("merch.season.p")}</p></div>
<div class="col"><ul class="ticks">{seasons}</ul></div>
</div>
</section>
<section class="section bg-white" aria-labelledby="mwork-h">
<div class="wrap"><h2 id="mwork-h" class="h2">{t("home.work.k")}</h2><div class="row mt-l">{case("kenvue", "merch")}{case("henkel", "merch")}</div></div>
</section>
{doors()}'''

    def posm():
        cats = "".join(tile(t(f"posm.c{i}")) for i in range(1, 7))
        items = "".join(f'<li><div class="n">0{i}</div><h3>{t(f"posm.p{i}.h")}</h3><p>{t(f"posm.p{i}.p")}</p></li>' for i in range(1, 5))
        return f'''{page_hero(t("nav.services"), t("svc.posm.h"), t("posm.lead"))}
<section class="section" aria-labelledby="pwhat-h">
<div class="wrap"><h2 id="pwhat-h" class="h2">{t("posm.what.h")}</h2><div class="row mt-m" style="gap:16px">{cats}</div></div>
</section>
<section class="section bg-white" aria-labelledby="pproc-h">
<div class="wrap"><h2 id="pproc-h" class="h2">{t("posm.proc.h")}</h2><ol class="steps">{items}</ol></div>
</section>
<section class="section" aria-labelledby="pwork-h">
<div class="wrap"><h2 id="pwork-h" class="h2">{t("home.work.k")}</h2><div class="row mt-l">{case("tbc", "posm")}{case("tbc", "posm")}</div></div>
</section>
{doors()}'''

    def activations():
        cards = "".join(tile(t(f"act.c{i}.h"), t(f"act.c{i}.p")) for i in range(1, 5))
        return f'''{page_hero(t("nav.services"), t("svc.act.h"), t("act.lead"))}
<section class="section" aria-labelledby="awhat-h">
<div class="wrap"><h2 id="awhat-h" class="h2">{t("act.what.h")}</h2><div class="row mt-m" style="gap:16px">{cards}</div><p class="small mt-m">{t("act.partner")}</p></div>
</section>
<section class="section bg-white" aria-labelledby="awork-h">
<div class="wrap"><h2 id="awork-h" class="h2">{t("home.work.k")}</h2><div class="row mt-l">{case("mdl", "merch act")}{case("tbc", "act")}</div></div>
</section>
{doors()}'''

    def work():
        chips = "".join(
            f'<button class="chip" type="button" data-filter="{f}" aria-pressed="{"true" if f == "all" else "false"}">{t("work.f." + f)}</button>'
            for f in ["all", "merch", "posm", "act"])
        return f'''{page_hero(t("nav.work"), t("work.h1"), t("work.lead"), cta=False)}
<section class="section">
<div class="wrap">
<div class="chips" role="group" aria-label="{t("work.filter")}">{chips}</div>
<div class="row mt-l" style="row-gap:56px">{case("kenvue", "merch")}{case("henkel", "merch")}{case("mdl", "merch act")}{case("tbc", "posm")}{case("tbc", "posm")}{case("tbc", "act")}</div>
</div>
</section>
{doors()}'''

    def sectors():
        cards = "".join(tile(t(f"sec.{i}.h"), t(f"sec.{i}.p")) for i in range(1, 7))
        return f'''{page_hero(t("nav.sectors"), t("sec.h1"), t("sec.lead"))}
<section class="section"><div class="wrap"><div class="row" style="gap:16px">{cards}</div></div></section>
{doors()}'''

    def sustainability():
        pillars = "".join(tile(t(f"susp.p{i}.h"), t(f"susp.p{i}.p")) for i in range(1, 4))
        return f'''{page_hero(t("sus.k"), t("susp.h1"), t("sus.p"), cta=False)}
<section class="section"><div class="wrap"><div class="row" style="gap:16px">{badges()}</div></div></section>
<section class="section bg-white" aria-labelledby="pil-h">
<div class="wrap"><h2 id="pil-h" class="h2">{t("susp.pillars.h")}</h2><div class="row mt-m" style="gap:16px">{pillars}</div></div>
</section>
<section class="section" aria-labelledby="docs-h">
<div class="wrap measure"><h2 id="docs-h" class="h2">{t("susp.docs.h")}</h2><p class="lead">{t("susp.docs.p")}</p><div class="btns"><a class="btn" href="{u("brief")}">{t("cta.brief")}</a></div></div>
</section>'''

    def about():
        values = "".join(tile(t(f"about.v{i}.h"), t(f"about.v{i}.p")) for i in range(1, 5))
        offices = (tile(t("foot.dubai"), t("foot.dxb.addr").replace("<br>", ", ")) +
                   tile(t("foot.riyadh"), t("foot.addr.tbc").replace("<br>", ", ")) +
                   tile(t("foot.beirut"), t("foot.addr.tbc").replace("<br>", ", ")))
        return f'''{page_hero(t("nav.about"), t("about.h1"), t("about.lead"), cta=False)}
<section class="section" aria-labelledby="val-h">
<div class="wrap"><h2 id="val-h" class="h2">{t("about.values.h")}</h2><div class="row mt-m" style="gap:16px">{values}</div></div>
</section>
<section class="section bg-white" aria-labelledby="ldr-h">
<div class="wrap"><h2 id="ldr-h" class="h2">{t("about.lead.h")}</h2>
<div class="row mt-m" style="gap:16px">{tile("Marcel Khairallah", t("about.ceo"))}{tile(t("about.more"))}</div></div>
</section>
<section class="section" aria-labelledby="igc-h">
<div class="wrap row gap-lg">
<div class="col"><h2 id="igc-h" class="h2">{t("about.igc.h")}</h2><p class="lead">{t("about.igc.p")}</p></div>
<div class="col"><h2 class="h3">{t("about.offices.h")}</h2><div class="row mt-s" style="gap:16px">{offices}</div></div>
</div>
</section>
{doors()}'''

    def brief():
        steps_html = "".join(f'<li><span class="dot">{i}</span><span>{t(f"brief.n{i}")}</span></li>' for i in range(1, 4))
        return f'''<section class="section">
<div class="wrap row gap-lg" style="align-items:flex-start">
<aside class="col">
<p class="kicker">{t("brief.k")}</p>
<h1 class="h1 page">{t("brief.h1")}</h1>
<p class="lead">{t("brief.lead")}</p>
<h2 class="h3 mt-l" style="font-size:20px">{t("brief.next.h")}</h2>
<ol class="numbered mt-s">{steps_html}</ol>
<div class="aside-box">
<h2 class="h3" style="font-size:18px">{t("brief.stock.h")}</h2>
<p class="small" style="color:var(--ink-2)">{t("brief.stock.p")}</p>
<a class="link" href="{GLOSSARY}">{t("brief.stock.a")}</a>
</div>
</aside>
<div class="col-2">
<div id="brief-form" class="embed-slot">
<!-- ZOHO_FORM_EMBED: replace this block with the Zoho Forms iframe embed code -->
<p style="margin:0;font-weight:600">{t("brief.slot")}</p>
<p class="small" style="margin:0">{t("brief.fallback")} <a href="mailto:{EMAIL}" class="ltr">{EMAIL}</a></p>
</div>
</div>
</div>
</section>'''

    def privacy():
        return f'''<section class="section"><div class="wrap prose"><h1 class="h1 page">{t("priv.h1")}</h1>{t("priv.body")}</div></section>'''

    bodies = {"": home, "merchandise": merchandise, "posm-displays": posm, "activations": activations,
              "work": work, "sectors": sectors, "sustainability": sustainability, "about": about,
              "brief": brief, "privacy": privacy}
    meta = {"": "home", "merchandise": "merch", "posm-displays": "posm", "activations": "act", "work": "work",
            "sectors": "sec", "sustainability": "susp", "about": "about", "brief": "brief", "privacy": "priv"}

    def page(slug):
        m = meta[slug]
        title, desc = t(m + ".title"), t(m + ".desc")
        en_url = DOMAIN + "/" + (slug + "/" if slug else "")
        ar_url = DOMAIN + "/ar/" + (slug + "/" if slug else "")
        canon = ar_url if ar else en_url
        ld = ""
        if slug == "":
            org = {"@context": "https://schema.org", "@type": "Organization", "name": "Traffik360",
                   "url": DOMAIN, "telephone": PHONE_DXB, "sameAs": [LINKEDIN],
                   "address": {"@type": "PostalAddress", "streetAddress": "Thuraya Tower, Office 805, Barsha Heights",
                               "addressLocality": "Dubai", "addressCountry": "AE"}}
            ld = f'<script type="application/ld+json">{json.dumps(org)}</script>'
        robots = '<meta name="robots" content="noindex">' if slug == "privacy" else ""
        return f'''<!doctype html>
<html lang="{lang}" dir="{"rtl" if ar else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{"ar_AE" if ar else "en_AE"}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{ld}
</head>
<body>
{header(slug)}
<main id="main">
{bodies[slug]()}
</main>
{footer(slug)}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

    return page, t, u


def not_found():
    _, ten, _ = builder("en")
    _, tar, _ = builder("ar")
    return f'''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Traffik360</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@800&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Sans+Arabic:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css"></head>
<body>
<main class="section bg-dark" style="min-height:100vh"><div class="wrap">
<p class="logo">Traffik360</p>
<h1 class="h1 page mt-l">{ten("nf.h")}</h1>
<p class="btns"><a class="btn" href="/">{ten("nf.home")}</a></p>
<div lang="ar" dir="rtl" class="mt-l"><h2 class="h2">{tar("nf.h")}</h2><p class="btns"><a class="btn ghost" href="/ar/">{tar("nf.home")}</a></p></div>
</div></main>
</body></html>
'''


def main():
    for lang in ["en", "ar"]:
        page, _, _ = builder(lang)
        for slug in PAGES:
            d = OUT / ("ar" if lang == "ar" else "") / slug
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(page(slug), encoding="utf-8")
    (OUT / "404.html").write_text(not_found(), encoding="utf-8")
    urls = []
    for slug in PAGES:
        if slug == "privacy":
            continue
        for pre in ["/", "/ar/"]:
            urls.append(f"  <url><loc>{DOMAIN}{pre}{slug + '/' if slug else ''}</loc></url>")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    print(f"Built {len(PAGES) * 2} pages, 404 and sitemap into {OUT}")


if __name__ == "__main__":
    main()
