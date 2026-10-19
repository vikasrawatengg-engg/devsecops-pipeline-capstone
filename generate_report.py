import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Formatting: Left Margin = 2.5", Others = 1.0"
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.left_margin = Inches(2.5)

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
r = p.add_run("Design and Implementation of an Automated DevSecOps Pipeline using Policy-as-Code and Continuous Security Scanning\n\n")
r.font.name = 'Times New Roman'
r.font.size = Pt(16)
r.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("A Project Report\nSubmitted in partial fulfilment of the requirements for the\nAward of the degree of\n")
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r_deg = p.add_run("Master of Computer Applications (MCA)\n\nBy\n")
r_deg.font.name = 'Times New Roman'
r_deg.font.size = Pt(16)
r_deg.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("VIKAS RAWAT\nRegistration Number: 324200509\n\n\n[Affix Lovely Professional University Seal Here]\n\n\n")
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.bold = True

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Centre for Distance and Online Education\nLOVELY PROFESSIONAL UNIVERSITY\nPHAGWARA, PUNJAB\n2026")
r.font.name = 'Times New Roman'
r.font.size = Pt(14)
r.bold = True

doc.add_page_break()

# DECLARATION
add_h1("DECLARATION BY THE STUDENT", center=True)
add_p("To whom-so-ever it may concern,")
add_p("I, Vikas Rawat, Registration Number 324200509, hereby declare that the work done by me on 'Design and Implementation of an Automated DevSecOps Pipeline using Policy-as-Code and Continuous Security Scanning', is a record of original work for the partial fulfilment of the requirements for the award of the degree, Master of Computer Applications (MCA).")
add_p("I certify that this project work has not formed the basis for the award of any other Degree or Diploma, and conforms strictly to the academic integrity policies of Lovely Professional University.")
add_p("\n\nVikas Rawat (324200509)")
add_p("Signature of the student: ___________________________")
add_p("Dated: October 19, 2026")

doc.add_page_break()

# ACKNOWLEDGEMENT
add_h1("ACKNOWLEDGEMENT", center=True)
add_p("I express my sincere gratitude to the Centre for Distance and Online Education, Lovely Professional University, for providing the academic infrastructure and research methodology required to execute this capstone engineering work.")
add_p("I extend my deepest appreciation to the project mentors, course supervisors, and academic evaluators for their continuous review and structured feedback during the design of this DevSecOps policy-as-code automation framework.")
add_p("I also acknowledge the open-source engineering teams maintaining HashiCorp Terraform, GitHub Actions, Checkov (Palo Alto Networks), and Aqua Security Trivy, whose tools and security vulnerability databases enabled the concrete implementation of this research.")

doc.add_page_break()

# ABSTRACT
add_h1("ABSTRACT", center=True)
add_p("Traditional software deployment pipelines prioritize deployment velocity over comprehensive security checks, deferring static analysis and compliance auditing to manual post-provisioning audits. This latency increases organizational exposure to credential leakages, open network ports, and vulnerable container runtime environments. This capstone project designs and deploys a deterministic, automated DevSecOps delivery pipeline operating under the Shift-Left architectural paradigm.")
add_p("Using GitHub Actions, Terraform (Infrastructure-as-Code), Checkov (Policy-as-Code), TFSec, and Aqua Security Trivy, the pipeline evaluates infrastructure and container artifacts against Center for Internet Security (CIS) Benchmarks and National Vulnerability Database CVE registries directly upon code commit. The implementation employs an automated two-stage workflow comprising shift-left static validation followed by idempotent, state-reconciled AWS cloud provisioning.")
add_p("Experimental verification demonstrates a 100% pre-deployment interception rate for simulated high-risk misconfigurations (public storage ACLs, unrestricted SSH ingress, and unencrypted block storage) while eliminating pipeline execution duplicates. The remediated production release achieves a green gate execution latency of 57 seconds and cleanly provisions a personalized AWS demonstration web server in the ap-south-1 region.")

doc.add_page_break()

# TABLE OF CONTENTS
add_h1("TABLE OF CONTENTS", center=True)
toc_items = [
    ("1. Declaration by Student", "2"),
    ("2. Acknowledgement", "3"),
    ("3. Abstract", "4"),
    ("4. List of Tables", "6"),
    ("5. List of Figures / Charts", "7"),
    ("6. List of Abbreviations", "8"),
    ("7. Chapter-1 Introduction", "9"),
    ("8. Chapter-2 Review of Literature", "13"),
    ("9. Chapter-3 Implementation of Project", "17"),
    ("10. Chapter-4 Results and Discussions", "25"),
    ("11. Final Chapter – Conclusion and Future Scope", "32"),
    ("12. References", "35"),
    ("13. Annexure-I: Project Summary Sheet", "37")
]
create_table(["Particulars", "Page No."], toc_items)

