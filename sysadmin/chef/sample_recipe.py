import chef                                                                                                                                           
import urllib3                                                                                                                                        
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)                                                                                   
nodeShow = {}                                                                                                                                         

readFile = open('D:\PyChef.json','r')
content = json.load(readFile)
readFile.close()
url=content["aws_chef_server"]["url"]
key=content["aws_chef_server"]["key"]
client=content["aws_chef_server"]["client"]
ssl_verify=content["aws_chef_server"]["ssl_verify"]

with chef.ChefAPI(url, key, client, ssl_verify):   
#with chef.ChefAPI('https://10.1.1.35:443/organizations/govindarajanv', '../../../chef/.chef/govindarajanv.key', 'govindarajanv', ssl_verify=False):   
#with chef.ChefAPI.from_config_file("../../../chef/.chef/knife.rb"):                                                                                  
        for node in chef.Node.list():                                                                                                                 
                #print ("fetching node " + node)                                                                                                      
                nodeObj = chef.Node(node)                                                                                                             
                #print ("Run List of a node:", nodeObj.run_list)                                                                                      
                nodeShow[node] = nodeObj.run_list                                                                                                     
                # Prints chef environment from node object                                                                                            
                #print (nodeObj.chef_environment)                                                                                                     
                                                                                                                                                      
                #Prints default attributes                                                                                                            
                #print (nodeObj.attributes.values())                                                                                                   
#print (nodeShow)                                                                                                                                     
print ("List of nodes with their run lists:")                                                                                                         
print ("===================================")                                                                                                         
for key, value in nodeShow.items():                                                                                                                   
        print ("Node:",key," has run List:",value)                                                                                                    
'''
###################################################                                                                                                   
#       Creation of node                                                                                                                              
###################################################                                                                                                   
                                                                                                                                                      
###################################################                                                                                                   
#       Search                                                                                                                                        
###################################################                                                                                                   
for row in chef.Search('node', 'roles:load-balancer'):                                                                                                
        pass                                                                                                                                          
        #print (row)                                                                                                                                  
print (row['automatic']['roles'])                                                                                                                     
'''
