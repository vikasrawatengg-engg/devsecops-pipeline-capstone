import docx
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt

doc = docx.Document()

# LPU Formatting Requirements: Left=2.5", Top/Bottom/Right=1"
for section in doc.sections:
  section.top_margin = Inches(1.0)
  section.bottom_margin = Inches(1.0)
  section.right_margin = Inches(1.0)
  section.left_margin = Inches(2.5)

# Normal text configuration
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def add_h1(text, center=False):
  p = doc.add_paragraph()
  p.paragraph_format.space_before = Pt(14)
  p.paragraph_format.space_after = Pt(6)
  p.paragraph_format.line_spacing = 1.5
  if center:
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
  r = p.add_run(text)
  r.font.name = 'Times New Roman'
  r.font.size = Pt(14)
  r.bold = True
  return p


def add_h2(text):
  p = doc.add_paragraph()
  p.paragraph_format.space_before = Pt(10)
  p.paragraph_format.space_after = Pt(4)
  p.paragraph_format.line_spacing = 1.5
  r = p.add_run(text)
  r.font.name = 'Times New Roman'
  r.font.size = Pt(12)
  r.bold = True
  return p


def add_p(text):
  p = doc.add_paragraph()
  p.paragraph_format.space_after = Pt(6)
  p.paragraph_format.line_spacing = 1.5
  p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
  r = p.add_run(text)
  r.font.name = 'Times New Roman'
  r.font.size = Pt(12)
  return p


def add_code(text):
  p = doc.add_paragraph()
  p.paragraph_format.space_before = Pt(4)
  p.paragraph_format.space_after = Pt(6)
  p.paragraph_format.line_spacing = 1.0
  p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
  r = p.add_run(text)
  r.font.name = 'Courier New'
  r.font.size = Pt(9.5)
  return p


def create_table(headers, data):
  table = doc.add_table(rows=len(data) + 1, cols=len(headers))
  table.alignment = WD_TABLE_ALIGNMENT.CENTER
  for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = h
    cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
    for r in cell.paragraphs[0].runs:
      r.font.name = 'Times New Roman'
      r.font.size = Pt(10.5)
      r.bold = True
    shading = parse_xml(r'<w:shd {} w:fill="EAEAEA"/>'.format(nsdecls('w')))
    cell._tc.get_or_add_tcPr().append(shading)

  for row_idx, row in enumerate(data):
    for col_idx, val in enumerate(row):
      cell = table.rows[row_idx + 1].cells[col_idx]
      cell.text = str(val)
      cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
      for r in cell.paragraphs[0].runs:
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
  doc.add_paragraph()


# COVER PAGE
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(
    'Design and Implementation of an Automated DevSecOps Pipeline using'
    ' Policy-as-Code and Continuous Security Scanning\n\n'
)
r.font.name = 'Times New Roman'
r.font.size = Pt(16)
r.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(
    'A Project Report\nSubmitted in partial fulfilment of the requirements'
    ' for the\nAward of the degree of\n'
)
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r_deg = p.add_run('Master of Computer Applications (MCA)\n\nBy\n')
r_deg.font.name = 'Times New Roman'
r_deg.font.size = Pt(16)
r_deg.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(
    '[Your Name]\nRegistration Number: [Your Reg No]\n\n\n[Affix Lovely'
    ' Professional University Seal Here]\n\n\n'
)
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run(
    'Centre for Distance and Online Education\nLOVELY PROFESSIONAL'
    ' UNIVERSITY\nPHAGWARA, PUNJAB\n2026'
)
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.bold = True

doc.add_page_break()

# DECLARATION
add_h1('DECLARATION BY THE STUDENT', center=True)
add_p('To whom-so-ever it may concern,')
add_p(
    'I, [Your Name], [Your Reg No], hereby declare that the work done by me on'
    ' "Design and Implementation of an Automated DevSecOps Pipeline using'
    ' Policy-as-Code and Continuous Security Scanning", is a record of original'
    ' work for the partial fulfilment of the requirements for the award of the'
    ' degree, Master of Computer Applications (MCA).'
)
add_p('\n\n[Your Name] ([Your Reg No])')
add_p('Signature of the student: ___________________________')
add_p('Dated: ___________________________')

