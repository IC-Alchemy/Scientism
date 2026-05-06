from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
LOOKUPS_JSON = WIKI / "synthesis" / "gutknecht-letter-questions-7-9-api-lookups.json"
Q_PAGE = WIKI / "synthesis" / "gutknecht-letter-questions-7-9.md"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def link(slug: str, label: str) -> str:
    return f"[[sources/{slug}|{label}]]"


def yaml_quote(text: str) -> str:
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


STUDIES = [
    {
        "key": "larsson-1985-hemophilia-life-expectancy",
        "slug": "larsson-1985-life-expectancy-of-swedish-haemophiliacs",
        "q": "Q7",
        "label": "Larsson 1985",
        "title": "Life expectancy of Swedish haemophiliacs, 1831-1980",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "historical survival analysis",
        "study_type": "Historical survival analysis",
        "subjects": "948 Swedish hemophiliacs, with survival estimated across 1831-1980",
        "exposure": "Modern hemophilia care and replacement therapy era",
        "comparator": "Earlier birth or calendar periods and Swedish male population rates",
        "endpoint": "Median life expectancy",
        "result": "Severe hemophilia median life expectancy rose from 11 years in 1831-1920 to 56.8 years in 1961-1980; moderate hemophilia rose from 27.5 to 71.5 years.",
        "limitation": "Swedish historical data ending before the HIV-era mortality peak; does not test HIV causation.",
        "can_answer": "Documents pre-HIV survival improvement in hemophilia under changing treatment conditions.",
        "cannot_answer": "Does not answer whether HIV, hepatitis, treatment toxicity, or other factors caused later AIDS-era deaths.",
        "full_text": "Abstract is enough for the broad life-expectancy row; full text is needed for method-level audit of demographic calculations.",
        "tags": "[aids, hiv, hemophilia, survival]",
    },
    {
        "key": "johnson-1985-hemophilia-treatment-centers",
        "slug": "johnson-1985-aids-among-hemophilia-treatment-center-patients",
        "q": "Q7",
        "label": "Johnson 1985",
        "title": "Acquired immunodeficiency syndrome among patients attending hemophilia treatment centers and mortality experience of hemophiliacs in the United States",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "U.S. hemophilia treatment-center survey and mortality analysis",
        "study_type": "Treatment-center survey plus mortality trend analysis",
        "subjects": "U.S. hemophilia treatment-center attendees monitored for AIDS cases through June 1984",
        "exposure": "Hemophilia care with clotting-factor concentrates and early AIDS-era exposure",
        "comparator": "Hemophilia mortality trends before and after clotting-factor concentrate use",
        "endpoint": "AIDS incidence and hemophilia mortality trends",
        "result": "Improved care reduced hemophilia mortality during the 1970s, while AIDS became a new cause of illness and mortality by 1982-1984.",
        "limitation": "Does not reach 1987 and the abstract does not verify the letter's exact 11-to-27 life-expectancy statistic.",
        "can_answer": "Anchors early U.S. hemophilia AIDS surveillance and pre-AIDS mortality improvement.",
        "cannot_answer": "Does not support the exact life-expectancy statistic in the Gutknecht letter without full-text confirmation.",
        "full_text": "Full text needed for the median-age or life-expectancy statistic audit.",
        "tags": "[aids, hiv, hemophilia, mortality]",
    },
    {
        "key": "chorba-1994-hemophilia-a-longevity-causes",
        "slug": "chorba-1994-longevity-and-causes-of-death-in-hemophilia-a",
        "q": "Q7",
        "label": "Chorba 1994",
        "title": "Changes in longevity and causes of death among persons with hemophilia A",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "U.S. death-certificate mortality analysis",
        "study_type": "Multiple-cause death-certificate analysis",
        "subjects": "2,792 U.S. deaths with hemophilia A or congenital Factor VIII disorder listed, 1968-1989",
        "exposure": "HIV-era deaths among persons with hemophilia A",
        "comparator": "Pre-HIV-era death periods and deaths without HIV-related disease listed",
        "endpoint": "Death rate, cause of death, and median age at death",
        "result": "Median age at death decreased from 57 years in 1979-1981 to 40 years in 1987-1989 as HIV-related deaths increased.",
        "limitation": "Death-certificate analysis of decedents, not a controlled cohort with direct exposure assignment.",
        "can_answer": "Shows a U.S. HIV-era mortality signal among people with hemophilia A.",
        "cannot_answer": "Does not by itself isolate HIV from all treatment, hepatitis, or ascertainment cofactors.",
        "full_text": "Abstract is enough for the main median-age row; full text needed for detailed cause categories.",
        "tags": "[aids, hiv, hemophilia, mortality]",
    },
    {
        "key": "chorba-2001-hiv-age-cause-death-hemophilia-a",
        "slug": "chorba-2001-hiv-effects-on-age-and-cause-of-death-in-hemophilia-a",
        "q": "Q7",
        "label": "Chorba 2001",
        "title": "Effects of HIV infection on age and cause of death for persons with hemophilia A in the United States",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "extended U.S. death-record analysis",
        "study_type": "Multiple-cause death-record trend analysis",
        "subjects": "4,781 U.S. hemophilia A deaths, 1979-1998",
        "exposure": "HIV-related disease listed on death records",
        "comparator": "Hemophilia A deaths without HIV-related disease listed",
        "endpoint": "Median age at death and cause-of-death patterns",
        "result": "Median age at death decreased from 55 years in 1979-1982 to 40.5 years in 1987-1990, then rose later as HIV-related mortality declined.",
        "limitation": "Decedent-only death-record design; later publication cannot answer what was knowable in March 1995.",
        "can_answer": "Gives the cleanest long-run U.S. mortality trend around the HIV era.",
        "cannot_answer": "Does not replace pre-1995 evidence for historical knowledge at the time of the letter.",
        "full_text": "Abstract is enough for the broad time trend; full text needed for detailed age strata.",
        "tags": "[aids, hiv, hemophilia, mortality]",
    },
    {
        "key": "darby-1995-mortality-before-after-hiv-hemophilia",
        "slug": "darby-1995-mortality-before-and-after-hiv-infection-in-uk-haemophiliacs",
        "q": "Q7/Q8",
        "label": "Darby 1995",
        "title": "Mortality before and after HIV infection in the complete UK population of haemophiliacs",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "complete-population hemophilia mortality cohort",
        "study_type": "Complete national cohort mortality analysis",
        "subjects": "6,278 UK males with hemophilia, including 1,227 with HIV infection",
        "exposure": "HIV infection among hemophiliacs",
        "comparator": "HIV-seronegative hemophiliacs in the same national population",
        "endpoint": "Annual death rate and excess mortality",
        "result": "Mortality stayed near baseline among HIV-seronegative hemophiliacs but rose sharply after HIV infection.",
        "limitation": "Observational national cohort and published after the March 1995 letter.",
        "can_answer": "Directly compares mortality before and after HIV infection in a hemophilia population.",
        "cannot_answer": "Does not randomize HIV exposure or fully separate every cofactor.",
        "full_text": "Abstract is enough for the main mortality contrast; full text needed for exact annual rates.",
        "tags": "[aids, hiv, hemophilia, mortality]",
    },
    {
        "key": "triemstra-1995-hemophilia-mortality-dutch",
        "slug": "triemstra-1995-mortality-in-patients-with-hemophilia",
        "q": "Q7",
        "label": "Triemstra 1995",
        "title": "Mortality in patients with hemophilia. Changes in a Dutch population from 1986 to 1992 and 1973 to 1986",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "Dutch hemophilia cohort mortality analysis",
        "study_type": "Cohort mortality analysis",
        "subjects": "919 Dutch males with hemophilia followed from 1986 to June 1992 and compared with 1973-1986",
        "exposure": "HIV infection and viral-related deaths",
        "comparator": "Earlier hemophilia period and general male mortality",
        "endpoint": "Death, standardized mortality ratio, and median life expectancy",
        "result": "HIV infection was the strongest independent predictor of death in the model; viral deaths drove excess mortality.",
        "limitation": "Observational cohort and not a randomized exposure.",
        "can_answer": "Separates pre-HIV survival gains from HIV-era mortality in a national hemophilia cohort.",
        "cannot_answer": "Does not alone resolve the exact U.S. statistic in the letter.",
        "full_text": "Abstract is adequate for the model direction; full text needed for all model coefficients.",
        "tags": "[aids, hiv, hemophilia, mortality]",
    },
    {
        "key": "kroner-1994-hiv-incidence-hemophilia",
        "slug": "kroner-1994-hiv-1-incidence-among-persons-with-hemophilia",
        "q": "Q7/Q8",
        "label": "Kroner 1994",
        "title": "HIV-1 infection incidence among persons with hemophilia in the United States and western Europe, 1978-1990",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "multicenter hemophilia HIV-incidence reconstruction",
        "study_type": "Multicenter cohort incidence reconstruction",
        "subjects": "Persons with hemophilia at 16 U.S. and western European centers",
        "exposure": "Blood-product exposure era and clotting-factor safety interventions",
        "comparator": "Calendar periods before and after blood-safety interventions",
        "endpoint": "Estimated HIV-1 infection incidence",
        "result": "Incidence began in 1978, peaked around October 1982, and declined by July 1984, with few infections after 1987.",
        "limitation": "Incidence study, not a direct mortality or AIDS-progression study.",
        "can_answer": "Dates blood-product HIV infection patterns among hemophiliacs.",
        "cannot_answer": "Does not answer all AIDS-causation or survival questions by itself.",
        "full_text": "Abstract is enough for the incidence timing row; full text needed for center-specific reconstruction.",
        "tags": "[aids, hiv, hemophilia, blood-products]",
    },
    {
        "key": "goedert-1989-hiv-aids-hemophilia",
        "slug": "goedert-1989-hiv-1-infection-and-aids-in-hemophilia",
        "q": "Q7",
        "label": "Goedert 1989",
        "title": "A prospective study of human immunodeficiency virus type 1 infection and the development of AIDS in subjects with hemophilia",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "prospective hemophilia HIV natural-history cohort",
        "study_type": "Prospective multicenter cohort",
        "subjects": "1,219 subjects with hemophilia or related disorders, including 319 with documented seroconversion dates",
        "exposure": "HIV-1 seroconversion timing and age",
        "comparator": "Time since seroconversion and age strata",
        "endpoint": "AIDS incidence after seroconversion",
        "result": "AIDS risk increased with time after seroconversion and with older age at seroconversion.",
        "limitation": "AIDS-progression endpoint, not overall hemophilia life expectancy.",
        "can_answer": "Documents progression after HIV infection in hemophilia subjects.",
        "cannot_answer": "Does not adjudicate total mortality causes in hemophilia.",
        "full_text": "Abstract is adequate for direction; full text needed for exact cumulative risks.",
        "tags": "[aids, hiv, hemophilia, cohort]",
    },
    {
        "key": "smit-1989-dutch-hemophiliacs-1972-85",
        "slug": "smit-1989-physical-condition-longevity-and-social-performance-of-dutch-haemophiliacs",
        "q": "Q7",
        "label": "Smit 1989",
        "title": "Physical condition, longevity, and social performance of Dutch haemophiliacs, 1972-85",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "repeated Dutch hemophilia survey and longevity analysis",
        "study_type": "Repeated national questionnaire and cohort assessment",
        "subjects": "Dutch hemophiliacs surveyed from 1972 to 1985",
        "exposure": "Modern substitution, home treatment, and prophylactic treatment over time",
        "comparator": "Earlier survey periods and Dutch male population",
        "endpoint": "Mortality, calculated life expectancy, hospital use, and social performance",
        "result": "Modern treatment improved function and reduced hospital use; life expectancy remained below that of the general male population.",
        "limitation": "Mostly pre-HIV-era outcome framing and not U.S. data.",
        "can_answer": "Documents pre-HIV hemophilia health and longevity improvements.",
        "cannot_answer": "Does not directly test HIV-era mortality.",
        "full_text": "Abstract gives enough for broad placement; full text needed for exact life-expectancy calculations.",
        "tags": "[aids, hiv, hemophilia, survival]",
    },
    {
        "key": "donegan-1990-transfusion-risk-aids",
        "slug": "donegan-1990-risk-of-aids-after-transfusion-of-hiv-positive-blood",
        "q": "Q8",
        "label": "Donegan 1990",
        "title": "Infection with human immunodeficiency virus type 1 after transfusion of blood from seropositive donors",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "transfusion-recipient cohort",
        "study_type": "Transfusion-recipient cohort",
        "subjects": "Recipients of HIV-antibody-positive blood donations",
        "exposure": "Transfusion of blood from HIV-seropositive donors",
        "comparator": "Time after transfusion and study comparison assumptions",
        "endpoint": "AIDS within follow-up",
        "result": "The abstract-level record supports progression to AIDS after HIV-positive transfusion exposure in a subset of recipients.",
        "limitation": "Does not test all alternative cofactors and full text is needed for exact risk table details.",
        "can_answer": "Shows a non-recreational exposure route followed by AIDS outcomes.",
        "cannot_answer": "Does not alone settle broader AIDS causation.",
        "full_text": "Full text needed for exact cumulative AIDS risk and comparator details.",
        "tags": "[aids, hiv, transfusion, cohort]",
    },
    {
        "key": "ward-1989-transfusion-associated-hiv-natural-history",
        "slug": "ward-1989-natural-history-of-transfusion-associated-hiv-infection",
        "q": "Q8",
        "label": "Ward 1989",
        "title": "The natural history of transfusion-associated infection with human immunodeficiency virus. Factors influencing the rate of progression to disease",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "transfusion-associated HIV natural-history study",
        "study_type": "Natural-history cohort study",
        "subjects": "Transfusion recipients infected through blood from donors later associated with AIDS",
        "exposure": "Transfusion-associated HIV infection",
        "comparator": "Other transfusion recipients and progression strata in the study",
        "endpoint": "Progression to AIDS",
        "result": "Transfusion-associated infection was followed by progression to AIDS, with progression rate varying by factors such as recipient age.",
        "limitation": "Observational transfusion cohort and not a randomized exposure.",
        "can_answer": "Places AIDS progression in a non-recreational exposure cohort.",
        "cannot_answer": "Does not rule out every cofactor in every AIDS case.",
        "full_text": "Abstract is adequate for broad row; full text needed for detailed risk factors.",
        "tags": "[aids, hiv, transfusion, cohort]",
    },
    {
        "key": "giesecke-1988-swedish-hemophiliacs-transfusion-recipients",
        "slug": "giesecke-1988-symptoms-and-aids-in-swedish-haemophiliacs-and-transfusion-recipients",
        "q": "Q8",
        "label": "Giesecke 1988",
        "title": "Incidence of symptoms and AIDS in 146 Swedish haemophiliacs and blood transfusion recipients infected with human immunodeficiency virus",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "Swedish non-recreational exposure cohort",
        "study_type": "Prospective cohort",
        "subjects": "98 hemophiliacs and 48 transfusion recipients infected with HIV",
        "exposure": "Infected blood products or blood transfusion",
        "comparator": "Hemophilia route versus transfusion route",
        "endpoint": "First clinical symptom and AIDS",
        "result": "Transfusion recipients progressed faster than hemophiliacs in this early cohort.",
        "limitation": "Modest sample size and early-era clinical definitions.",
        "can_answer": "Directly compares two non-recreational exposure routes.",
        "cannot_answer": "Does not provide a recreational-drug comparison group.",
        "full_text": "Abstract is adequate for inclusion; full text needed for exact incidence curves.",
        "tags": "[aids, hiv, hemophilia, transfusion]",
    },
    {
        "key": "darby-1989-aids-excess-mortality-hemophiliacs",
        "slug": "darby-1989-aids-and-excess-mortality-in-uk-haemophiliacs",
        "q": "Q8",
        "label": "Darby 1989",
        "title": "Incidence of AIDS and excess mortality associated with HIV in haemophiliacs in the United Kingdom",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "UK hemophilia AIDS and mortality registry analysis",
        "study_type": "National survey and registry analysis",
        "subjects": "1,201 HIV-positive men with hemophilia in the United Kingdom",
        "exposure": "HIV infection through contaminated factor therapy",
        "comparator": "Time since estimated infection and age strata",
        "endpoint": "AIDS diagnosis and excess mortality",
        "result": "AIDS incidence and excess mortality rose with time and age in HIV-positive hemophiliacs.",
        "limitation": "Seroconversion dates were estimated from available evidence.",
        "can_answer": "Builds a blood-product progression boundary independent of recreational-drug exposure.",
        "cannot_answer": "Does not randomize infection or fully resolve cofactor disputes.",
        "full_text": "Abstract is adequate for direction; full text needed for age-specific estimates.",
        "tags": "[aids, hiv, hemophilia, blood-products]",
    },
    {
        "key": "simmonds-1991-edinburgh-hemophilia-hiv-cohort",
        "slug": "simmonds-1991-determinants-of-hiv-disease-progression-in-edinburgh-haemophilia-cohort",
        "q": "Q8",
        "label": "Simmonds 1991",
        "title": "Determinants of HIV disease progression: six-year longitudinal study in the Edinburgh haemophilia/HIV cohort",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "Edinburgh hemophilia HIV longitudinal cohort",
        "study_type": "Longitudinal cohort",
        "subjects": "18 hemophiliacs infected from a contaminated factor VIII exposure event",
        "exposure": "Known contaminated factor VIII exposure",
        "comparator": "Progression markers and time since exposure within the cohort",
        "endpoint": "AIDS symptoms or signs over follow-up",
        "result": "Progression was observed within five years and associated with immune activation markers.",
        "limitation": "Very small cohort.",
        "can_answer": "Provides unusually clear exposure timing for a blood-product cohort.",
        "cannot_answer": "Too small to carry the broad Q8 question alone.",
        "full_text": "Abstract is adequate for screening; full text needed for marker definitions.",
        "tags": "[aids, hiv, hemophilia, cohort]",
    },
    {
        "key": "schinaia-1994-italian-hiv-positive-hemophiliacs",
        "slug": "schinaia-1994-progression-to-aids-in-italian-hiv-positive-hemophiliacs",
        "q": "Q8",
        "label": "Schinaia 1994",
        "title": "Clinical factors associated with progression to AIDS in the Italian cohort of HIV-positive hemophiliacs",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "Italian national hemophilia cohort",
        "study_type": "National hemophilia registry cohort analysis",
        "subjects": "767 HIV-1-positive congenital coagulation-disorder patients",
        "exposure": "HIV infection associated with replacement therapy",
        "comparator": "Age, disorder, and clinical factor strata",
        "endpoint": "Cumulative AIDS incidence",
        "result": "Eight-year AIDS incidence was estimated at 17 percent, with higher progression in older seroconverters and some factor-treatment strata.",
        "limitation": "Seroconversion dates modeled rather than directly observed for all subjects.",
        "can_answer": "Adds a large blood-product cohort to the non-recreational exposure reconstruction.",
        "cannot_answer": "Does not isolate every treatment cofactor.",
        "full_text": "Abstract is adequate for row-level inclusion; full text needed for all covariate estimates.",
        "tags": "[aids, hiv, hemophilia, cohort]",
    },
    {
        "key": "roosendaal-1998-clotting-product-consumption-aids",
        "slug": "roosendaal-1998-progression-to-aids-and-clotting-product-consumption",
        "q": "Q8",
        "label": "Roosendaal 1998",
        "title": "Progression to AIDS in relation to clinical factors and clotting product consumption",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "Dutch hemophilia progression cohort",
        "study_type": "Longitudinal cohort",
        "subjects": "52 HIV-1-infected hemophiliacs followed for 14 to 15 years",
        "exposure": "Clotting-factor product consumption and clinical hemophilia factors",
        "comparator": "Product-consumption and clinical strata",
        "endpoint": "Progression to AIDS",
        "result": "Progression varied by clinical factors and was not explained by total clotting-factor amount alone in the abstract-level record.",
        "limitation": "Small sample and post-1995 publication.",
        "can_answer": "Helps separate HIV exposure route from clotting-product amount as a proposed cofactor.",
        "cannot_answer": "Does not answer what was available to the 1995 letter author.",
        "full_text": "Full text needed for exact factor-consumption model.",
        "tags": "[aids, hiv, hemophilia, blood-products]",
    },
    {
        "key": "european-collaborative-1991-children-born-hiv",
        "slug": "european-collaborative-study-1991-children-born-to-women-with-hiv-1-infection",
        "q": "Q8",
        "label": "European Collaborative Study 1991",
        "title": "Children born to women with HIV-1 infection: natural history and risk of transmission",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "prospective perinatal HIV cohort",
        "study_type": "Prospective pediatric follow-up cohort",
        "subjects": "600 children born to women with HIV-1 infection",
        "exposure": "Maternal HIV-1 infection and vertical transmission",
        "comparator": "Infected versus uninfected exposed children",
        "endpoint": "Vertical transmission, AIDS, death, and clinical or laboratory features",
        "result": "The study estimated vertical transmission and recorded AIDS/death outcomes among infected children.",
        "limitation": "Evolving early pediatric diagnostic criteria.",
        "can_answer": "Captures transmission and early progression through a non-recreational exposure path.",
        "cannot_answer": "Does not provide a recreational-drug comparison group.",
        "full_text": "Abstract is adequate for row-level inclusion; full text needed for endpoint definitions.",
        "tags": "[aids, hiv, perinatal, cohort]",
    },
    {
        "key": "european-collaborative-1994-vertical-hiv-natural-history",
        "slug": "european-collaborative-study-1994-natural-history-of-vertically-acquired-hiv-1",
        "q": "Q8",
        "label": "European Collaborative Study 1994",
        "title": "Natural history of vertically acquired human immunodeficiency virus-1 infection",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "prospective vertically acquired HIV natural-history cohort",
        "study_type": "Prospective pediatric cohort",
        "subjects": "124 vertically infected children followed across 10 centers",
        "exposure": "Mother-to-child HIV-1 transmission",
        "comparator": "Age and disease-progression strata",
        "endpoint": "AIDS, death, and symptoms",
        "result": "A substantial fraction developed AIDS in early childhood in the abstract-level record.",
        "limitation": "Early treatment and diagnostic practices varied.",
        "can_answer": "Shows AIDS progression in children with vertical HIV exposure.",
        "cannot_answer": "Does not answer adult recreational-drug or AZT-toxicity claims.",
        "full_text": "Full text needed for exact cumulative AIDS percentages and definitions.",
        "tags": "[aids, hiv, perinatal, cohort]",
    },
    {
        "key": "abrams-1998-hiv-load-infants-progression",
        "slug": "abrams-1998-hiv-load-early-in-life-and-infant-disease-progression",
        "q": "Q8",
        "label": "Abrams 1998",
        "title": "Association of human immunodeficiency virus load early in life with disease progression among HIV-infected infants",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "pediatric HIV viral-load progression cohort",
        "study_type": "Pediatric cohort",
        "subjects": "89 HIV-1-infected children",
        "exposure": "Perinatal HIV infection and early viral-load levels",
        "comparator": "Viral-load strata after early life",
        "endpoint": "CDC category 3 or C disease classification or death",
        "result": "Higher early viral load was associated with progression or death.",
        "limitation": "Predictor study among already infected infants, not an initial transmission study.",
        "can_answer": "Supplements perinatal natural-history evidence with a progression predictor.",
        "cannot_answer": "Does not by itself establish transmission route.",
        "full_text": "Abstract is adequate for direction; full text needed for cutoff values.",
        "tags": "[aids, hiv, perinatal, viral-load]",
    },
    {
        "key": "cardo-1997-occupational-seroconversion",
        "slug": "cardo-1997-occupational-hiv-seroconversion-after-percutaneous-exposure",
        "q": "Q8",
        "label": "Cardo 1997",
        "title": "A case-control study of HIV seroconversion in health care workers after percutaneous exposure",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "occupational HIV seroconversion case-control study",
        "study_type": "Case-control study",
        "subjects": "33 seroconverting health care workers and 665 exposed controls",
        "exposure": "Percutaneous exposure to HIV-infected blood",
        "comparator": "Exposed health care workers who did not seroconvert",
        "endpoint": "HIV seroconversion",
        "result": "Deep injury, visible blood, artery or vein needle placement, and advanced disease in the source patient increased seroconversion risk.",
        "limitation": "Transmission endpoint, not AIDS progression.",
        "can_answer": "Shows non-recreational occupational HIV transmission.",
        "cannot_answer": "Does not show later AIDS progression in the same row.",
        "full_text": "Abstract is enough for the transmission row; full text needed for odds ratios.",
        "tags": "[aids, hiv, occupational-exposure, case-control]",
    },
    {
        "key": "ippolito-1999-occupational-hiv-cases",
        "slug": "ippolito-1999-occupational-hiv-infection-in-health-care-workers",
        "q": "Q8",
        "label": "Ippolito 1999",
        "title": "Occupational human immunodeficiency virus infection in health care workers: worldwide cases through September 1997",
        "tier": "tier-2",
        "claim_type": "medical",
        "role": "case-series review and surveillance compilation",
        "study_type": "Case-series review and surveillance compilation",
        "subjects": "Documented and possible occupational HIV infections in health care workers through September 1997",
        "exposure": "Occupational blood or body-fluid exposure",
        "comparator": "Documented versus possible occupational cases",
        "endpoint": "Documented occupational HIV infection",
        "result": "The compilation preserves documented occupational-infection cases, but it is not a progression cohort.",
        "limitation": "Review/case compilation rather than a controlled cohort.",
        "can_answer": "Useful as a bibliography and route-of-exposure map.",
        "cannot_answer": "Should not be used as primary progression evidence.",
        "full_text": "Abstract is sufficient for exclusion from primary-study rows; full text useful for bibliography mining.",
        "tags": "[aids, hiv, occupational-exposure, review]",
    },
    {
        "key": "cdc-1981-pneumocystis-los-angeles",
        "slug": "cdc-1981-pneumocystis-pneumonia-los-angeles",
        "q": "Q8 chronology",
        "label": "MMWR 1981 PCP",
        "title": "Pneumocystis pneumonia - Los Angeles",
        "tier": "tier-1",
        "claim_type": "historical",
        "role": "primary surveillance case report",
        "study_type": "Primary MMWR case report",
        "subjects": "Five previously healthy men in Los Angeles treated from October 1980 to May 1981",
        "exposure": "Pre-AZT AIDS-defining clinical syndrome chronology",
        "comparator": "No formal comparator",
        "endpoint": "Biopsy-confirmed Pneumocystis pneumonia and deaths",
        "result": "Records PCP cases and deaths before published human AZT use.",
        "limitation": "Small case report and the AIDS label was not yet established.",
        "can_answer": "Establishes pre-AZT AIDS-defining illness chronology.",
        "cannot_answer": "Does not establish full AIDS causation.",
        "full_text": "PubMed has no abstract; MMWR full text is needed for case details.",
        "tags": "[aids, hiv, azt, chronology]",
    },
    {
        "key": "cdc-1981-ks-pcp-homosexual-men",
        "slug": "cdc-1981-kaposis-sarcoma-and-pneumocystis-pneumonia",
        "q": "Q8 chronology",
        "label": "MMWR 1981 KS/PCP",
        "title": "Kaposi's sarcoma and Pneumocystis pneumonia among homosexual men - New York City and California",
        "tier": "tier-1",
        "claim_type": "historical",
        "role": "primary surveillance case report",
        "study_type": "Primary MMWR case report",
        "subjects": "Early Kaposi's sarcoma and Pneumocystis pneumonia cases in New York City and California",
        "exposure": "Pre-AZT AIDS-defining clinical syndrome chronology",
        "comparator": "No formal comparator",
        "endpoint": "Kaposi's sarcoma, Pneumocystis pneumonia, and deaths",
        "result": "Records additional AIDS-defining clinical clusters in 1981 before AZT approval.",
        "limitation": "Early surveillance case report with incomplete causal model.",
        "can_answer": "Adds a second primary pre-AZT chronology anchor.",
        "cannot_answer": "Does not adjudicate mechanism.",
        "full_text": "PubMed has no abstract; MMWR full text is needed for case details.",
        "tags": "[aids, hiv, azt, chronology]",
    },
    {
        "key": "gottlieb-1981-pcp-candidiasis",
        "slug": "gottlieb-1981-pneumocystis-carinii-pneumonia-and-mucosal-candidiasis",
        "q": "Q8 chronology",
        "label": "Gottlieb 1981",
        "title": "Pneumocystis carinii pneumonia and mucosal candidiasis in previously healthy homosexual men",
        "tier": "tier-1",
        "claim_type": "historical",
        "role": "peer-reviewed clinical case series",
        "study_type": "Clinical case series",
        "subjects": "Previously healthy men with Pneumocystis pneumonia and mucosal candidiasis in 1980-1981",
        "exposure": "Pre-AZT acquired cellular immunodeficiency cases",
        "comparator": "No formal comparator",
        "endpoint": "Opportunistic infection and immunologic findings",
        "result": "Documents acquired cellular immunodeficiency clinical cases before AZT use.",
        "limitation": "Small case series and early pathogenesis uncertainty.",
        "can_answer": "Provides a peer-reviewed pre-AZT clinical anchor.",
        "cannot_answer": "Does not establish all later AIDS mechanisms.",
        "full_text": "Abstract is enough for chronology; full text needed for case-level immunology details.",
        "tags": "[aids, hiv, azt, chronology]",
    },
    {
        "key": "cdc-1982-aids-update-united-states",
        "slug": "cdc-1982-update-on-acquired-immune-deficiency-syndrome-united-states",
        "q": "Q8 chronology",
        "label": "MMWR 1982 AIDS update",
        "title": "Update on acquired immune deficiency syndrome (AIDS) - United States",
        "tier": "tier-1",
        "claim_type": "historical",
        "role": "primary national surveillance report",
        "study_type": "Primary MMWR surveillance report",
        "subjects": "U.S. AIDS surveillance cases reported by September 15, 1982",
        "exposure": "Pre-AZT national AIDS surveillance chronology",
        "comparator": "Diagnosis time periods",
        "endpoint": "Reported AIDS cases and diagnosis timing",
        "result": "Records hundreds of AIDS cases before published human AZT use and before 1987 approval.",
        "limitation": "Surveillance definition and reporting completeness limits.",
        "can_answer": "Strong primary chronology evidence against an AZT-origin explanation for AIDS generally.",
        "cannot_answer": "Does not address post-approval AZT toxicity.",
        "full_text": "PubMed has no abstract; MMWR full text is needed for exact case counts and dates.",
        "tags": "[aids, hiv, azt, chronology]",
    },
    {
        "key": "cdc-1982-aids-hemophilia-a",
        "slug": "cdc-1982-aids-among-patients-with-hemophilia-a",
        "q": "Q8 chronology",
        "label": "MMWR 1982 hemophilia AIDS",
        "title": "Update on acquired immune deficiency syndrome (AIDS) among patients with hemophilia A",
        "tier": "tier-1",
        "claim_type": "historical",
        "role": "primary surveillance case update",
        "study_type": "Primary MMWR case update",
        "subjects": "Patients with hemophilia A and AIDS cases identified by 1982",
        "exposure": "Hemophilia blood-product context before AZT approval",
        "comparator": "No formal comparator",
        "endpoint": "AIDS cases among hemophilia A patients",
        "result": "Records hemophilia-associated AIDS cases before AZT approval.",
        "limitation": "Case-series surveillance, not a controlled causation study.",
        "can_answer": "Adds a pre-AZT chronology anchor outside recreational-drug-only framing.",
        "cannot_answer": "Does not itself identify the causal agent.",
        "full_text": "PubMed has no abstract; MMWR full text is needed for case details.",
        "tags": "[aids, hiv, hemophilia, chronology]",
    },
    {
        "key": "yarchoan-1986-first-azt-administration",
        "slug": "yarchoan-1986-administration-of-azt-to-patients-with-aids-or-arc",
        "q": "Q8 chronology",
        "label": "Yarchoan 1986",
        "title": "Administration of 3'-azido-3'-deoxythymidine, an inhibitor of HTLV-III/LAV replication, to patients with AIDS or AIDS-related complex",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "early human AZT clinical study",
        "study_type": "Early clinical administration study",
        "subjects": "19 patients with AIDS or AIDS-related complex",
        "exposure": "Azidothymidine administration",
        "comparator": "No placebo comparator in the abstract-level record",
        "endpoint": "Early clinical and laboratory response to AZT",
        "result": "Published human AZT administration appears in 1986, after multiple pre-AZT AIDS records.",
        "limitation": "Small early study and not an origin-chronology source by itself.",
        "can_answer": "Anchors the earliest published human AZT-use boundary found in this pass.",
        "cannot_answer": "Does not answer long-term AZT toxicity or efficacy.",
        "full_text": "Full text needed for dosing, adverse events, and clinical response details.",
        "tags": "[aids, hiv, azt, chronology]",
    },
    {
        "key": "fischl-1987-azt-efficacy",
        "slug": "fischl-1987-efficacy-of-azidothymidine-in-aids-and-arc",
        "q": "Q9",
        "label": "Fischl 1987",
        "title": "The efficacy of azidothymidine (AZT) in the treatment of patients with AIDS and AIDS-related complex: a double-blind, placebo-controlled trial",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "pivotal AZT efficacy trial",
        "study_type": "Double-blind placebo-controlled trial",
        "subjects": "282 patients with AIDS or advanced AIDS-related complex",
        "exposure": "Oral zidovudine",
        "comparator": "Placebo",
        "endpoint": "Short-term clinical progression, opportunistic disease, and death",
        "result": "The short-term result direction favored zidovudine in this advanced-disease population.",
        "limitation": "Short follow-up, early high-dose era, selected advanced disease population, and toxicity must be read with the companion paper.",
        "can_answer": "Supports a narrow short-term efficacy claim for advanced AIDS or ARC.",
        "cannot_answer": "Does not justify broad claims about long-term safety or all 1990s prescribing.",
        "full_text": "Full text needed for exact event counts, stopping context, and endpoint definitions.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "richman-1987-azt-toxicity",
        "slug": "richman-1987-toxicity-of-azidothymidine-in-aids-and-arc",
        "q": "Q9",
        "label": "Richman 1987",
        "title": "The toxicity of azidothymidine (AZT) in the treatment of patients with AIDS and AIDS-related complex: a double-blind, placebo-controlled trial",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "companion AZT toxicity analysis",
        "study_type": "Companion toxicity analysis from a double-blind placebo-controlled trial",
        "subjects": "Participants in the 1987 AZT AIDS/ARC trial",
        "exposure": "Zidovudine",
        "comparator": "Placebo",
        "endpoint": "Hematologic toxicity, anemia, neutropenia, and transfusion requirement",
        "result": "Bone-marrow toxicity and transfusion needs were higher in zidovudine recipients.",
        "limitation": "Same early high-dose and advanced-disease setting as the efficacy trial.",
        "can_answer": "Establishes that early AZT use carried measurable toxicity.",
        "cannot_answer": "Does not show whether later doses or combinations had the same risk profile.",
        "full_text": "Abstract is enough for toxicity direction; full text needed for full adverse-event table.",
        "tags": "[aids, hiv, azt, toxicity]",
    },
    {
        "key": "fischl-1990-actg-016",
        "slug": "fischl-1990-actg-016-zidovudine-in-mildly-symptomatic-hiv",
        "q": "Q9",
        "label": "ACTG 016 1990",
        "title": "The efficacy of azidothymidine (AZT) in the treatment of patients with mildly symptomatic human immunodeficiency virus infection",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "mildly symptomatic HIV zidovudine trial",
        "study_type": "Double-blind randomized placebo-controlled trial",
        "subjects": "711 mildly symptomatic HIV-infected subjects",
        "exposure": "Zidovudine 200 mg every four hours",
        "comparator": "Placebo",
        "endpoint": "AIDS, advanced ARC, or death",
        "result": "Benefit was concentrated in the CD4 200-499 subgroup in the abstract-level record, with measurable anemia and neutropenia.",
        "limitation": "Subgroup-dependent benefit and early dosing context.",
        "can_answer": "Extends AZT evidence beyond advanced AIDS into earlier symptomatic disease.",
        "cannot_answer": "Does not settle asymptomatic timing or long-term survival.",
        "full_text": "Full text needed for subgroup table and toxicity detail.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "volberding-1990-actg-019",
        "slug": "volberding-1990-actg-019-zidovudine-in-asymptomatic-hiv",
        "q": "Q9",
        "label": "ACTG 019 1990",
        "title": "Zidovudine in asymptomatic human immunodeficiency virus infection: a controlled trial in persons with fewer than 500 CD4-positive cells per cubic millimeter",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "asymptomatic HIV zidovudine timing trial",
        "study_type": "Controlled randomized trial",
        "subjects": "Asymptomatic HIV-infected persons with fewer than 500 CD4-positive cells per cubic millimeter",
        "exposure": "Zidovudine dose arms",
        "comparator": "Placebo",
        "endpoint": "Progression to AIDS or advanced disease and CD4 changes",
        "result": "Zidovudine delayed progression in the initial trial frame but did not by itself prove long-term survival benefit.",
        "limitation": "Surrogate and timing questions remained open.",
        "can_answer": "Defines early asymptomatic prescribing evidence.",
        "cannot_answer": "Does not answer whether immediate treatment improved survival over deferred treatment.",
        "full_text": "Full text needed for endpoint hierarchy and dose-specific adverse events.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "fischl-1992-actg-019-toxicity",
        "slug": "fischl-1992-safety-and-toxicity-of-zidovudine-in-actg-019",
        "q": "Q9",
        "label": "ACTG 019 toxicity 1992",
        "title": "Safety and toxicity of zidovudine in asymptomatic HIV-infected individuals",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "asymptomatic zidovudine toxicity analysis",
        "study_type": "Detailed toxicity analysis from ACTG 019",
        "subjects": "1,567 asymptomatic HIV-infected subjects",
        "exposure": "Zidovudine 500 mg/day or 1500 mg/day",
        "comparator": "Placebo",
        "endpoint": "Hematologic, hepatic, renal, and symptom toxicity",
        "result": "Severe anemia and neutropenia increased in a dose-related pattern, especially at 1500 mg/day.",
        "limitation": "Toxicity analysis tied to a specific trial population and dosing era.",
        "can_answer": "Quantifies harm in people not yet clinically ill.",
        "cannot_answer": "Does not establish efficacy.",
        "full_text": "Abstract is enough for direction; full text needed for full adverse-event tables.",
        "tags": "[aids, hiv, azt, toxicity]",
    },
    {
        "key": "volberding-1994-actg-019-duration",
        "slug": "volberding-1994-duration-of-zidovudine-benefit-in-actg-019",
        "q": "Q9",
        "label": "ACTG 019 follow-up 1994",
        "title": "The duration of zidovudine benefit in persons with asymptomatic HIV infection",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "extended ACTG 019 follow-up",
        "study_type": "Extended follow-up of randomized trial cohort",
        "subjects": "1,565 asymptomatic HIV-infected subjects from ACTG 019",
        "exposure": "Earlier zidovudine initiation",
        "comparator": "Deferred/open-label treatment after original placebo or dose arms",
        "endpoint": "AIDS or death",
        "result": "Earlier 500 mg zidovudine delayed AIDS/death but did not add survival compared with delayed initiation in the abstract-level record.",
        "limitation": "Open-label crossover complicates long-term interpretation.",
        "can_answer": "Tests duration and timing of asymptomatic benefit.",
        "cannot_answer": "Does not prove a simple universal benefit or harm claim.",
        "full_text": "Full text needed for survival and crossover details.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "concorde-1994-immediate-deferred-zidovudine",
        "slug": "concorde-1994-immediate-versus-deferred-zidovudine",
        "q": "Q9",
        "label": "Concorde 1994",
        "title": "Concorde: MRC/ANRS randomised double-blind controlled trial of immediate and deferred zidovudine in symptom-free HIV infection",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "immediate versus deferred zidovudine timing trial",
        "study_type": "Large double-blind randomized controlled trial",
        "subjects": "Symptom-free HIV-infected adults",
        "exposure": "Immediate zidovudine",
        "comparator": "Deferred zidovudine until clinical or CD4 indication",
        "endpoint": "Survival and disease progression",
        "result": "Immediate therapy changed short-term markers or progression timing but did not show durable survival advantage over deferred therapy.",
        "limitation": "Timing trial with evolving clinical practice and later treatment changes.",
        "can_answer": "Central evidence for asymptomatic immediate-start ethics.",
        "cannot_answer": "Does not answer advanced AIDS benefit-risk.",
        "full_text": "Full text needed for exact endpoint definitions and subgroup results.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "mulder-1994-european-australian-study-017",
        "slug": "mulder-1994-zidovudine-twice-daily-in-asymptomatic-hiv",
        "q": "Q9",
        "label": "Study 017 1994",
        "title": "Zidovudine twice daily in asymptomatic subjects with HIV infection, and a high risk of progression to AIDS: a randomized, double-blind placebo-controlled study",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "asymptomatic high-risk zidovudine trial",
        "study_type": "Randomized double-blind placebo-controlled trial",
        "subjects": "329 asymptomatic high-risk HIV-infected subjects",
        "exposure": "Zidovudine 500 mg twice daily",
        "comparator": "Placebo",
        "endpoint": "AIDS or severe ARC as primary endpoint",
        "result": "Primary endpoint difference was limited and not significant overall in the abstract-level record; symptomatic disease was delayed.",
        "limitation": "Endpoint-dependent benefit strength.",
        "can_answer": "Adds an asymptomatic RCT with limited primary-endpoint strength.",
        "cannot_answer": "Does not prove broad survival benefit.",
        "full_text": "Full text needed for primary and secondary endpoint separation.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "connor-1994-pactg-076",
        "slug": "connor-1994-zidovudine-to-reduce-maternal-infant-hiv-transmission",
        "q": "Q9",
        "label": "Connor 1994",
        "title": "Reduction of maternal-infant transmission of human immunodeficiency virus type 1 with zidovudine treatment",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "perinatal zidovudine transmission trial",
        "study_type": "Randomized double-blind placebo-controlled trial",
        "subjects": "HIV-positive pregnant women and infants",
        "exposure": "Maternal, intrapartum, and newborn zidovudine regimen",
        "comparator": "Placebo",
        "endpoint": "Infant HIV infection",
        "result": "Infant infection was lower in the zidovudine group than in placebo at 18 months in the abstract-level record.",
        "limitation": "Narrow perinatal-transmission endpoint and short toxicity window.",
        "can_answer": "Supports a perinatal transmission-prevention claim.",
        "cannot_answer": "Does not answer adult monotherapy ethics.",
        "full_text": "Abstract is enough for direction; full text needed for full safety follow-up.",
        "tags": "[aids, hiv, azt, perinatal]",
    },
    {
        "key": "actg-116b-117-1995-zidovudine-didanosine",
        "slug": "actg-116b-117-1995-zidovudine-versus-didanosine",
        "q": "Q9",
        "label": "ACTG 116B/117 1995",
        "title": "Zidovudine compared with didanosine in patients with advanced HIV disease and little or no previous experience with zidovudine",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "advanced HIV comparator antiretroviral trial",
        "study_type": "Randomized double-blind comparative trial",
        "subjects": "617 patients with advanced HIV disease and little or no prior zidovudine",
        "exposure": "Zidovudine",
        "comparator": "Didanosine dose arms with crossover design",
        "endpoint": "New AIDS-defining event or death",
        "result": "Result direction depended on prior zidovudine exposure and comparator timing.",
        "limitation": "Complex crossover and treatment-history-dependent interpretation.",
        "can_answer": "Shows that monotherapy ethics depended on comparator and prior exposure by 1995.",
        "cannot_answer": "Does not answer initial placebo-controlled efficacy.",
        "full_text": "Full text needed for treatment-history strata.",
        "tags": "[aids, hiv, azt, clinical-trial]",
    },
    {
        "key": "daquila-1995-zidovudine-resistance",
        "slug": "daquila-1995-zidovudine-resistance-mutations-and-clinical-progression",
        "q": "Q9",
        "label": "D'Aquila 1995",
        "title": "Human immunodeficiency virus type 1 zidovudine resistance mutations and disease progression during antiretroviral therapy",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "zidovudine resistance and prognosis analysis",
        "study_type": "Resistance and clinical-progression analysis",
        "subjects": "Long-term zidovudine-treated ACTG patients",
        "exposure": "Zidovudine therapy and resistance mutations",
        "comparator": "Mutation strata",
        "endpoint": "Resistance mutations and progression or death",
        "result": "Long-term zidovudine therapy selected resistance mutations associated with progression risk in the abstract-level record.",
        "limitation": "Not itself a randomized prescribing trial.",
        "can_answer": "Adds a strategy-level harm or limitation signal for long-term monotherapy.",
        "cannot_answer": "Does not prove AZT caused AIDS.",
        "full_text": "Full text needed for mutation-specific risk estimates.",
        "tags": "[aids, hiv, azt, resistance]",
    },
    {
        "key": "delta-1996-combination-therapy",
        "slug": "delta-1996-zidovudine-combinations-versus-zidovudine-alone",
        "q": "Q9",
        "label": "Delta 1996",
        "title": "Delta: a randomised double-blind controlled trial comparing combinations of zidovudine plus didanosine or zalcitabine with zidovudine alone in HIV-infected individuals",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "combination therapy versus zidovudine monotherapy trial",
        "study_type": "Randomized double-blind international trial",
        "subjects": "3,207 HIV-infected individuals",
        "exposure": "Zidovudine plus didanosine or zalcitabine",
        "comparator": "Zidovudine alone",
        "endpoint": "Survival and AIDS or death",
        "result": "Combination therapy improved survival compared with zidovudine alone, especially in zidovudine-naive subjects.",
        "limitation": "Post-1995 context and not a placebo comparison.",
        "can_answer": "Shows that later evidence undermined AZT monotherapy as a default.",
        "cannot_answer": "Does not answer the 1987 placebo-controlled question.",
        "full_text": "Abstract is enough for direction; full text needed for subgroup details.",
        "tags": "[aids, hiv, azt, combination-therapy]",
    },
    {
        "key": "actg-175-1996-monotherapy-combination",
        "slug": "actg-175-1996-zidovudine-monotherapy-versus-combination-nucleosides",
        "q": "Q9",
        "label": "ACTG 175 1996",
        "title": "A trial comparing nucleoside monotherapy with combination therapy in HIV-infected adults with CD4 cell counts from 200 to 500 per cubic millimeter",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "monotherapy versus combination nucleoside trial",
        "study_type": "Double-blind randomized controlled trial",
        "subjects": "2,467 adults with CD4 counts from 200 to 500 per cubic millimeter",
        "exposure": "Zidovudine alone",
        "comparator": "Zidovudine plus didanosine, zidovudine plus zalcitabine, or didanosine alone",
        "endpoint": "CD4 decline, AIDS, or death",
        "result": "Progression was more frequent with zidovudine alone than in the combination or didanosine arms in the abstract-level record.",
        "limitation": "Post-1995 context and not an untreated comparison.",
        "can_answer": "Directly informs monotherapy ethics after better comparators existed.",
        "cannot_answer": "Does not negate earlier short-term AZT benefit in advanced AIDS.",
        "full_text": "Full text needed for exact adverse-event and subgroup analysis.",
        "tags": "[aids, hiv, azt, combination-therapy]",
    },
    {
        "key": "lamivudine-1996-3tc-zidovudine",
        "slug": "lamivudine-1996-lamivudine-plus-zidovudine-versus-zidovudine-alone",
        "q": "Q9",
        "label": "Lamivudine 1996",
        "title": "A randomized trial of lamivudine plus zidovudine versus zidovudine alone in previously untreated patients with HIV infection",
        "tier": "tier-1",
        "claim_type": "medical",
        "role": "lamivudine plus zidovudine versus zidovudine monotherapy trial",
        "study_type": "Double-blind randomized multicenter trial",
        "subjects": "129 antiretroviral-naive adults",
        "exposure": "Lamivudine plus zidovudine",
        "comparator": "Zidovudine alone",
        "endpoint": "CD4, p24, cellular viremia, viral load, and safety",
        "result": "Combination therapy was superior on virologic and immunologic endpoints in the abstract-level record.",
        "limitation": "Small trial and mostly surrogate endpoints.",
        "can_answer": "Adds transition evidence away from AZT-alone strategy.",
        "cannot_answer": "Does not answer clinical survival directly.",
        "full_text": "Full text needed for safety and resistance details.",
        "tags": "[aids, hiv, azt, combination-therapy]",
    },
]


