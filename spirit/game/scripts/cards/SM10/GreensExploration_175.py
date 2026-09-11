from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='227a00bb-895e-553a-91d4-f11b64bfc756',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name',
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", 'Supporter', 'GreensExploration'],
    subtypes=['Supporter'],
    collector_number=175,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('You can play this card only if you have no Pokémon with Abilities in play. Search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
    condition=standard_trainer_condition('You can play this card only if you have no Pokémon with Abilities in play. Search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.'),
)
