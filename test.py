from fpdf import FPDF

border = 0

pdf = FPDF()
pdf.add_font('Garamond', '', '.\\GARA.TTF', uni=True)
pdf.add_font('Garamond Bold', '', '.\\GARABD.TTF', uni=True)
pdf.add_font('Garamond Italic', '', '.\\GARAIT.TTF', uni=True)
pdf.add_font('Segoe UI Light', '', '.\\SEGOEUIL.TTF', uni=True)
pdf.add_font('Segoe UI Black', '', '.\\SEGUIBL.TTF', uni=True)
pdf.add_font('Segoe UI', '', '.\\SEGOEUI.TTF', uni=True)

def multi_align_cell(w, h, text, border=0, ln=0, align='L', fill=False):
   '''
   MultiCell with alignment as in Cell
   '''
   x = pdf.get_x() + w
   y = pdf.get_y()

   pdf.multi_cell(w, h, text, border, align, fill)
   if ln == 0:
      pdf.set_xy(x, y)

def add_title(name, address, phone_number, email):
   '''
   Gives resume a title

   Puts the name at the top as the title to the resume

   Parameters:
   name (string): Person's Name
   address (string): Person's Address
   phone_number (string): Person's Phone Number
   email (string): Person's Email

   Returns:
   void: N/A
   '''
   pdf.set_font('Segoe UI Black', '', 27)
   pdf.set_text_color(194,8,8)
   pdf.cell(0, 10, name, border, 1, 'C')
   pdf.set_text_color(0, 0, 0)
   pdf.set_font('Segoe UI', '', 11)
   pdf.cell(0, 5, '{} | P: {} | {}'.format(address, phone_number, email), border, 1, 'C')
   pdf.ln()

def add_profile(description):
   '''
   Gives resume a profile

   Puts the profile statement section on the resume

   Parameters:
   description (string): Statement for the profile section

   Returns:
   void: N/A
   '''
   pdf.set_font('Segoe UI Black', '', 27)
   pdf.set_text_color(194,8,8)
   pdf.cell(0, 7, 'PROFILE', border, 1, 'L')
   pdf.set_text_color(0, 0, 0)
   pdf.set_font('Segoe UI Light', '', 11)
   pdf.multi_cell(0, 4, description, border, 'L')
   pdf.ln()

def add_areas_of_expertise(*descriptions):
   '''
   Gives resume a list of expertise
   '''
   pdf.set_font('Segoe UI Black', '', 23)
   pdf.set_text_color(194,8,8)
   pdf.cell(0, 7, 'AREAS OF EXPERTISE', border, 1, 'L')
   pdf.set_text_color(0, 0, 0)
   pdf.set_font('Segoe UI Light', '', 11)
   position = False
   for description in descriptions:
      multi_align_cell(95, 4, '{} {}'.format(chr(127), description), border, 0 if position == False else 1, 'L')
      position = not position
   
   pdf.ln()
   pdf.ln()

def add_resume_subsection(job, title, startDate, endDate = 'PRESENT', *duties):
   pdf.set_font('Segoe UI Black', '', 11)
   pdf.set_text_color(204, 153, 0)
   cellWidth = pdf.get_string_width(job)
   pdf.cell(cellWidth, 4, job, border, 0, 'L')
   pdf.set_font('Segoe UI Light', '', 11)
   pdf.set_text_color(0, 0, 0)
   pdf.cell(0, 4, ' - {}'.format(title), border, 1, 'L')
   pdf.set_font('Segoe UI Light', '', 8)
   pdf.set_text_color(194, 8, 8)
   pdf.cell(0, 4, '{} - {}'.format(startDate, endDate), border, 1, 'L')
   pdf.set_text_color(0, 0, 0)
   pdf.set_font('Segoe UI Light', '', 11)
   for duty in duties:
      multi_align_cell(0, 4, '{} {}'.format(chr(127), duty), border, 1, 'L')
   
   pdf.ln()

