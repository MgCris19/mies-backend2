from rest_framework import serializers
from app.entrepreneurcourses.models  import EntrepreneurCourse
from app.entrepreneur.models import Entrepreneur

class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'

class EntrepreneurCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurCourse
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'state': instance.state,
            'observations': instance.observations,
            'type_observation': instance.type_observation,
            'course': instance.course.id,
            'course_name': instance.course.name,
            'entrepreneur': instance.entrepreneur.id,
            'entrepreneur_name': instance.entrepreneur.entrepreneur,
        }