from flask import Flask, request, render_template ,redirect
from flask_cors import cross_origin

# import get_allMan

app = Flask(__name__)
list_arr = []
loopTurn = True
score = {'1' : 0 , "2" : 0}

@app.route('/', methods=['GET', 'POST'])
@cross_origin()

def home():
    global loopTurn  # Declare loopTurn as a global variable
    x = request.form.get('x')
    if x is not None:
        for i in range(8):
            new_data = {"x" : int(x)+1 , "y" : 8-i , 'color': '#BF2232' if loopTurn else '#950740'}
            new_data2 = {"x" : int(x)+1 , "y" : 8-i , 'color': '#950740' if loopTurn else '#BF2232'}
            if new_data not in list_arr and new_data2 not in list_arr:
                list_arr.append(new_data)
                break
    
        loopTurn = not loopTurn
    resulte = check_win(list_arr)   
    return render_template("index.html", title="My Home Page" , list_arr=list_arr , resulte=resulte , turn=loopTurn , score=score)

@app.route('/clear', methods=['POST'])
@cross_origin()
def clear():
    list_arr.clear()
    return redirect('/')

@app.route('/restart', methods=['POST'])
@cross_origin()
def restart():
    list_arr.clear()
    score['1'] = 0
    score['2'] = 0
    return redirect('/')


def check_win(board):
    for i in ['#BF2232' , '#950740']:
        filtered_list = [[item.get('x'),item.get('y')] for item in list_arr if item.get("color") == i]
        print(filtered_list)
        for item in filtered_list:
            x = item[0]
            y = item[1]
            list_corecte = [
            [[x-1,y],[x,y],[x+1,y],[x+2,y]],
            [[x,y+1],[x,y],[x,y-1],[x,y-2]],
            [[x-1,y+1],[x,y],[x+1,y-1],[x+2,y-2]],
            [[x-2,y-2],[x-1,y-1],[x,y],[x+1,y+1]]
            ]
            for e in list_corecte:
                if all(j in filtered_list for j in e):
                    if i == '#BF2232':
                        score['1'] += 1
                        return {'win' : "Player 1" }
                    else:
                        score['2'] += 1
                        return {'win' : "Player 2" }
    return False
        



if __name__ == '__main__':
    app.run(debug=True)
