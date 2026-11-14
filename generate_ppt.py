import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette (Modern Executive DevOps Palette)
    C_BG_DARK = RGBColor(15, 23, 42)      # #0F172A Deep Navy
    C_BG_CARD = RGBColor(30, 41, 59)      # #1E293B Slate Navy
    C_BORDER = RGBColor(51, 65, 85)       # #334155 Border
    C_TEXT_WHITE = RGBColor(248, 250, 252)# #F8FAFC
    C_TEXT_MUTED = RGBColor(148, 163, 184)# #94A3B8 Slate Gray
    C_INDIGO = RGBColor(99, 102, 241)     # #6366F1 Brand Accent
    C_CYAN = RGBColor(56, 189, 248)       # #38BDF8 Cyan
    C_EMERALD = RGBColor(16, 185, 129)    # #10B981 Success Green
    C_AMBER = RGBColor(245, 158, 11)      # #F59E0B Warning/Highlight
    C_AWS_ORANGE = RGBColor(255, 153, 0)  # #FF9900 AWS Orange

    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_DARK
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="INT333 • DEVOPS ADVANCE CONFIGURATION MANAGEMENT"):
        # Category Tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.4))
        tf = cat_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_CYAN
        p.font.name = "Arial"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.5), Inches(0.8))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE
        p.font.name = "Arial"

        # Accent Line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.65), Inches(2.5), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = C_INDIGO
        line.line.fill.background()

    def add_card(slide, left, top, width, height, bg_color=C_BG_CARD, border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        return card

    # ==========================================================
    # SLIDE 1: Title Slide
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)

    # Accent Top Banner
    t_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.1))
    t_bar.fill.solid()
    t_bar.fill.fore_color.rgb = C_INDIGO
    t_bar.line.fill.background()

    # Pill Tag
    pill = add_card(s1, 0.9, 0.9, 4.2, 0.45, C_BG_CARD, C_CYAN)
    tf = pill.text_frame
    p = tf.paragraphs[0]
    p.text = "☁️ INT333 • CAPSTONE PROJECT PRESENTATION"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN
    p.alignment = PP_ALIGN.CENTER

    # Project Title
    t_box = s1.shapes.add_textbox(Inches(0.9), Inches(1.5), Inches(11.5), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "Automated Cloud Infrastructure Provisioning\n& Configuration Management"
    p1.font.size = Pt(34)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_WHITE
    p1.font.name = "Arial"

    p2 = tf.add_paragraph()
    p2.text = "End-to-End DevOps Pipeline Using HashiCorp Terraform and Puppet on AWS"
    p2.font.size = Pt(18)
    p2.font.color.rgb = C_AMBER
    p2.font.name = "Arial"
    p2.space_before = Pt(12)

    # Student Card
    add_card(s1, 0.9, 4.3, 5.5, 2.3)
    s_box = s1.shapes.add_textbox(Inches(1.1), Inches(4.45), Inches(5.1), Inches(2.0))
    tf = s_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SUBMITTED BY:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    items = [
        ("Student Name", "Kushagra"),
        ("Roll Number", "63"),
        ("Registration No.", "12323868"),
        ("Section / Batch", "K302316 | 2023 - 2027"),
    ]
    for lbl, val in items:
        p = tf.add_paragraph()
        p.text = f"• {lbl}: {val}"
        p.font.size = Pt(13)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(4)

    # Faculty & Uni Card
    add_card(s1, 6.9, 4.3, 5.5, 2.3)
    f_box = s1.shapes.add_textbox(Inches(7.1), Inches(4.45), Inches(5.1), Inches(2.0))
    tf = f_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "SUBMITTED TO & INSTITUTION:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    f_items = [
        ("Faculty Guide", "Harpreet Kaur"),
        ("Designation", "Assistant Professor, Dept. of CSE"),
        ("School", "School of Computer Science & Engineering"),
        ("University", "Lovely Professional University (LPU)"),
    ]
    for lbl, val in f_items:
        p = tf.add_paragraph()
        p.text = f"• {lbl}: {val}"
        p.font.size = Pt(13)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(4)

    # ==========================================================
    # SLIDE 2: Problem Statement & Motivation
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_header(s2, "Problem Statement & Industry Motivation")

    # Left Card: Traditional / Manual Problems
    add_card(s2, 0.8, 2.0, 5.6, 4.8)
    p_box = s2.shapes.add_textbox(Inches(1.1), Inches(2.2), Inches(5.0), Inches(4.4))
    tf = p_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚠️ The Traditional Manual Approach"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(248, 113, 113) # Coral Red

    points_left = [
        ("Manual Cloud Setup", "Creating EC2 instances and firewalls via web console is slow, tedious, and prone to human typos."),
        ("Configuration Drift", "When servers are manually touched, configurations slowly diverge over time, making debugging impossible."),
        ("Lack of Reproducibility", "Re-creating the exact same environment in staging or production requires complex manual checklists."),
        ("No Version Control", "Manual clicks cannot be tracked, peer-reviewed, or rolled back in Git repositories.")
    ]
    for title, desc in points_left:
        p = tf.add_paragraph()
        p.text = f"• {title}:"
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(10)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = C_TEXT_MUTED

    # Right Card: Modern DevOps Solution
    add_card(s2, 6.9, 2.0, 5.6, 4.8)
    s_box = s2.shapes.add_textbox(Inches(7.2), Inches(2.2), Inches(5.0), Inches(4.4))
    tf = s_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "✅ The DevOps Automation Solution"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD

    points_right = [
        ("Infrastructure as Code (IaC)", "Terraform defines compute, storage, and networking declaratively in version-controlled HCL code."),
        ("Configuration Management (CM)", "Puppet automatically enforces the desired state of software, packages, and config files."),
        ("Guaranteed Idempotency", "Applying the automation multiple times produces identical results with zero duplicate effort."),
        ("Single-Command Provisioning", "Entire cloud stack spins up in under 2 minutes with 'terraform apply'.")
    ]
    for title, desc in points_right:
        p = tf.add_paragraph()
        p.text = f"• {title}:"
        p.font.bold = True
        p.font.size = Pt(13)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(10)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 3: Key Technologies & Toolchain
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_header(s3, "Key Technologies & DevOps Toolchain")

    techs = [
        ("HashiCorp Terraform", "Infrastructure as Code", "• Provisions cloud resources declaratively\n• Manages state lifecycle (.tfstate)\n• Automates AWS EC2 & Security Group\n• Cloud-agnostic execution engine", C_INDIGO),
        ("Puppet Open Source", "Configuration Management", "• Declarative desired-state language\n• Automated Apache web server install\n• Continuous configuration enforcement\n• Guarantees complete idempotency", C_AMBER),
        ("Amazon Web Services (AWS)", "Cloud Infrastructure", "• Region: ap-south-1 (Mumbai)\n• Compute: EC2 t3.micro (Free Tier)\n• Networking: Default VPC & Subnets\n• Security: Stateful Security Group (22/80)", C_AWS_ORANGE),
        ("Ubuntu 22.04 LTS & Apache", "Operating System & Web App", "• Canonical Ubuntu Jammy LTS AMI\n• Cloud-init bootstrap automation\n• Apache HTTP Server (Port 80)\n• High-performance interactive UI", C_CYAN)
    ]

    col_w = 2.7
    gap = 0.25
    left_start = 0.8
    for i, (t_title, t_sub, t_desc, accent_color) in enumerate(techs):
        c_left = left_start + i * (col_w + gap)
        c = add_card(s3, c_left, 2.0, col_w, 4.8)
        
        # Color bar on top of card
        bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(2.0), Inches(col_w), Inches(0.1))
        bar.fill.solid()
        bar.fill.fore_color.rgb = accent_color
        bar.line.fill.background()

        tb = s3.shapes.add_textbox(Inches(c_left + 0.15), Inches(2.2), Inches(col_w - 0.3), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = t_title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE
        
        p2 = tf.add_paragraph()
        p2.text = t_sub
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = accent_color
        p2.space_before = Pt(4)
        
        p3 = tf.add_paragraph()
        p3.text = t_desc
        p3.font.size = Pt(11)
        p3.font.color.rgb = C_TEXT_MUTED
        p3.space_before = Pt(14)

    # ==========================================================
    # SLIDE 4: Architecture & Workflow Diagram
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_header(s4, "System Architecture & End-to-End Pipeline")

    steps = [
        ("1. Code & Blueprint", "Developer", "Writes main.tf & site.pp in Git repository.", C_CYAN),
        ("2. Cloud IaC Apply", "Terraform Engine", "Provisions EC2 & Security Group on AWS.", C_INDIGO),
        ("3. Boot & Agent Init", "cloud-init", "Installs Puppet Agent on Ubuntu instance.", C_AMBER),
        ("4. State Enforcement", "Puppet Agent", "Enforces Apache2 package, service, & HTML.", C_EMERALD),
        ("5. Public Service", "Live Web Server", "Live dashboard accessible on Port 80.", C_AWS_ORANGE),
    ]

    for i, (title, who, desc, col) in enumerate(steps):
        s_card = add_card(s4, 0.8 + i*2.4, 2.1, 2.2, 3.4)
        
        # Indicator badge
        num_box = s4.shapes.add_shape(MSO_SHAPE.OVAL, Inches(1.0 + i*2.4), Inches(2.3), Inches(0.5), Inches(0.5))
        num_box.fill.solid()
        num_box.fill.fore_color.rgb = col
        num_box.line.fill.background()
        tf = num_box.text_frame
        p = tf.paragraphs[0]
        p.text = str(i+1)
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = s4.shapes.add_textbox(Inches(0.9 + i*2.4), Inches(2.9), Inches(2.0), Inches(2.4))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE

        p2 = tf.add_paragraph()
        p2.text = f"Role: {who}"
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = col
        p2.space_before = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(11)
        p3.font.color.rgb = C_TEXT_MUTED
        p3.space_before = Pt(8)

    # Bottom summary box
    summary_card = add_card(s4, 0.8, 5.8, 11.7, 1.1, C_BG_CARD, C_INDIGO)
    stb = s4.shapes.add_textbox(Inches(1.0), Inches(5.9), Inches(11.3), Inches(0.9))
    tf = stb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚡ Key Architectural Advantage:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_AMBER
    p2 = tf.add_paragraph()
    p2.text = "Decoupled Provisioning & Configuration: Terraform handles 'What infrastructure to build' while Puppet handles 'How the software inside must behave', ensuring seamless multi-cloud scaling and clean separation of concerns."
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_TEXT_WHITE

    # ==========================================================
    # SLIDE 5: Terraform Infrastructure Code
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_header(s5, "Cloud Provisioning with HashiCorp Terraform")

    # Left: Code Highlights
    add_card(s5, 0.8, 2.0, 6.0, 4.8)
    c_box = s5.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.6), Inches(4.5))
    tf = c_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📄 terraform/main.tf Highlights"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    code_snip = """# Dynamic AMI Lookup
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical
  filter { name = "name", values = ["*jammy-22.04*"] }
}

