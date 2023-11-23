from totalsegmentator.python_api import totalsegmentator
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/segmentacao', methods=['POST'])
def perform_segmentation():

    data = request.json
    input_path = data.get('input_path')
    output_path = data.get('output_path')
    segmentation_task = data.get('task')
    organs = data.get('organs', [])
    statistics = data.get('statistics', False)
    fast_mode = data.get('fast mode', False)

    if segmentation_task != "total":
        totalsegmentator(input_path, output_path, task=segmentation_task,
                        statistics=statistics, fast=fast_mode)
    else:
        if len(organs) == 0:
            totalsegmentator(input_path, output_path, task=segmentation_task,
                         statistics=statistics, fast=fast_mode)
        else:
            totalsegmentator(input_path, output_path, task=segmentation_task, roi_subset=organs,
                     statistics=statistics, fast=fast_mode)


    # Return a response
    response = {
        'status': 'sucesso!',
        'message': 'Segmentacao realizada',
        'output_path': output_path
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