doc.add_page_break()

# LIST OF TABLES & ABBREVIATIONS
add_h1("LIST OF TABLES")
add_p("Table 1.1 Project objectives and technical contributions")
add_p("Table 2.1 Comparative analysis of Shift-Left security auditing engines")
add_p("Table 3.1 Implemented software and cloud engineering stack")
add_p("Table 3.2 Policy-as-Code rule validation and enforcement matrix")
add_p("Table 4.1 Functional testing and security gate interception results")
add_p("Table 4.2 Quantitative performance evaluation: Baseline vs. Hardened pipeline")

add_h1("LIST OF ABBREVIATIONS")
abbrevs = [
    ("AMI", "Amazon Machine Image"),
    ("AWS", "Amazon Web Services"),
    ("CI/CD", "Continuous Integration / Continuous Deployment"),
    ("CIS", "Center for Internet Security"),
    ("CVE", "Common Vulnerabilities and Exposures"),
    ("CVSS", "Common Vulnerability Scoring System"),
    ("DevSecOps", "Development, Security, and Operations"),
    ("EBS", "Elastic Block Store"),
    ("EC2", "Elastic Compute Cloud"),
    ("HCL", "HashiCorp Configuration Language"),
    ("IaC", "Infrastructure as Code"),
    ("IAM", "Identity and Access Management"),
    ("KMS", "Key Management Service"),
    ("SAST", "Static Application Security Testing"),
    ("VPC", "Virtual Private Cloud")
]
create_table(["Abbreviation", "Meaning"], abbrevs)

doc.add_page_break()

# CHAPTER 1
add_h1("CHAPTER-1: INTRODUCTION")
add_h2("1.1 Background and Context")
add_p("Cloud infrastructure management has transitioned from manual server configuration to codified, automated provisioning through Infrastructure as Code (IaC). Declarative frameworks like HashiCorp Terraform allow engineering teams to define virtual private clouds, access control lists, block devices, and compute clusters using version-controlled text files.")
add_p("While IaC enhances delivery speed, it replicates misconfigurations instantly across enterprise cloud environments. Traditional IT workflows handle security reviews via asynchronous audits right before production cutover. The DevSecOps methodology mitigates this operational barrier by shifting security audits left—validating configurations and container layers within continuous integration runners before deployment.")

add_h2("1.2 Problem Statement")
add_p("Modern cloud security incidents frequently originate from simple infrastructure misconfigurations: unencrypted storage volumes, world-accessible SSH (Port 22) management ingress, and container base images containing known CVE vulnerabilities. To resolve this, continuous deployment pipelines require deterministic security gates that halt provisioning immediately when defined security thresholds are breached.")

add_h2("1.3 Project Objectives")
objs = [
    ("Objective 1", "Architect a multi-stage GitHub Actions CI/CD pipeline enforcing strict shift-left validation."),
    ("Objective 2", "Implement Policy-as-Code via Checkov and TFSec to audit Terraform against CIS Benchmarks."),
    ("Objective 3", "Integrate Aqua Security Trivy container auditing to intercept High and Critical CVE vulnerabilities."),
    ("Objective 4", "Enforce idempotent, single-resource AWS cloud provisioning with S3 remote state tracking."),
    ("Objective 5", "Measure pipeline interception accuracy, gate execution overhead, and Mean Time to Detect (MTTD).")
]
create_table(["Identifier", "Description"], objs)

doc.add_page_break()

# CHAPTER 2
add_h1("CHAPTER-2: REVIEW OF LITERATURE")
add_h2("2.1 Shift-Left Security in Modern Delivery Systems")
add_p("Academic and industrial consensus emphasizes that the cost to remediate defects escalates exponentially as software moves through development, testing, staging, and production. Introducing automated static analysis during the Git pull-request phase reduces defect resolution costs close to zero while eliminating human auditor bottlenecks.")

add_h2("2.2 Comparative Tooling Evaluation")
comp_tools = [
    ("Checkov", "Terraform, CloudFormation, Docker", "Graph-based CIS Benchmark Policy-as-Code", "5-14s", "Hard fail on CIS violations"),
    ("TFSec", "Terraform HCL", "Abstract Syntax Tree (AST) static parser", "<3s", "Rapid pre-flight linting"),
    ("Trivy", "Container Images, OS packages", "Comprehensive CVE database lookup", "8-15s", "Deterministic vulnerability blocking")
]
create_table(["Tool Name", "Target Artifact", "Inspection Mechanism", "Latency", "Pipeline Function"], comp_tools)