# Stateful Security Group
resource "aws_security_group" "puppet_sg" {
  name = "puppet-apache-sg"
  ingress { from_port = 22, to_port = 22, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] }
  ingress { from_port = 80, to_port = 80, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] }
}

# EC2 Compute Node
resource "aws_instance" "puppet_node" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type # t3.micro
  key_name      = "puppet-key"
  user_data     = file("bootstrap.sh")
}"""
    p2 = tf.add_paragraph()
    p2.text = code_snip
    p2.font.size = Pt(10)
    p2.font.color.rgb = RGBColor(186, 230, 253)
    p2.font.name = "Courier New"
    p2.space_before = Pt(8)

    # Right: Responsibilities
    add_card(s5, 7.1, 2.0, 5.4, 4.8)
    r_box = s5.shapes.add_textbox(Inches(7.3), Inches(2.1), Inches(5.0), Inches(4.5))
    tf = r_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚙️ Terraform Key Responsibilities"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_INDIGO

    tf_features = [
        ("Declarative HCL", "Human-readable syntax specifying the target cloud state without writing manual API calls."),
        ("Dynamic AMI Resolution", "Always retrieves the latest verified official Ubuntu 22.04 LTS AMI automatically."),
        ("Security Group Hardening", "Precisely restricts inbound ports: Port 22 (SSH Remote Admin) & Port 80 (HTTP Web)."),
        ("Immutable State Management", "Maintains 'terraform.tfstate' to track live cloud resource mappings and dependencies."),
        ("User Data Orchestration", "Injects boot-time shell script that triggers Puppet Agent setup automatically.")
    ]
    for h, d in tf_features:
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 6: Puppet Configuration Management Code
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_header(s6, "Configuration Management with Puppet")

    # Left: Puppet Manifest Code
    add_card(s6, 0.8, 2.0, 6.0, 4.8)
    c_box = s6.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.6), Inches(4.5))
    tf = c_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📄 puppet/manifests/site.pp (Manifest)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_AMBER

    puppet_snip = """node default {

  # 1. Ensure apache2 package is installed
  package { 'apache2':
    ensure => installed,
  }

  # 2. Ensure apache2 service is active on boot
  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'],
  }

  # 3. Deploy custom interactive web UI
  file { '/var/www/html/index.html':
    ensure  => file,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    source  => '/tmp/index.html',
    require => Package['apache2'],
    notify  => Service['apache2'],
  }

}"""
    p2 = tf.add_paragraph()
    p2.text = puppet_snip
    p2.font.size = Pt(11)
    p2.font.color.rgb = RGBColor(254, 240, 138) # Light yellow
    p2.font.name = "Courier New"
    p2.space_before = Pt(8)

    # Right: Puppet Core Pillars
    add_card(s6, 7.1, 2.0, 5.4, 4.8)
    r_box = s6.shapes.add_textbox(Inches(7.3), Inches(2.1), Inches(5.0), Inches(4.5))
    tf = r_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎯 Puppet Architectural Concepts"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    pup_features = [
        ("Resource Declarations", "Expresses 'what' the state must be ('package', 'service', 'file') rather than procedural step-by-step shell commands."),
        ("Relationship Metaparameters", "Uses 'require' and 'notify' to guarantee Apache is installed before starting and reloads automatically when files update."),
        ("Resource Abstraction Layer (RAL)", "Puppet abstracts OS specifics — 'package { apache2: }' works seamlessly on Debian/Ubuntu via APT."),
        ("Catalog Compilation", "Manifests compile into a system catalog which the Puppet Agent evaluates against current system state."),
        ("Automated Healing", "If an administrator inadvertently terminates Apache, Puppet's next run detects drift and restarts it.")
    ]
    for h, d in pup_features:
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(6)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 7: Key Concept - Idempotency & Zero Drift
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_header(s7, "Core Concept: Idempotency & Zero Drift")

    # Concept explanation box
    add_card(s7, 0.8, 2.0, 11.7, 1.4)
    ib = s7.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(11.3), Inches(1.2))
    tf = ib.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "💡 What is Idempotency in Configuration Management?"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_AMBER
    p2 = tf.add_paragraph()
    p2.text = "Idempotency is the property where an operation can be applied multiple times without changing the result beyond the initial application. In this project, running Puppet 100 times leaves the system in the exact same pristine state with zero duplicate packages or broken configurations."
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_TEXT_WHITE
    p2.space_before = Pt(4)

    # 1st Run Card
    add_card(s7, 0.8, 3.6, 5.6, 3.2)
    r1 = s7.shapes.add_textbox(Inches(1.0), Inches(3.7), Inches(5.2), Inches(3.0))
    tf = r1.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1️⃣ Initial Execution (1st Run)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    items_r1 = [
        ("Package Check", "Puppet inspects system → detects apache2 missing."),
        ("Action Taken", "Executes APT install → packages deployed successfully."),
        ("Service Check", "Detects daemon inactive → starts apache2 service."),
        ("File Check", "Generates custom Bento Grid index.html on Port 80."),
        ("Run Report", "Changes: 3 applied, 0 failed, System state = DESIRED.")
    ]
    for h, d in items_r1:
        p = tf.add_paragraph()
        p.text = f"• {h}: {d}"
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(4)

    # 2nd Run Card
    add_card(s7, 6.9, 3.6, 5.6, 3.2)
    r2 = s7.shapes.add_textbox(Inches(7.1), Inches(3.7), Inches(5.2), Inches(3.0))
    tf = r2.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2️⃣ Subsequent Execution (2nd Run)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD

    items_r2 = [
        ("Package Check", "Puppet inspects system → apache2 already present."),
        ("Action Taken", "NO ACTION REQUIRED (skips reinstall)."),
        ("Service Check", "Detects apache2 running → NO ACTION REQUIRED."),
        ("File Check", "Checksum matches index.html → NO ACTION REQUIRED."),
        ("Run Report", "Changes: 0 applied, 0 failed → 100% IDEMPOTENT!")
    ]
    for h, d in items_r2:
        p = tf.add_paragraph()
        p.text = f"• {h}: {d}"
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(4)

    # ==========================================================
    # SLIDE 8: Deployment Lifecycle & Commands
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_header(s8, "Deployment Lifecycle & Practical CLI Workflow")

    cmds = [
        ("1. terraform init", "Provider Initialization", "• Downloads HashiCorp AWS provider plugin (~v5.0)\n• Configures backend and local lock file (.terraform.lock.hcl)\n• Validates workspace directory structure", C_CYAN),
        ("2. terraform plan", "Execution Blueprinting", "• Compares local .tf files against live cloud state\n• Previews 2 resources to add (Security Group + EC2)\n• Dry-run verification with zero billing impact", C_INDIGO),
        ("3. terraform apply", "Cloud Provisioning", "• Authenticates with AWS credentials via STS\n• Creates Security Group & launches Ubuntu EC2\n• Executes user_data bootstrap script automatically", C_EMERALD),
        ("4. terraform destroy", "Automated Cleanup", "• Tears down all provisioned cloud resources in reverse order\n• Prevents unnecessary AWS billing after evaluation\n• Complete infrastructure lifecycle management", RGBColor(248, 113, 113))
    ]

    for i, (c_name, c_sub, c_body, col) in enumerate(cmds):
        top_pos = 2.0 + (i % 2) * 2.5
        left_pos = 0.8 if i < 2 else 6.9
        
        c = add_card(s8, left_pos, top_pos, 5.6, 2.3)
        tb = s8.shapes.add_textbox(Inches(left_pos + 0.15), Inches(top_pos + 0.1), Inches(5.3), Inches(2.1))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = c_name
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = col
        p.font.name = "Courier New"

        p2 = tf.add_paragraph()
        p2.text = c_sub
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = C_AMBER
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = c_body
        p3.font.size = Pt(11)
        p3.font.color.rgb = C_TEXT_MUTED
        p3.space_before = Pt(6)

    # ==========================================================
    # SLIDE 9: Project Results & Verification
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_header(s9, "Deployment Results & Live System Verification")

    # Table Card
    add_card(s9, 0.8, 2.0, 6.2, 4.8)
    t_box = s9.shapes.add_textbox(Inches(1.0), Inches(2.1), Inches(5.8), Inches(4.5))
    tf = t_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📊 Live AWS Infrastructure Telemetry"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

    res_table = [
        ("Target Cloud", "Amazon Web Services (AWS)"),
        ("AWS Region", "ap-south-1 (Mumbai, India)"),
        ("EC2 Instance ID", "i-0ed9db706fd79bab9"),
        ("Compute Instance Type", "t3.micro (Free Tier, 2 vCPU, 1 GB)"),
        ("Operating System", "Ubuntu 22.04 LTS (Jammy)"),
        ("Live Public Endpoint", "http://13.201.137.244 (Port 80)"),
        ("HTTP Response Code", "200 OK (Verified live)"),
        ("Configuration Status", "Puppet Catalog Applied (0 Drift)")
    ]
    for k, v in res_table:
        p = tf.add_paragraph()
        p.text = f"• {k}: {v}"
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(6)

    # Right Card: Dashboard Verification
    add_card(s9, 7.3, 2.0, 5.2, 4.8)
    d_box = s9.shapes.add_textbox(Inches(7.5), Inches(2.1), Inches(4.8), Inches(4.5))
    tf = d_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎨 Modern Nixtio Bento Grid UI"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_AMBER

    features = [
        ("Dribbble-Style Bento Grid", "Clean rounded modern cards with executive warm badami/beige luxury aesthetic."),
        ("Live Ticking Uptime Ring", "Interactive circular progress ring tracking active node availability in real-time."),
        ("Pipeline Stage Checklist", "Visual 4/4 checklist confirming Terraform, Puppet, Apache, and Security Group status."),
        ("Dynamic Student Branding", "Prominently displays Kushagra, Roll #63, INT333, and Lovely Professional University.")
    ]
    for h, d in features:
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 10: Testing & Verification Matrix
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_header(s10, "Test Cases & Quality Assurance Matrix")

    tests = [
        ("TC-01", "Terraform Cloud Provisioning", "terraform apply creates VPC SG and EC2", "EC2 instance running with Public IP", "PASS", C_EMERALD),
        ("TC-02", "Firewall Port Verification", "curl http://13.201.137.244 on port 80", "TCP port 80 accessible; HTTP 200 OK", "PASS", C_EMERALD),
        ("TC-03", "Puppet Bootstrap Execution", "cloud-init executes puppet-agent installer", "Puppet Agent installed and catalog applied", "PASS", C_EMERALD),
        ("TC-04", "Apache Service Daemon", "systemctl status apache2 on Ubuntu node", "Active (running) status & enabled at boot", "PASS", C_EMERALD),
        ("TC-05", "Idempotency & Drift Test", "Re-run puppet apply on configured node", "0 packages changed, 0 failures reported", "PASS", C_EMERALD),
    ]

    for i, (tc_id, tc_name, tc_input, tc_exp, tc_status, col) in enumerate(tests):
        top_y = 2.0 + i * 0.95
        card = add_card(s10, 0.8, top_y, 11.7, 0.82)
        
        # Test ID Pill
        pill = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(top_y + 0.16), Inches(1.1), Inches(0.48))
        pill.fill.solid()
        pill.fill.fore_color.rgb = C_BG_DARK
        pill.line.color.rgb = C_CYAN
        pill.line.width = Pt(1)
        tf = pill.text_frame
        p = tf.paragraphs[0]
        p.text = tc_id
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_CYAN
        p.alignment = PP_ALIGN.CENTER

        # Test Details
        tb = s10.shapes.add_textbox(Inches(2.3), Inches(top_y + 0.1), Inches(8.3), Inches(0.65))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{tc_name}  |  {tc_input}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE
        p2 = tf.add_paragraph()
        p2.text = f"Expected Result: {tc_exp}"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

        # Status Badge
        badge = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.9), Inches(top_y + 0.18), Inches(1.3), Inches(0.45))
        badge.fill.solid()
        badge.fill.fore_color.rgb = col
        badge.line.fill.background()
        tf = badge.text_frame
        p = tf.paragraphs[0]
        p.text = f"✓ {tc_status}"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_WHITE
        p.alignment = PP_ALIGN.CENTER

    # ==========================================================
    # SLIDE 11: Future Scope & Conclusion
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11)
    add_header(s11, "Future Scope & Conclusion")

    # Left: Future Scope
    add_card(s11, 0.8, 2.0, 5.6, 4.8)
    f_box = s11.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.4))
    tf = f_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🚀 Future Enhancements"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = C_AMBER

    f_points = [
        ("CI/CD Pipeline Integration", "Trigger automated 'terraform plan' and 'puppet apply' on GitHub pull requests using GitHub Actions."),
        ("Remote State & Locking", "Migrate Terraform state to an AWS S3 bucket with DynamoDB state locking for enterprise collaboration."),
        ("Multi-Node Cluster Scaling", "Extend Puppet manifests to configure multi-tier architectures (NGINX Load Balancers, MySQL databases)."),
        ("Puppet Server / Master Mode", "Upgrade from standalone 'puppet apply' to centralized Puppet Master/Agent architecture with PuppetDB analytics.")
    ]
    for h, d in f_points:
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # Right: Conclusion
    add_card(s11, 6.9, 2.0, 5.6, 4.8)
    c_box = s11.shapes.add_textbox(Inches(7.1), Inches(2.2), Inches(5.2), Inches(4.4))
    tf = c_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🏁 Conclusion"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = C_EMERALD

    c_points = [
        ("100% Automated Workflow", "Demonstrated complete elimination of manual server setup, reducing provisioning time from hours to under 2 minutes."),
        ("Elimination of Configuration Drift", "Puppet enforces declarative state compliance, ensuring zero divergence across server lifecycles."),
        ("Real-World Production DevOps", "Provides hands-on mastery of industry-standard tools (Terraform, Puppet, AWS, Linux, Git) essential for SRE and Cloud engineering."),
        ("Cost-Effective Academic Architecture", "Leverages AWS Free Tier (t3.micro) with clean lifecycle destruction commands.")
    ]
    for h, d in c_points:
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_WHITE
        p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 12: Thank You / Q&A Slide
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12)

    # Accent Top Banner
    t_bar = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.1))
    t_bar.fill.solid()
    t_bar.fill.fore_color.rgb = C_INDIGO
    t_bar.line.fill.background()

    # Center Card
    add_card(s12, 2.5, 1.2, 8.333, 5.2)

    tb = s12.shapes.add_textbox(Inches(2.7), Inches(1.5), Inches(7.9), Inches(4.6))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Thank You!"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_WHITE
    p.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = "Questions & Answers (Q&A)"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = C_AMBER
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = "Automated Cloud Infrastructure Provisioning & Configuration Management"
    p3.font.size = Pt(14)
    p3.font.color.rgb = C_CYAN
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(14)

    # Divider line
    div = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.5), Inches(3.6), Inches(4.3), Inches(0.02))
    div.fill.solid()
    div.fill.fore_color.rgb = C_BORDER
    div.line.fill.background()

    p4 = tf.add_paragraph()
    p4.text = "Presented by: Kushagra | Roll No. 63 | Reg. No. 12323868\nCourse: INT333 – DevOps Advance Configuration Management\nUnder the Guidance of: Harpreet Kaur (Assistant Professor, CSE)\nSchool of Computer Science and Engineering\nLovely Professional University (LPU)"
    p4.font.size = Pt(13)
    p4.font.color.rgb = C_TEXT_MUTED
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(36)

    # Save
    out_path = r"c:\Users\Kushagra Saxena\Desktop\devops-project\Kushagra_RollNo_63_DevOps_Presentation.pptx"
    prs.save(out_path)
    print(f"Presentation saved successfully to: {out_path}")

if __name__ == "__main__":
    create_deck()

