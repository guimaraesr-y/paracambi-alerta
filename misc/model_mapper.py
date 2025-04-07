

def map_model_to_entity(model_obj, entity_class):
    return entity_class(**{
        k: getattr(model_obj, k)
        for k in entity_class.__dataclass_fields__.keys()
    })
