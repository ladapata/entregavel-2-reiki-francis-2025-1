import rclpy
from rclpy.node import Node

from example_interfaces.srv import SetBool # esse serviço é atualizado aleatoriamente
from std_msgs.msg import Float64 # esse tópico é atualizado a cada 0,5s

temperaturas = []
# fila criada pra armazenar as temperaturas publicadas

class temperature_monitor(Node):
  def __init__(self):
    super().__init__('temperature_monitor')

# SERVER (/reset_average para average_reset_client)
    self.srv = self.create_service(SetBool, 'reset_average', self.reset_average_callback.callback)

# PUBLISHER (/average_temperature para temperature_avg_monitor)
    self.publisher_ = self.create_publisher(Float64, 'average_temperature', 10)
    timer_period = 0.5
    self.timer = self.create_timer(timer_period, self.timer_callback)

# SUBSCRIBER (/temperature para temperature_publisher)
    self.subscription = self.create_subscription(Float64, 'temperature', self.listener_callback, 10)
    self.subscription

#=============================================================================================
#=============================================================================================

  def set_bool_callback(self, request, response):
    if request == True: # se o valor que average_reset_client for True \/
      temperaturas.clear() # limpa a lista
      self.get_logger().info('Média reiniciada!')
      response.data = True # retorna True para o nó average_reset_client 
      return response

#=============================================================================================
#=============================================================================================

  def timer_callback(self):
    msg = Float64()
    if len(temperaturas) == 5: # verifica se a lista já possui 5 elementos
      i = 0
      while i < 4:
        pre_media += temperaturas[i] # calcula o dividendo da média aritmética
        i+=1
      msg.data = pre_media/5 # coloca a média no campo de dados da mensagem
    else:
      msg.data = float('nan') # coloca NaN (Not a Number) no campo de dados da mensagem
      self.get_logger().info('Sem dados suficientes, aguardando...')
    self.publisher_.publish(msg)

#=============================================================================================
#=============================================================================================

  def listener_callback(self, msg):
    self.get_logger().info('Temperatura recebida é de "%f" graus Célsius.' % msg.data)
    if len(temperaturas) >= 5: # checa se tem 5 ou mais elementos na fila
      self.temperaturas.pop(0) # se for verdade, remove o mais antigo (elemento mais à esquerda)
    self.temperaturas.append(msg.data) # adiciona o elemento recebido ao final da lista (à direita)

#=============================================================================================
#=============================================================================================
#=============================================================================================

def main():
  rclpy.init()

  temperature_monitor = temperature_monitor()
  
  rclpy.spin(temperature_monitor)

#=============================================================================================
#=============================================================================================
#=============================================================================================

if __name__ == '__main__':
  main()
