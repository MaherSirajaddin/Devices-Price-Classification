from flask import Flask
from flask_restful import Api, Resource, reqparse
import pickle
import warnings

warnings.simplefilter(action='ignore')

app = Flask(__name__)
api = Api(app)

# Loading the model
try:
    model_path = "model/saved_model/mobile_classifer_SVC.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print("Model not found: ", e)


# Adding all required specs to predict the mobile price
parser = reqparse.RequestParser()
parser.add_argument('battery_power', type=int, required=True)
parser.add_argument('blue', type=int, required=True)
parser.add_argument('clock_speed', type=float, required=True)
parser.add_argument('dual_sim', type=int, required=True)
parser.add_argument('fc', type=int, required=True)
parser.add_argument('four_g', type=int, required=True)
parser.add_argument('int_memory', type=int, required=True)
parser.add_argument('m_dep', type=float, required=True)
parser.add_argument('mobile_wt', type=int, required=True)
parser.add_argument('n_cores', type=int, required=True)
parser.add_argument('pc', type=int, required=True)
parser.add_argument('px_height', type=int, required=True)
parser.add_argument('px_width', type=int, required=True)
parser.add_argument('ram', type=int, required=True)
parser.add_argument('sc_h', type=int, required=True)
parser.add_argument('sc_w', type=int, required=True)
parser.add_argument('talk_time', type=int, required=True)
parser.add_argument('three_g', type=int, required=True)
parser.add_argument('touch_screen', type=int, required=True)
parser.add_argument('wifi', type=int, required=True)

class DetectMobilePrice(Resource):
    def predict_mobile_price(self, specs):
        return model.predict(specs)[0]

    def post(self):
        args = parser.parse_args()
        battery_power = args['battery_power']
        blue = args['blue']
        clock_speed = args['clock_speed']
        dual_sim = args['dual_sim']
        fc = args['fc']
        four_g = args['four_g']
        int_memory = args['int_memory']
        m_dep = args['m_dep']
        mobile_wt = args['mobile_wt']
        n_cores = args['n_cores']
        pc = args['pc']
        px_height = args['px_height']
        px_width = args['px_width']
        ram = args['ram']
        sc_h = args['sc_h']
        sc_w = args['sc_w']
        talk_time = args['talk_time']
        three_g = args['three_g']
        touch_screen = args['touch_screen']
        wifi = args['wifi']
        
        price_range = self.predict_mobile_price([[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep,
                                                mobile_wt, n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi]])
        
        return int(price_range)

api.add_resource(DetectMobilePrice, '/predict/mobile_price')

if __name__ == '__main__':
    app.run(debug=True)