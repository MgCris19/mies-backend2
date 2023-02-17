from rest_framework import serializers
from dataclasses import field, fields
from .models import Course, CourseCategory, LocalityCourses, CourseTrainer
from app.academic.models import Trainer, Student, TrainerCategory

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class LocalityCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalityCourses
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class CourseTrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTrainer
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'course': instance.course.id,
            'course_name': instance.course.name,
            'trainer': instance.trainer.id,
            'trainer_name': StudentSerializer(instance.trainer.student_id).data['name'],
            'trainer_lastname': StudentSerializer(instance.trainer.student_id).data['lastname'],
            'observation': instance.observation,
        }