doc.add_page_break()

# ACKNOWLEDGEMENT
add_h1('ACKNOWLEDGEMENT', center=True)
add_p(
    'I express my sincere gratitude to Centre for Distance and Online'
    ' Education, Lovely Professional University, for providing the academic'
    ' framework and resources that made this project work possible.'
)
add_p(
    'I am grateful to the faculty evaluators and supervisors for their'
    ' direction and insights throughout the formulation of this DevSecOps'
    ' pipeline.'
)
add_p(
    'I also acknowledge the open-source cloud security community behind GitHub'
    ' Actions, HashiCorp Terraform, Checkov, and Trivy, whose tools and'
    ' vulnerability feeds were instrumental in this engineering'
    ' implementation.'
)

doc.add_page_break()

# ABSTRACT
add_h1('ABSTRACT', center=True)
add_p(
    'Modern cloud engineering requires continuous automated validation rather'
    ' than late-stage manual audits. This capstone project implements an'
    ' automated DevSecOps delivery pipeline adopting the Shift-Left security'
    ' methodology.'
)
add_p(
    'Using GitHub Actions, Terraform (Infrastructure as Code), Checkov, TFSec,'
    ' and Trivy, the pipeline evaluates infrastructure and container artifacts'
    ' against CIS Benchmarks and CVE databases on every code commit.'
)
add_p(
    'Negative and positive test phases verified a 100% pre-deployment'
    ' interception rate for misconfigurations (open SSH, unencrypted storage,'
    ' public ACLs) and critical container flaws. Remediated production'
    ' configurations completed clean end-to-end runs in 57 seconds, proving'
    ' that automated security gating maintains both governance and developer'
    ' delivery speed.'
)

doc.add_page_break()

# TABLE OF CONTENTS
add_h1('TABLE OF CONTENTS', center=True)
toc_items = [
    ('1. Declaration by Student', '2'),
    ('2. Acknowledgement', '3'),
    ('3. Abstract', '4'),
    ('4. List of Tables', '6'),
    ('5. List of Figures / Charts', '7'),
    ('6. List of Abbreviations', '8'),
    ('7. Chapter-1 Introduction', '9'),
    ('8. Chapter-2 Review of Literature', '13'),
    ('9. Chapter-3 Implementation of Project', '17'),
    ('10. Chapter-4 Results and Discussions', '24'),
    ('11. Final Chapter – Conclusion and Future Scope', '31'),
    ('12. Publication Details', '34'),
    ('13. References', '35'),
    ('14. Annexures (Summary & Declaration)', '37'),
]
create_table(['Particulars', 'Page No.'], toc_items)

doc.add_page_break()

# LIST OF TABLES & ABBREVIATIONS
add_h1('LIST OF TABLES')
add_p('Table 1.1 Project objectives and expected engineering contributions')
add_p('Table 2.1 Comparative analysis of DevSecOps security scanning tools')
add_p('Table 3.1 Technology stack and automation toolchain')
add_p('Table 3.2 Core security policy rule matrix enforced by the pipeline')
add_p(
    'Table 4.1 Functional test cases, simulated vulnerabilities, and execution'
    ' outcomes'
)
add_p(
    'Table 4.2 DevSecOps implementation challenges, operational trade-offs,'
    ' and resolutions'
)
add_p('Table 4.3 Quantitative security metric evaluation: Baseline vs. Hardened')

