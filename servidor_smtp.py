import smtplib

servidor_email = smtplib.SMTP('smtp.gmail.com',587)

print(servidor_email.starttls())

servidor_email.login("gmail.com", 'senha')

remetente = '...'
destinatarios = ['...']

conteudo = '...'

servidor_email.sendmail(remetente, destinatarios, conteudo)

servidor_email.quit()