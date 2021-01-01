from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method=="POST":
        resp = request.form
        resp.get('record')
        import speech_recognition as sr

        # get audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)

        try:
            output = " " + r.recognize_google(audio)

        except sr.UnknownValueError:
            output = "Could not understand audio"
        except sr.RequestError as e:
            output = "Could not request results; {0}".format(e)

        return render_template('input.html', data=output)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
