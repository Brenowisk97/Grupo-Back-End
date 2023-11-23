from totalsegmentator.python_api import totalsegmentator
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/segmentacao', methods=['POST'])
def perform_segmentation():

    data = request.json
    input_path = data.get('input_path')
    output_path = data.get('output_path')
    segmentation_task = data.get('task')
    lista_orgaos = data.get('lista de orgaos', [])
    estatisticas = data.get('estatisticas', False)
    fast_mode = data.get('fast mode', False)


    totalsegmentator(input_path, output_path, task=segmentation_task, roi_subset=lista_orgaos,
                     statistics=estatisticas, fast=fast_mode)

    # Return a response
    response = {
        'status': 'sucesso!',
        'message': 'Segmentacao realizada',
        'output_path': output_path
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

