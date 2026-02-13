#----------------------------------------------------------------------
#	1. Construccion de redis
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Construir una imagen de redis
# Asignar un nombre al contenedor
# Asignar un tag mediante la variable
#----------------------------------------------------------------------

REDIS_TAG=3
REDIS_CONTAINER_NAME=redis
REDIS_IMAGE_NAME=redis

#Construccion y despliegue de redis
build_redis: ## Construccion y despliegue de redis
	@echo 'Construccion de redis con TAG=$(REDIS_TAG)'
	docker pull $(REDIS_IMAGE_NAME):$(REDIS_TAG)
	@echo 'Ejecucion de un contenedor de ${REDIS_IMAGE_NAME} con el nombre $(REDIS_CONTAINER_NAME)'
	docker run -d --name $(REDIS_CONTAINER_NAME) $(REDIS_IMAGE_NAME):$(REDIS_TAG)

#----------------------------------------------------------------------
# Visualizar todas las imagenes de docker
# Visualizar contenedores activos
# Visualizar contenedores inactivos
#----------------------------------------------------------------------

show_images_containers: ## Visualizacion de redis
	@echo 'Imagenes de docker'
	docker images -a
	@echo ''
	@echo 'Contenedores en ejecucion'
	docker ps --filter status=running
	@echo ''
	@echo 'Contenedores fuera de ejecucion'
	docker ps --filter status=exited

#----------------------------------------------------------------------
# Eliminar el contenedor de redis
# Visualizar de nuevo
#----------------------------------------------------------------------

delete_redis: ## Eliminacion de redis
	@echo 'Parar redis'
	docker stop $(REDIS_CONTAINER_NAME)
	@echo 'Eliminacion del contenedor $(REDIS_CONTAINER_NAME)'
	docker rm $(REDIS_CONTAINER_NAME)
	@echo 'Eliminacion de la imagen $(REDIS_IMAGES_NAME)'
	docker rmi $(REDIS_IMAGE_NAME):$(REDIS_TAG)
	@echo 'Verificacion final'
	docker ps -a


#----------------------------------------------------------------------
# 2. DESPLIEGUE DEL MONITOR
#----------------------------------------------------------------------

#Construccion del monitor 
build_monitor_prometheus: ## Despliegue de Prometheus
	@echo 'Construccion y despliegue de Prometheus'
	cd monitor/prometheus && docker-compose up -d

build_monitor_grafana: ## Despliegue de Grafana
	@echo 'Construccion y despliegue de Grafana'
	cd monitor/grafana && docker-compose up -d

build_monitor_redis: ## Despliegue de Redis
	@echo 'Construccion y despliegue de Redis'
	cd monitor/redis && docker-compose up -d

build_monitor_redis_exporter: ## Despliegue de Redis-Exporter
	@echo 'Construccion y despliegue de Redis-Exporter'
	cd monitor/redis-exporter && docker-compose up -d

build_monitor: ## Despliegue de todos los contenedores del monitor
	@echo 'Contenedores en ejecucion'
	docker ps -a
	$(MAKE) build_monitor_prometheus
	$(MAKE) build_monitor_grafana
	$(MAKE) build_monitor_redis
	$(MAKE) build_monitor_redis_exporter
	@echo 'Contenedores en ejecucion'
	docker ps -a

# Parar los servicios del monitor
stop_monitor_prometheus: ## Parar Prometheus
	@echo 'Parar Prometheus'
	cd monitor/prometheus && docker-compose stop prometheus

stop_monitor_grafana: ## Para Grafana
	@echo 'Parar Grafana'
	cd monitor/grafana && docker-compose stop grafana

stop_monitor_redis: ## Para Redis
	@echo 'Parar Redis'
	cd monitor/redis && docker-compose stop redis

stop_monitor_redis_exporter: ## Parar Redis-Exporter
	@echo 'Parar Redis-Exporter'
	cd monitor/redis-exporter && docker-compose stop redis-exporter

stop_monitor: ## Parar la ejecucion de los contenedores del monitor
	@echo 'Contenedores en ejecucion'
	docker ps -a 
	@echo 'Parar todos los servicios del monitor'
	$(MAKE) stop_monitor_prometheus
	$(MAKE) stop_monitor_grafana
	$(MAKE) stop_monitor_redis
	$(MAKE) stop_monitor_redis_exporter
	@echo 'Contenedores en ejecucion'
	docker ps -a

#Eliminar los servicios del monitor
down_monitor_prometheus: ## Eliminar servicio de Prometheus
	@echo 'Eliminar servicio de Prometheus'
	cd monitor/prometheus && docker-compose down

