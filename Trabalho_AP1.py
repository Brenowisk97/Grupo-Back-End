from flask import Flask, request, jsonify
import pydicom

app = Flask(__name__)

UPLOAD_FOLDER = '\\API_Dicom\\upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def anonimizador(caminho_arquivo):
    dcm_dados = pydicom.dcmread(caminho_arquivo)

    dcm_dados.PatientName = "Anônimo"
    dcm_dados.PatientID = "Anônimo"
    dcm_dados.PatientBirthDate = ""
    dcm_dados.PatientSex = ""
    dcm_dados.PatientAddress = ""
    dcm_dados.PatientAge = "999Y"

    return dcm_dados


@app.route('/', methods=['POST'])
def controle_arquivo():
    try:
        if 'arquivo_dicom' not in request.files:
            return jsonify({'error': 'Nenhum arquivo encontrado'}), 400

        arquivo_dicom = request.files['arquivo_dicom']
        nome_arquivo = arquivo_dicom.filename

        if arquivo_dicom.filename == '':
            return jsonify({'error': 'Nome de arquivo inválido'}), 400

        arquivo_anonimizado = anonimizador(arquivo_dicom)
        arquivo_anonimizado.save_as(f'./upload/anonimizado_{nome_arquivo}')

        return jsonify({'message': 'Arquivo anonimizado!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