FDA = {
    "slug": "fda-1987-zidovudine-retrovir-approval-record",
    "title": "FDA Orphan Drug Designation and Approval Record for Zidovudine/Retrovir",
    "summary": "Primary regulatory chronology record for zidovudine/Retrovir orphan designation and 1987 marketing approval.",
    "tags": "[aids, hiv, azt, chronology, regulatory-history]",
}


def load_lookup_by_key() -> dict[str, dict[str, object]]:
    records = json.loads(LOOKUPS_JSON.read_text(encoding="utf-8"))
    return {record["candidate_key"]: record for record in records}


def source_page(study: dict[str, str], lookup: dict[str, object]) -> str:
    pmid = lookup.get("pmid") or ""
    doi = lookup.get("doi") or ""
    abstract = lookup.get("abstract") or ""
    publication_types = "; ".join(lookup.get("publication_types") or [])
    authors = "; ".join(lookup.get("authors") or [])
    journal = lookup.get("journal_iso") or lookup.get("journal") or ""
    year = lookup.get("year") or ""
    summary = f"{study['role']} relevant to Gutknecht letter {study['q']}."
    summary = summary[:1].upper() + summary[1:]
    return f"""---
title: {yaml_quote(study['title'])}
category: source
summary: {yaml_quote(summary)}
tags: {study['tags']}
updated: 2026-05-05
claim_status: exploratory
claim_type: {study['claim_type']}
source_tier: {study['tier']}
evidence_role: {study['role']}
pmid: {pmid}
doi: {doi}
---

# {study['title']}

## Source type
- Role in this vault: {study['role']}
- API lookup: PubMed PMID {pmid or 'not found'}{f'; DOI {doi}' if doi else ''}
- Journal/year: {journal}, {year}
- Publication types: {publication_types or 'not listed in API output'}
- Authors in API output: {authors or 'not listed in API output'}

> Warning: This page is for research analysis only. It is not medical advice.

## Vault extraction
| Field | Value |
|---|---|
| Study type | {cell(study['study_type'])} |
| Sample / subjects | {cell(study['subjects'])} |
| Exposure or intervention | {cell(study['exposure'])} |
| Comparator or control | {cell(study['comparator'])} |
| Endpoint | {cell(study['endpoint'])} |
| Result | {cell(study['result'])} |
| Main limitation | {cell(study['limitation'])} |

## What this source can answer
{study['can_answer']}

## What it cannot answer
{study['cannot_answer']}

## Abstract status
{study['full_text']}

## API abstract
{abstract or 'The PubMed lookup did not provide an abstract. Use the primary full text before relying on case details.'}

## Related
- [[sources/congressman-questions-aids-in-letter]]
- [[synthesis/gutknecht-letter-questions-7-9]]
"""


