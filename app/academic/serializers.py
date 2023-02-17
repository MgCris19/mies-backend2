from dataclasses import field, fields
from rest_framework import serializers
from .models import Trainer, Faculty, TrainerCategory, Career, Student


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'state' : instance.state,
            'student_id' : instance.student_id.id,
            'nameStudent': instance.student_id.name,
            'category_trainer' : instance.category_trainer.id,
            'categoryTrainer': instance.category_trainer.name
        }

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'               


class TrainerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerCategory
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'observation': instance.observation,
            'faculty_id': instance.faculty_id.id,
            'nameFaculty': instance.faculty_id.observation, 
        }

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'document': instance.document,
            'name': instance.name,
            'lastname': instance.lastname,
            'email': instance.email,
            'telephone': instance.telephone,
            'career': instance.career.id,
            'career_name': instance.career.name,
        }