import smtplib                                                                                                                                                                                                                  
from email.mime.text import MIMEText                                                                                                                                                                                            
from email.mime.multipart import MIMEMultipart                                                                                                                                                                                  
                                                                                                                                                                                                                                
# Email configuration                                                                                                                                                                                                           
sender_email = "andrew@cia.gov"                                                                                                                                                                                                 
receiver_email = "gulanemarvel@gmail.com"                                                                                                                                                                                       
                                                                                                                                                                                                                                
username = ""                                                                                                                                                                                                                   
password = "Never2"                                                                                                                                                                                                             
smtp_server = "mail.smtp2go.com"                                                                                                                                                                                                
smtp_port = 2525                                                                                                                                                                                                                
                                                                                                                                                                                                                                
# Create a multipart message                                                                                                                                                                                                    
message = MIMEMultipart('mixed')                                                                                                                                                                                                
message["From"] = sender_email                                                                                                                                                                                                  
message["To"] = receiver_email                                                                                                                                                                                                  
message["Subject"] = "MALICIOUS EMAIL PENETRATION TESTING (SOCIAL ENGINEERING ACTIVITY)"                                                                                                                                        

# Add body to the email
body = "Please feel free to join our survey for statistic analysis about brain hacking , just click the link <a href='https://ezstat.ru/statistics-link-survey'>Statistic Survey Kaspersky</a>"
message.attach(MIMEText(body, "plain"))

try:
    # Create a secure SSL/TLS connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    
    # Login to the email account
    server.login(username, password)
    
    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")

except Exception as e:
    print("An error occurred while sending the email:")
    print(str(e))
    
finally:
    # Close the SMTP connection
    server.quit()

