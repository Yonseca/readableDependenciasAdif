import requests

# Using the looooooong URL so it does not convert ":" into "%-like" format
url = "https://ideadif.adif.es/gservices/Tramificacion/wfs?request=GetFeature&service=WFS&version=2.0.0&typename=Tramificacion:Dependencias"

def main():
    output_formats = ["text/csv", "json", "kml"]
    for output_format in output_formats:
        get_file_as(output_format)

def get_file_as(output):
    full_url = url + "&outputFormat=" + output
    print("URL: " + full_url)

    r = requests.get(full_url)
    output_filename = "files/DependenciasAdif" + get_extension(output)
    with open(output_filename, "w") as file:
        print("Generating " + output_filename)
        for lines in r.text:
            file.write(lines)

def get_extension(output):
    match output:
        case "text/csv":
            return ".csv"
        case "json":
            return ".json"
        case "kml":
            return ".kml"
        case _:
            return ""

if __name__ == "__main__":
    main()