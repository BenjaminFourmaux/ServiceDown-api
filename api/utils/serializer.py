from api.utils import SerializerHasNoField


class SerializerUtils:

    @staticmethod
    def check_field_is_in_serializer(requested_fields: [], serializer_field: [], serializer_name: str):
        for field in requested_fields:
            if field not in serializer_field:
                # Raise error
                raise SerializerHasNoField([field, serializer_name])