def fda_page() -> str:
    return f"""---
title: {yaml_quote(FDA['title'])}
category: source
summary: {yaml_quote(FDA['summary'])}
tags: {FDA['tags']}
updated: 2026-05-05
claim_status: exploratory
claim_type: historical
source_tier: tier-1
evidence_role: primary regulatory chronology record
source_url: https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=8185
---

# {FDA['title']}

## Source type
Primary regulatory chronology record for zidovudine/Retrovir.

> Warning: This page is for research analysis only. It is not medical advice.

## Vault extraction
| Field | Value |
|---|---|
| Document type | FDA orphan-drug designation and approval record |
| Subject | Zidovudine/Retrovir |
| Chronology endpoint | Orphan designation and marketing approval dates |
| Result | Orphan designation is listed as July 17, 1985; marketing approval is listed as March 19, 1987. |
| Main limitation | Regulatory chronology record, not a clinical trial or proof of biomedical efficacy. |

## What this source can answer
This record can anchor the approval-date boundary used in the AZT chronology section of [[synthesis/gutknecht-letter-questions-7-9]].

## What it cannot answer
It cannot prove AZT efficacy, toxicity, or AIDS causation. Those questions require direct trial or cohort evidence.

## Related
- [[sources/congressman-questions-aids-in-letter]]
- [[synthesis/gutknecht-letter-questions-7-9]]
"""


