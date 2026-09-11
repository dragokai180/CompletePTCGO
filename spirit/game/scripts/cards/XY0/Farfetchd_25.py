from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5838fd37-a90a-587b-8ae1-0485699e05a0',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name',
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", 'Basic', 'Farfetchd'],
    subtypes=['Basic'],
    collector_number=25,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
