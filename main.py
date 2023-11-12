from graph import Graph
import json

def create_question(question):
    question = question.split("'")
    final = []
    for part in question:
        part = part.lower().strip('?').strip(" ")
        final.append(part)
    return final

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    data = read_json('data.json')
    G = Graph(len(data['edges'])+1)
    for item in data['edges']:
        vtx = item['to']
        vertex = G.get_vertex()
        G.set_vertex(vtx)

        G.set_vertex(item['frm'])
        G.set_edge(item['frm'], item['to'], item['value'])


    print(G.get_vertex())
    question = input("Введите запрос: ")
    fin = create_question(question)
    print(fin)


    if (len(fin)<4):
        res = G.BFS(fin[1], fin[1], 'ako')
        print(res)
    else:
        res = G.BFS(fin[1], fin[3], fin[0])
        if (res == True):
            print("Да")
        elif (res == []):
            print("Нет")