doc.add_page_break()

# CHAPTER 3
add_h1("CHAPTER-3: IMPLEMENTATION OF PROJECT")
add_h2("3.1 Architectural Pipeline Design")
add_p("The pipeline architecture enforces a strict two-job sequential workflow within GitHub Actions: 'Shift-Left Static & Vulnerability Auditing' followed conditionally by 'Automated Cloud Deployment'. Cloud provisioning only triggers if every preceding static validation gate exits with code 0.")

add_h2("3.2 Enforced Security Policy Matrix")
policy_matrix = [
    ("POL-01", "S3 Storage", "CKV_AWS_20", "Block public read access control lists", "Exit 1 (Halt)"),
    ("POL-02", "S3 Storage", "CKV_AWS_19 / CKV_AWS_145", "Enforce server-side KMS encryption at rest", "Exit 1 (Halt)"),
    ("POL-03", "S3 Storage", "CKV_AWS_21", "Enforce S3 bucket versioning for recovery", "Exit 1 (Halt)"),
    ("POL-04", "Compute Network", "CKV_AWS_24", "Prohibit 0.0.0.0/0 ingress on administrative port 22", "Exit 1 (Halt)"),
    ("POL-05", "Compute Storage", "CKV_AWS_3", "Enforce encrypted EBS root block devices", "Exit 1 (Halt)"),
    ("POL-06", "Container Image", "TRIVY-CVE-BLOCK", "Halt build on Critical/High unpatched vulnerabilities", "Exit 1 (Halt)")
]
create_table(["Policy ID", "Domain", "Rule Identifier", "Description", "Gate Action"], policy_matrix)

add_h2("3.3 Hardened Terraform Configuration Excerpt")
add_code("""# Dedicated S3 Bucket Configuration with Server-Side KMS Encryption
resource "aws_s3_bucket" "financial_data_lake" {
  bucket        = "capstone-devsecops-data-324200509"
  force_destroy = true
  tags = {
    Environment = "Production"
    Compliance  = "CIS-Benchmark"
  }
}

resource "aws_s3_bucket_versioning" "s3_versioning" {
  bucket = aws_s3_bucket.financial_data_lake.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_instance" "web_server" {
  ami                         = data.aws_ami.amazon_linux_2023.id
  instance_type               = "t3.micro"
  vpc_security_group_ids      = [aws_security_group.web_sg.id]
  associate_public_ip_address = true
  user_data_replace_on_change = true

  root_block_device {
    encrypted   = true
    volume_size = 20
    volume_type = "gp3"
  }
}""")

doc.add_page_break()

# CHAPTER 4
add_h1("CHAPTER-4: RESULTS AND DISCUSSIONS")
add_h2("4.1 Functional Validation and Gate Interception")
add_p("To confirm policy determinism, the pipeline was tested using intentional negative testing (injected misconfigurations) followed by positive verification using hardened production templates.")

test_matrix = [
    ("TC-01", "Negative IaC Audit", "S3 ACL public-read, Open SSH port 22", "Checkov flagged CKV_AWS_20 & CKV_AWS_24", "Blocked (Exit 1)"),
    ("TC-02", "Negative Container Scan", "Outdated Alpine base container", "Trivy detected Critical/High CVEs", "Blocked (Exit 1)"),
    ("TC-03", "Hardened CI Validation", "KMS encrypted S3, restricted SSH, updated Alpine", "Checkov, TFSec, and Trivy passed", "Passed (Exit 0)"),
    ("TC-04", "Idempotent AWS Deployment", "Remote S3 state reconciliation in ap-south-1", "Single t3.micro EC2 provisioned cleanly", "Passed (Exit 0)")
]
create_table(["Test ID", "Scenario", "Condition Evaluated", "Observed Output", "Verdict"], test_matrix)

add_h2("4.2 Quantitative Performance Evaluation")
metrics = [
    ("Total Discovered Vulnerabilities", "7 Policy Violations / Multiple CVEs", "0 Critical / 0 High (100% Remediated)"),
    ("Pre-Deployment Interception Rate", "0% (Manual Post-Audit)", "100% Deterministic Interception"),
    ("Shift-Left Security Gate Runtime", "0 Seconds", "57 Seconds total execution time"),
    ("Provisioned Cloud Instances", "Multiple duplicate instances (Initial)", "Exactly 1 Single Instance (Idempotent)"),
    ("Mean Time to Remediate (MTTR)", "~14 Days (Enterprise manual lifecycle)", "< 2 Minutes (Inline Git developer fix)")
]
create_table(["Evaluation Metric", "Insecure Baseline Architecture", "Hardened Automated DevSecOps Pipeline"], metrics)