pdf.add_page()
add_title('FAUSTO ARIEL LORENZO', '16 Dix St., Worcester, MA, 01609', '774-329-6395', 'ariellorenzo08@gmail.com')
add_profile('IT customer service specialist with knowledge and hands-on experience in all aspects of web development and system administration. Enthusiastic team player and willing to go above and beyond to make sure the work is done efficiently.')
add_areas_of_expertise('Excellent programming and design skills',
   'Strong collaborative and problem-solving skills',
   'Strong system administration knowledge',
   'ASP.NET MVC and WebForms, Django, Flask, PHP/MySQL',
   'Proficient in Python, C#, PHP, SQL, JavaScript, React, Vue,VB.NET, HTML, CSS, AJAX, XML, C, Java',
   'Bash, PowerShell')
pdf.set_font('Segoe UI Black', '', 23)
pdf.set_text_color(194,8,8)
pdf.cell(0, 7, 'EXPERIENCE', border, 1, 'L')
pdf.set_text_color(0, 0, 0)
add_resume_subsection('KP & Sons Automotive', 'Customer Support', 'NOVEMBER 2019', 'MARCH 2020',
   'Activate and manage the infrastructure of the devices in the office, including networking, computer maintenance',
   'Manage and assist in website creation (SVG, Wordpress)',
   'Assist in company advertising and graphic design (SVG)')
add_resume_subsection('Keypoint Intelligence', 'Back-End Systems Engineer', 'JANUARY 2018', 'NOVEMBER 2018',
   'Built back-end database SQL Server functions and procedures for the company website, bliQ (SQL, SQL Server)',
   'Assist in the overall change of the back-end intranet applications (ASP.NET WebForms, C#, VB.NET)',
   'Drastically improve runtime and execution of procedures and functions (SQL Server, T-SQL)')
add_resume_subsection('SAI Global', 'Software Engineer', 'MAY 2017', 'OCTOBER 2017',
   'Built and deployed a large amount of web courses (HTML5, JavaScript, XML)',
   'Repaired and made recommendations on courses built either by me or other employees (HTML5, JavaScript, XML)')
add_resume_subsection('Information Systems, Southern Adventist University', 'Software Engineer', 'MAY 2016', 'JANUARY 2017',
   'Recreated the back-end functionality for the university account login site still used today (ASP.NET MVC, C#,, HTML5,CSS,JavaScript, jQuery)',
   'Design front-end view of main site search for students that is still used today (ASP.NET MVC, C#, Bootstrap, HTML5,CSS,JavaScript, jQuery)',
   'Assist in project planning and fix current projects (ASP.NET MVC, C#, Angular, HTML5, CSS, JavaScript, jQuery)')
add_resume_subsection('School of Education & Psychology, Southern Adventist University', 'Computer Lab Manager', 'SEPTEMBER 2015', 'AUGUST 2016',
   'Assessed customer needs and made recommendations',
   'Implemented agreed upon solutions and employee rotation schedule',
   'Changed the look and content of the department site (HTML, CSS)')
add_resume_subsection('Online Campus, Southern Adventist University', 'Web Programming Specialist', 'MAY 2015', 'JANUARY 2016',
   'Created back-end functionality for the university web tools online directory still used today (PHP/MySQL, C#, .NET)',
   'Made recommendations on web software for online classes that are still used today (PHP/MySQL)')
pdf.set_font('Segoe UI Black', '', 23)
pdf.set_text_color(194,8,8)
pdf.cell(0, 7, 'EDUCATION', border, 1, 'L')
pdf.set_text_color(0, 0, 0)
add_resume_subsection('Southern Adventist University, Collegedale, TN', 'B.S. Computer Systems Administration', 'JULY 2011', 'DECEMBER 2016',
   'Coursework in networking, programming, software development, computer architectures, databases, server administration, and virtualization')
pdf.output('result.pdf', 'F')