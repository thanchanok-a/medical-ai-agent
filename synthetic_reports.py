# ============================================================
# MEDICAL AI EXPLANATION AGENT
# Synthetic Test Report Dataset — 20 Reports
# All patients and data are ENTIRELY FICTIONAL
# Created for: MedGemma Impact Challenge / Grad AI Final Project
# ============================================================

import json

REPORTS = {

    # ════════════════════════════════════════════════════════
    # LOW URGENCY (7 reports) — Routine / Stable / Normal
    # ════════════════════════════════════════════════════════

    "annual_checkup_young_female": {
        "label": "Annual Checkup — Young Female (Expected: Low urgency)",
        "domain": "Preventive Medicine",
        "urgency_true": "Low",
        "word_count": 198,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Sarah Mitchell, 28F
Visit: Annual preventive care visit
Vitals: BP 112/70, HR 68 bpm, BMI 22.4, Temp 98.4°F, O2 sat 99%
Allergies: None known

Labs (fasting):
Total cholesterol 168 mg/dL, LDL 92 mg/dL, HDL 62 mg/dL
Fasting glucose 84 mg/dL, TSH 1.8 mIU/L
CBC: WBC 6.2, Hgb 13.4, Plt 245 — all within normal limits
Pap smear: Normal, no atypical cells

Assessment: Healthy 28-year-old female. All screening labs within normal limits.
No chronic conditions identified. BMI appropriate for height/weight.
Reproductive health screening completed and normal.

Plan: Continue current lifestyle. Recommend 150 min moderate exercise weekly.
Annual flu vaccine administered today. HPV booster series complete.
Routine screening colonoscopy not indicated until age 45.
Return in 1 year for annual preventive visit.
No medications prescribed. No referrals at this time."""
    },

    "stable_hypothyroid_followup": {
        "label": "Stable Hypothyroid Follow-up (Expected: Low urgency)",
        "domain": "Endocrinology",
        "urgency_true": "Low",
        "word_count": 212,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Linda Kowalski, 45F
Visit: Hypothyroidism follow-up, 3-month check
Vitals: BP 118/76, HR 72 bpm, Weight 154 lbs (stable), Temp 98.6°F

Current Medications:
Levothyroxine 75mcg QD (taking consistently, no missed doses)

Labs:
TSH: 2.1 mIU/L (within target range 0.5–4.0)
Free T4: 1.2 ng/dL (Normal)
CBC: Normal
Lipid panel: Total chol 192, LDL 112, HDL 58 — acceptable

Symptoms: Patient reports energy levels improved since last visit.
No fatigue, no cold intolerance, no weight gain since starting current dose.
Hair texture has improved. No palpitations reported.

Assessment: Hypothyroidism well-controlled on current Levothyroxine dose.
TSH within therapeutic target range. No dose adjustment needed.
Patient reports good medication adherence and symptom improvement.

Plan: Continue Levothyroxine 75mcg QD unchanged.
Recheck TSH and Free T4 in 6 months.
Patient counseled to take medication 30–60 min before breakfast.
No new medications added. Return visit in 6 months."""
    },

    "mild_seasonal_allergies": {
        "label": "Seasonal Allergies Visit (Expected: Low urgency)",
        "domain": "Allergy / Immunology",
        "urgency_true": "Low",
        "word_count": 186,
        "has_lab_values": False,
        "has_medications": True,
        "text": """Patient: James Thornton, 34M
Visit: Seasonal allergic rhinitis, annual follow-up
Vitals: BP 124/78, HR 74 bpm, Temp 98.5°F, O2 sat 99%

Chief Complaint: Runny nose, sneezing, itchy eyes since March onset.
Symptoms worsen outdoors, improve indoors with AC.
No fever, no facial pain, no loss of smell.

Physical Exam:
Nasal mucosa: Pale, boggy — consistent with allergic rhinitis
Eyes: Mild conjunctival injection bilaterally
Throat: No erythema, no exudate
Lungs: Clear to auscultation bilaterally. No wheezing.

Skin prick test (performed last year): Positive for tree pollen, grass pollen.
Negative for dust mites, pet dander, mold.

Assessment: Seasonal allergic rhinitis, tree and grass pollen sensitivity.
Well-controlled with current antihistamine regimen.
No evidence of asthma component at this visit.

Plan: Continue Cetirizine 10mg QD as needed during pollen season (March–June).
Add Fluticasone nasal spray 2 sprays each nostril QD for nasal congestion.
Avoid outdoor activities on high pollen count days.
Return only if symptoms worsen or become year-round."""
    },

    "post_op_followup_knee": {
        "label": "Post-Op Knee Follow-up (Expected: Low urgency)",
        "domain": "Orthopedics",
        "urgency_true": "Low",
        "word_count": 224,
        "has_lab_values": False,
        "has_medications": True,
        "text": """Patient: Robert Garcia, 52M
Visit: Post-operative follow-up, right knee arthroscopy — 6 weeks post-procedure

Vitals: BP 130/82, HR 76 bpm, Weight 198 lbs, Temp 98.5°F

Surgery Summary: Right knee arthroscopic partial medial meniscectomy
performed 6 weeks ago without complications. Tourniquet time 22 minutes.

Current Status:
Patient ambulating without assistive device since week 3.
Pain: 1/10 at rest, 3/10 with stairs — significantly improved from pre-op 8/10.
No joint effusion noted on exam today.
Incision sites: Well-healed, no erythema, no discharge, no dehiscence.
ROM: 0–125 degrees flexion (pre-op was 0–95 degrees).
Quad strength 4+/5 compared to contralateral side.

Current Medications:
Ibuprofen 400mg PRN pain (patient using ~2x/week, down from daily use).
Ceased narcotic pain medication at week 2 as planned.

Physical Therapy: Attending 2x/week, progressing well per PT notes.

Assessment: Excellent 6-week post-operative recovery. ROM and strength
progressing appropriately. No complications.

Plan: Continue PT until full strength restoration (est. 4–6 more weeks).
Clear for return to recreational walking, swimming, cycling.
No running or jumping sports until 3-month clearance visit.
Ibuprofen PRN as needed. Return in 6 weeks."""
    },

    "healthy_geriatric_checkup": {
        "label": "Healthy Geriatric Annual Checkup (Expected: Low urgency)",
        "domain": "Geriatrics",
        "urgency_true": "Low",
        "word_count": 238,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Dorothy Simmons, 72F
Visit: Annual geriatric wellness visit
Vitals: BP 128/78, HR 70 bpm, Weight 138 lbs (stable), BMI 22.8, Temp 98.3°F

Current Medications:
Atorvastatin 20mg QD (cardiovascular prevention)
Calcium 600mg + Vitamin D 800IU BID (osteoporosis prevention)
Low-dose aspirin 81mg QD (cardiovascular prevention)

Labs:
Lipid panel: Total chol 178, LDL 88, HDL 62, TG 95 — at goal on statin
CBC: Normal — no anemia
CMP: All values within normal limits
HbA1c: 5.4% — normal, no diabetes
eGFR: 74 mL/min/1.73m² — normal for age
TSH: 2.4 mIU/L — normal
Vitamin D: 38 ng/mL — sufficient

Functional Assessment:
MMSE: 29/30 — no cognitive impairment
ADLs: Fully independent
Falls in past year: 0
Mobility: Walking unaided, steady gait

Cancer Screenings:
Mammogram (last year): Normal
Colonoscopy (3 years ago): 2 small polyps removed, repeat in 3 years
Bone density (2 years ago): Osteopenia T-score -1.8

Assessment: Healthy, functionally independent 72-year-old.
All labs within age-appropriate normal limits.
Cardiovascular risk well-managed.

Plan: Continue all current medications unchanged. Flu and pneumococcal
vaccines updated. DEXA scan repeat due next year. Return in 1 year."""
    },

    "well_child_4year": {
        "label": "Well-Child Visit — 4 Year Old (Expected: Low urgency)",
        "domain": "Pediatrics",
        "urgency_true": "Low",
        "word_count": 205,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Ethan Park, 4M
Visit: Well-child visit — 4-year-old health supervision
Parent: Jennifer Park (mother), present throughout

Vitals: Height 41.5 inches (65th percentile), Weight 38 lbs (60th percentile)
BP 92/56, HR 96 bpm, Temp 98.6°F, O2 sat 100%

Development Screening (Ages & Stages Questionnaire):
Communication: On track — speaks in complete 4–5 word sentences
Gross motor: On track — hops on one foot, catches ball
Fine motor: On track — draws circle, uses scissors
Problem-solving: On track — understands counting to 10
Social-emotional: On track — plays cooperatively with peers

Physical Exam:
HEENT: Normal, TMs clear bilaterally, no cerumen impaction
Heart: Regular rate and rhythm, no murmurs
Lungs: Clear to auscultation
Abdomen: Soft, non-tender, no organomegaly
Skin: No rashes or lesions
Vision screen: Passed. Hearing screen: Passed.

Labs: Lead screening 2 mcg/dL — within acceptable range

Immunizations today: DTaP booster, IPV booster, MMR, Varicella — all administered

Assessment: Healthy, normally developing 4-year-old.
Growth and development appropriate for age. All immunizations now current.

Plan: Dental visit recommended. Limit screen time to 1 hour/day.
Return in 1 year for 5-year well-child visit."""
    },

    "stable_migraines_followup": {
        "label": "Stable Migraines — Neurology Follow-up (Expected: Low urgency)",
        "domain": "Neurology",
        "urgency_true": "Low",
        "word_count": 219,
        "has_lab_values": False,
        "has_medications": True,
        "text": """Patient: Amanda Okafor, 31F
Visit: Chronic migraine management follow-up
Vitals: BP 116/72, HR 68 bpm, Weight 132 lbs, Temp 98.4°F

Chief Complaint: Migraine frequency — currently 2–3 episodes/month,
down from 6–8/month when first presenting 6 months ago.

Current Medications:
Topiramate 50mg BID (prophylaxis — started 6 months ago)
Sumatriptan 50mg PRN acute migraine (using ~2–3 times/month)
Magnesium glycinate 400mg QD (supplement)

Migraine Diary Review (past 3 months):
Frequency: 2–3/month (significant improvement from baseline)
Duration: 4–6 hours average (was 12–18 hours)
Severity: 6/10 average (was 9/10)
Triggers identified: Poor sleep, red wine, skipping meals
Aura: Visual, present in ~40% of episodes — unchanged pattern

Neuro Exam: Normal. No focal deficits. Cognitive intact.
No new neurological symptoms reported.

Side effects of Topiramate: Mild word-finding difficulty, resolving.
No paresthesias, no significant weight change.

Assessment: Episodic migraine with visual aura, significantly improved
on current prophylactic regimen. Response to treatment excellent.

Plan: Continue Topiramate 50mg BID and Sumatriptan PRN unchanged.
Continue migraine diary. Counseled on sleep hygiene and trigger avoidance.
MRI brain not indicated at this time — no red flag features.
Return in 3 months."""
    },


    # ════════════════════════════════════════════════════════
    # MODERATE URGENCY (7 reports) — Needs Attention / Follow-up
    # ════════════════════════════════════════════════════════

    "hba1c_suboptimal_diabetes": {
        "label": "Suboptimal Diabetes Control (Expected: Moderate urgency)",
        "domain": "Endocrinology",
        "urgency_true": "Moderate",
        "word_count": 256,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Marcus Williams, 58M
Visit: Type 2 diabetes follow-up — 3-month interval
Vitals: BP 142/88, HR 82 bpm, Weight 212 lbs (up 6 lbs since last visit), BMI 31.2

Current Medications:
Metformin 1000mg BID
Glipizide 5mg QD
Lisinopril 10mg QD

Labs:
HbA1c: 8.9% (previous 3 months ago: 8.1% — worsening)
Fasting glucose: 198 mg/dL (target <130 mg/dL)
eGFR: 58 mL/min/1.73m² (stage 3a CKD — stable, unchanged)
Urine albumin-creatinine ratio: 48 mg/g (borderline elevated, up from 32)
Total cholesterol: 224 mg/dL, LDL 148 mg/dL (above goal <100)
Potassium: 4.2 mEq/L — normal

Assessment:
Type 2 DM with suboptimal glycemic control — HbA1c worsening despite
current regimen. Weight gain likely contributing. Stage 3a CKD with
increasing microalbuminuria warrants attention. Hypertension not at goal
(target <130/80 for diabetic patients). Lipids above goal.

Plan:
1. Add Empagliflozin 10mg QD — renal protective, weight benefit, cardiac benefit
2. Increase Lisinopril to 20mg QD for improved BP and renal protection
3. Add Atorvastatin 40mg QD for lipid management
4. Diabetes education referral for nutrition counseling
5. Recheck HbA1c, CMP, urine ACR in 3 months
Patient counseled on weight reduction target of 10 lbs minimum.
If HbA1c not improved in 3 months, will consider adding GLP-1 agonist."""
    },

    "elevated_bp_new_diagnosis": {
        "label": "New Hypertension Diagnosis (Expected: Moderate urgency)",
        "domain": "Cardiology / Internal Medicine",
        "urgency_true": "Moderate",
        "word_count": 231,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Patricia Nguyen, 49F
Visit: New patient visit — elevated blood pressure found at pharmacy screening

Vitals: BP 158/96 (confirmed on 3 separate readings, 5 min apart)
HR 80 bpm, Weight 168 lbs, BMI 27.8, Temp 98.5°F

History:
No prior hypertension diagnosis. Father had heart attack at age 62.
Mother has hypertension. Currently taking no medications. No OCP.
Denies chest pain, palpitations, shortness of breath, vision changes, headache.
Sodium intake appears high per dietary history (processed foods daily).
Alcohol: 1–2 glasses wine nightly.

Physical Exam:
Cardiovascular: Regular rate and rhythm, no S3/S4, no murmurs
Fundoscopic: Mild AV nicking — consistent with early hypertensive changes
Peripheral pulses: Normal and symmetric
No peripheral edema

Labs:
CMP: All normal — creatinine 0.8, glucose 94, electrolytes WNL
CBC: Normal
TSH: 1.9 mIU/L — normal (thyroid cause ruled out)
Urinalysis: No proteinuria
EKG: Normal sinus rhythm, no LVH pattern
Lipid panel: Total chol 218, LDL 138, HDL 52 — borderline elevated

Assessment: Stage 2 hypertension, newly diagnosed. No secondary cause identified.
Mild hypertensive retinal changes suggest this is not entirely new.

Plan: Start Amlodipine 5mg QD. DASH diet counseling provided.
Reduce alcohol to <7 drinks/week. Recheck BP in 4 weeks.
If BP not controlled, add second agent. Cardiology referral if resistant."""
    },

    "copd_moderate_exacerbation": {
        "label": "COPD Moderate Exacerbation (Expected: Moderate urgency)",
        "domain": "Pulmonology",
        "urgency_true": "Moderate",
        "word_count": 248,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Harold Jensen, 67M
Visit: COPD exacerbation — 5-day history worsening dyspnea and cough
Vitals: BP 138/86, HR 98 bpm, RR 22/min, Temp 99.2°F, O2 sat 91% on room air

Current Medications:
Tiotropium inhaler 18mcg QD (LAMA)
Salmeterol/Fluticasone 50/250mcg BID (LABA/ICS)
Albuterol MDI PRN (using 4–6x/day currently, up from 1–2x/day baseline)

History: 35 pack-year smoking history, quit 4 years ago.
COPD diagnosed 3 years ago, GOLD Stage II (moderate).
Last exacerbation 8 months ago, treated as outpatient.

Physical Exam:
Chest: Barrel chest, accessory muscle use present
Auscultation: Diffuse expiratory wheezing and prolonged expiratory phase
No crackles, no focal consolidation

Labs:
ABG: pH 7.38, PaCO2 46 mmHg, PaO2 62 mmHg — mild hypoxemia, no hypercapnia
WBC: 11.8 (mild leukocytosis — possible infection)
Sputum: Purulent, sent for culture
CXR: Hyperinflation, no focal consolidation, no pneumothorax

Assessment: Moderate COPD exacerbation. O2 sat borderline, likely infectious
trigger given purulent sputum and low-grade fever. No indication for admission
at this time but requires close monitoring.

Plan: Prednisone 40mg QD x 5 days.
Azithromycin 500mg QD x 5 days pending culture.
Albuterol nebulizer q4h. Supplemental O2 to maintain sat >92%.
Return in 48 hours for reassessment. ER instructions given — return if sat drops
below 88% or breathing worsens significantly."""
    },

    "uti_complicated_elderly": {
        "label": "Complicated UTI — Elderly Female (Expected: Moderate urgency)",
        "domain": "Urology / Internal Medicine",
        "urgency_true": "Moderate",
        "word_count": 219,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Eleanor Thompson, 78F
Visit: Urinary symptoms — 3-day history
Vitals: BP 134/82, HR 92 bpm, Temp 100.1°F (low-grade fever), O2 sat 97%

Chief Complaint: Dysuria, urinary frequency, mild confusion (new for patient).
Caregiver reports patient more disoriented than usual since yesterday.

Current Medications:
Lisinopril 5mg QD, Atorvastatin 20mg QD, Aspirin 81mg QD
Alendronate 70mg weekly

Physical Exam:
General: Alert but mildly confused (unusual per caregiver baseline)
Abdomen: Suprapubic tenderness on palpation
CVA tenderness: Negative bilaterally
No peritoneal signs

Labs:
Urinalysis: WBC 50–100/hpf, RBC 10–25/hpf, Nitrites positive, Leukocyte esterase 3+
Urine culture: Sent — pending
CBC: WBC 13.2 (elevated), neutrophil predominance
CMP: Creatinine 1.1 (baseline 0.9 — mild elevation), BUN 28
Blood cultures: 2 sets sent given confusion and fever

Assessment: Complicated UTI in elderly female with new-onset confusion
and low-grade fever. Blood cultures sent to rule out early urosepsis.
Renal function mildly impacted. Age and confusion elevate risk level.

Plan: IV fluids 500mL bolus. Ceftriaxone 1g IV x1 in office.
Transition to oral Cephalexin 500mg QID x 7 days once culture sensitivity available.
Strict return precautions. If confusion worsens or fever exceeds 101.5°F — ER immediately.
Recheck creatinine in 48 hours. Follow-up in 72 hours."""
    },

    "depression_moderate_new": {
        "label": "New Moderate Depression Diagnosis (Expected: Moderate urgency)",
        "domain": "Psychiatry / Mental Health",
        "urgency_true": "Moderate",
        "word_count": 227,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Christopher Lee, 38M
Visit: Mental health evaluation — referred by PCP for mood concerns

Vitals: BP 122/78, HR 74 bpm, Weight 178 lbs, Temp 98.6°F

Chief Complaint: Persistent low mood, fatigue, loss of interest for 3 months.
Patient reports difficulty concentrating at work, sleeping 10–11 hours/night
but still feeling unrefreshed. Decreased appetite, 8 lb unintentional weight loss.
Denies suicidal ideation, self-harm, or homicidal ideation.
Denies hallucinations or psychotic symptoms.
No prior psychiatric history. No family history of bipolar disorder.
No substance use (alcohol <2 drinks/week, no illicit substances).

PHQ-9 Score: 14 — Moderate depression

Physical Exam: No focal abnormalities. Thyroid non-enlarged.

Labs (to rule out medical causes):
TSH: 2.2 mIU/L — normal (hypothyroid ruled out)
CBC: Normal — no anemia
CMP: Normal
Vitamin B12: 310 pg/mL — low-normal (supplement recommended)
Vitamin D: 18 ng/mL — deficient

Assessment: Major Depressive Disorder, moderate severity (first episode).
No organic medical cause identified. Vitamin D deficiency may be contributing.

Plan: Start Sertraline 50mg QD, increase to 100mg in 2 weeks if tolerated.
Refer to CBT therapist — 8-session course.
Vitamin D 2000 IU QD. B12 supplement.
Safety plan discussed and provided. PHQ-9 repeat in 4 weeks.
Return in 2 weeks to assess medication tolerability."""
    },

    "kidney_stone_recurrent": {
        "label": "Recurrent Kidney Stones (Expected: Moderate urgency)",
        "domain": "Urology / Nephrology",
        "urgency_true": "Moderate",
        "word_count": 235,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Michael Torres, 44M
Visit: Recurrent nephrolithiasis evaluation following second stone episode

Vitals: BP 136/84, HR 78 bpm, Weight 195 lbs, Temp 98.5°F
Pain today: 2/10 (passed stone at home yesterday, confirmed by patient)

History: Second calcium oxalate kidney stone in 18 months.
First stone (14 months ago) required lithotripsy — 7mm.
Current stone passed spontaneously — estimated 3–4mm per CT done in ER 2 days ago.
No current fever, no rigors, urine now clear.

Current Medications:
Tamsulosin 0.4mg QD (started in ER — may discontinue since stone passed)
Ibuprofen 400mg PRN pain (minimal use now)

Labs:
24-hour urine collection results:
Urine oxalate: 52 mg/day (elevated, normal <40 mg/day)
Urine calcium: 285 mg/day (elevated, normal <250 mg/day)
Urine citrate: 420 mg/day (low, normal >550 mg/day)
Urine volume: 1.4L/day (insufficient — target >2.5L/day)
Serum calcium: 9.8 mg/dL — normal
PTH: 42 pg/mL — normal (primary hyperparathyroidism ruled out)

Assessment: Recurrent calcium oxalate nephrolithiasis. Metabolic workup reveals
hypercalciuria, hyperoxaluria, and hypocitraturia — all treatable risk factors.
Inadequate fluid intake is primary driver.

Plan: Increase fluid intake to >3L/day (target urine output >2.5L).
Start Potassium citrate 20mEq BID to increase urine citrate.
Reduce oxalate-rich foods (spinach, nuts, chocolate).
Hydrochlorothiazide 25mg QD for hypercalciuria.
Urology referral for ongoing stone surveillance. Repeat imaging in 6 months."""
    },

    "atrial_fibrillation_stable": {
        "label": "Stable Atrial Fibrillation Follow-up (Expected: Moderate urgency)",
        "domain": "Cardiology",
        "urgency_true": "Moderate",
        "word_count": 241,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Barbara Whitfield, 68F
Visit: Atrial fibrillation management — quarterly follow-up

Vitals: BP 126/78, HR 84 bpm (irregular), Weight 162 lbs, O2 sat 97%

Current Medications:
Apixaban 5mg BID (anticoagulation — CHA2DS2-VASc score 4)
Metoprolol succinate 100mg QD (rate control)
Atorvastatin 40mg QD

History: Paroxysmal AF diagnosed 2 years ago. No prior stroke or TIA.
No current palpitations reported. Patient denies chest pain, presyncope.
Mild exercise intolerance — gets SOB climbing 2 flights of stairs.
Medication adherence: Good. No missed doses of Apixaban in past month.

EKG today: Atrial fibrillation with controlled ventricular response ~85 bpm.
No significant ST or T-wave changes from baseline.

Labs:
INR: N/A (on NOAC not warfarin)
CBC: Normal — no anemia to worsen palpitations
CMP: Normal — creatinine 0.9 (Apixaban dose appropriate for renal function)
TSH: 1.7 mIU/L — normal (hyperthyroidism as AF trigger ruled out)
BNP: 148 pg/mL (mildly elevated — watching for decompensation)

Echocardiogram (6 months ago): EF 55%, mild left atrial dilation, no thrombus

Assessment: Paroxysmal AF with controlled rate on current regimen.
BNP mildly elevated — monitor for development of heart failure symptoms.
Anticoagulation appropriate and adherent.

Plan: Continue all medications unchanged. BNP trending — repeat in 3 months.
If SOB worsens or BNP rises further, consider cardiology referral for
rhythm control strategy. Holter monitor at next visit."""
    },


    # ════════════════════════════════════════════════════════
    # HIGH URGENCY (6 reports) — Needs Urgent Evaluation
    # ════════════════════════════════════════════════════════

    "acute_mi_symptoms": {
        "label": "Acute MI Symptoms — ED Evaluation (Expected: High urgency)",
        "domain": "Cardiology / Emergency Medicine",
        "urgency_true": "High",
        "word_count": 242,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Frank Deluca, 61M
Visit: Emergency Department — chest pain onset 2 hours ago
Vitals: BP 158/96, HR 104 bpm, RR 20/min, Temp 98.8°F, O2 sat 95% on room air

Chief Complaint: Sudden onset severe crushing chest pain, 8/10 intensity.
Radiates to left jaw and left arm. Associated diaphoresis and nausea.
Denies vomiting. No prior similar episodes.

PMH: Hypertension, hyperlipidemia. Father died of MI age 58.
Current Medications: Amlodipine 10mg QD, Atorvastatin 40mg QD
Allergies: Penicillin (rash)

Physical Exam:
General: Diaphoretic, uncomfortable, in visible distress
Cardiovascular: Tachycardic, regular, no murmurs, S4 gallop present
Lungs: Bibasilar crackles (early pulmonary edema)
Extremities: Cool, clammy

EKG: ST elevation 2–3mm in leads II, III, aVF — inferior STEMI pattern
Reciprocal ST depression in I, aVL confirmed.

Labs:
Troponin I: 2.8 ng/mL (markedly elevated — normal <0.04 ng/mL)
CK-MB: 48 U/L (elevated)
BMP: Creatinine 1.1, glucose 186 — mild stress hyperglycemia
CBC: WBC 14.2 — stress response

Assessment: STEMI — inferior wall, acute phase. 
Cardiogenic compromise beginning (S4 gallop, basal crackles).
Time-sensitive emergency — door-to-balloon target 90 minutes.

Actions taken: Aspirin 325mg given, Heparin infusion started.
Cardiology notified — patient being taken to cath lab immediately.
Family notified. Consent obtained for emergent PCI."""
    },

    "stroke_symptoms_acute": {
        "label": "Acute Stroke Symptoms — Time-Critical (Expected: High urgency)",
        "domain": "Neurology / Emergency Medicine",
        "urgency_true": "High",
        "word_count": 228,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Georgina Patel, 74F
Setting: Emergency Department — brought by husband, symptom onset ~90 minutes ago

Vitals: BP 186/104, HR 88 bpm, RR 16/min, O2 sat 97%, Glucose 142 mg/dL

Chief Complaint: Sudden right-sided facial droop and arm weakness noticed by husband.
Patient unable to repeat phrase clearly — mild dysarthria.
Right arm drift on motor exam. Denies headache. No prior TIA history.

PMH: Hypertension, type 2 diabetes, hyperlipidemia, atrial fibrillation
Medications: Metformin 1000mg BID, Lisinopril 20mg QD, Apixaban 5mg BID
Last dose Apixaban: 14 hours ago (morning dose)

Neuro Exam:
NIHSS Score: 7 (moderate stroke)
Right facial droop: Present
Right arm weakness: 3/5 strength
Dysarthria: Mild
Visual fields: No hemianopia
No neglect, no ataxia

Imaging:
CT head (STAT): No hemorrhage identified
CT angiogram: Partial occlusion left MCA — M2 segment
MRI diffusion: Small established infarct (<1/3 MCA territory)

Labs: INR 1.1 (subtherapeutic despite Apixaban — breakthrough event possible)
Platelet count: 218 — normal

Assessment: Acute ischemic stroke, moderate severity. Within thrombolysis window.
Anticoagulant use complicates tPA eligibility — neurology decision pending.
Mechanical thrombectomy being evaluated given CTA findings.

Actions: Neurology called STAT. BP management initiated.
Patient transferred to stroke unit. tPA eligibility discussion in progress."""
    },

    "sepsis_early_signs": {
        "label": "Early Sepsis — Post-Surgical (Expected: High urgency)",
        "domain": "Infectious Disease / Surgery",
        "urgency_true": "High",
        "word_count": 244,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Antonio Reyes, 55M
Visit: Urgent care — 8 days post appendectomy (laparoscopic), worsening since yesterday

Vitals: BP 98/62 (LOW), HR 118 bpm (tachycardic), RR 24/min, Temp 103.4°F (HIGH), O2 sat 94%

Chief Complaint: Increasing abdominal pain, high fever, shaking chills since yesterday.
Not eating or drinking well for 48 hours. Feeling confused this morning per wife.
Incision site: Two port sites appear erythematous, one has purulent discharge.

Physical Exam:
General: Acutely ill appearing, flushed, diaphoretic
Abdomen: Diffuse tenderness, worse in RLQ and periumbilical regions
Peritoneal signs: Guarding and rebound tenderness present
Wound: Port site #2 — erythema 4cm surrounding, purulent discharge expressed
Mental status: Mildly confused, disoriented to date

SIRS Criteria Met: Temp >103°F, HR >118, RR >24, WBC elevated (3 of 4 met)

Labs:
WBC: 19.4 with 92% neutrophils and 18% bands (left shift — severe infection)
Lactate: 3.8 mmol/L (elevated — tissue hypoperfusion)
Creatinine: 1.8 (up from baseline 1.0 — acute kidney injury)
Blood cultures: 2 sets drawn — pending
CRP: 284 mg/L (markedly elevated)
CT abdomen/pelvis: Pelvic fluid collection, possible abscess — radiology read pending

Assessment: Sepsis with possible septic shock developing. Post-operative
complication — likely intra-abdominal abscess and wound infection.
Lactate elevation and hypotension indicate need for immediate intervention.

Actions: IV access x2, aggressive fluid resuscitation 30mL/kg.
Broad-spectrum antibiotics started (Piperacillin-tazobactam + Vancomycin).
General surgery and ICU notified. Transfer to hospital via EMS arranged."""
    },

    "pulmonary_embolism": {
        "label": "Suspected Pulmonary Embolism (Expected: High urgency)",
        "domain": "Pulmonology / Emergency Medicine",
        "urgency_true": "High",
        "word_count": 237,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Stephanie Chen, 42F
Setting: Urgent care clinic — referred immediately to ED after evaluation

Vitals: BP 108/68, HR 116 bpm, RR 26/min, O2 sat 88% on room air, Temp 99.0°F

Chief Complaint: Acute onset right-sided pleuritic chest pain and shortness of breath
beginning 6 hours ago. Worsened with deep breathing. Right calf swelling x 3 days
(ignored, attributed to long flight 10 days ago — 14-hour flight from Hong Kong).

PMH: Oral contraceptive pill use (Ethinyl estradiol), no prior clot history.
No current medications other than OCP. No known clotting disorders.

Risk Factors: Recent prolonged immobilization (14-hour flight), OCP use,
mild obesity (BMI 29.2) — Wells Score 7.5 (HIGH probability PE)

Physical Exam:
Respiratory: Tachypneic, splinting right side, decreased breath sounds right base
Cardiovascular: Tachycardic, no murmur, JVD present (elevated)
Right calf: Erythema, warmth, tenderness, calf circumference 3.5cm larger than left
No calf Homan sign (unreliable, not used for diagnosis)

Labs:
D-dimer: 4,820 ng/mL (markedly elevated — normal <500 ng/mL)
ABG: PaO2 58 mmHg, PaCO2 30 mmHg — hypoxemia with hypocapnia
Troponin: 0.18 ng/mL (mildly elevated — right heart strain)
BNP: 340 pg/mL (elevated — right ventricular stress)
EKG: Sinus tachycardia, S1Q3T3 pattern — classic PE pattern

CT Pulmonary Angiogram: STAT ordered — bilateral PE with right heart strain

Assessment: High-probability massive/submassive pulmonary embolism.
Hemodynamically borderline. OCP discontinued immediately.

Actions: O2 supplementation started. IV heparin infusion initiated.
Vascular surgery and pulmonology notified. ICU monitoring arranged."""
    },

    "diabetic_ketoacidosis": {
        "label": "Diabetic Ketoacidosis — Type 1 (Expected: High urgency)",
        "domain": "Endocrinology / Emergency Medicine",
        "urgency_true": "High",
        "word_count": 231,
        "has_lab_values": True,
        "has_medications": True,
        "text": """Patient: Tyler Johnson, 19M
Setting: Emergency Department — brought by roommate

Vitals: BP 102/64 (low), HR 126 bpm, RR 28/min (Kussmaul breathing), Temp 99.6°F
O2 sat 97%, Weight 148 lbs

Chief Complaint: Nausea, vomiting x 48 hours, abdominal pain, altered consciousness.
Roommate reports patient has Type 1 diabetes and ran out of insulin 3 days ago.
Decreased urine output today. Last ate 2 days ago. Strong fruity breath noted.

Current Medications (missed x 3 days): Insulin glargine 22 units QHS, Insulin lispro PRN meals

Physical Exam:
General: Lethargic, responding to voice only, dry mucous membranes
Skin: Poor turgor, dry, flushed
Abdomen: Diffuse tenderness without guarding (pseudo-peritoneum of DKA)
Kussmaul respirations: Present (deep, rapid breathing — respiratory compensation)

Labs:
Glucose: 524 mg/dL (critically elevated)
Venous pH: 7.18 (severe acidosis)
Bicarbonate: 8 mEq/L (critically low, normal 22–29)
Anion gap: 28 mEq/L (elevated — high AG acidosis)
Serum ketones: Large positive (4+)
Beta-hydroxybutyrate: 8.2 mmol/L (markedly elevated)
Potassium: 5.8 mEq/L (appears high — will drop with insulin treatment)
Creatinine: 2.4 mg/dL (acute kidney injury from dehydration)
WBC: 18.6 (stress response — check for precipitating infection)

Assessment: Severe diabetic ketoacidosis with significant dehydration,
acute kidney injury, and altered consciousness. Life-threatening emergency.

Actions: 2 large-bore IVs placed. 1L NS bolus given. Insulin infusion started.
Potassium replacement protocol initiated. Endocrinology notified STAT.
ICU admission arranged. Foley placed for strict I&O monitoring."""
    },

    "acute_appendicitis": {
        "label": "Acute Appendicitis — Surgical Abdomen (Expected: High urgency)",
        "domain": "General Surgery / Emergency Medicine",
        "urgency_true": "High",
        "word_count": 226,
        "has_lab_values": True,
        "has_medications": False,
        "text": """Patient: Nicole Brown, 24F
Setting: Emergency Department — acute abdominal pain

Vitals: BP 118/74, HR 102 bpm, Temp 100.8°F, O2 sat 99%
Pain score: 9/10

Chief Complaint: Severe right lower quadrant abdominal pain, onset 18 hours ago.
Initially periumbilical, now migrated to RLQ (classic appendicitis migration).
Associated nausea and 1 episode vomiting. No diarrhea. Last menstrual period 2 weeks ago.
Anorexia since symptom onset — unable to eat anything today.

Physical Exam:
Abdomen:
McBurney's point: Maximum tenderness at McBurney's point — RLQ
Rovsing sign: Positive (RLQ pain with LLQ palpation)
Psoas sign: Positive (pain with right hip extension)
Obturator sign: Equivocal
Guarding: Voluntary guarding present in RLQ
Rebound tenderness: Positive

Pelvic exam: No cervical motion tenderness, no adnexal mass
Urine beta-hCG: Negative (ectopic pregnancy ruled out)

Labs:
WBC: 15.8 with left shift (bands 12%)
CRP: 142 mg/L (elevated)
Urinalysis: Normal — no pyuria (UTI ruled out)
Appendix ultrasound: Non-visualized — CT ordered

CT abdomen/pelvis with contrast: Dilated appendix 9mm diameter,
periappendiceal fat stranding, no free perforation identified.
Alvarado Score: 9/10

Assessment: Acute appendicitis, non-perforated based on CT findings.
Surgical emergency — standard of care is appendectomy within 6–12 hours.

Actions: NPO immediately. IV antibiotics (Cefoxitin) started.
IV morphine 4mg for pain control. General surgery notified — OR arranged.
Consent for laparoscopic appendectomy obtained."""
    },

}

# ════════════════════════════════════════════════════════
# Data Dictionary
# ════════════════════════════════════════════════════════

DATA_DICTIONARY = {
    "report_id":        "Unique identifier for each report (string key)",
    "label":            "Human-readable description including expected urgency",
    "domain":           "Medical specialty / clinical domain",
    "urgency_true":     "Ground truth urgency label: Low / Moderate / High",
    "word_count":       "Approximate word count of report text",
    "has_lab_values":   "Boolean — whether report contains quantitative lab results",
    "has_medications":  "Boolean — whether report lists medications",
    "text":             "Full synthetic medical report text",
}

# ════════════════════════════════════════════════════════
# Dataset Summary
# ════════════════════════════════════════════════════════

print("=" * 65)
print("SYNTHETIC MEDICAL REPORT DATASET — SUMMARY")
print("=" * 65)
print(f"\nTotal reports:    {len(REPORTS)}")

urgency_counts = {}
domain_list = []
for r in REPORTS.values():
    u = r["urgency_true"]
    urgency_counts[u] = urgency_counts.get(u, 0) + 1
    domain_list.append(r["domain"])

print(f"\nUrgency Distribution:")
for label, count in sorted(urgency_counts.items()):
    bar = "█" * count
    print(f"  {label:10} {bar} ({count} reports)")

print(f"\nClinical Domains Covered ({len(set(domain_list))} unique):")
for d in sorted(set(domain_list)):
    print(f"  - {d}")

print(f"\nData Dictionary:")
for col, desc in DATA_DICTIONARY.items():
    print(f"  {col:25} {desc}")

print("\n⚠️  ETHICS NOTE: All patients, names, and clinical data")
print("   are entirely FICTIONAL. For research/education only.")
print("=" * 65)