def rows(studies: list[dict[str, str]]) -> str:
    lines = ["| Source | Study type | Sample / subjects | Exposure or intervention | Comparator / control | Endpoint | Result | Main limitation |", "|---|---|---|---|---|---|---|---|"]
    for s in studies:
        lines.append(
            f"| {link(s['slug'], s['label'])} | {cell(s['study_type'])} | {cell(s['subjects'])} | {cell(s['exposure'])} | {cell(s['comparator'])} | {cell(s['endpoint'])} | {cell(s['result'])} | {cell(s['limitation'])} |"
        )
    return "\n".join(lines)


def short_rows(studies: list[dict[str, str]]) -> str:
    lines = ["| Source | Classification | Why it is not a primary direct-study row |", "|---|---|---|"]
    for s in studies:
        lines.append(f"| {link(s['slug'], s['label'])} | {cell(s['study_type'])} | {cell(s['limitation'])} |")
    return "\n".join(lines)


def render_q_page() -> str:
    q7 = [s for s in STUDIES if s["q"] in {"Q7", "Q7/Q8"}]
    q8_direct = [s for s in STUDIES if s["q"] in {"Q8", "Q7/Q8"} and s["key"] != "ippolito-1999-occupational-hiv-cases"]
    q8_review = [s for s in STUDIES if s["key"] == "ippolito-1999-occupational-hiv-cases"]
    q8_chron = [s for s in STUDIES if s["q"] == "Q8 chronology"]
    q9 = [s for s in STUDIES if s["q"] == "Q9"]
    source_count = len(STUDIES) + 1
    return f"""---
title: Gutknecht Letter Questions 7-9
category: synthesis
summary: Direct-study audit of the Gutknecht letter's questions about hemophiliac survival, recreational drugs or AZT as causes of AIDS, and the ethics of prescribing AZT.
tags: [aids, hiv, azt, hemophilia, gutknecht]
sources: {source_count}
updated: 2026-05-05
claim_status: unresolved
claim_type: medical
---

# Gutknecht Letter Questions 7-9

Scope: This page addresses only questions 7-9 from [[sources/congressman-questions-aids-in-letter]]. It is rebuilt from identifier-level API lookups in `wiki/synthesis/gutknecht-letter-questions-7-9-api-lookups.json` and `wiki/synthesis/gutknecht-letter-questions-7-9-api-lookups.csv`, then filtered under this vault's direct-evidence standard.

> Warning: This page is for research analysis only. It is not medical advice.

> Note: Agency, regulatory, and MMWR records below are used only for primary chronology or surveillance-document value. They are not treated as authority proof of biomedical causation.

## API lookup and triage notes
- The batch script `scripts/gutknecht_pmid_doi_lookup.py` performed one PubMed PMID or DOI lookup per candidate paper and wrote JSON plus CSV output.
- No duplicate PMID/DOI records were found in the batch, although some studies are relevant to more than one Gutknecht question.
- Primary studies and primary historical documents were kept in the main registers. [[sources/ippolito-1999-occupational-hiv-infection-in-health-care-workers]] was separated as a case-series review and bibliography aid.
- Abstracts are sufficient for some row-level screening, but exact event counts, model coefficients, dosing, adverse-event tables, and MMWR case details require full text where flagged on the source pages.

## Question 7
### Status
Unresolved. The direct studies below support narrower findings: hemophilia survival improved before the HIV era, and HIV-era mortality signals appear in U.S., UK, Dutch, and hemophilia natural-history cohorts. They do not close every causation question.

> Note: The exact letter statistic that American hemophiliacs' median life expectancy rose from 11 in 1972 to 27 in 1987 remains unresolved in this audit. [[sources/johnson-1985-aids-among-hemophilia-treatment-center-patients]] supports related U.S. treatment-center and mortality facts, but full text is needed before converting that into the letter's exact statistic.

### Direct-study register
{rows(q7)}

### What was unresolved in 1995 vs. now
- In 1995, the long-term split between HIV-related, hepatitis-related, treatment-related, and background hemophilia mortality still required cohort-by-cohort reconstruction.
- This page supports only the narrower claim that pre-HIV hemophilia survival improved and that HIV-era mortality/progression signals are visible in the cited direct studies.

## Question 8
### Status
The current direct-study register does not support a recreational-drug-only explanation for AIDS generally. It does show AIDS, HIV infection, or HIV progression endpoints in transfusion, hemophilia, perinatal, and occupational exposure settings where recreational-drug use is not the central exposure being tested.

This does not by itself prove a single-factor HIV-only model for every case; cofactor and treatment-toxicity questions remain separate.

### Non-recreational exposure direct-study register
{rows(q8_direct)}

### AZT chronology register
These records address only chronology. They make a general AZT-origin claim chronologically untenable because AIDS-defining case records predate published human AZT use and March 19, 1987 marketing approval. They do not answer narrower post-approval AZT toxicity questions.

{rows(q8_chron)}

| Source | Document type | Chronology endpoint | Result | Limitation |
|---|---|---|---|---|
| [[sources/fda-1987-zidovudine-retrovir-approval-record|FDA 1987 Retrovir record]] | Primary regulatory chronology record | Zidovudine/Retrovir approval date | Marketing approval is listed as March 19, 1987 | Regulatory chronology only; not trial evidence |

### Separated review or compilation
{short_rows(q8_review)}

### What was unresolved in 1995 vs. now
- In 1995, cofactors, progression variability, treatment toxicity, and endpoint definitions were still live issues.
- The valid takeaway here is narrower: multiple non-recreational exposure cohorts and chronology documents make recreational drugs or AZT alone insufficient as general explanations for all AIDS cases.

## Question 9
### Status
The direct trial literature supports a mixed, endpoint-specific conclusion. Zidovudine showed short-term benefit in some advanced, symptomatic, asymptomatic, and perinatal settings, but toxicity, timing, resistance, and comparator evidence sharply limit any broad ethical claim.

### Direct-study register
{rows(q9)}

### What was unresolved in 1995 vs. now
- In 1995, major unresolved questions included long-term toxicity, resistance, the best time to start therapy, and whether AZT monotherapy remained appropriate once better comparator and combination data emerged.
- The evidence does not support a one-line conclusion that AZT was simply safe and ethically mandatory, or that it had no direct trial benefit. It supports narrower benefit-risk statements tied to population, dose, comparator, endpoint, and year.

## What this wiki currently concludes
- This page remains unresolved at the broad-causation and broad-ethics level.
- Q7: pre-HIV hemophilia survival gains and HIV-era mortality signals are directly documented, but the letter's exact life-expectancy statistic is not yet verified from a direct source.
- Q8: non-recreational exposure cohorts and pre-AZT chronology records prevent a recreational-drug-only or AZT-origin explanation from carrying the whole AIDS phenomenon.
- Q9: direct AZT trials show both measurable benefits and meaningful harms; ethical analysis must be endpoint-specific and historically time-bound.

## Related
- [[sources/congressman-questions-aids-in-letter]]
- [[sources/aids]]
- [[concepts/clinical-endpoints]]
- [[concepts/inferential-leap]]
"""


def main() -> int:
    lookup_by_key = load_lookup_by_key()
    sources_dir = WIKI / "sources"
    for study in STUDIES:
        (sources_dir / f"{study['slug']}.md").write_text(source_page(study, lookup_by_key[study["key"]]), encoding="utf-8")
    (sources_dir / f"{FDA['slug']}.md").write_text(fda_page(), encoding="utf-8")
    Q_PAGE.write_text(render_q_page(), encoding="utf-8")
    print(f"source_pages: {len(STUDIES) + 1}")
    print(f"updated: {Q_PAGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
