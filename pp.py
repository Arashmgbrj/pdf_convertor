import asposewordscloud

words_api = WordsApi(client_id = '####-####-####-####-####', client_secret = '##################')

doc = open('Input.pdf', 'rb')
request = asposewordscloud.models.requests.ConvertDocumentRequest(document=doc, format='docx')
convert = words_api.convert_document(request)