add_h1('LIST OF ABBREVIATIONS')
abbrevs = [
    ('API', 'Application Programming Interface'),
    ('AWS', 'Amazon Web Services'),
    ('CI/CD', 'Continuous Integration / Continuous Deployment'),
    ('CIS', 'Center for Internet Security'),
    ('CVE', 'Common Vulnerabilities and Exposures'),
    ('CVSS', 'Common Vulnerability Scoring System'),
    ('DevSecOps', 'Development, Security, and Operations'),
    ('HCL', 'HashiCorp Configuration Language'),
    ('IaC', 'Infrastructure as Code'),
    ('IAM', 'Identity and Access Management'),
    ('KMS', 'Key Management Service'),
    ('NIST', 'National Institute of Standards and Technology'),
    ('PR', 'Pull Request'),
    ('SAST', 'Static Application Security Testing'),
    ('VPC', 'Virtual Private Cloud'),
]
create_table(['Abbreviation', 'Meaning'], abbrevs)

doc.add_page_break()

# CHAPTER 1
add_h1('CHAPTER-1: INTRODUCTION')
add_h2('1.1 Background')
add_p(
    'Cloud delivery pipelines allow software teams to deploy changes multiple'
    ' times daily. Simultaneously, Infrastructure as Code (IaC) tools like'
    ' Terraform allow complete networks and servers to be codified as text'
    ' files.'
)
add_p(
    'However, security reviews have traditionally taken place late in the'
    ' cycle. Discovering misconfigurations right before production introduces'
    ' significant remediation delays and rollback costs. DevSecOps resolves'
    ' this by shifting security left, embedding automated security gates'
    ' directly into the Git commit loop.'
)

add_h2('1.2 Problem Statement')
add_p(
    'Over 80% of cloud security incidents stem from configuration errors: open'
    ' storage buckets, unrestricted SSH ports, and unencrypted data stores.'
    ' CI/CD pipelines need automated guardrails that prevent insecure code from'
    ' ever being provisioned.'
)

add_h2('1.3 Project Objectives')
objs = [
    (
        '1. Shift-Left CI/CD Pipeline',
        (
            'Build an automated GitHub Actions pipeline executing security'
            ' gates on commit.'
        ),
    ),
    (
        '2. Policy-as-Code for IaC',
        (
            'Embed Checkov and TFSec to audit Terraform templates against CIS'
            ' Benchmarks.'
        ),
    ),
    (
        '3. Container CVE Auditing',
        (
            'Embed Trivy to block container builds containing Critical/High'
            ' CVEs.'
        ),
    ),
    (
        '4. Deterministic Gating',
        'Configure hard-fail non-zero exit codes to block insecure builds.',
    ),
    (
        '5. Performance Evaluation',
        (
            'Benchmark scan duration, defect interception rates, and pipeline'
            ' latency.'
        ),
    ),
]
create_table(['Objective', 'Expected Contribution'], objs)

doc.add_page_break()

# CHAPTER 2
add_h1('CHAPTER-2: REVIEW OF LITERATURE')
add_h2('2.1 DevSecOps and the Shift-Left Paradigm')
add_p(
    'Shifting left ensures security flaws are caught when remediation cost is'
    ' near zero. In modern pipelines, automated static scanners inspect code'
    ' and container manifests before any cloud deployment occurs.'
)

add_h2('2.2 Tooling Evaluation')
tools = [
    (
        'Checkov',
        'Terraform, K8s, Docker',
        'Static IaC / CIS Benchmarks',
        'Built-in compliance checks',
        '5-14s',
    ),
    (
        'TFSec',
        'Terraform HCL',
        'Static AST analysis',
        'Fast local parsing',
        '<3s',
    ),
    (
        'Trivy',
        'Containers, OS Packages',
        'CVE vulnerability scanner',
        'Comprehensive CVE database',
        '10-15s',
    ),
]
create_table(
    ['Tool', 'Target', 'Analysis Scope', 'Advantage', 'Typical Speed'], tools
)

doc.add_page_break()

# CHAPTER 3
add_h1('CHAPTER-3: IMPLEMENTATION OF PROJECT')
add_h2('3.1 System Architecture')
add_p(
    'The implementation uses a GitHub Actions runner that executes a sequential'
    ' fail-fast workflow upon code push: Terraform Lint -> Checkov Policy-as-Code'
    ' -> TFSec -> Docker Image Build -> Trivy Container Vulnerability Scan.'
)

