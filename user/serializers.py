from rest_framework import serializers

from user.models import CustomUserGroup, CustomUser


class GroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)

    class Meta:
        model = CustomUserGroup
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128, required=False)
    groups = GroupSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'groups')

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user = CustomUser.objects.create(**validated_data)

        for group in groups:
            group_instance, _ = CustomUserGroup.objects.get_or_create(name=group['name'])
            user.groups.add(group_instance)

        return user

    def update(self, instance, validated_data):
        groups = validated_data.pop('groups')

        groups_list = []

        for group in groups:
            group_instance, _ = CustomUserGroup.objects.get_or_create(name=group['name'])
            groups_list.append(group_instance)
        instance.groups.set(groups_list)
        instance.save()
        return instance
