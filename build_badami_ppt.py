import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # ==========================================
    # Project Palette: Badami & Bento Executive
    # ==========================================
    C_BG_BADAMI = RGBColor(245, 239, 230)       # #F5EFE6 Warm Cream Badami
    C_CARD_WHITE = RGBColor(255, 255, 255)      # #FFFFFF Pure White
    C_CARD_BORDER = RGBColor(226, 213, 197)     # #E2D5C5 Soft Almond Border
    C_CARD_DARK = RGBColor(30, 31, 36)          # #1E1F24 Charcoal Dark
    C_TEXT_DARK = RGBColor(30, 31, 36)          # #1E1F24
    C_TEXT_MUTED = RGBColor(120, 108, 100)      # #786C64 Warm Muted Gray
    C_ACCENT_YELLOW = RGBColor(247, 201, 72)    # #F7C948 Nixtio Yellow
    C_TF_PURPLE = RGBColor(124, 58, 237)        # #7C3AED Terraform Violet
    C_AWS_ORANGE = RGBColor(234, 88, 12)        # #EA580C AWS Deep Orange
    C_PUPPET_GOLD = RGBColor(202, 138, 4)       # #CA8A04 Puppet Gold
    C_SUCCESS_GREEN = RGBColor(22, 163, 74)     # #16A34A Success Emerald
    C_CODE_BG = RGBColor(40, 42, 54)            # #282A36 Dark Editor Code BG

    FONT_FAMILY = "Segoe UI"
    FONT_CODE = "Consolas"

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG_BADAMI
        bg.line.fill.background()
        return bg

    def add_card(slide, left, top, width, height, bg_color=C_CARD_WHITE, border_color=C_CARD_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1.2)
        else:
            card.line.fill.background()
        return card

    def add_header(slide, title_text, category="INT333 • DEVOPS ADVANCE CONFIGURATION MANAGEMENT"):
        # Category Pill
        cat_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(4.8), Inches(0.35))
        cat_card.fill.solid()
        cat_card.fill.fore_color.rgb = C_CARD_WHITE
        cat_card.line.color.rgb = C_CARD_BORDER
        cat_card.line.width = Pt(1)
        tf = cat_card.text_frame
        tf.word_wrap = True
        tf.margin_top = Inches(0.04)
        p = tf.paragraphs[0]
        p.text = category
        p.font.name = FONT_FAMILY
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = C_PUPPET_GOLD
        p.alignment = PP_ALIGN.CENTER

        # Slide Main Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.75))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK

    # ==========================================================
    # SLIDE 1: Title Slide (Bento Luxury Badami)
    # ==========================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Top Pill Header
    top_pill = add_card(s1, 0.8, 0.6, 11.733, 0.55, C_CARD_WHITE, C_CARD_BORDER)
    tf = top_pill.text_frame
    tf.margin_top = Inches(0.08)
    p = tf.paragraphs[0]
    p.text = "☁️ INT333 • DEVOPS ADVANCE CONFIGURATION MANAGEMENT  |  ACADEMIC SESSION 2026-2027"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PUPPET_GOLD
    p.alignment = PP_ALIGN.CENTER

    # Main Hero Title Card
    hero = add_card(s1, 0.8, 1.35, 11.733, 2.5, C_CARD_WHITE, C_CARD_BORDER)
    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(10.9), Inches(2.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Automated Cloud Infrastructure Provisioning\n& Configuration Management"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK

    p2 = tf.add_paragraph()
    p2.text = "End-to-End Automated Pipeline Using HashiCorp Terraform and Puppet on AWS Cloud"
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(15)
    p2.font.bold = True
    p2.font.color.rgb = C_AWS_ORANGE
    p2.space_before = Pt(8)

    # Badges bar inside hero
    p3 = tf.add_paragraph()
    p3.text = "[ AWS ap-south-1 (Mumbai) ]   [ Terraform v1.15 ]   [ Puppet Agent v8 ]   [ Ubuntu 22.04 LTS ]"
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(11)
    p3.font.bold = True
    p3.font.color.rgb = C_TEXT_MUTED
    p3.space_before = Pt(12)

    # Student Card (Left)
    add_card(s1, 0.8, 4.1, 5.7, 2.7)
    sb = s1.shapes.add_textbox(Inches(1.1), Inches(4.3), Inches(5.1), Inches(2.3))
    tf = sb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "👤 SUBMITTED BY"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_TF_PURPLE

    details_s = [
        ("Student Name", "Kushagra"),
        ("Roll Number", "63"),
        ("Registration No.", "12323868"),
        ("Course & Section", "B.Tech CSE  |  Section K302316"),
        ("Batch", "2023 - 2027"),
    ]
    for lbl, val in details_s:
        p = tf.add_paragraph()
        p.text = f"• {lbl}: {val}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(4)

    # Faculty & University Card (Right)
    add_card(s1, 6.833, 4.1, 5.7, 2.7)
    fb = s1.shapes.add_textbox(Inches(7.133), Inches(4.3), Inches(5.1), Inches(2.3))
    tf = fb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎓 SUBMITTED TO & INSTITUTION"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_PUPPET_GOLD

    details_f = [
        ("Faculty Mentor", "Harpreet Kaur"),
        ("Designation", "Assistant Professor, Dept. of CSE"),
        ("School", "School of Computer Science & Engineering"),
        ("Institution", "Lovely Professional University (LPU)"),
        ("Academic Year", "2026 - 2027"),
    ]
    for lbl, val in details_f:
        p = tf.add_paragraph()
        p.text = f"• {lbl}: {val}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(4)

    # ==========================================================
    # SLIDE 2: Problem Statement & Motivation
    # ==========================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Problem Statement & Industry Motivation")

    # Left: The Problem
    add_card(s2, 0.8, 1.8, 5.7, 5.1)
    
    # Red accent pill
    pill = add_card(s2, 1.1, 2.05, 3.2, 0.35, RGBColor(254, 242, 242), RGBColor(252, 165, 165))
    tf = pill.text_frame
    tf.margin_top = Inches(0.04)
    p = tf.paragraphs[0]
    p.text = "⚠️ TRADITIONAL / MANUAL ISSUES"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(220, 38, 38)
    p.alignment = PP_ALIGN.CENTER

    tb = s2.shapes.add_textbox(Inches(1.1), Inches(2.55), Inches(5.1), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    probs = [
        ("Manual Cloud Setup", "Creating EC2 instances and firewalls manually through the AWS console is slow, tedious, and prone to human typos."),
        ("Configuration Drift", "When servers are manually modified, configurations gradually diverge, leading to environments that are impossible to reproduce."),
        ("Lack of Version Control", "Manual console clicks cannot be reviewed, tracked, or rolled back in Git repositories."),
        ("Slow Disaster Recovery", "Rebuilding crashed servers by hand can take hours or days, causing significant business downtime.")
    ]
    for idx, (title, desc) in enumerate(probs):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = f"• {title}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        if idx > 0: p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # Right: The Solution
    add_card(s2, 6.833, 1.8, 5.7, 5.1)

    # Green accent pill
    pill = add_card(s2, 7.133, 2.05, 3.4, 0.35, RGBColor(240, 253, 244), RGBColor(187, 247, 208))
    tf = pill.text_frame
    tf.margin_top = Inches(0.04)
    p = tf.paragraphs[0]
    p.text = "✅ THE DEVOPS AUTOMATION SOLUTION"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = C_SUCCESS_GREEN
    p.alignment = PP_ALIGN.CENTER

    tb = s2.shapes.add_textbox(Inches(7.133), Inches(2.55), Inches(5.1), Inches(4.1))
    tf = tb.text_frame
    tf.word_wrap = True
    sols = [
        ("Infrastructure as Code (IaC)", "Terraform defines compute, VPC, and firewall rules in declarative, version-controlled HCL code."),
        ("Declarative State Management", "Puppet enforces desired packages, active services, and web configurations continuously."),
        ("Guaranteed Idempotency", "Running the pipeline multiple times guarantees zero unintended changes and zero system corruption."),
        ("Single-Command Deployment", "Complete cloud infrastructure is provisioned and configured in under 2 minutes with 'terraform apply'.")
    ]
    for idx, (title, desc) in enumerate(sols):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = f"• {title}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(12.5)
        p.font.color.rgb = C_TEXT_DARK
        if idx > 0: p.space_before = Pt(8)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 3: Key Technologies & Toolchain
    # ==========================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "DevOps Toolchain & Technology Stack")

    tech_boxes = [
        ("HashiCorp Terraform", "Infrastructure as Code (IaC)", C_TF_PURPLE, [
            ("Core Role", "Cloud Provisioner"),
            ("Language", "HashiCorp HCL"),
            ("Capabilities", "EC2, VPC, Security Group"),
            ("State Tracking", "terraform.tfstate"),
            ("Advantage", "Multi-cloud, declarative")
        ]),
        ("Puppet Open Source", "Configuration Management", C_PUPPET_GOLD, [
            ("Core Role", "OS & Software Enforcer"),
            ("Language", "Puppet Declarative DSL"),
            ("Capabilities", "Packages, Services, Files"),
            ("Idempotency", "Zero-Drift Guarantee"),
            ("Advantage", "Resource abstraction layer")
        ]),
        ("Amazon Web Services", "Cloud Infrastructure Host", C_AWS_ORANGE, [
            ("Region", "ap-south-1 (Mumbai)"),
            ("Compute Node", "EC2 t3.micro (Free Tier)"),
            ("Networking", "Default VPC & Subnet"),
            ("Firewall", "Security Group (Port 22/80)"),
            ("Advantage", "Enterprise high-availability")
        ]),
        ("Ubuntu & Apache Server", "Operating System & App Tier", RGBColor(180, 83, 9), [
            ("Distribution", "Ubuntu 22.04 LTS (Jammy)"),
            ("Web Daemon", "Apache HTTP Server (apache2)"),
            ("Port", "Port 80 (HTTP)"),
            ("UI Design", "Nixtio Modern Bento Grid"),
            ("Status", "200 OK (Verified Live)")
        ])
    ]

    card_w = 2.75
    gap = 0.244
    for i, (name, role, accent, items) in enumerate(tech_boxes):
        c_left = 0.8 + i * (card_w + gap)
        add_card(s3, c_left, 1.8, card_w, 5.1)

        # Top Color Accent
        bar = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(c_left), Inches(1.8), Inches(card_w), Inches(0.12))
        bar.fill.solid()
        bar.fill.fore_color.rgb = accent
        bar.line.fill.background()

        tb = s3.shapes.add_textbox(Inches(c_left + 0.15), Inches(2.05), Inches(card_w - 0.3), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.name = FONT_FAMILY
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK

        p2 = tf.add_paragraph()
        p2.text = role
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.bold = True
        p2.font.color.rgb = accent
        p2.space_before = Pt(3)

        for idx, (k, v) in enumerate(items):
            p = tf.add_paragraph()
            p.text = f"• {k}:"
            p.font.name = FONT_FAMILY
            p.font.bold = True
            p.font.size = Pt(10.5)
            p.font.color.rgb = C_TEXT_DARK
            p.space_before = Pt(8 if idx > 0 else 12)
            p2 = tf.add_paragraph()
            p2.text = v
            p2.font.name = FONT_FAMILY
            p2.font.size = Pt(9.5)
            p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 4: Architecture & Workflow Diagram
    # ==========================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "System Architecture & 5-Step Pipeline Flow")

    pipe_steps = [
        ("STEP 1", "Developer Code", "Writes declarative main.tf and Puppet site.pp in version control.", C_CARD_DARK),
        ("STEP 2", "Terraform Apply", "Calls AWS APIs to provision VPC Security Group and Ubuntu EC2 node.", C_TF_PURPLE),
        ("STEP 3", "cloud-init Boot", "EC2 boot script installs Puppet Agent 8 from official repository.", C_PUPPET_GOLD),
        ("STEP 4", "Puppet Catalog", "Enforces apache2 package installation, active daemon, and HTML files.", C_SUCCESS_GREEN),
        ("STEP 5", "Live Endpoint", "Public access via browser on Port 80 with guaranteed Zero Drift.", C_AWS_ORANGE),
    ]

    card_w = 2.18
    gap = 0.20
    for i, (step_num, title, desc, accent) in enumerate(pipe_steps):
        c_left = 0.8 + i * (card_w + gap)
        add_card(s4, c_left, 1.8, card_w, 3.8)

        # Step Pill
        pill = add_card(s4, c_left + 0.2, 2.05, 1.2, 0.35, accent, None)
        tf = pill.text_frame
        tf.margin_top = Inches(0.04)
        p = tf.paragraphs[0]
        p.text = step_num
        p.font.name = FONT_FAMILY
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_CARD_WHITE
        p.alignment = PP_ALIGN.CENTER

        tb = s4.shapes.add_textbox(Inches(c_left + 0.15), Inches(2.6), Inches(card_w - 0.3), Inches(2.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_FAMILY
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_TEXT_MUTED
        p2.space_before = Pt(8)

    # Bottom Architectural Advantage Banner
    bot_card = add_card(s4, 0.8, 5.85, 11.733, 1.05, C_CARD_WHITE, C_CARD_BORDER)
    tb = s4.shapes.add_textbox(Inches(1.0), Inches(5.95), Inches(11.3), Inches(0.85))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚡ Separation of Concerns: The Cloud Engineering Golden Rule"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = C_AWS_ORANGE

    p2 = tf.add_paragraph()
    p2.text = "Terraform answers 'What infrastructure to build' (hardware/network) while Puppet answers 'How the software inside must behave'. Decoupling provisioning from configuration ensures seamless portability, easy maintenance, and true enterprise scale."
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_TEXT_DARK
    p2.space_before = Pt(2)

    # ==========================================================
    # SLIDE 5: Terraform Infrastructure Code
    # ==========================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Cloud Provisioning with HashiCorp Terraform")

    # Left: Code Snippet Card
    add_card(s5, 0.8, 1.8, 6.0, 5.1, C_CODE_BG, None)
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(5.6), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📄 terraform/main.tf (HCL Blueprint)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_ACCENT_YELLOW

    code_text = """# 1. Official Canonical Ubuntu 22.04 LTS AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]
  filter { name = "name", values = ["*jammy-22.04*"] }
}

# 2. Stateful Firewall Security Group
resource "aws_security_group" "puppet_sg" {
  name = "puppet-apache-sg"
  ingress { from_port = 22, to_port = 22, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] }
  ingress { from_port = 80, to_port = 80, protocol = "tcp", cidr_blocks = ["0.0.0.0/0"] }
  egress  { from_port = 0,  to_port = 0,  protocol = "-1",  cidr_blocks = ["0.0.0.0/0"] }
}

# 3. AWS EC2 Compute Node
resource "aws_instance" "puppet_node" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  key_name      = "puppet-key"
  user_data     = file("bootstrap.sh")
}"""
    p2 = tf.add_paragraph()
    p2.text = code_text
    p2.font.name = FONT_CODE
    p2.font.size = Pt(9.5)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_before = Pt(8)

    # Right: Technical Explanations
    add_card(s5, 7.0, 1.8, 5.533, 5.1)
    tb = s5.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.1), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "⚙️ Terraform Architectural Responsibilities"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_TF_PURPLE

    tf_pts = [
        ("Declarative Infrastructure", "Specifies desired cloud state in HCL without writing complex low-level API integration code."),
        ("Dynamic AMI Resolution", "Automatically queries AWS catalog for the freshest verified Ubuntu 22.04 LTS image ID."),
        ("Network Security Hardening", "Opens exclusively Port 22 (SSH Admin) and Port 80 (HTTP Web), dropping all other unauthorized traffic."),
        ("Immutable State Tracking", "Maintains 'terraform.tfstate' to lock resources and detect unauthorized drift in the cloud."),
        ("Automated cloud-init Injection", "Passes the bootstrap shell script as EC2 user_data to trigger Puppet initialization at first boot.")
    ]
    for idx, (h, d) in enumerate(tf_pts):
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8 if idx > 0 else 10)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 6: Puppet Configuration Management Code
    # ==========================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Configuration Management with Puppet")

    # Left: Puppet Manifest Code
    add_card(s6, 0.8, 1.8, 6.0, 5.1, C_CODE_BG, None)
    tb = s6.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(5.6), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📄 puppet/manifests/site.pp (Manifest)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = C_ACCENT_YELLOW

    puppet_text = """node default {

  # 1. Package: Install Apache Web Server
  package { 'apache2':
    ensure => installed,
  }

  # 2. Service: Enable & keep running on boot
  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Package['apache2'],
  }

  # 3. File: Deploy custom Nixtio Dashboard
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
    p2.text = puppet_text
    p2.font.name = FONT_CODE
    p2.font.size = Pt(10)
    p2.font.color.rgb = RGBColor(254, 240, 138)
    p2.space_before = Pt(8)

    # Right: Puppet Explanations
    add_card(s6, 7.0, 1.8, 5.533, 5.1)
    tb = s6.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.1), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎯 Puppet Architectural Concepts"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_PUPPET_GOLD

    pup_pts = [
        ("Declarative State Model", "Defines the desired end-state ('package must exist, service must run') rather than procedural step-by-step commands."),
        ("Dependency Graph Enforcement", "Uses 'require' to guarantee packages install before services start, preventing boot-order race conditions."),
        ("Automated Event Notification", "'notify => Service[apache2]' restarts the web server automatically only when website code changes."),
        ("Resource Abstraction Layer (RAL)", "Puppet abstracts package managers — translating to APT on Ubuntu, YUM on RedHat, and Homebrew on macOS."),
        ("Continuous Self-Healing", "If Apache is accidentally stopped, the next Puppet agent run detects the discrepancy and revives it instantly.")
    ]
    for idx, (h, d) in enumerate(pup_pts):
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8 if idx > 0 else 10)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 7: Key Concept - Idempotency & Zero Drift
    # ==========================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Core DevOps Concept: Idempotency & Zero Drift")

    # Top Concept Banner
    top_c = add_card(s7, 0.8, 1.8, 11.733, 1.35)
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(1.95), Inches(11.3), Inches(1.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "💡 What is Idempotency in Configuration Management?"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_AWS_ORANGE

    p2 = tf.add_paragraph()
    p2.text = "An operation is idempotent if running it multiple times produces the exact same result as running it once. In traditional bash scripts, running 'install' multiple times can fail or corrupt configurations. Puppet guarantees that running 100 times leaves the system in the pristine target state with zero duplicate work."
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(11)
    p2.font.color.rgb = C_TEXT_DARK
    p2.space_before = Pt(4)

    # 1st Run Card (Left)
    add_card(s7, 0.8, 3.35, 5.7, 3.55)
    tb = s7.shapes.add_textbox(Inches(1.05), Inches(3.5), Inches(5.2), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1️⃣ INITIAL EXECUTION (Run 1)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_TF_PURPLE

    r1_items = [
        ("System State Check", "Puppet evaluates node → detects apache2 missing."),
        ("Package Action", "Executes APT install → packages deployed."),
        ("Service Action", "Detects inactive daemon → starts apache2 service."),
        ("File Action", "Deploys custom Nixtio Bento Grid index.html on Port 80."),
        ("Result Report", "Changes: 3 applied, 0 failed. Desired state achieved.")
    ]
    for h, d in r1_items:
        p = tf.add_paragraph()
        p.text = f"• {h}: {d}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(5)

    # 2nd Run Card (Right)
    add_card(s7, 6.833, 3.35, 5.7, 3.55)
    tb = s7.shapes.add_textbox(Inches(7.083), Inches(3.5), Inches(5.2), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2️⃣ SUBSEQUENT EXECUTION (Run 2+)"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_SUCCESS_GREEN

    r2_items = [
        ("System State Check", "Puppet evaluates node → apache2 package already present."),
        ("Package Action", "NO-OP (skips reinstall, saves bandwidth & CPU)."),
        ("Service Action", "Detects apache2 running → NO ACTION REQUIRED."),
        ("File Action", "Checksum matches index.html → NO ACTION REQUIRED."),
        ("Result Report", "Changes: 0 applied, 0 failed → 100% IDEMPOTENT!")
    ]
    for h, d in r2_items:
        p = tf.add_paragraph()
        p.text = f"• {h}: {d}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(5)

    # ==========================================================
    # SLIDE 8: Deployment Lifecycle & Commands
    # ==========================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "CLI Deployment Lifecycle & Practical Commands")

    cli_cards = [
        ("1. terraform init", "Provider Initialization", C_TF_PURPLE, [
            "Downloads HashiCorp AWS provider (~v5.0)",
            "Configures local dependency lock (.terraform.lock.hcl)",
            "Initializes workspace backend directory"
        ]),
        ("2. terraform plan", "Execution Dry-Run", C_PUPPET_GOLD, [
            "Compares local code with live AWS cloud state",
            "Pre-calculates resources to add (Security Group + EC2)",
            "Zero cost & zero impact dry-run safety verification"
        ]),
        ("3. terraform apply", "Cloud Provisioning", C_SUCCESS_GREEN, [
            "Authenticates via AWS IAM credentials",
            "Provisions Security Group and launches Ubuntu EC2 node",
            "Executes user_data bootstrap script automatically"
        ]),
        ("4. terraform destroy", "Automated Cleanup", RGBColor(220, 38, 38), [
            "Tears down all provisioned cloud resources cleanly",
            "Eliminates unnecessary AWS billing after evaluation",
            "Guarantees complete infrastructure lifecycle control"
        ])
    ]

    for i, (cmd_title, subtitle, accent, bullets) in enumerate(cli_cards):
        top_y = 1.8 + (i % 2) * 2.65
        left_x = 0.8 if i < 2 else 6.833

        add_card(s8, left_x, top_y, 5.7, 2.45)
        tb = s8.shapes.add_textbox(Inches(left_x + 0.2), Inches(top_y + 0.15), Inches(5.3), Inches(2.15))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = cmd_title
        p.font.name = FONT_CODE
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = accent

        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = C_TEXT_DARK
        p2.space_before = Pt(2)

        for b in bullets:
            p = tf.add_paragraph()
            p.text = f"• {b}"
            p.font.name = FONT_FAMILY
            p.font.size = Pt(10)
            p.font.color.rgb = C_TEXT_MUTED
            p.space_before = Pt(4)

    # ==========================================================
    # SLIDE 9: Project Results & Verification
    # ==========================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Deployment Results & Live System Telemetry")

    # Left: Infrastructure Metrics Card
    add_card(s9, 0.8, 1.8, 6.0, 5.1)
    tb = s9.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.5), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "📊 Live AWS Node Specifications"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_TF_PURPLE

    res_items = [
        ("Cloud Provider", "Amazon Web Services (AWS)"),
        ("Deployment Region", "ap-south-1 (Mumbai, India)"),
        ("EC2 Instance ID", "i-0ed9db706fd79bab9"),
        ("Compute Tier", "t3.micro (Free Tier, 2 vCPU, 1 GB RAM)"),
        ("Operating System", "Ubuntu 22.04 LTS (Jammy Jellyfish)"),
        ("Live Public IP", "13.201.137.244"),
        ("Web Endpoint", "http://13.201.137.244 (Port 80)"),
        ("HTTP Response Code", "200 OK (Verified Live)"),
        ("Puppet Configuration", "Enforced (0 Failed, 0 Drift)")
    ]
    for idx, (k, v) in enumerate(res_items):
        p = tf.add_paragraph()
        p.text = f"• {k}: {v}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(6 if idx > 0 else 8)

    # Right: Dashboard Aesthetics Card
    add_card(s9, 7.0, 1.8, 5.533, 5.1)
    tb = s9.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.1), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🎨 Nixtio Bento Grid UI Highlights"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_AWS_ORANGE

    ui_highlights = [
        ("Dribbble-Style Bento Grid", "Rounded modular cards on warm badami / cream background with modern typography and clean drop shadows."),
        ("Interactive Ticking Uptime Ring", "SVG circular progress ring displaying real-time live server uptime and health state."),
        ("Student & Course Branding", "Features Kushagra, Roll #63, INT333, and Lovely Professional University prominently."),
        ("Idempotency Verification Button", "Interactive 'Test Drift' trigger demonstrating zero-drift state compliance.")
    ]
    for idx, (h, d) in enumerate(ui_highlights):
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8 if idx > 0 else 10)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 10: Testing & QA Matrix
    # ==========================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Test Cases & Quality Assurance Matrix")

    tests = [
        ("TC-01", "Terraform Cloud Provisioning", "Execute 'terraform apply -auto-approve'", "EC2 instance running with public IPv4", "PASS"),
        ("TC-02", "Firewall Port Inbound Access", "curl http://13.201.137.244 on Port 80", "TCP port 80 accessible; returns HTTP 200", "PASS"),
        ("TC-03", "Puppet Bootstrap Execution", "cloud-init executes bootstrap script", "Puppet Agent 8 installs & applies catalog", "PASS"),
        ("TC-04", "Apache Service Daemon Health", "systemctl status apache2 on instance", "Active (running) daemon & enabled at boot", "PASS"),
        ("TC-05", "Idempotency & Zero Drift Test", "Re-run puppet apply on configured node", "0 packages changed, 0 failures reported", "PASS")
    ]

    for i, (tc_id, tc_name, tc_input, tc_exp, tc_res) in enumerate(tests):
        top_y = 1.8 + i * 1.02
        add_card(s10, 0.8, top_y, 11.733, 0.88)

        # ID Pill
        pill = add_card(s10, 1.0, top_y + 0.18, 1.2, 0.5, C_CARD_DARK, None)
        tf = pill.text_frame
        tf.margin_top = Inches(0.08)
        p = tf.paragraphs[0]
        p.text = tc_id
        p.font.name = FONT_CODE
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_ACCENT_YELLOW
        p.alignment = PP_ALIGN.CENTER

        # Details
        tb = s10.shapes.add_textbox(Inches(2.4), Inches(top_y + 0.12), Inches(8.3), Inches(0.68))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{tc_name}  |  Action: {tc_input}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p2 = tf.add_paragraph()
        p2.text = f"Expected & Actual Result: {tc_exp}"
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = C_TEXT_MUTED

        # Status Pill
        stat_pill = add_card(s10, 10.9, top_y + 0.2, 1.4, 0.48, RGBColor(240, 253, 244), RGBColor(187, 247, 208))
        tf = stat_pill.text_frame
        tf.margin_top = Inches(0.06)
        p = tf.paragraphs[0]
        p.text = f"✓ {tc_res}"
        p.font.name = FONT_FAMILY
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_SUCCESS_GREEN
        p.alignment = PP_ALIGN.CENTER

    # ==========================================================
    # SLIDE 11: Future Scope & Conclusion
    # ==========================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "Future Scope & Project Conclusion")

    # Left: Future Scope
    add_card(s11, 0.8, 1.8, 5.7, 5.1)
    tb = s11.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.2), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🚀 Future Extensions"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_AWS_ORANGE

    f_exts = [
        ("CI/CD Pipeline Integration", "Trigger automated 'terraform plan' and 'puppet apply' on pull requests using GitHub Actions or Jenkins."),
        ("Remote State & DynamoDB Locking", "Migrate Terraform state to an AWS S3 bucket with DynamoDB state locking for enterprise team collaboration."),
        ("Multi-Tier Cluster Scaling", "Scale manifests across 5-10 nodes managing load balancers (NGINX) and databases (MySQL)."),
        ("Puppet Master / Server Mode", "Upgrade from standalone 'puppet apply' to centralized Puppet Master architecture with PuppetDB analytics.")
    ]
    for idx, (h, d) in enumerate(f_exts):
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.size = Pt(12)
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8 if idx > 0 else 10)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

    # Right: Conclusion
    add_card(s11, 6.833, 1.8, 5.7, 5.1)
    tb = s11.shapes.add_textbox(Inches(7.083), Inches(2.0), Inches(5.2), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "🏁 Conclusion & Key Learnings"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_SUCCESS_GREEN

    concls = [
        ("Complete Automation Achieved", "Demonstrated zero-touch server provisioning, reducing setup time from hours to under 2 minutes."),
        ("Zero Configuration Drift", "Puppet declarative manifests ensure systems stay in compliance without manual human intervention."),
        ("Production DevOps Proficiency", "Provides hands-on mastery of industry-standard tools (Terraform, Puppet, AWS, Linux, Git) vital for Cloud & SRE roles."),
        ("Academic Excellence", "Fully fulfills INT333 Capstone requirements with verifiable live cloud infrastructure.")
    ]
    for idx, (h, d) in enumerate(concls):
        p = tf.add_paragraph()
        p.text = f"• {h}:"
        p.font.name = FONT_FAMILY
        p.font.bold = True
        p.font.color.rgb = C_TEXT_DARK
        p.space_before = Pt(8 if idx > 0 else 10)
        p2 = tf.add_paragraph()
        p2.text = d
        p2.font.name = FONT_FAMILY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT_MUTED

    # ==========================================================
    # SLIDE 12: Thank You / Q&A Slide
    # ==========================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)

    # Center Card
    main_c = add_card(s12, 1.8, 1.0, 9.733, 5.5)
    
    # Accent top border
    bar = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.8), Inches(1.0), Inches(9.733), Inches(0.12))
    bar.fill.solid()
    bar.fill.fore_color.rgb = C_ACCENT_YELLOW
    bar.line.fill.background()

    tb = s12.shapes.add_textbox(Inches(2.2), Inches(1.4), Inches(8.9), Inches(4.8))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "Thank You!"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = C_TEXT_DARK
    p.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = "Questions & Answers (Q&A)"
    p2.font.name = FONT_FAMILY
    p2.font.size = Pt(19)
    p2.font.bold = True
    p2.font.color.rgb = C_PUPPET_GOLD
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(6)

    p3 = tf.add_paragraph()
    p3.text = "Automated Cloud Infrastructure Provisioning & Configuration Management"
    p3.font.name = FONT_FAMILY
    p3.font.size = Pt(13)
    p3.font.bold = True
    p3.font.color.rgb = C_AWS_ORANGE
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(12)

    # Info Box
    p4 = tf.add_paragraph()
    p4.text = "Presented by: Kushagra  |  Roll No. 63  |  Registration No. 12323868\nCourse: INT333 – DevOps Advance Configuration Management\nUnder the Guidance of: Harpreet Kaur (Assistant Professor, CSE)\nSchool of Computer Science and Engineering\nLovely Professional University (LPU)"
    p4.font.name = FONT_FAMILY
    p4.font.size = Pt(12.5)
    p4.font.color.rgb = C_TEXT_MUTED
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(28)

    # Save Deck
    dest = r"c:\Users\Kushagra Saxena\Desktop\devops-project\Kushagra_DevOps_Project_Badami_Bento.pptx"
    prs.save(dest)
    print(f"Badami Bento PPT generated successfully at: {dest}")

if __name__ == "__main__":
    build_presentation()
