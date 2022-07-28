def solution(routes):
    answer = 0
    camera = []
    routes.sort(key = lambda x:x[1])
    
    for route in routes :
        if len(camera) > 0 :
            flag = True
            for i in camera :
                if route[0] <= i <= route[1] :
                    flag = False
                    break
            if flag == True :
                camera.append(route[1])
        else :
            camera.append(route[1])
    
    return len(camera)