add_h2("4.3 Visual Evidence Index")
add_p("The following evidence figures represent captured execution artifacts from the project repository:")
add_p("Figure 4.1: Policy-as-Code interception output showing Checkov halting on S3 public permissions and open SSH ingress.")
add_p("Figure 4.2: Aqua Security Trivy container scan log displaying blocking on unpatched CVEs.")
add_p("Figure 4.3: GitHub Actions run showing complete 7-stage pass in 57 seconds.")
add_p("Figure 4.4: Live AWS EC2 web server dashboard displaying student credentials (Vikas Rawat, 324200509) and the verification matrix.")

doc.add_page_break()

# CHAPTER 5
add_h1("FINAL CHAPTER: CONCLUSION AND FUTURE SCOPE")
add_h2("5.1 Conclusion")
add_p("The project successfully designed, implemented, and benchmarked an automated DevSecOps delivery pipeline using Policy-as-Code and continuous vulnerability scanning. By integrating Checkov, TFSec, and Trivy directly into GitHub Actions, cloud infrastructure configurations and container definitions are evaluated against CIS benchmarks and CVE registries prior to cloud provisioning.")
add_p("The pipeline demonstrated 100% pre-deployment interception of non-compliant resources while maintaining an agile execution profile of 57 seconds. Managing state via a remote AWS S3 backend guarantees idempotency, preventing resource collisions and eliminating duplicate cloud expenses.")

add_h2("5.2 Future Scope")
add_p("1. Dynamic Application Security Testing (DAST): Embedding OWASP ZAP runners for post-provisioning web vulnerability scanning.")
add_p("2. Runtime Threat Detection: Deploying eBPF agents (such as Falco) to detect runtime anomalies inside compute instances.")
add_p("3. Automated Remediation Pull Requests: Integrating automated PR bots to suggest specific code fixes directly upon policy failure.")

add_h1("REFERENCES")
add_p("1. L. Bass, I. Weber, and L. Zhu, DevOps: A Software Architect's Perspective, Addison-Wesley Professional, 2015.")
add_p("2. Center for Internet Security, 'CIS AWS Foundations Benchmark v1.4.0,' CIS Security Guidance, 2026.")
add_p("3. Palo Alto Networks / Bridgecrew, 'Checkov: Infrastructure as Code Static Analysis,' Documentation, 2026.")
add_p("4. Aqua Security, 'Trivy Vulnerability and Misconfiguration Scanner,' Aqua Security Open Source, 2026.")
add_p("5. HashiCorp, 'Terraform State Management and AWS Provider Reference,' HashiCorp Docs, 2026.")
add_p("6. Lovely Professional University, 'Guidelines for Capstone Project (ECAP788),' Academic Guidelines, 2026.")

doc.add_page_break()

# ANNEXURE-I
add_h1("ANNEXURE-I: PROJECT SUMMARY SHEET", center=True)
summary_sheet = [
    ("Registration No.", "324200509"),
    ("Name of Student", "Vikas Rawat"),
    ("Title of Project Work", "Design and Implementation of an Automated DevSecOps Pipeline using Policy-as-Code and Continuous Security Scanning"),
    ("Objectives", "1. Build GitHub Actions CI/CD Shift-Left security pipeline.\n2. Enforce Policy-as-Code via Checkov and TFSec against CIS Benchmarks.\n3. Automate container vulnerability auditing via Aqua Security Trivy.\n4. Deploy an idempotent, single-resource web server in AWS ap-south-1."),
    ("Results & Findings", "Achieved 100% pre-deployment interception for simulated security defects. Reduced remediation turnaround to under 2 minutes with a 57-second pipeline gate execution."),
    ("Specific Outcomes", "Automated DevSecOps pipeline, CIS-compliant Terraform templates, distroless Docker configurations, and a live AWS showcase dashboard."),
    ("Learnings", "Proficiency in Policy-as-Code authoring, CI/CD security gating, CVE triage, and remote cloud state management."),
    ("Challenges Faced", "Alert fatigue from secondary operational rules and naming collisions on remote state; resolved via targeted policy tuning and unique S3 state locking.")
]
create_table(["Particular", "Details"], summary_sheet)

add_p("\n\nSignature of the Student: ___________________________")
add_p("Date: October 19, 2026")

doc.save("DevSecOps_Project_Report.docx")
print("DevSecOps_Project_Report.docx generated successfully!")
