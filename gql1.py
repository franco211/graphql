try:
    import json
    import graphene
    import os
    print('All ok')
except Exception as e:
    print("Error : {} ".format(e))

'''
{
    name:"Bob",
    age:45
}
'''
class Query(graphene.ObjectType):
    """Query object."""
    name = graphene.String(required=True)
    age = graphene.Int(required=True)

    def resolve_name(self, info):
        """Resolve name."""
        return self.name

    def resolve_age(self, info):
        """Resolve age."""
        return self.age

schema = graphene.Schema(query=Query)
print(schema)