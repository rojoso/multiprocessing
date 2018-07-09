from multiprocessing import Process,Pipe

def f(conn):
	conn.send([66,None,'hello word'])

	conn.close()

if __name__ == '__main__':
	parent_conn,child_conn = Pipe() #管道的生成都是返回两个实例的，分别为发送管道和接受管道，而发送管道指的是向文件发送的那一侧

	p = Process(target = f,args = (child_conn,))

	p.start()
	print(parent_conn.recv())

	p.join()