down_monitor_grafana: ## Eliminar servicio de Grafana
	@echo 'Eliminar servicio de Grafana'
	cd monitor/grafana && docker-compose down

down_monitor_redis: ## Eliminar servicio de Redis
	@echo 'Eliminar servicio de Redis'
	cd monitor/redis && docker-compose down

down_monitor_redis_exporter: ## Eliminar servicio de Redis-Exporter
	@echo 'Eliminar servicio de Redis-Exporter'
	cd monitor/redis-exporter && docker-compose down

down_monitor: ## Eliminar la ejecucion de los contenedores del monitor
	@echo 'Contenedores en ejecucion'
	docker ps -a
	@echo 'Eliminar todos los servicios del monitor'
	$(MAKE) down_monitor_prometheus
	$(MAKE) down_monitor_grafana
	$(MAKE) down_monitor_redis
	$(MAKE) down_monitor_redis_exporter
	@echo 'Contenedores en ejecucion'
	docker ps -a


.PHONY: help
help: ## Comando de ayuda
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'


#----------------------------------------------------------------------
# 3. DESPLIEGUE DE ELK
#----------------------------------------------------------------------

build_elk: #Construccion y despliegue de ELK
	@echo 'Construccion de ELK'
	cd ELK && docker-compose build
	@echo 'Despliegue de ELK'
	cd ELK && docker-compose up -d

stop_elk: ##Parar ELK
	@echo 'Parar ELK'
	cd ELK && docker-compose stop

start_elk: ##Iniciar ELK
	@echo 'Iniciar ELK'
	cd ELK && docker-compose start

restart_elk: ##reiniciar ELK
	@echo 'Reiniciar ELK'
	$(MAKE) stop_elk
	$(MAKE) start_elk
	docker ps -a

show_elk: ##Mostrar ELK
	@echo 'Imagenes de docker'
	docker images -a 
	@echo 'Contenedores en ejecucion'
	docker ps --filter status=running
	@echo 'Contenedores fuera de ejecucion'
	docker ps --filter status=exited	

ELASTICSEARCH_IMAGE=elasticsearch:9.2.3
LOGSTASH_IMAGE=logstash:9.2.3
KIBANA_IMAGE=kibana:9.2.3

deep_delete_elk: ##Eliminar ELK
	@echo 'Eliminacion profunda de ELK'
	$(MAKE) show_elk
	@echo 'Eliminacion de ELK'
	cd ELK && docker-compose down
	@echo 'Eliminacion de las imagenes de ELK'
	docker rmi $(ELASTICSEARCH_IMAGE) $(LOGSTASH_IMAGE) $(KIBANA_IMAGE)
	$(MAKE) show_elk


#----------------------------------------------------------------------
# 4. DESPLIEGUE DE CADVISOR
#----------------------------------------------------------------------

CADVISOR_IMAGE=google/cadvisor
CADVISOR_TAG=v0.33.0
CADVISOR_NAME_CONTAINER=cadvisor
CADVISOR_PATH=.

build_cadvisor: ##Construccion y despliegue de cAdvisor
	@echo 'Construccion y despliegue de cAdvisor $(CADVISOR_IMAGE):$(CADVISOR_TAG)'
	docker pull $(CADVISOR_IMAGE):$(CADVISOR_TAG)
	@echo 'Ejecucion de $(CADVISOR_IMAGE)'
	docker run -dp 8080:8080 --name $(CADVISOR_NAME_CONTAINER) $(CADVISOR_IMAGE):$(CADVISOR_TAG)

save_cadvisor: ##Guardar la imagen de cAdvisor
	@echo 'Guardando la imagen de cAdvisor'
	docker save $(CADVISOR_IMAGE):$(CADVISOR_TAG) | gzip > $(CADVISOR_PATH)/cadvisor.tar.gz

load_cadvisor: ##Cargar la imagen de cAdvisor y ejecutarla
	@echo 'Cargando la imagen de cAdvisor'
	gunzip -c $(CADVISOR_PATH)/cadvisor.tar.gz | docker load
	@echo 'Ejecucion de $(CADVISOR_IMAGE)'
	docker run -dp 8080:8080 --name $(CADVISOR_NAME_CONTAINER) $(CADVISOR_IMAGE):$(CADVISOR_TAG)

delete_cadvisor: ## Eliminación de contenedores y imagenes de cadvisor
	docker rm -f $(CADVISOR_NAME_CONTAINER)
	docker rmi $(CADVISOR_IMAGE):$(CADVISOR_TAG)

proceso_completo: ## Proceso completo de despliegue
	@echo 'Despliegue completo'
	$(MAKE) build_cadvisor
	$(MAKE) save_cadvisor
	$(MAKE) delete_cadvisor
	$(MAKE) load_cadvisor

