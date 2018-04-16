with chef.ChefAPI('https://10.1.1.35:443', '../../chef/.chef/govindarajanv.key', 'client'):
    for node in chef.Node.list():
            print "fetching node " + node
            nodeObj = chef.Node(node)
            print ("Run List of a node:", nodeObj.run_list())