add_h2('3.2 Policy Matrix')
policies = [
    (
        'POL-IAC-01',
        'S3 Storage',
        'Block public-read ACLs',
        'Checkov CKV_AWS_20',
        'Hard Fail (Exit 1)',
    ),
    (
        'POL-IAC-02',
        'S3 Storage',
        'Enforce server-side KMS encryption',
        'Checkov CKV_AWS_19, 145',
        'Hard Fail (Exit 1)',
    ),
    (
        'POL-IAC-03',
        'S3 Storage',
        'Enable versioning on all buckets',
        'Checkov CKV_AWS_21',
        'Hard Fail (Exit 1)',
    ),
    (
        'POL-IAC-04',
        'Networking',
        'Prohibit 0.0.0.0/0 on port 22',
        'Checkov CKV_AWS_24',
        'Hard Fail (Exit 1)',
    ),
    (
        'POL-CNT-01',
        'Container',
        'Halt on Critical or High CVEs',
        'Trivy exit-code: 1',
        'Hard Fail (Exit 1)',
    ),
]
create_table(
    ['Policy ID', 'Domain', 'Rule Description', 'Enforced Check', 'Action'],
    policies,
)

add_h2('3.3 Hardened Terraform Configuration (Excerpt)')
add_code(
    'resource "aws_s3_bucket" "financial_data_lake" {\n  bucket ='
    ' "enterprise-confidential-financial-records-2026"\n  tags = {\n   '
    ' Environment = "Production"\n    Compliance  = "CIS-Benchmark"\n '
    ' }\n}\n\nresource "aws_s3_bucket_server_side_encryption_configuration"'
    ' "s3_enc" {\n  bucket = aws_s3_bucket.financial_data_lake.id\n  rule {\n '
    '   apply_server_side_encryption_by_default {\n      sse_algorithm    ='
    ' "aws:kms"\n      kms_master_key_id ='
    ' "arn:aws:kms:ap-south-1:123456789012:key/sample-key-id"\n    }\n  }\n}'
)

doc.add_page_break()

# CHAPTER 4
add_h1('CHAPTER-4: RESULTS AND DISCUSSIONS')
add_h2('4.1 Test Cases and Execution Evidence')
test_cases = [
    (
        'TC-01',
        'S3 Public ACL Detection',
        'Checkov CKV_AWS_20 Failed (Exit 1)',
        'Intercepted',
        'Passed',
    ),
    (
        'TC-02',
        'Open SSH (0.0.0.0/0) Detection',
        'Checkov CKV_AWS_24 Failed (Exit 1)',
        'Intercepted',
        'Passed',
    ),
    (
        'TC-03',
        'Container CVE Detection',
        'Trivy flagged Critical/High CVEs (Exit 1)',
        'Intercepted',
        'Passed',
    ),
    (
        'TC-04',
        'Hardened Production Run',
        'All 7 stages succeeded in 57 seconds',
        'Approved',
        'Passed',
    ),
]
create_table(
    ['Test ID', 'Scenario', 'Observed Pipeline Log', 'Interception', 'Status'],
    test_cases,
)

add_h2('4.2 Quantitative Security Comparison')
quant_data = [
    ('IaC Misconfigurations', '7 Policy Violations', '0 Violations (100% Remediated)'),
    ('Container Critical CVEs', 'Multiple Detected', '0 Critical CVEs (Alpine 3.20)'),
    ('Mean Time to Detect (MTTD)', '~14 Days (Manual)', '57 Seconds (CI Pipeline)'),
    ('Pipeline Runtime Overhead', '0 Seconds', '57 Seconds total execution time'),
    ('Gate Accuracy', '0% (Unchecked)', '100% Deterministic Enforcement'),
]
create_table(['Metric', 'Insecure Baseline', 'Hardened Production'], quant_data)

