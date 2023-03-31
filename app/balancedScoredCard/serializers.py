from rest_framework import serializers
from .models import Perspective,Objective, Indicator, Bsc, Control

class PerspectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perspective
        fields = '__all__'

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class ObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objective
        fields = '__all__'  
      
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['perspective'] = {'id_perspective': 
        instance.perspective.id,'name':instance.perspective.name}
        ret['indicator'] = {'id_indicator': 
        instance.indicator.id,'name':instance.indicator.name}
        return ret

class BscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bsc
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['Id_Objetivo'] = {'id_objetivo': 
        instance.Id_Objetivo.id,'name':instance.Id_Objetivo.name}
        ret['perspectiva']= {'id_perspectiva': 
        instance.Id_Objetivo.perspective.id,'name':instance.Id_Objetivo.perspective.name}
        ret['Id_Indicator'] = {'id_indicador': 
        instance.Id_Indicator.id,'name':instance.Id_Indicator.name}
        ret['Id_emprendedor'] = {'id_emprendedor': 
        instance.Id_emprendedor.id,'name':instance.Id_emprendedor.entrepreneur}
        return ret
        
"""
    def create(self, validated_data):
        
       # Create and return a new `Snippet` instance, given the validated data.
       
        #(validated_data.get('bsc'))
        peso_bsc = self.validated_data['peso']
        peso_suma = 0
        bsc_list = list(Bsc.objects.all().filter(bsc=bsc_model.id,state = 'A'))
        
        if len(control_list) > 0:
            for e in control_list:
              
                avance_suma += (e.avance * e.peso_actividad)/100
                peso_suma += e.peso_actividad

            peso_suma += peso_actividad
            avance_suma += (peso_actividad * avance)/100
            if peso_suma > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_suma)/100
           
           # bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_suma
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
                 
            bsc.save()
        else:

            if peso_actividad > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            avance_actividad = (peso_actividad * avance)/100
            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_actividad)/100
            #bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_actividad
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado

            bsc.save()

        return Control.objects.create(**validated_data)


    def update(self, instance, validated_data):
      
        #Update and return an existing `Snippet` instance, given the validated data.
        
        instance.state = validated_data.get('state', instance.state)
        instance.id_user_created = validated_data.get('id_user_created', instance.id_user_created)
        instance.id_user_modified = validated_data.get('id_user_modified', instance.id_user_modified)
        instance.actividad = validated_data.get('actividad', instance.actividad)
        instance.fecha_inicio = validated_data.get('fecha_inicio', instance.fecha_inicio)
        instance.fecha_fin = validated_data.get('fecha_fin', instance.fecha_fin)
        instance.peso_actividad = validated_data.get('peso_actividad', instance.peso_actividad)
        instance.avance = validated_data.get('avance', instance.avance)
        instance.bsc = validated_data.get('bsc', instance.bsc)

         #(validated_data.get('bsc'))
        bsc_model = self.validated_data['bsc']
        avance = self.validated_data['avance']
        peso_actividad = self.validated_data['peso_actividad']
        avance_suma = 0
        peso_suma = 0
      
        control_list = list(Control.objects.all().filter(bsc=bsc_model.id,state = 'A').exclude(id=instance.id))
        
        if len(control_list) > 0:
            for e in control_list:
                
                avance_suma += (e.avance * e.peso_actividad)/100
                peso_suma += e.peso_actividad

            peso_suma += peso_actividad
            avance_suma += (peso_actividad * avance)/100
            if peso_suma > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_suma)/100
            
           # bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_suma
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
                 
            bsc.save()
        else:
            if peso_actividad > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            avance_actividad = (peso_actividad * avance)/100
            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_actividad)/100
            #bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_actividad
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
            bsc.save()

        instance.save()
        return instance
"""
class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['bsc'] = {'id_bsc': 
        instance.bsc.id,'peso':instance.bsc.peso,
        'peso_avance':instance.bsc.peso_avance,
        'peso_alcanzado':instance.bsc.peso_alcanzado,
        'id_objetivo':instance.bsc.Id_Objetivo.id,
        'objetivo':instance.bsc.Id_Objetivo.name,
        'id_indicador':instance.bsc.Id_Indicator.id,
        'nombre_indicador':instance.bsc.Id_Indicator.name,
        'id_emprendedor':instance.bsc.Id_emprendedor.id,
        'emprendedor':instance.bsc.Id_emprendedor.entrepreneur
        }

        return ret

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        #(validated_data.get('bsc'))
        bsc_model = self.validated_data['bsc']
        avance = self.validated_data['avance']
        peso_actividad = self.validated_data['peso_actividad']
        avance_suma = 0
        peso_suma = 0
        print(bsc_model)
        control_list = list(Control.objects.all().filter(bsc=bsc_model.id,state = 'A'))
        
        if len(control_list) > 0:
            for e in control_list:
              
                avance_suma += (e.avance * e.peso_actividad)/100
                peso_suma += e.peso_actividad

            peso_suma += peso_actividad
            avance_suma += (peso_actividad * avance)/100
            if peso_suma > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_suma)/100
           
           # bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_suma
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
                 
            bsc.save()
        else:

            if peso_actividad > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            avance_actividad = (peso_actividad * avance)/100
            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_actividad)/100
            #bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_actividad
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado

            bsc.save()

        return Control.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.state = validated_data.get('state', instance.state)
        instance.id_user_created = validated_data.get('id_user_created', instance.id_user_created)
        instance.id_user_modified = validated_data.get('id_user_modified', instance.id_user_modified)
        instance.actividad = validated_data.get('actividad', instance.actividad)
        instance.fecha_inicio = validated_data.get('fecha_inicio', instance.fecha_inicio)
        instance.fecha_fin = validated_data.get('fecha_fin', instance.fecha_fin)
        instance.peso_actividad = validated_data.get('peso_actividad', instance.peso_actividad)
        instance.avance = validated_data.get('avance', instance.avance)
        instance.bsc = validated_data.get('bsc', instance.bsc)

         #(validated_data.get('bsc'))
        bsc_model = self.validated_data['bsc']
        avance = self.validated_data['avance']
        peso_actividad = self.validated_data['peso_actividad']
        avance_suma = 0
        peso_suma = 0
      
        control_list = list(Control.objects.all().filter(bsc=bsc_model.id,state = 'A').exclude(id=instance.id))
        
        if len(control_list) > 0:
            for e in control_list:
                
                avance_suma += (e.avance * e.peso_actividad)/100
                peso_suma += e.peso_actividad

            peso_suma += peso_actividad
            avance_suma += (peso_actividad * avance)/100
            if peso_suma > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_suma)/100
            
           # bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_suma
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
                 
            bsc.save()
        else:
            if peso_actividad > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            avance_actividad = (peso_actividad * avance)/100
            peso_bsc = bsc_model.peso
            peso_alcanzado = (peso_bsc * avance_actividad)/100
            #bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=bsc_model.id)
            bsc.peso_alcanzado = avance_actividad
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
            bsc.save()

        instance.save()
        return instance

    def delete(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.state = 'I'
        instance.id_user_modified = self.validated_data['id_user_modified']

         #(validated_data.get('bsc'))
        avance_suma = 0
        peso_suma = 0
      
        control_list = list(Control.objects.all().filter(bsc=bsc_model.id,state = 'A').exclude(id=instance.id))
        print(control_list)
        if len(control_list) > 0:
            for e in control_list:
                
                avance_suma += (e.avance * e.peso_actividad)/100
                peso_suma += e.peso_actividad

            if peso_suma > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

           
          
           # bsc_model.update(peso_alcanzado=peso_alcanzado,peso_avance=avance_actividad)
            bsc = Bsc.objects.get(id=instance.bsc.id)
            peso_bsc = bsc.peso
            peso_alcanzado = (peso_bsc * avance_suma)/100
            bsc.peso_alcanzado = avance_suma
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = peso_alcanzado
                 
            bsc.save()
        else:
            if peso_actividad > 100:
                raise serializers.ValidationError("El peso de las actividades no puede ser mayor a 100%")

            bsc = Bsc.objects.get(id=instance.bsc.id)
            bsc.peso_alcanzado = 0
           # bsc.peso_avance = (peso_alcanzado * bsc.peso)/100
            bsc.peso_avance = 0
            bsc.save()

        instance.save()
        return instance

    