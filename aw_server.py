import json
from flask import Flask
from flask import request
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_file('config.json', load=json.load)


@app.route("/", methods=['GET', 'POST'])
def aw_server():
    """
    Main Flask listener that receives data from the weather station.
    :return: Empty JSON
    """

    # Get the submitted weather data
    submitted_fields = request.values.to_dict()

    # If the PASSKEY doesn't match, return. This isn't your weather station.
    if submitted_fields['PASSKEY'] != app.config['PASSKEY']:
        return {}

    # Init the MySQL connection
    mysql = MySQL()
    mysql.init_app(app)
    conn = mysql.connect()
    cursor = conn.cursor()

    # Create the SQL insertion to put the submitted data into your DB.
    insert = """INSERT INTO `weather` VALUES (NULL, '{dateutc}', {tempinf}, {humidityin}, 
    {baromrelin}, {baromabsin}, {tempf}, {humidity}, {winddir}, {windspeedmph},
    {windgustmph}, {maxdailygust}, {hourlyrainin}, {eventrainin}, {dailyrainin},
    {weeklyrainin}, {monthlyrainin}, {totalrainin}, {solarradiation}, {uv})""".format(
        dateutc=submitted_fields['dateutc'],
        tempinf=submitted_fields['tempinf'],
        humidityin=submitted_fields['humidityin'],
        baromrelin=submitted_fields['baromrelin'],
        baromabsin=submitted_fields['baromabsin'],
        tempf=submitted_fields['tempf'],
        humidity=submitted_fields['humidity'],
        winddir=submitted_fields['winddir'],
        windspeedmph=submitted_fields['windspeedmph'],
        windgustmph=submitted_fields['windgustmph'],
        maxdailygust=submitted_fields['maxdailygust'],
        hourlyrainin=submitted_fields['hourlyrainin'],
        eventrainin=submitted_fields['eventrainin'],
        dailyrainin=submitted_fields['dailyrainin'],
        weeklyrainin=submitted_fields['weeklyrainin'],
        monthlyrainin=submitted_fields['monthlyrainin'],
        totalrainin=submitted_fields['totalrainin'],
        solarradiation=submitted_fields['solarradiation'],
        uv=submitted_fields['uv']
    )

    # Execute the insert
    cursor.execute(insert)
    conn.commit()

    # Done!
    return {}