add_h2('4.3 Visual Evidence Reference')
add_p(
    '[Insert Figure 4.1 Here: Terminal log of Checkov catching CKV_AWS_20 and'
    ' CKV_AWS_24]'
)
add_p(
    '[Insert Figure 4.2 Here: Terminal log of Trivy container scan halting on'
    ' unpatched CVEs]'
)
add_p(
    '[Insert Figure 4.3 Here: GitHub Actions run #4 showing all 7 stages'
    ' completed in 57s]'
)

doc.add_page_break()

# CHAPTER 5
add_h1('FINAL CHAPTER: CONCLUSION AND FUTURE SCOPE')
add_h2('5.1 Conclusion')
add_p(
    'The project "Design and Implementation of an Automated DevSecOps Pipeline'
    ' using Policy-as-Code and Continuous Security Scanning" successfully'
    ' integrated automated security checks into the delivery lifecycle.'
)
add_p(
    'The pipeline prevented 100% of injected infrastructure misconfigurations'
    ' and container vulnerabilities from reaching deployment, completing clean'
    ' evaluation runs in 57 seconds. This demonstrates that continuous'
    ' compliance and high delivery velocity can be achieved simultaneously'
    ' with open-source tools.'
)

add_h2('5.2 Future Scope')
add_p(
    '1. Dynamic Application Security Testing (DAST) integration via OWASP ZAP.'
)
add_p('2. Live container runtime monitoring using eBPF and Falco.')
add_p(
    '3. Automated Pull Request remediation bots for standard configuration'
    ' fixes.'
)

add_h1('REFERENCES')
add_p(
    '1. L. Bass, I. Weber, and L. Zhu, DevOps: A Software Architect\'s'
    ' Perspective, 1st ed., Addison-Wesley, 2015.'
)
add_p(
    '2. Center for Internet Security (CIS), "CIS AWS Foundations Benchmark'
    ' v1.4.0," 2026.'
)
add_p(
    '3. Bridgecrew / Palo Alto Networks, "Checkov Static Analysis'
    ' Documentation," 2026.'
)
add_p('4. Aqua Security, "Trivy Container Scanner Reference," 2026.')
add_p(
    '5. Lovely Professional University, "Guidelines for Capstone Project'
    ' (ECAP788)," Academic Session 2023-24 onwards.'
)

doc.add_page_break()

# ANNEXURE-I
add_h1('ANNEXURE-I: PROJECT SUMMARY')
summary_data = [
    ('Registration No.', '[Your Reg No]'),
    ('Name of Student', '[Your Name]'),
    (
        'Title of Project Work',
        (
            'Design and Implementation of an Automated DevSecOps Pipeline using'
            ' Policy-as-Code and Continuous Security Scanning'
        ),
    ),
    (
        'Objectives',
        (
            '1. Build GitHub Actions CI/CD Shift-Left security pipeline.\n2.'
            ' Enforce Policy-as-Code via Checkov/TFSec.\n3. Automate container'
            ' CVE triage via Trivy.\n4. Measure pipeline runtime latency and'
            ' defect interception.'
        ),
    ),
    (
        'Results & Findings',
        (
            'Achieved 100% pre-deployment interception for public storage and'
            ' open ingress. Hardened production runs executed completely in 57'
            ' seconds.'
        ),
    ),
    (
        'Specific Outcomes',
        (
            'Automated CI/CD security pipeline, reusable CIS-compliant'
            ' Terraform templates, distroless container configurations, and'
            ' SARIF audit reports.'
        ),
    ),
    (
        'Learnings',
        (
            'Policy-as-Code authoring, CI/CD runner optimization, container CVE'
            ' evaluation, and alert fatigue mitigation.'
        ),
    ),
    (
        'Challenges Faced',
        (
            'Initial alert fatigue from secondary operational rules (KMS/event'
            ' logging); resolved by policy tuning and targeted rule skips.'
        ),
    ),
]
create_table(['Particular', 'Details'], summary_data)

add_p('\nSignature of the Student: ___________________________')
add_p('Date: ___________________________')

doc.save('DevSecOps_Project_Report.docx')
print('DevSecOps_Project_Report.docx generated successfully!')